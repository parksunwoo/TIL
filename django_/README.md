# TIL
Today I Learned

## [기초편] 장고 차근차근 시작하기 > 01 개발환경 구축하기
### 웹프레임워크가 왜 필요한가요?
- 서버의역할: 모든 서비스의 근간. 서버없이 머신러닝만 한다고해서 서비스가 되겠는가?

### 다양한 파이썬 웹프레임워크
- Django: 백엔드 개발에 필요한 거의 모든 기능을 제공
- Flask: 백엔드 개발에 필요한 일부분의 기능을 제공. ORM으로서 SQLAlchemy를 주로 사용 

### Django의 강점
- 파이썬 생태계. 크롤링,자동화, 머신러닝 코드와 같은 언어
- 풀스택 웹프레임워크
- 10년동안 충분히 성숙

### Django
- 2003년부터 개발하여 2005년에 세상에 공개
- 파이썬의 인기와 더불어 국내외에 장고를 쓰는 곳이 많다. 하이퍼커넥트, 한국은행

### 백엔드는 서비스의 중심
- 백엔드/서비스운영을 먼저 탄탄하게 하시고 나서, 그 후 프론트/앱을 고민하시는 것이 순서에 맞습니다

### 기본 생성된 파일/디렉토리 목록
- askdjango : 프로젝트명으로 생성된 디렉토리. 다른 이름으로 변경해도 Don't care
    - manage.py : 명령행을 통해 각종 장고 명령을 수행
    - askdjango : 프로젝트명으로 생성된 디렉토리. 이 이름을 참조하고 있는 코드가 몇 개 있기에 함부로 수정X
        - __init__.py : 팩키지를 임포트할 때의 임포트 대상
        - settings.py : 현재 프로젝트에서 장고 기본설정을 덮어쓰고, 새롭게 지정할 설정들
        - url.py : 최상위 URL 설정
        - wsgi.py : 실서비스에서의 웹서비스 진입

## [기초편] 장고 차근차근 시작하기 > 02 장고의 주요 구성 요소
### 장고 주요 기능들
- Function Based Views : 함수로 HTTP 요청처리
- Models : 데이터베이스와의 인터페이스
- Templates : 복잡한 문자열 조합을 보다 용이하게. 주로 HTML 문자열 조합 목적으로 사용하지만,
- Admin 기초 : 심플한 데이터베이스 레코드 관리 UI
- Logging : 다양한 경로로 메세지 로깅
- Static files : 개발 목적으로의 정적인 파일 관리
- Messages framework : 유저에게 1회성 메세지 노출 목적

- 웹서버, 데이터베이스서버, 캐시서버, 파일시스템의 기본구조

## [기초편] 장고 차근차근 시작하기 > 03 장고 앱
- 재사용성을 목적으로한 파이썬 패키지
 - 재사용성을 목적으로 둔 것이 아니라면, 하나의 장고 앱에서 현재 프로젝트의 거의 모든 기능을 구현해도 무방합니다
 - 하나의 앱이름은 현재 프로젝트 상에서 유일해야
 - 새롭게 생성한 장고앱이나 외부 라이브러리 형태의 장고앱은        
   settings.INSTALLED_APPS 에 등록 시켜줘야만 장고앱으로서 대접을 받는다.
    
## [기초편] 장고 차근차근 시작하기 > 04 VSCode 장고 디버깅 세팅하기
- 디버깅을 위해서 기본 적용되는 옵션
 - runserver 서버 시작옵션 --norelod --nothreading
 - 디버깅 메뉴를 통한 명시적인 재시작 및 정
- 다양한 pylint 메세지
 - 파이썬 정적 코드 분석툴
 
## [기초편] 장고 차근차근 시작하기 > 05 URLConf와 정규 표현식
### 정규 표현식
 - 문자열의 패턴, 규칙, Rule을 정의
 - 문법
    - 1글자에 대한 패턴 + 연속된 출연 횟수 지정
    - 대괄호 내에 1글자에 대한 후보 글자들을 나열  
    
