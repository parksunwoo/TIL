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

from Django.db import models


class Post(models.Model):
    message = models.TextField()


# myapp/forms.py
from Django import forms


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

from Django.db import models


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


class PostViewSet(viewsets.ModelViewsets):
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
from Django.db import models


class Post(models.Model):
    message = models.TextField()


# myapp/forms.py
from Django import forms
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
        data = [{'pk': post.pk, 'message': post.message} for post in qs]  # 수동 JSON 직렬화
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
        data = {'pk': post.pk, 'message': post.message}
        return JsonResponse(data=data, status=201)
    return JsonResponse(form.errors)

elif request.method == 'DELETE':
post.delete()
return HttpResponse('', status=204)

# myapp/urls.py
from Django.conf.urls import url
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
from Django.db import models


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
from Django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'post', PostViewSets)

urlpatterns = [
    url(r'', include(router.urls)),
]
```

## 02. JSON 직렬화

모든 프로그래밍 언어의 통신에서 데이터는 필히 문자열로 표현

- 송신자 : 객체를 문자열로 변환하여, 데이터 전송 -> 이를 직렬화 (Serialization) 라고 한다
- 수신자 : 수신한 문자열을 다시 객체로 변환하여, 활용 -> 이를 비직렬화 혹은 역직렬화

각 언어에서 모두 지원하는 직렬화 포맷(JSON, XML) 도 있고, 특정 언어에서만 지원하는 직렬화 포맷 (파이썬은 Pickle)

### JSON

보통의 웹애플리케이션에서는 일반적으로 웹브라우저가 주 클라이언트 프로그램이기 때문에, 주로 HTML 포맷으로 통신을 한다. 그런데, 최근이 API 서버에는 대개 JSON 포맷으로 통신을 수행. 그렇기에 항상 장고 API 뷰 함수에서는 최종적으로 JSON 포맷의 문자열 응답을 해야

- JSON 포맷 : 다른 언어/플랫폼과 통신할 때 주로 사용. 표준 라이브러리 json이 제공
  - pickle에 비해 직렬화를 지원하는 데이터타입의 수가 적다. 공통 데이터타입에 한해서만 직렬화를 지원
- PICKLE 포맷 : 파이썬 전용 포맷으로서 파이썬 시스템끼리 통신할 때 사용합니다만, 최근 파이썬끼리 통신에 json 포맷도 많이 사용. 표준 라이브러리 pickle 이 제공
  - JSON에서 지원하지 않는 파이썬 데이터타입을 지원
  - 파이썬 버전 특성을 탄다

```python
post_list = [
  {'message' : 'hello askdjango'},
]

# 아래와 같이 JSON 포맷의 문자열로 직렬화 
import json

json_string = json.dumps(post_list)
json_string # '[{'message' : 'hello askdjango'}]'

# 비직렬화
json.loads(json_string)
[{'message' : 'hello askdjango'}]
```

JSON 직렬화와 유사한 방식으로, PICKLE 포맷의 문자열로 직렬화를 할수 있음

```python
import pickle

pickle_data = pickle.dumps(post_list)
pickle_data # b'\x80\x03]q\x00}q\x01X\x07\x00\x00\x00messageq\x02X\x0f\x00\x00\x00hello askdjangoq\x03sa.'

pickle.loads(pickle_data) # [{'message': 'hello askdjango'}]


```

json/pickle 라이브러리는 파이썬 표준 라이브러리로서 파이썬 표준 데이터타입에 대한 직렬화/비직렬화를 수행. 이는 파이썬 표준 데이터타입에 대해서는 각각의 타입에 대해서 직렬화/비직렬화 룰을 파이썬이 지원해주고 있음.
하지만 장고 Model/QuerySet 과 같은 파이썬 언어 외부타입에 대해서는 파이썬의 json 모듈은 직렬화/비직렬화 Rule 을 모르기에 직렬화가 불가

User 모델 인스턴스에 대해 JSON 직렬화를 수행했는데, TypeError 가 발생했으며 "Objects of type 'User' is not JSON serializable" 메세지가 나온다. 장고의 데이터타입에 대해 JSON 직렬화를 수행하는 방법에 대해서 살펴

```python
python3
manage.py
shell

