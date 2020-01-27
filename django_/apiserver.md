# TIL
# [장고이론편] 장고 - API 서버 만들기 및 초간단 안드로이드 앱 만들기

## 01 Overview 및 JSNON 응답뷰 만들기
### API 서버란?

- 앱/웹 서비스를 만드는 개발자들이 이용하는 데이터 위주의 서비스
- 시간이 지나도 호환성을 유지해야하고 API 버전 개념을 둔다
  ex) /api/v1/posts/, /api/v2/posts
- REST API 라고 부르는 것들은 단순히 HTTP프로토콜을 통한 API, 즉 HTTP API 라고 불러야

- djangorestframework 는 아래 REST API 컨세을 쉽게 만들수 있도록 도와준다. 이것이 REST API 전부는 아니다

  - URI는 https://{serviceRoot}/{collection}/{id} 형식
  - GET, PUT, DELETE, POST, HEAD, PATCH, OPTIONS 를 지원
  - API 버저닝은 Major.minor로 하고, URI에 버전정보를 포함

  ### REST  API 식의 URL 예

  한 Post 모델에 대한 API 서비스를 제공할 때, 다음기능이 필요

  - 새 포스팅 내용을 받아 등록하고 확인응답
  - 포스팅 목록 및 검색 응답
  - 특정 포스팅 내용 응답
  - 특정 포스팅 내용 갱신하고 확인응답
  - 특정 포스팅 내용 삭제하고 확인응답

  이에 대해 URL을 설계한다면, 다음과 같이 설계해볼 수도 있음

  - 새 포스팅 내용을 받아 등록하고 확인응답 : /postnew/ 주소로 POST 요청
  - 포스팅 목록 및 검색 응답 : /post/ 주소로 GET 요청
  - 특정 포스팅 내용 응답 : /post/10/ 주소로 POST 요청
  - 특정 포스팅 내용 갱신하고 확인응답 : /post/10/update/ 주소로 POST 요청
  - 특정 포스팅 내용 삭제하고 확인응답 : /post/10/delete/ 주소로 POST 요청

이를 REST API 식의 URL 로 다시 설계해보낟면 다음과 같이

- /post/ 주소
  - GET 방식 요청 : 목록 응답
  - POST 방식 요청 : 새 글 생성하고, 확인 응답
- /post/1/ 주소
  - GET 방식 요청 : 1번 글 내용 응답
  - PUT 방식 요청 : 1번 글 갱신하고, 확인 응답_ DELETE 방식 요청 : 1번 글 삭제하고, 확인 응답

위 API를 장고로 구현함에 있어서, URL이 2개이므로 2개의 뷰를 구현하지만, 실제로는 5개의 로직을 구현해야

```python
# myapp/models.py

from django.db import models

class Post(models.Model):
  		message = models.TextField()
    
# myapp/forms.py
from django import forms

class PostForm(forms.ModelForm):
  		class Meta:
       		model = Post
        	fields = '__all__'
          
# myapp/views.py
def post_list(request):
    if request.method == 'POST':
       # 새 글 저장을 구현
       form = PostForm(request.POST, request.FILES)
       if form.is_valid():
          	post = form.save()
            return JsonResponse(post)
       return JsonResponse(form.errors)
    else:
       # 목록 응답을 구현
       return JsonResponse(Post.objects.all())
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'PUT':
       # 특정 글 갱신을 구현
        put_data = QueryDict(request.body)
        form = PostForm(put_data, instance=post)
        if form.is_valid():
          	post = form.save()
            return JsonResponse(post)
        return JsonResponse(form.errors)
    elif request.method == 'DELETE':
        # 특정 글 삭제를 구현
        post.delete()
        return HttpResponse()
    else:
        # 특정 글 내용 응답을 구현
        return JsonResponse(post)
      
```

Djangorestframework 는 REST API 구현을 도와주는 Class Based View를 제공해주는 프레임워크