### 다양한 예시
 - 1자리 숫자 
    - "[0123456789]" 혹은 "[0-9]" 혹은 "[\d]"
 - 2자리 숫자
    - "[0123456789][0123456789]" 혹은 "[0-9][0-9]" 혹은 "\d\d"
 - 3자리 숫자
    - "\d\d\d" 혹은 "\d{3}"
 - 2자리 ~ 4자리 숫자 : "\d{2,4}"
 - 휴대폰 번호 : "010[1-9]\d{7}"
 - 알파벳 소문자 1글자
    - "[a-z]"  
    
### 반복횟수 지정 문법
 - r"\d?" : 0회 혹은 1회 반복
 - r"\d*" : 0회 이상 반복
 - r"\d+" : 1회 이상 반복
 
### URL Dispatcher
 - "특정 URL 패턴" -> view의 list
 - http 요청이 들어올 때마다, 등록된 urlpatterns 상의 매핑 리스트를 처음부터 순차적으로 훝으며 URL 매칭을 시도
    - 매칭이 되는 URL Rule이 다수 존재하더라도, 처음 Rule만을 사용

### 기본 제공되는 Path Converter
- StringConverter -> r"[^/]+"
- IntConverter    -> r"[0-9]+"
- SlugConverter(StringConverter) -> r"[-a-zA-Z0-9_]+"
- UUIDConverter -> r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"  ``하이픈 포함 36자리``
    
### 새로운 장고 앱을 생성할 때, 추천 작업
- 앱 내 urls.py 를 생성하고 등록
    1. 앱 생성
    2. 앱이름/urls.py 파일 생성
    3. 프로젝트/urls.py 에 include 적용
    4. 프로젝트/settings.py 의 INSTALLED_APPS에 앱 이름 등록    

## [기초편] 장고 차근차근 시작하기 > 06 다양한 응답의 함수 기반 뷰 만들기
### View
 - 1개의 HTTP 요청에 대해 -> 1개의 뷰가 호출
 - urls.py/urlpatterns 리스트에 매핑된 호출 가능한 객체
 - 웹 클라이언트로부터의 HTTP 요청을 처리
 - 크게 2가지 형태의 뷰
    - 함수 기반  : 장고 뷰의 기본. 호출 가능한 객체 그 자체
    - 클래스 기반 : 클래스.as_view() 를 통해 호출가능한 객체를 생성/리턴
    
### View 호출시, 인자
- 1번째 인자: HttpRequest 객체 
- 2번쨰 인자: 현재 요청의 URL로부터 Capture 된 문자열들
    - url/re_path 를 통한 처리에서는 모든 인자는 str 타입으로 전달
    - path를 통한 처리에서는 매핑된 Converter의 to_python 에 맞게 변환된 값이 인자로 전달
    
### View 호출에 대한 리턴값
- 필히 HttpResponse 객체를 리턴
 - 장고 middleware 에서는 뷰에서 HttpResponse 객체를 리턴하기를 기대 -> 다른 타입을 리턴하면 middlewar에서 처리 오류
- 파일 like 객체 혹은 str/bytes 타입의 응답 지원
 - response = HttpResponse( 파일like객체 또는 str객체 또는 bytes 객체)
- 파일 like 객체
 - response.write( str객체 또는 bytes객체)
  
## [기초편] 장고 차근차근 시작하기 > 07 적절한 HTTP 상태코드로 응답하기
### HTTP 상태코드
- 웹 서버는 적절한 상태코드로서 응답
- 각 HttpResponse 클래스마다 고유한 status_code 가 할당
- REST API를 마늗ㄹ 때, 특히 유

## [기초편] 장고 차근차근 시작하기 > 08 장고 쉘
- SQL 출력 옵션
 - 쉘 > python manage.py shell_plus --print-sql
 - 혹은 settings.SHELL_PLUS_PRINT_SQL = True


## [기초편] 장고 차근차근 시작하기 > 09 장고 모델 (ORM)
### 애플리케이션의 다양한 데이터 저장방법
- 데이터베이스 : RDBMS , NoSQL 등
- 파일 : 로컬, 외부 정적 스토리지
- 캐시서버 : memcached, redis 등

### 데이터베이스와 SQL
- 데이터베이스에 쿼리하기 위한 언어 -> SQL
 - 직접 SQL을 만들어내기도 하지만, ORM(Object-relational mapping)을 통해 SQL을 생성/실행하기도 합니다.
 - ORM을 쓰더라도, 내가 작성된 ORM코드를 통해 어떤 SQL이 실행되고 있는지, 파악을 하고 이를 최적화할 수 있어야한다.

