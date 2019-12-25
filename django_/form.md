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
    
    
## 04 Cross Site Request Forgery
### 사이트 간 요청 위조 공격
- 사옹자가 의도하지 않게 게시판에 글을 작성하거나, 쇼핑을 하게 하는 등의 공격

### 요청을 받는 서버 입장에서, 공격을 막기 위해 Token 을 통한 체크
- POST 요청에 한해 CsrfViewMiddleware 를 통한 체크
    - POST 요청을 받을 떄 Token 값이 없거나 유효하지 않다면, 403 Forbidden 응답
- 처리순서
    1) 입력 Form을 보여줄 때, Token값도 값이 할당
        - token은 User마다 다르며, 주기적으로 변경됩니다
    2) 그 입력 Form을 통해 Token 값이 전달이 되면, Token 유효성 검증
    
### CSRF Token 체크기능을 끈다
- 가급적이면 끄지 말자
    - 기본 제공되는 보안기능이며,
    - 이를 유지하는 데에 비용이 거의 들지 않는다.
- 앱 API에서는 끄는 것이 필요할 수 있다
    - django-rest-framework에서는 관련 View에 대해 모두 배제
- 특정 View에 한해, CSRF Token 체크에서 배제할려면?
    - 해당 뷰에 @csrf_exempt 장식자를 적용
    
## 05. ModelForm
### ModelForm
- 장고 Form을 상속
- 지정된 Model로부터 필드정보를 읽어들여, Form Fields를 세팅
- 내부적으로 Model Instance 를 유지
- 유효성 검증에 통과한 값들로, 지정 Model Instance로의 저장(save) 지원 (Create 또는 Update)

### ModelForm.save(commit=True)
- form의 cleaned_data를 Model Instance 생성에 사용하고, 그 Instance를 리턴
- commit = True
    - model instance 의 save() 및 form.save_m2m()을 호출
    - form.save() != instance.save()
- commit = False
    - instance.save() 함수 호출을 지연시키고자할 때 사용

## 06. Form Validation
### 유효성 검사 호출 로직
- form.is_valid() 호출 당시
1. form.full_clean() 호출
    1. 각 필드 객체 별로
        - 각 필드객체.clean() 호출을 통해 각 필드 Type에 맞춰 유효성 감사
    2. Form 객체 내에서
        - 필드 이름 별로 Form객체.clean_필드명() 함수가 있다면 호출해서 유효성 검사
        - Form객체.clean() 함수가 있다면 호출해서 유효성 검사
2. 에러 유무에 따른 True/False 리턴

### Form에서 수행하는 2가지 유효성 검사
1. validator 함수를 통한 유효성 검사
    - 값이 원하는 조건에 맞지 않을 때, ValidationError 예외를 발생
        - 주의 : 리턴값은 사용되지 않습니다
2. Form 클래스 내 clean, clean_ 멤버함수를 통한 유효성 검사 및 변경
    - 값이 원하는 조건에 맞지 않을 때, ValidationError 예외를 발생
    - 리턴값을 통해 값 반환
    
### 함수형/클래스형 Validator(1)
- 함수형
    - 유효성 검사를 수행할 값 인자를 1개 받은 Callable Object
- 클래스형
    - 클래스의 인스턴스가 Callable Object

### 모델 필드에 디폴트 적용된 validators
- models.EmailField (CharField)
    - validators.validate_email 적용
- models.URLField
    - validators.URLValidator() 적용
- models.GenericIPAddressField
    - validators.ip_address_validators 적용
- models.SlugField
    - validators.validate_slug 적용
    
### Form clean 멤버함수에게 기대하는 것
1. "필드별 Error 기록" 혹은 "Non 필드 Error 기록"
    - 값이 조건에 안 맞으면 ValidationError 예외를 통해 오류 기록
    - 혹은 add_error(필드명, 오류내용)  직접 호출을 통해 오류 기록
2. 원하는 포맷으로 값 변경
    - 리턴값을 통해 값 변경하기

### 멤버 함수별, 검사/변경의 책임
- clean_필드명() 멤버함수
    - 특정 필드별 검사/변경의 책임
    - ValidationError 예외 발생 시, 해당 필드 Error로 분류
- clean() 멤버함수
    - 다수 필드에 대한 검사/변경의 책임
    - ValidationError 예외 발생 시, non_field_error로 분류
    - add_error(...) 함수를 통해 필드별 Error 기록도 가능
    
### 언제 validators를 쓰고, 언제 clean을?
- 가급적이면 모든 validators는 모델에 정의하고, ModelForm을 통해 모델의 validators 정보도 같이 가져오세요
- clean이 필요할 때
    - 특정 Form에서 1회성 유효성 검사 루틴이 필요할 때
    - 다수 필드값에 걸쳐서, 유효성 검사가 필요할 때
    - 필드 값을 변경할 필요가 있을 때
        - validator는 값만 체크할 뿐, 값을 변경할 수는 없습니다.
   
    
    
    
    
    
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    