```python
# myapp/models.py

from django.db import models

class Post(models.Model):
  		message = models.TextField()
    
# myapp/serializers.py
from rest_framework import serializers
from .forms import Post

# ModelForm 대신에 ModelSerializer
class PostSerializer(serializers.ModelSerializer):
  		class Meta:
       		model = Post
        	fields = '__all__'
          
# myapp/views.py
from rest_framework import viewsets

class PostViewSet (viewsets.ModelViewsets):
  		queryset = Post.objects.all()
    	serializer_class = PostSerializer
      
# myapp/urls.py
from rest_framework.routers import Defaultrouter
from . import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
  	url(r'', include(router.urls)),
]
```

### API호출

API 뷰 호출은 다양한 클라이언트 프로그램에 의해서 호출

- 웹 프론트엔드에서 JavaScript 를 통한 호출
- Android/iOS 앱 코드를 통한 호출
- 브라우저를 통한 호출 : 유저가 웹페이지를 탐색할 때, selenium 을 통해 자동화를 할 때 등
- 웹요청 개발 프로그램을 통한 호출
  - GUI 프로그램: Postman : Powerful API Client
  - CLI 프로그램: cURL, HTTPie
  - 라이브러리 : requests

HTTPie를 통한 HTTP 요청

```shell
pip3 install --upgrade httpie
http GET 요청할주소 GET인자명==값 GET인자명==값
http --json POST 요청할주소 GET인자명==값 GET인자명==값 POST인자명==값 POST인자명==값 
http --form POST 요청할주소 GET인자명==값 GET인자명==값 POST인자명==값 POST인자명==값 
```

이 중에 POST 요청은 2종류로 구분됩니다. 서버로 요청이 전달될 때, 전달 데이터를 어떻게 인코딩하느냐의  차이

- --form 옵션 지정 시 : multipart/form-data 요청 : HTML Form과 동일
- --jsno 옵션 지정하거나 생략 시 : application/jsno 요청 : 요청 데이터를 JSON 포맷으로 직렬화해서 전달

GET/POST/PUT/DELETE 요청을 날려볼 서버가 필요. httpbin.org 서비스로  쏴보겠습니다. API개발을 도와주는 서비스로서, 요청내역에 대한 상세정보를 응답으로 준다.

```shell
# GET 
http GET httpbin.org/get x==1 y==2

HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: *
Connection: keep-alive
Content-Length: 337
Content-Type: application/json
Date: Mon, 27 Jan 2020 04:31:10 GMT
Server: gunicorn/19.9.0

{
    "args": {
        "x": "1",
        "y": "2"
    },
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Host": "httpbin.org",
        "User-Agent": "HTTPie/2.0.0",
        "X-Amzn-Trace-Id": "Root=1-5e2e678e-210e34ec0ff99b209c27e4ac"
    },
    "origin": "218.234.111.110",
    "url": "http://httpbin.org/get?x=1&y=2"
}

# POST 요청
http --form POST "httpbin.org/post" a=1 b=2 c=3

HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: *
Connection: keep-alive
Content-Length: 510
Content-Type: application/json
Date: Mon, 27 Jan 2020 04:32:29 GMT
Server: gunicorn/19.9.0

{
    "args": {},
    "data": "",
    "files": {},
    "form": {
        "a": "1",
        "b": "2",
        "c": "3"
    },
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Content-Length": "11",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "Host": "httpbin.org",
        "User-Agent": "HTTPie/2.0.0",
        "X-Amzn-Trace-Id": "Root=1-5e2e67dd-5b83b52024499d10dc74a99e"
    },
    "json": null,
    "origin": "218.234.111.110",
    "url": "http://httpbin.org/post"
}

# PUT요청
http PUT httpbin.org/put hello=world

HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: *
Connection: keep-alive
Content-Length: 493
Content-Type: application/json
Date: Mon, 27 Jan 2020 04:33:44 GMT
Server: gunicorn/19.9.0

{
    "args": {},
    "data": "{\"hello\": \"world\"}",
    "files": {},
    "form": {},
    "headers": {
        "Accept": "application/json, */*",
        "Accept-Encoding": "gzip, deflate",
        "Content-Length": "18",
        "Content-Type": "application/json",
        "Host": "httpbin.org",
        "User-Agent": "HTTPie/2.0.0",
        "X-Amzn-Trace-Id": "Root=1-5e2e6828-264df9a14b380fb98eb9499d"
    },
    "json": {
        "hello": "world"
    },
    "origin": "218.234.111.110",
    "url": "http://httpbin.org/put"
}

# DELETE 요청
http DELETE "httpbin.org/delete"

HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: *
Connection: keep-alive
Content-Length: 392
Content-Type: application/json
Date: Mon, 27 Jan 2020 04:34:42 GMT
Server: gunicorn/19.9.0

{
    "args": {},
    "data": "",
    "files": {},
    "form": {},
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Content-Length": "0",
        "Host": "httpbin.org",
        "User-Agent": "HTTPie/2.0.0",
        "X-Amzn-Trace-Id": "Root=1-5e2e6862-0a5c0f12584e00a2afc60768"
    },
    "json": null,
    "origin": "218.234.111.110",
    "url": "http://httpbin.org/delete"
}
```