### 장고의 강점은 model과 form

### Django Model
- 데이터베이스 테이블과 파이썬 클래스를 1:1로 매핑
 - 모델 클래스명은 단수형으로 지정 - Post(o)
 - 매핑되는 모델 클래스는 DB 테이블 필드 내역이 일치
 
### 모델 활용 순서
 - 장고 모델을 통해, 데이터베이스 형상을 관리할 경우
    1. 모델 클래스 형성
    2. 모델 클래스로부터 마이그레이션 파일 생성 -> makemigrations 명령
    3. 마이그레이션 파일을 데이터베이스에 적용 -> migrate 명령
    4. 모델활용
 - 장고 외부에서, 데이터베이스 형상을 관리할 경우
  - 데이터베이스로부터 모델 클래스 소스 생성 -> inspectdb 명령
  
### 모델명과 DB 테이블명
 - DB 테이블명 : 디폴트 "앱이름_모델명"
    - blog 앱
        - post 모델 -> blog_post
        
### 적용순서
 - item 모델정의
 - 마이그레이션 파일 생성
 - 마이그레이션 파일 적용
 - 데이터베이스 확인
    - db 종류에 따라 다양한 방
    
## [기초편] 장고 차근차근 시작하기 > 10 장고 모델 필드
 - Primary Key: AutoField, BigAutoField
 - 문자열 : CharField, TextField, SlugField
 - 날짜/시간 : DateField, TimeField, DateTimeField, DurationField     
 - 참/거짓 : BooleanField, NullBooleanField
 - 숫자 : IntegerField, SmallIntegerField, PositiveIntegerField
 - 파일 : FileField, ImageField, FilePathField
 - 이메일 : EmailField
 - URL : URLField
 - UUID : UUIDField
 - 아이피 : GenericIPAddressField
 - Relation Types
    - Foreign Key
    - 
        
### 자주 쓰는 필드 공통 옵션
 - blank : 파이썬 validation 시에 empty 허용 여부 (디폴트 : False)
 - null : null 허용 여부 
 - db_index : 인덱스 필드 여부
 - default : 디폴트 값 지정, 혹은 값을 리턴해줄 함수 지정
 - unique : 현재 테이블 내에서 유일성 여부
 - choices : select 박스 소스로 사용
 - validators : validators 를 수행할 함수를 다수 지정
  - 모델 필드에 따라 고유한 validators 들이 등록 

### Tip
- 설계한 데이터베이스 구조에 따라, 최대한 필드타입을 타이트하게 지정해주는 것이, 입력값 오류를 막을 수 있음 
 - 필요하다면, validators들을 추가로 타이트하게 지정
- ORM은 SQL 쿼리를 만들엉주는 역할일 뿐, 보다 성능높은 애플리케이션을 위해서는, 사용하려는 DB 엔진에 대한 깊은 이해가 필요 
    
## [기초편] 장고 차근차근 시작하기 > 11 마이그레이션을 통한 데이터베이스 스키마 관리
- 데이터베이스에 어떤 변화를 가하는 Operation들을 나열
    - 테이블 생성/삭제, 필드 추가/삭제 등
- 대개 모델로부터 자동 생성 -> makemigrations 명령
    - 모델 참조 없이 빈 마이그레이션 파일 만들어서 직접 채워넣기도
- 같은 migration 파일이라 할지라도, DB종류에 따라 다른 SQL이 생    
    
### 언제 makemigrations 를 하는가?
- 모델 필드 관련된 어떠한 변경이라도 발생 시에 마이그레이션 파일 생성
- 마이그레이션 파일은 모델의 변경내역을 누적하는 역할

### 마이그레이션 migrations (정/역 방향)
- python manage.py migrate <앱 이름>
 - 미적용 마이그레이션 파일 부터 최근 마이그레이션 파일까지 정방향으로
- python manage.py migrate <앱 이름> <마이그레이션-이름>
 - 지정된 <마이그레이션-이름> 이 현재 적용된 마이그레이션보다
    - 이후라면, 정방향으로 순차적으로 지정
    - 이전이라면, 역방향으로 순차적으로 지정
    
