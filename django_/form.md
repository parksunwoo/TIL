# TIL
[중급편] 장고 Form/ModelForm 제대로 알고 쓰기

## 02 HttpRequest와 HttpResponse
### HttpRequest 객체
- 클라이언트로부터의 모든 요청 내용을 담고 있으며
    - 함수 기반 뷰 : 매 요청 시마다 뷰 함수의 첫번째 인자 request로 전달
    - 클래스 기반 뷰 : 매 요청 시마다 self.request 를 통해 접근
- Form 처리 관련 속성들
    - .method : 요청의 종류 "GET" 또는 "POST" 로서 몸두 대문자
    - .GET : GET 인자 목록 (QueryDict 타입)
    - .POST : POST 인자 목록 (QueryDict 타입)
    - .FILES : POST 인자 중에서 파일 목록 (MultiValueDict 타입)
    
### MultiValueDict(1)
- dict을 상속받은 클래스
- 동일 key의 다수 value를 지원하는 사전
- URL의 QueryString은 같은 Key로서 다수 Value지정을 지원

### MultiValueDict(2)
- 동일 key의 다수 value를 지원하는 사전

### MultiValueDict(3)
- 수정 불가능한 Immutable 특성

### HttpResponse 객체
- 다양한 응답을 wrapping : HTML 문자열, 이미지 등등
- View에서는 반환값으로서 HttpResponse 객체를 기대
    - Middleware에서 HttpResponse 객체를 기대

### django.http.HttpResponse (3)
- 사전-like 인터페이스로 응답의 커스텀 헤더 추가/삭제
- 파일 첨부로 처리되기를 브라우저에게 알리기
    response = HttpResponse(excel_data, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="foo.xls"'
    
### django.http.StreamingHttpResponse (1)
- 효율적인 큰(긴) 응답을 위함
    - 혹은 메모리를 많이 먹는 응답 -> iterator를 통한 응답
- 하지만, django는 short-lived 요청에 맞게 디자인
    - 큰(긴) 응답 시에는 극심한 성능 저하로 이어질 수 있습니다.
- HttpResponse를 상속받지 않음.
    - 필히 iterator를 지정해야만, 제대로 동작
    - .content 속성 사용 X -> .streaming_content 사용
    - .tell(), .write() 사용 Xs
    
### django.http.FileResponse
- StreamingHttpResponse 를 상속받음
    - 파일 내용 응답에 최적화
    -  Content-Length, Content-Type, Content-Disposition 헤더 자동지정
- 인자
    - open_file : Streaming Content
    - as_attachment : Content-Disposition 헤더 지정 여부
    - filename
    
```python

from django.http import FileResponse
response = FileResponse(open('myfile.png', 'rb'))
response = FileResponse(open('myfile.png', 'rb'), as_attachment=True)

```
    
### django.shortcuts.render
- context : 템플릿 context에 추가할 값 목록(dict)
- content_type : 응답의 MIME Type (디폴트: "text/html")
- status : 응답의 상태 코드 (디폴트:200)
- using : 템플릿 엔진 지정

### django.shortcuts.redirect
- to
    1. get_absolute_url() 이 구현된 모델 객체
    2. URL_Reverse를 수행할 문자열
    3. 직접 지정한 URL 문자열
    
- permanent
    - True: HttpResponsePermanentRedirect (301 응답)
    - False: HttpResponseRedirect (302 응답)

### django.shortcuts.get_object_or_404 (1)
- Model.DoesNotExist 예외 대신에 404 응답 발생

### django.shortcuts.get_list_or_404
- 지정 QuerySet 조건에 대해 empty일 경우, 404 응답 발생    
    
## 03. Form
### Form
- 장고를 더욱 장고스럽게 만들어주는 주옥같은 Feature
- 주요 역할
    - 입력폼 HTML 생성
    - 입력폼 값에 대한 유효성 검증(Validation) 및 값 변환
    - 검증을 통과한 값들을 dict 형태로 제공
    
### Django style의 form 처리(1)
- 하나의 URL(하나의 View)에서 2가지 역할을 모두 수행
    - 빈 폼을 보여주는 역할과
    - 폼을 통해 입력된 값을 검증하고 저장하는 역할

### Django style의 form 처리(2)
- get 방식으로 요청받았을 때
    - new/edit 입력폼을 보여준다
- post 방식으로 요청받았을 떄
    - 데이터를 입력받아 (request.POST, request.FILES) 유효성 검증 수행
    - 검증 성공 시 : 해당 데이터를 저장하고 SUCCESS URL로 이동
    - 검증 실패 시 : 오류메세지와 함께 입력폼을 다시 보여준다.
    
- 템플릿을 통해 HTML 폼 노출
    1. GET요청일 때
        - 유저가 Form을 채우고 Submit -> post 요청
    2. POST 요청이지만 유효성 검증에서 실패했을 때
        - form 인스턴스를 통해 HTML폼 출력
        - 오류메세지도 있다면 같이 출력
        - -> 유저가 Form을 채우고 Submit -> POST 재요청
        
### Form Fields
- Model Fields 와 유사
    - Model Fields : Database Field 들을 파이썬 클래스화
    - Form Fields : HTML Form Field 들을 파이썬 클래스화
- 필드 종류
    - BooleanField, CharField, ChoiceField, DateField, DateTimeField, EmailField, FileField, ImageField, FloatField, IntegerField, RegexField 등
    
    
    
    
    
    
    
    
    
     
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    