### Django 를 통한 API 구현 샘플

django 에서는 데이터 유효성 검사 및 처리를 Form/ModelForm 를 통해 처리하고, JSON 직렬화는 DjangoJSONEncoder 를 사용하거나 직접 변환

drf 는 장고의 Form/CBV 컨셉을 그대로 가져옴. Django에서 기본제공해주는 Model/ModelForm/View를 통해 다음 5가지 API를 구현해보고, 이어서 동일한 기능을 django-rest-framework를 통해 구현

- 새 포스팅 내용을 받아 등록하고 확인응답 : /postnew/ 주소로 POST 요청
- 포스팅 목록 및 검색 응답 : /post/ 주소로 GET 요청
- 특정 포스팅 내용 응답 : /post/10/ 주소로 POST 요청
- 특정 포스팅 내용 갱신하고 확인응답 : /post/10/update/ 주소로 POST 요청
- 특정 포스팅 내용 삭제하고 확인응답 : /post/10/delete/ 주소로 POST 요청

```python
# myapp/models.py
from django.db import models

class Post(models.Model):
  		message = models.TextField()
    

# myapp/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
  		class Meta:
       		model = Post
        	fields = '__all__'
          

# myapp/views.py
@csrf_exempt
def post_list(request):
    if request.method == 'GET':
       qs = Post.objects.all()
       data = [{'pk':post.pk, 'message':post.message} for post in qs] # 수동 JSON 직렬화
      return JsonResponse(data, safe=False)
    elif request.method == 'POST':
       form = PostForm(request.POST)
       if form.is_valid():
          	post = form.save()
            return HttpResponse(status=201)
       data = form.errors
       return JsonResponse(data, status=400)
           
@csrf_exempt        
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
		
    if request.method == 'GET':
  		  return JsonResponse({'pk': post.pk, 'message': post.message})
    elif request.method == 'PUT':
				put = QueryDict(request.body)
        form = PostForm(put, instance=post)
        if form.is_valid():
            post = form.save()
            data = {'pk':post.pk, 'message':post.message}
            return JsonResponse(data=data, status=201)
        return JsonResponse(form.errors)
      elif request.method == 'DELETE':
        post.delete()
        return HttpResponse('', status=204)

 # myapp/urls.py
from django.conf.urls import url
from .views import post_list, post_detail

urlpatterns = [
  url(r'^post/$', post_list, name='post-list'),
  url(r'^post/(?P<pk>\d+)/$', post_detail, name='post-detail'),
]
```

### django-rest-framework 를 통한 API 구현 샘플

```shell
# 설치
pip3 install djangorestframework

# settings.py 에 앱 추가
INSTALLED_APPS = [
		'rest_framework',
]
```

아래의 PostViewSet은 Class Based View 로서 위에서 장고로 구현했던 모든 기능을 일괄 제공

```python
# myapp/models.py
from django.db import models

class Post(models.Model):
  		title = models.CharField(max_length=100)
    
# myapp/serializers.py (Form과 유사)
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
  		class Meta:
       		model = Post
        	fields = '__all__'
          
# myapp/views.py
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
  		queryset = Post.objects.all()
    	serializer_class = PostSerializer

 # myapp/urls.py
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'post', PostViewSets)

urlpatterns = [
  url(r'', include(router.urls)),
]
```






















