### 새로운 필드가 필수필드라면?
- 필수필드 여부 : blank, null이 모두 False인    
    
### 협업 Tip
- 절대 하지 말아야할 일
 - 팀원 각자가 마이그레이션 파일을 생성하면 충돌
- 마이그레이션 파일 생성은 1명이 전담해서 생성.
 - 생성한 마이그레이션 파일을 버전관리에 넣고, 다른 팀원들은 이를 받아서 migrate만 수행
- 개발 시에 "서버에 아직 반영하지 않은" 마이그레이션을 다수 생성했었다면?
 - 하나의 마이그레이션으로 합쳐서 적용하기를 권장
    - 방법1) 서버로의 미적용 마이그레이들을 모두 롤백하고 -> 롤백된 마이그레이션들을 모두 제거하고 -> 새로이 마이그레이션 파일 생성
    - 방법2) 미적용 마이그레이션들을 하나로 합치기 -> squashmigrations

## [기초편] 장고 차근차근 시작하기 > 12 장고 admin을 통한 데이터 관리
### django admin
- djnago.contrib.admin 앱을 통해 제공
    - 디폴트 경로: /admin/ -> 실제 서비스에서는 다른 주소로 변경 권장
- 모델 클래스 등록을 통해, 조회/추가/수정/삭제 웹UI를 제공
    - 서비스 초기에 관리도구로서 사용하기에 제격
    - 관리도구 만들 시간을 줄이고 End - User 서비스에 집중
    
## [기초편] 장고 차근차근 시작하기 > 13 모델을 통한 데이터 조회
### Model Manager
- 데이터베이스 질의 인터페이스를 제공
- 디폴트 Manager로서 ModelCls.Objects가 제공

```djangotemplate
ModelCls.objects.all()
ModelCls.objects.all().order_by('-id')[:10]
ModelCls.objects.create(title="New Title")
```
    
### QuerySet
- SQL을 생성해주는 인터페이스
- 순회가능한 객체
- Model Manager를 통해, 해당 Model에 대한 QuerySet을 획득
- Chanining을 지원
    - Post.objects.all().filter().exclude().filter() -> QuerySet
    - QuerySet은 Lazy한 특성
        - QuerySet을 만드는 동안에는 DB접근을 하지 않습니다.
        - 실제로 데이터가 필요한 시점에 접근을 합니다.

### 다양한 조회요청 방법
- 조건을 추가한 Queryset, 획득할 준비
    - queryset.filter() -> queryset
    - queryset.exclude() -> queryset
- 특정 모델객체 1개 획득을 시도
    - queryset(숫자인덱스)
    - queryset.get()
    - queryset.first() last()
- filter <-> exclude
    - 인자로 "필드명 = 조건값" 지정
    - 1개 이상의 인자 지정 -> 모두 AND 조건으로 묶임
    - OR 조건을 묶을려면, django.db.models.Q 활

### 필드 타입별 다양한 조건 매칭
- 숫자/날짜/시간 필드
    - 필드명 __lt
    - 필드명 __lte
    - 필드명 __gt
    - 필드명 __gte
- 문자열 필드
    - 필드명 __startswith
    - 필드명 __endswith
    - 필드명 __contains
    - 필드명 __istartswith
    - 필드명 __iendswith
    - 필드명 __icontains
    
### 정렬 조건 추가
- 정렬 조건을 추가하지 않으면 일관된 순서를 보장받을 수 없음
- DB에서 다수 필드에 대한 정렬을 지원
    - 하지만 가급적 단일 필드로 하는 것이 성능에 이익
    - 시간순/역순 정렬이 필요한 경우, id필드를 활용해볼 수 있음
- 정렬 조건을 지정하는 2가지 방법
    1. (추천) 모델 클래스의 Meta 속성으로 ordering 설정 : list로 설정
    2. 모든 queryset에 order by(..) 에 지정

### 슬라이싱을 통한  범위조건추가
- str/list/tuple 에서의 슬라이싱과 거의 유사하나, 역순 슬라이싱은 지원하지 않음
 - db에서 지원하지 않음
- 객체 [start:stop:step]
    -offset -> start
    -limit -> stop - start
    