>> > import json
>> > from Django.contrib.auth import get_user_model
>> > User = get_user_model()
>> > json.dumps(User.objects.first())

TypeError: Object
of
type
'User' is not JSON
serializable
```

### Django 프로젝트 기본 셋업

```python
# 최소한의 settings 설정
import Django
import os

SECRET_KEY = 'askdjango'  # 임의 문자열
DATABASES = {
    'default': {
        'ENGINE': 'Django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
ROOT_URLCONF = '__main__'

urls = []

os.environ['DJANGO_SETTINGS_MODULE'] = '__main__'

Django.setup()

# 모델 정의
from Django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'api'  # 앱이 따로 없으므로, app label을 필히 지정해줘야합니다.

    def __str__(self):
        return self.title


# DB TABLE 생성
from Django.db import connection

table_name = Post._meta.db_table

with connection.cursor() as cursor:
    cursor.execute('''
CREATE TABLE "{}"
    ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
     "title" varchar(100) NOT NULL,
     "content" text NOT NULL,
     "created_at" datetime NOT NULL,
     "updated_at" datetime NOT NULL);
'''.format(table_name))

# 데이터 추가
Post.objects.create(
    title='횡단보도 보행자 없으면 우회전 가능?…혼란 빚은 까닭',
    content='교차로에서 우회전할 때 횡단 보도를 건너는 사람이 없다면 보행자 신호가 녹색이더라도 진입할 수 있을까요? 이 문제를 놓고 대법원과 경찰의 판단이 다른 상황입니다.')

Post.objects.create(
    title="'디지털세대, 아날로그에 빠지다'…아날로그 인기 이유는?",
    content='옛 방식을 고집하는 아날로그 공간들이 젊은 층을 중심으로 주목받고 있습니다.')

Post.objects.create(
    title='저녁 줄였는데 누구는 살 빠지고, 난 안 빠지고…이유는',
    content='늦은 시간에 야식 먹으면 다 살로 간다고 하죠? 그래서 야식 증후군이란 말까지 생겼습니다. 또 아침은 많이 먹고 저녁은 되도록 적게 먹는 것이 다이어트의 지름길이라고 생각하기도 합니다. 이게 다 얼마나 맞는 말일까요?')

for post in Post.objects.filter():
    print(post.id, post.title, ':', len(post.content), '글자')
```



### 장고의 JSON 직렬화

장고에서는 파이썬 표준 라이브러리 json 모듈을 그대로 쓰지 않고, django/core/serializers/json.py 의 DjangoJSONEncoder 클래스를 통한 직렬화를 수행

DjangoJSONEncoder 는 son.JSONEncoder 를 상속받았으며, 다음 타입에 대한 직렬화를 추가로 지원

- datetime.datetime
- datetime.date
- datetime.time
- datetime.timedelta
- decimal.Decimal, uuid.UUID

이는 파이썬 기본 데이터 타입에 대한 직렬화가 추가되었을 뿐, 장고 데이터타입인 QuerySet과 Model 인스턴스에 대한 직렬화는 지원하지 않음. 이 가려운 부분은 djangorestframework 가 해결

```python
import json
from Django.core.serializers.json import DjangoJSONEncoder

data = Post.objects.all()
data
# <QuerySet [<Post: 횡단보도 보행자 없으면 우회전 가능?…혼란 빚은 까닭>, <Post: '디지털세대, 아날로그에 빠지다'…아날로그 인기 이유는?>, <Post: 저녁 줄였는데 누구는 살 빠지고, 난 안 빠지고…이유는>]>

이렇게
직렬화할
데이터를
QuerySet으로
준비합니다.그리고
직렬화를
수행해봅니다.
TypeError: Object
of
type
'QuerySet' is not JSON
serializable
예외가
발생할
거예요.: (

    json.dumps(data, cls=DjangoJSONEncoder)
```

왜> DjangoJSONEncoder는 QuerySet의 직렬화/비직렬화 방법을 모르고 있기 때문에, not JSON serializable 오류가 발생. 어떻게 해야할까요?

QuerySet을 파이썬 표준 데이터타입의 값으로 직접 변환가능. json 모듈이 하던 일을 직접

```python
data = [
    {'id': post.id, 'title': post.title, 'content': post.content}
    for post in Post.objects.all()]

json.dumps(data, cls=DjangoJSONEncoder, ensure_ascii=False)

import json

mydata = ['안녕', '파이썬']
json.dumps(mydata)
#'["\\uc548\\ub155", "\\ud30c\\uc774\\uc36c"]'

json.dumps(mydata, ensure_ascii=False)
#'["안녕", "파이썬"]'


```

Json에게 직렬화 방법을 알려줄수도 있음. DjangoJSONEncoder 가 직렬화 방법을 알고 있기에 이를 확장. 다음 2가지 타입을 지원할수 있도록

- QuerySet 타입 : tuple 타입으로 변환
- Post 타입 : dict 타입으로 변환

```python
from Django.core.serializers.json import DjangoJSONEncoder
from Django.db.models.query import QuerySet


# 커스텀 JSON Encoder를 정의
class MyJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, QuerySet):
            return tuple(obj)
        elif isinstance(obj, Post):
            return {'id': obj.id, 'title': obj.title, 'content': obj.content}
        return super().default(obj)


data = Post.objects.all()

# 직렬화할 때, 직렬화를 수행해줄 JSON Encoder를 지정해줍니다.
json.dumps(data, cls=MyJSONEncoder, ensure_ascii=False)

# '[{"id": 1, "title": "횡단보도 보행자 없으면 우회전 가능?…혼란 빚은 까닭", "content": "교차로에서 우회전할 때 횡단 보도를 건너는 사람이 없다면 보행자 신호가 녹색이더라도 진입할 수 있을까요? 이 문제를 놓고 대법원과 경찰의 판단이 다른 상황입니다."}, {"id": 2, "title": "\'디지털세대, 아날로그에 빠지다\'…아날로그 인기 이유는?", "content": "옛 방식을 고집하는 아날로그 공간들이 젊은 층을 중심으로 주목받고 있습니다."}, {"id": 3, "title": "저녁 줄였는데 누구는 살 빠지고, 난 안 빠지고…이유는", "content": "늦은 시간에 야식 먹으면 다 살로 간다고 하죠? 그래서 야식 증후군이란 말까지 생겼습니다. 또 아침은 많이 먹고 저녁은 되도록 적게 먹는 것이 다이어트의 지름길이라고 생각하기도 합니다. 이게 다 얼마나 맞는 말일까요?"}]'
```

### rest_framework.renderer.JSONRender 의 직렬화 방식

rest_framework/utils/encoders.py의 JSONEncoder 클래스를 통한 직렬화를 수행

JSONEncoder는 장고의 DjangoJSONEncoder 를 상속받지는 않고, json.JSONEncoder를 직접 상속받아 다음 타입에 대한 직렬화를 추가로 지원

- 파이썬 표준 데이터 타입
  - datetime.datetime 타입
  - datetime.date 타입
  - datetime.time 타입
  - datetime.timedelta 타입
  - decimal.Decimal 타입
  - uuid.UUID 타입
  - six.binary_type 타입
  - ```__getitem__``` 함수를 지원할 경우, dict (obj) 의 리턴값을 취함
  - ```__iter__``` 함수를 지원할 경우, tuple(item for item in obj) 의 리턴값을 취함
- 장고 데이터 타입
  - QuerySet 타입일 경우, tuple(obj) 의 리턴값을 취함
  - .tolist 함수를 가질 경우, obj.tolist() 의 리턴값을 취함

QuerySet에 대한 직렬화를 지원해줍니다만, Model 타입에 대한 직렬화는 없습니다. 이는 ModelSerializer의 도움을 받습니다.

rest_framework/renderer.py 내 JSONRenderer 는 json.dumps 함수에 대한 래핑 클래스입니다. 보다 편리한 JSON 직렬화를 도와줍니다. 

```python
from rest_framework.renderers import JSONRenderer

data = {'이름': 'AskDjango'}
json_utf8_string = JSONRenderer().render(data)
json_utf8_string.decode('utf8')

#'{"이름":"AskDjango"}'
```

JSONRenderer 은 rest_framework.utils.encoders.JSONEncoder 를 사용. JSONEncoder는 Model 타입에 대한 직렬화를 지원하지 않기에 직렬화에 실패

```python
from rest_framework.renderers import JSONRenderer

data = Post.objects.all()
JSONRenderer().render(data)

TypeError: Object of type 'Post' is not JSON serializable

  
data = [
    {'id': post.id, 'title': post.title, 'content': post.content}
    for post in Post.objects.all()]

json_utf8_string = JSONRenderer().render(data)

json_utf8_string.decode('utf8')  # 출력포맷 조정을 위한 목적일 뿐, 실제 서비스에서는 decode하지 않습니다.
```

```python
from rest_framework.renderers import JSONRenderer
from rest_framework.utils.encoders import JSONEncoder

class MyJSONEncoder(JSONEncoder):
  	def default(self, obj):
      	if isinstance(obj, Post):
          	return {'id':obj.id, 'title':obj.title, 'content':obj.content}
        return super().default(obj)
      
data = Post.objects.all()

renderer = JSONRenderer()
renderer.encoder_class = MyJSONEncoder
json_utf8_string = renderer.render(data)
json_utf8_string.decode('utf8')

```

### ModelSerializer 를 통한 JSON 직렬화

django-rest-framework에서는 일반적으로 ModelSerializer 를 통해  JSONRenderer 에서 변환가능한 형태로 먼저 데이터를 변환

Serializer 는 장고의 Form 과 유사하며, ModelSerializer 는 장고의 ModelForm 과 유사합니다. 역할 면에서 Serializer 는 POST 요청만 처리하는 Form 이라 할 수 있다.

ModelSerializer 는 ModelForm 과 거의 동일

```python
from rest_framework.serializers import ModelSerializer

class PostModelSerializer(ModelSerializer):
  	class Meta:
      	model = Post
        fields = '__all__'
```

다음과 같이 Post 모델 인스턴스에 대해서도  dict 타입으로 변환 지원. PostModelSerializer에 Post 객체를 넘겨보세요

```python
post = Post.objects.first()
post
serializer = PostModelSerializer(post)
serializer.data

```

### QuerySet 변환 지원

ModelSerializer 는 QuerySet 에 대해서도 변환을 지원. ModelSerializer 의 many 인자는 디폴트 False 입니다. many=True 인자를 지정해줘야만 QuerySet을 처리

```python
serializer = PostModelSerializer(Post.objects.all(), many= True)

# 지정된 Model Instance 필드를 통해 list/OrderDict 획득
serializer.data
###[OrderedDict([('id', 1), ('title', '횡단보도 보행자 없으면 우회전 가능?…혼란 빚은 까닭'), ('content', '교차로에서 우회전할 때 횡단 보도를 건너는 사람이 없다면 보행자 신호가 녹색이더라도 진입할 수 있을까요? 이 문제를 놓고 대법원과 경찰의 판단이 다른 상황입니다.'), ('created_at', '2017-10-16T14:15:12.102064'), ('updated_at', '2017-10-16T14:15:12.102093')]), OrderedDict([('id', 2), ('title', "'디지털세대, 아날로그에 빠지다'…아날로그 인기 이유는?"), ('content', '옛 방식을 고집하는 아날로그 공간들이 젊은 층을 중심으로 주목받고 있습니다.'), ('created_at', '2017-10-16T14:15:12.102431'), ('updated_at', '2017-10-16T14:15:12.102446')])]

import json
json.dumps(serializer.data, ensure_ascii=False)

from rest_framework.renderers import JSONRender

json_utf8_string = JSONRender().render(serializer.data)
json_utf8_string.decode('utf8')
```



### 뷰에서의 Json 응답

장고스타일

JSON 포맷으로 직렬화된 문자열은 장고 뷰를 통해서 응답이 이뤄져야 한다. 다음 2가지가 가능

1. json.dumps 를 통해 직렬화된 문자열을 HttpResponse 를 통해 응답
2. json.dumps 기능을 제공하는 JsonResponse를 즉시 사용

2번째 방법으로 이때 JsonResponse는 장고의  DjangoJSONEncoder를 사용하고 있으니, QuerySet 에 대해서는 직렬화가 불가능하다 그래서 위에서 정의한 MyJSONEncoder를 활용

```python
data = Post.objects.all()
data
```

JsonResponse에 넘겨줄 인자를 준비

- encoder(디폴트 : DjangoJSONEncoer) : JSON 인코딩을 수행할 클래스
- safe (디폴트 : True) : 변환할 데이터의 dict 타입 체킹을 목적으로 한다. 데이터가 dict 타입이 아닐 경우에는  필히  False 를 지정. 미지정 시에 TypeError 예외를 발생
- json_dumps_params (디폴트 : None) : json.dumps 에 넘겨질 인자
- kwargs( 디폴트 : {}): 부모 클래스인  HttpResponse 에 넘겨질 인자

```python
encoder = MyJSONEncoder
safe = False # True: data가 dict일 경우,
json_dumps_params = {'ensure_ascii' : False}
kwargs = {} # HttpResponse 에 전해지는 Keyword 인자

```

다음과 같이 Http 응답을 생성하고 그 응답바디를 출력

```python
from Django.http import JsonResponse

response = JsonResponse(data, encoder, safe, json_dumps_params, **kwargs)

print(response)
response.content.decode('utf8')
```

### django-rest-framework 스타일

```python
queryst = Post.objects.all()

#queryset 을 통해 ModelSerializer 준비
serializer = PostModelSerializer(queryset, many=True)
serializer

serializer.data
##[OrderedDict([('id', 1), ('title', '횡단보도 보행자 없으면 우회전 가능?…혼란 빚은 까닭'), ('content', '교차로에서 우회전할 때 횡단 보도를 건너는 사람이 없다면 보행자 신호가 녹색이더라도 진입할 수 있을까요? 이 문제를 놓고 대법원과 경찰의 판단이 다른 상황입니다.'), ('created_at', '2017-10-16T14:15:12.102064'), ('updated_at', '2017-10-16T14:15:12.102093')]), OrderedDict([('id', 2), ('title', "'디지털세대, 아날로그에 빠지다'…아날로그 인기 이유는?"), ('content', '옛 방식을 고집하는 아날로그 공간들이 젊은 층을 중심으로 주목받고 있습니다.'), ('created_at', '2017-10-16T14:15:12.102431'), ('updated_at', '2017-10-16T14:15:12.102446')]), OrderedDict([('id', 3), ('title', '저녁 줄였는데 누구는 살 빠지고, 난 안 빠지고…이유는'), ('content', '늦은 시간에 야식 먹으면 다 살로 간다고 하죠? 그래서 야식 증후군이란 말까지 생겼습니다. 또 아침은 많이 먹고 저녁은 되도록 적게 먹는 것이 다이어트의 지름길이라고 생각하기도 합니다. 이게 다 얼마나 맞는 말일까요?'), ('created_at', '2017-10-16T14:15:12.102714'), ('updated_at', '2017-10-16T14:15:12.102729')])]
```

뷰에서는 Response를 통해 응답을 생성. 이는 HttpResponse 를 상속받은 클래스. Response는 단순히  JSON 직렬화뿐만 아니라, HTTP요청에 따라 다양한 포맷으로 변환(Render) 하여 응답을 생성

```python
from rest_framework.response import Response

response = Response(serializer.data)
response
##<Response status_code=200, "text/html; charset=utf-8">

```

```python
from rest_framework.views import APIView

renderer_cls = APIView.renderer_classed[0]
renderer_obj = renderer_cls()
response.accepted_renderer = renderer_obj # JSON 변환을 위한 JSONRenderer 인스턴스

response.accepted_media_type = renderer_obj.media_type # 'application/json'
response.renderer_context = {'view':None, 'args':(), 'kwargs': {}, 'request':None}

response
```

Response 객체는 아직 변환할 준비만 하고 있을 뿐, 아직 JSON 직렬화 변환은 수행하지 않았습니다 .rendered_content 속성에 접근할 때, 변환이 이뤄집니다

```python
response.rendered_content.decode('utf8')
```

### 실전에서의 Response 활용

```python
from rest_framework import generics


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()


serializer_class = PostModelSerializer

from Django.http import HttpRequest


class DummyUser:
    pass


request = HttpRequest()
request.user = DummyUser()
request.method = 'GET'

response = PostListView.as_view()(request)
response.rendered_content.decode('utf8')


```



## 03. JSON 응답뷰 만들기 ( 부제 - APIView 부터 Viewset까지)

장고에서는 뷰를 통해 HTTP 요청을 처리
rest_framework를 쓰면 APIView/ViewSet을 활용하면 API뷰를 보다 적은 양의 코드로 효율적으로 작성

장고 기본 뷰에서의  Serializer 활용코드를 먼저 살펴

### Serializer를 통한 뷰처리

rest_framework의 Serializer는 장고의  Form과 유사한 역할을 한다. 데이터 유효성 검사 및 데이터베이스로의 저장을 지원
Serializer 를 통한 뷰처리는 다음과 같다

```python
class PostSerializer(serializers.ModelSerializer):
  	class Meta:
      	model = Post
        fields = ['title', 'content']

# views
serializer = PostSerializer(data= request.POST)
if serializer.is_valid():
  	 serializer.save()
     return JsonResponse(serializer.data, status=201)
return JsonResponse(serializer.errors, status=400)
```

### APIView 클래스와 api_view 장식자

APIView 클래스와 api_view 장식자는 뷰에 여러 기본 설정을 부여

- 직렬화 클래스 지정 : renderer_classes 속성(list)
  - 디폴트
    - rest_framework.renderers.JSONRenderer : JSON 직렬화
    - rest_framework.renderers.TemplateHTMLRenderer : HTML 페이지 직렬화
- 비직렬화 클래스 지정 : parser_classes 속성(list)
  - 디폴트
    - rest_framework.parsers.JSONRenderer : JSON 직렬화
    - rest_framework.parsers.FormParser
    - rest_framework.parsers.MultiPartParser
- 인증 클래스 지정 : authentication_classes 속성 (list)
  - 디폴트
    - rest_framework.authentication.SessionAuthentication : 세션에 기반한 인증
    - rest_framework.authentication.BasicAuthentication : HTTP Basic 인증
- 사용량 제한 클래스 지정 : throttle_classes 속성(list)
  - 디폴트 : 빈 튜플
- 권한  클래스 지정 : permission_classes 속성 (list)
  - 디폴트
    - rest_framework.permissions.AllowAny : 누구라도 접근 허용

- 요청에 따라 적절한 직렬화/비직렬화 클래스를 선택 : content_negotiation_class 속성(문자열)
  - 같은 URL로의 요청이지만, JSON 응답을 요구하는 것이나 / HTML 응답을 요구하는 것인지 판단
  - 디폴트 : rest_framework.negotiation.DefaultContentNegotiation
- 요청 내역에서 API 버전 정보를 탐지할 클래스 지정 : versioning_class 속성
  - 디폴트 : None : API 버전 정보를 탐지하지 않겠다
  - 요청 URL에서, GET 인자에서, HEADER에서 버전정보를 탐지하여, 해당 버전의  API뷰를 호출토록 한다.

### 장고에는 FBV와 CBV가 있다

- FBV(함수 기반 뷰, Function Based View)
  - 함수로 구현한 뷰
  - Specialize 한 뷰는 FBV 로 구현하는 것이 훨씬 가ㅏㄴ단
- CBV(클래스 기반 뷰, Class Based View)
  - 클래스로 구현한 뷰
  - 재사용성에 포커스 : 여러 뷰에 걸쳐서 반복되는 루틴이 있다면 클래스 상속 문법을 통해 중복을 줄여갈 수 있음

Rest_framework 에서 지원하는 API 뷰를 구현하기 위해 다음 2가지를 지원

- APIView : CBV
- api_view : FBV

### APIView 샘플

APIView 는 django-rest-framework 규격의 Class Based View

1. 하나의 Class Based View 이므로, 한 URL 에 대해서만 처리할 수 있음
   - /post/ 에 대한 CBV일 경우
     - get 요청 : 포스팅 목록 요청
     - post 요청 : 새 포스팅 등록 요청
   - /post/10/ 에 대한 CBV 일 경우
     - get 요청 : 10번 포스팅 내용 요청
     - put 요청 : 10번 포스팅 수정 요청
     - delete 요청 : 10번 포스팅 삭제 요청
2. 요청 method 에 맞게 멤버함수를 정의하면, 해당 method 요청이 들어올 때 호출이 됩니다
   - def get(self, request)
   - def post(self, request)
   - def put(self, request)
   - def delete(self, request)
3. 각 method 가 호출될 때, 다음 처리가 이뤄집니다
   - 직렬화/ 비직렬화
   - 인증 처리 : 인증 체크
   - 사용량 제한 체크 : 호출 허용량 범위인지 체크
   - 권한 클래스 지정 : 비인증유저/ 인증유저에 대해 해당 API 호출을 허용할 것인지를 결정
   - 요청된 API 버전 문자열을 탐지하여 request.version 에 저장

APIView 클래스를 활용하여, 다음과 같이 글목록 응답/ 새글등록을 처리해주는 CBV를 만들어

```python
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer

class PostListAPIView(APIView):
  	def get(self, request):
      	serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(serializer.data)
    def post(self, request):
      	serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
          	serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
```

APIView 클래스를 활용하여 다음과 같이 특정 글의 내용응답/수정/삭제를 처리해주는 CBV를 만들어봄

```python
from Django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer


class PostDetailAPIVievw(APIView):
    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk)


def get(self, request, pk, format=None):
    post = self.get_object(pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)


def put(self, request, pk):
    post = self.get_object(pk)
    serializer = PostSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete(slef, request, pk):
    post = self.get_object(pk)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

```

POST 요청을 받기 위해 별도로 csrf_exempt 처리를 해줄 필요가 없습니다.  APIView.as_view() 에서 이미 csrf_exempt 처리된 뷰를 만들어주고 있기 때문

```python
# rest_framework/views.py
from Django.views.decorators.csrf import csrf_exempt


class APIView(View):

    @classmethod


def as_view(cls, **initkwargs):
    return csrf_exempt(view)

```

파이썬의 장식자는 다음과 같이 활용할 수 있음

```python
# 장식자 문법으로 써도 되고
@csrf_exempt
def myview1(request):
  	return HttpResponse('hello askdjango')
  
# 장식자는 실제로 다음과 같이 동작  
def myview2(request):
  	return HttpResponse('hello askdjango')
myview2 = csrf_exempt(myview2)
```

### @api_view 장식자 샘플

api_view 는 django-rest-framework 규격의  Function Based View 를 세팅해주는 장식자
위에서 구현한 CBV 버전의 PostListAPIView 를 FBV로 구현하면 다음과 같다

```python
from Django.http import get_object_or_404
from rest_framework import status, Response
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer


@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        serializer = PostSerializer(Post.objects.all(), many=True)
    return Response(serializer.data)

else:
serializer = PostSerializer(data=request.data)
if serializer.is_valid():
    serializer.save()
return Response(serializer.data, status=201)
return Response(serializer.errors, status=400)

```

@api_view 에서는 허용할 http method 를 지정해줘야하는 것이 조금 다름
위에서 구현한 CBV 버전의 PostDetailAPIView를 FBV로 구현하면 다음과 같다

```python
from rest_framework.decorators import api_view

@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
  	post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'GET':
      	serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
      	serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
          	serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
      	post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

### mixins 상속을 통한 APIView 로직 재사용

위에서 구현한 APIView 에서는 직접 Serializer 를 처리를 해줬어야한다 그런데 여러 Serializer에 대해서 구현을 하다보면 필연적을 중복이 발생. 이를 줄여보고자 한다

APIView는 클래스이기 때문에 클래스 상속을 통해 로직을 재활용할 수 있음

rest_framework.mixins에서는 다음 Mixin을 통해 위에서 구현한 기능들을 모두 지원 참고로 파이썬에서 Mixin 문법이 따로 있는 것이 아니라, 문법적으로 단순히 파이썬 클래스

- CreteModelMixin : create 함수
- ListModelMixin : list 함수
- RetrieveModelMixin : retrieve 함수
- UpdateModelMixin : update 함수
- DestroyModelMixin : destroy 함수

이렇게 여러 Mixin이 준비만 되어있음. 이 함수들이 호출되기 위해서는 직접 연결해야

PostListAPIView 를 다음과 같이 구현

```python
from rest_framework import generics
from rest_framework import mixins

class PostListAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
  		queryset = Post.objects.all()
    	serializer_class = PostSerializer
      
      def get(self, request, *args, **kwargs):
        	return self.list(request, *args, **kwargs)

      def post(self, request, *args, **kwargs):
        	return self.create(request, *args, **kwargs)        
```

PostDetailAPIView 를 다음과 같이 구현

```python
from rest_framework import generics
from rest_framework import mixins

class PostDetailAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
  		queryset = Post.objects.all()
    	serializer_class = PostSerializer
      
      def get(self, request, *args, **kwargs):
        	return self.retrieve(request, *args, **kwargs)

      def put(self, request, *args, **kwargs):
        	return self.update(request, *args, **kwargs) 
        
      def post(self, request, *args, **kwargs):
        	return self.destroy(request, *args, **kwargs)         
```

### Generics APIView 를 통한 로직 재사용

REST API 에서는 목록조회와 생성을 하나의 URL에서 처리. 그래서 이를 하나로 묶은 CBV도 rest_framework에서 지원

```python
# rest_framework/generics.py
class ListCreateAPIView(maxins.ListModelMixin, mixins.ListModelMixin, GenericAPIview):
  
  		def get(self, request, *args, **kwargs):
      		return self.list(request,t *args, **kwargs)
      
  		def post(self, request, *args, **kwargs):
      		return self.create(request,t *args, **kwargs)      
```

이를 활용하면 코드가 이렇게 간단

```python
from rest_framework import generics

class PostListAPIView(generics.ListCreateAPIView):
			queryset = Post.objects.all()
			serializer_class = PostSerializer
```

그리고 특정 레코드의 조회/수정/삭제도 하나의 URL에서 처리 이를 하나로 묶은 CBV도 지원

```python
# rest_framework/generics.py
class RetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin,
                                   GenericAPIView):

```

이를 활용하면 코드가 이렇게 간단

```python
from rest_framework import generics

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
  		queryset = Post.objects.all()
    	serializer_class = PostSerializer
```

위에서 살펴본 generics 외에도, 다음 generics 가 추가로 지원됩니다. 모두 GenericsAPIView 를 상속받으므로 추가로 상속받으실 필요가 없음

### 최종병기 ViewSet

하나의 Model에 대해서 기본적이 REST API 는 목록/생성/조회/수정/삭제인데요. 이를 지원하려면 2개의 URL, 즉 다음과 같이 2개의 뷰가 필요

```python
from rest_framework import generics

class PostListAPIView(generics.ListCreateAPIView):
  		queryset = Post.objects.all()
    	serializer_class = PostSerializer
      
class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
  		queryset = Post.objects.all()
    	serializer_class = PostSerializer
```

2개의 뷰 모두 queryset, serializer_class 를 동일하게 지정, 이를 한번에 처리, 그것이 ViewSet
ViewSet은 CBV가 아니다. 2개의 뷰를 만들어주는 헬퍼 클래스일 뿐. ViewSet은 다음 2가지가 지원

- Viewsets.ReadOnlyModelViewSet : 목록 조회, 특정 레코드 조회를 지원 => 2개의 URL 지원
- Viewsets.ModelViewSet : 목록조회, 생성, 특정 레코드 조회/수정/삭제 지원 => 2개의 URL 지원

조회만 지원하는 API를 만들어보면

가입한 회원 목록에 대한 API가 제공된다면 조회 기능만 제공. "회원 생성" 기능은 별도의 가입기능을 활용
UserViewSet 를 만들었다면, 목록조회/특정유저조회 API를 제공받을 수 있다.

```python
from rest_framework import viewsets

class UserViewSet(viewsets.ReadOnlyModelViewset):
  	qeuryset = User.objects.all()
    serializer_clss = UserSerializer
```

이렇게 만들어진 UserViewSet 을 URLConf 에 등록
다음과 같이 UserViewSet 을 통해, 개별 View를 생성할수도

```python
user_list = UserViewSet.as_view({
  		'get': 'list',    # 호출될 함수와 호출할 함수를 지정
})

user_detail = UserViewSet.as_view({
  		'get': 'retrieve',    # 호출될 함수와 호출할 함수를 지정
})
```

하지만 이렇게 하지 않아도 Router 를 통해 일괄적으로 URLConf에 등록

```python
from rest_framework.routers import DafaultRouter

router = DafaultRouter()
router.register(r'user', views.UserViewSet)
# router.register(r'post', views.PostViewSet) # PostViewSet이 있다면, 다음과 같이 추가등록할수

urlpatterns = [
  		url(r'', include(router.urls)),
]
```
























