## [기초편] 장고 차근차근 시작하기 > 13 모델을 통한 데이터 생성/수정/삭제
### 다양한 INSERT 예시
- 방법1
    ```djangotemplate
    post = Post.objects.create(field1=value1, field2=value2, ...)
    post.pk
    ``` 
    
- 방법2
    ```djangotemplate
    post = Post(field1=value1, field2=value2)
    post.pk  -> None
    post.save()
    post.pk
    ```
  
- 방법3
    ```djangotemplate
    form = PostModelForm(request.POST, request.FILES)
    if form.is_valid():
        post = form.save()
        post.pk
    ```

### 다양한 UPDATE 예시
- 방법1) 개별 모델 인스턴스의 save 함수 호출 -> 반환값 : None
    ```djangotemplate
      post = Post.objects.all().first()
      post.field1 = new value1
      post.field2 = new value2
      post.save()         
    ```    

- 방법2) querySet 의 update 함수 호출 -> 반환값 : count
    ```djangotemplate
      qs = Post.objects.all().filter().exclude()
      qs.update(field1=new_value1, field2=new_value2)
    ```    

- 방법3) 
    ```djangotemplate
      form = PostForm(request.POST, request.FILES, instance=post)
      if form.is_valid():
          post = form.save()
    ```    

### 다양한 DELETE 예시
- 방법1) 개별 모델 인스턴스의 delete 함수 호출 -> 반환값 : 삭제된 record 갯수
    ```djangotemplate
      post = Post.objects.all().first()
      post.delete()
    ```
- 방법2) QuerySet 의 delete 함수 호출 -> 반환값 : 삭제된 record 갯수
    ```djangotemplate
      qs = Post.objects.all().filter().exclude()
      qs.delete()
    ```  
### 대개의 경우, 데이터베이스가 주요 병목
- 같은 작업을 하더라도
    - DB로 전달/실행하는 SQL 개수를 주링고
    - 각 SQL의 성능/처리속도 최적화가 필요
    
- RDBMS 외에도 캐싱 솔루션이나 NoSQL 솔루션을 고려
    - 제일 먼저, DB엔진과 서비스에 맞는 적절한 DB설계가 중요

## [기초편] 장고 차근차근 시작하기 > 15 관계를 표현하는 모델 필드
### RDBMS에서의 관계 예시
-1:N 관계 -> models.ForeignKey 로 표현
    - 1명의 유저가 쓰는 다수의 포스팅
-1:1 관계 -> models.OneToOneField로 표현
    - 1명의 유저는 1개의 프로필
-M:N 관계 -> models.ManyToManyField로 표현
    - 1개의 포스팅에는 다수의 태그
        - 1개의 태그에는 다수의 포스

### ForeignKey
- 1:N 관계에서 N측에 명시
    - Post:Comment,
- ForeignKey(to, on_delete)
    - to: 대상모델
        - 클래스를 직접 지정하거나,
        - 클래스명을 문자열로 지정. 자기 참조는 "self" 지정
    - on_delete : record 삭제 시 Rule
        - CASCADE: FK로 참조하는 다른 모델의 record도 삭제
        - PROTECT: 삭제방지
        - SET_NULL: null로 대체. 필드에 null=True 옵션 필수
        - SET_DEFAULT: 디폴트 값으로 대체. 필드에 디폴트값 지정 필수
        - SET: 대체할 값이나 함수 지정. 함수의 경우 호출하여 리턴값을 사용
        - DO_NOTHING
    
### FK에서의 related_name
>>> comment.post
>>> post.comment_set.all() <-> comment.objects.filter(post=post)

- related_name 디폴트 명은 앱이름 고려 X, 모델명만 고려
- 다음의 경우, user.post_set 이름에 대한 충돌
    - blog앱 Post 모델, author = FK(User)
    - shop앱 Post 모델, author = FK(User)
- 이름이 충돌나면 makemigrations 실패
- 이름 충돌 피하기
    1. 어느 한 쪽의 FK에 대해, related_name을 포기 -> related_name = '+'
    2. 어느 한 쪽의 FK의 related_name 을 변경
        ex) FK(User, ..., related_name="blog_post_set")
        
### ForeignKey.limit_choices_to 옵션
- form을 통한 choice 위젯에서 선택항목 제한가능.
    - dict/Q 객체를 통한 지정: 일괄지정
    - dict/Q 객체를 리턴하는 함수 지정 : 매번 다른 조건 지정 가능

### OneToOneField
- 1:1 관계에서 어느 쪽이라도 가능
    - User.Profile
-ForeignKey(unique=True)와 유사하지만, reverse 차이
    - User:Profile 를 FK로 지정한다면 -> profile.user_set.first() -> user    
    - User:Profile 를 O2O로 지정한다면 -> profile.user -> user

### O2O에서의 related_name
>>> profile.user
>>> user.profile

### ManyToManyField
- M:N 관계에서 어느쪽이라도 가능
    - Post: Tag
- ManyToManyField(to, blank=False)

### RDBMS이지만 DB따라 NoSQL 기능도 지    

## [기초편] 장고 차근차근 시작하기 > 16 django-debug-toolbar 를 통한 SQL 디버깅
### django-debug-toolbar
- 현재 request/response 에 대한 다양한 디버깅 정보를 보여줌
- 다양한 panel 지원
    - SQLPanel을 통해, 각 요청 처리 시에 발생한 SQL 내역 확인 가능
    - Ajax 요청에 대한 내역은 미지원
    
- 웹페이지의 템프릿에 필히 "<body>" 태그가 있어야만, 동작
- 이유 : dbt의 html/script 디폴트 주입 타겟이 </body> 태그

### 코드를 통한 SQL 내역확인
- querySet의 query 속성참조
    ex) print(Post.objects.all().query) -> 실제 문자열 참조 시에 SQL 생성
- settings.DEBUG = True 시에만 쿼리 실행내역을 메모리에 누적
- 쿼리확인 
    ```djangotemplate
      from django.db import connection, connections
  
      for row_dict in connection.queries:
          print('{time} {sql}'.format(**row_dict))
  
      connections['default'].queries  
    ```    

- 쿼리초기화
    - 메모리에 누적되기에, 프로세스가 재시작됨되며 초기화
    - django.db.reset_queries() 통해서 수동 초기화도 가
    
## [기초편] 장고 차근차근 시작하기 > 17 장고 Logging과 SQL Logging 처리
### 로그 
- 특정 형식으로 현 상황을 기록하는 문자열 기록
- 로깅을 파이썬에서 기본 지원
- 로그 레벨
    - DEBUG
    - INFO : 분석이 필요한 유용한 상태 정보
    - WARNING : 중요도가 낮은 문제를 발생할 가능성
    - ERROR: 상용 환경의 에러
    - CRITICAL : 급하게 주의가 요구되는 심각한 상황, ex) 내부 API 서비스에 접근 불가
    
### named bucket
- 마침표로 parent/child 계층 구분
    - django.security.csrf 로그 : django.security 와 django에 전파
- 부모 namespace 로의 전파를 막으려면
    - 해당 handler 설정에서 propagate = False 설정
- 장고에서 사용중인 named bucket
    - django / django.contrib.gis
    - django.db.backends / django.db.backends.schema
    
### 로깅
- named bucket을 지정하여, 현 모듈에서 쓸 logger 객체 획득하고 , logger.debug () 등으로 로깅
    ```python
      import logging
      logger = logging.getLogger(__name__)
      
      def post_list(request):
          logger.error('Something went wrong!')
    
    ```    
  
## [기초편] 장고 차근차근 시작하기 > 19 장고 템플릿 엔진
### 왜 템플릿을 사용하는가?
- 코드만으로 직접 복잡한 문자열을 조합하기 까다롭다.
    - 조합한 문자열이 조금만 복잡해져도 코드가 산으로..
- 복잡한 문자열을 좀 더 편리하게 조합할 수 있도록 도와주는 라이브러리
    - 단지 HTML 응답 뿐만이 아니라, 다양한 문자열 조합에 사용
    - 이메일, 푸쉬메세지, SMS
    
### "Stupid 장고 템플릿 언어"의 철학
- 장고의 기본 철학
    - 풍성한 Model
    - 비즈니스 로직이 없는 (Stupid) Template
    - 간결한 (Thin) View
- 템플릿 기능에 제한을 둠으로서 비즈니스 로직을 템플릿 단에 구현함을 방지
    - 비즈니스 로직은 Model에 그리고 Form/ModelForm 을 통한 유효성 검사 및 저장을 권장
    - 다른 템플릿 엔진을 씀으로서, 이러한 제약에서 벗어날 수 있으나, 비권장
    
### 템플릿 엔진 활용 주요코드
- django.shortcuts.render -> HttpResponse
- django.template.loader.render_to_string -> str

    ```python
        def render(request, template_name, context=None, content_type=None, using=None):
            content = loader.render_to_string(template_name, context, request, using=using)    
            return HttpResponse(content, content_type, status)
    ```    
    
### 장고의 빌트인 백엔드
- django.template.backends.django.DjangoTemplates
    - 장고에서의 일반적인 템플릿 엔진
    - 대개의 장고 라이브러리에서 사용하는 템플릿 엔진
    - 함수 호출은 가능하되, 인자없는 함수만 가능
        - 함수 호출 시에 소괄호를 쓰지 않습니다. Callable Object 라면 템플릿 엔진에서 알아서 호출

- django.template.backends.jinja2.Jinja2
    - 부분 지원
    
### 장고에서는 2개 템플릿 엔진만 쓸 수 있나요?
- 다른 템플릿 엔진도 물론 사용가능합니다만, 장고에서는 Django Template Engine에 한해서 다양한 기능을 지원하고 있습니다.
- 한 프로젝트에서 다수의 템플릿 엔진을 활성화할 수 있으나,
    - 하나의 render 수행 시에는 하나의 템플릿 엔진만 선택적으로 사용
    
### CBV에서의 템플릿 처리
- django.template.response.SimpleTemplateResponse 클래스에서 로직 구현
    - 특정 CBV에서 template_name 인자 지정을 통한, 템플릿 지정
    - CBV 종류에 따라, 모델 이름을 따라 template_name 자동 지정
       - ex) ListView 에서의 Post 모델 -> "앱이름/post_list.html"
       - 각 CBV마다의 기본 템플릿 경로를 활용하시면 (관례에 기반), 코드를 줄이실 수 있습니다.
       
### settings.TEMPLATES 설정 리스트
- BACKEND : 템플릿 엔진 지정
- DIRS : 템플릿을 둘 디렉토리 경로 리스트
- APP_DIRS: 앱별 templates 경로 추가 여부
- OPTIONS/ context_processors
    - 템플릿 내에서 디폴트 참조할 변수목록을 제공하는 함수 목록
    - 인자로 request를 받고, dict을 반환

### 최소한의 템플릿 settings
- 각 앱들을 위한 템플릿은 각 "앱/templates/" 경로에 배치
    - 장고 앱은 재사용성에 포커스가 맞춰져 있기 떄문    
- 프로젝트 전반적으로 사용할 템플릿은 DIRS에 명시한 경로에 배치

### 장고 템플릿 태그/필터
- 유틸리티 성격의 장고 템플릿 내에서 호출할 수 있는 함수 목록들
    - Django Template Tag {% 태그명 "인자1" "인자2" %} 와 같은 방식으로 호출
        - 필터보다 범용적인 문법
    - Django Template Filter : {{ 값|필터1:인자|필터2:인자|필터3 }} 와 같은 방식으로 호출
- 다양한 빌트인 템플릿 태그/필터가 제공
    - for/endfor, if/endif, include, load, verbatim 등
- 커스텀 템플릿 태그/필터 구현 지원
    - 주의 : 템플릿 태그/필터에 커스텀 함수를 구현할 수 있다고, 여기에 비즈니스 로직을 넣지는 마세요.
    - 유틸리티 목적으로만 사용하기
    
### 디폴트 에러 템플릿 경로
- django/views/defaults.py 내에서 다음 경로 지정
    - "400.html", "403.html", "404.html", "500.html"
    - 위 파일들을 구현하지 않으면, "기본 흰바탕 까만글씨 에러화면" 출력
    - 실제 서비스에서는 구현을 권장 


    
    
    
    











    
    
    
    
    
    
    
    
    
    
           
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      
    
    
    
    
    

























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
        
        
        
    






    
    
    











    
    
    
    
    
    
        
    

























    
    
    
    
    
    

 
 
 
 
 
        
    
    
    
    
    
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 






































