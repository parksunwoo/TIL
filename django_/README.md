# TIL
Today I Learned

##  01 개발환경 구축하기
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

##  02 장고의 주요 구성 요소
### 장고 주요 기능들
- Function Based Views : 함수로 HTTP 요청처리
- Models : 데이터베이스와의 인터페이스
- Templates : 복잡한 문자열 조합을 보다 용이하게. 주로 HTML 문자열 조합 목적으로 사용하지만,
- Admin 기초 : 심플한 데이터베이스 레코드 관리 UI
- Logging : 다양한 경로로 메세지 로깅
- Static files : 개발 목적으로의 정적인 파일 관리
- Messages framework : 유저에게 1회성 메세지 노출 목적

- 웹서버, 데이터베이스서버, 캐시서버, 파일시스템의 기본구조

##  03 장고 앱
- 재사용성을 목적으로한 파이썬 패키지
 - 재사용성을 목적으로 둔 것이 아니라면, 하나의 장고 앱에서 현재 프로젝트의 거의 모든 기능을 구현해도 무방합니다
 - 하나의 앱이름은 현재 프로젝트 상에서 유일해야
 - 새롭게 생성한 장고앱이나 외부 라이브러리 형태의 장고앱은        
   settings.INSTALLED_APPS 에 등록 시켜줘야만 장고앱으로서 대접을 받는다.
   
##  04 VSCode 장고 디버깅 세팅하기
- 디버깅을 위해서 기본 적용되는 옵션
 - runserver 서버 시작옵션 --norelod --nothreading
 - 디버깅 메뉴를 통한 명시적인 재시작 및 정
- 다양한 pylint 메세지
 - 파이썬 정적 코드 분석툴

##  05 URLConf와 정규 표현식
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

##  06 다양한 응답의 함수 기반 뷰 만들기
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

##  07 적절한 HTTP 상태코드로 응답하기
### HTTP 상태코드
- 웹 서버는 적절한 상태코드로서 응답
- 각 HttpResponse 클래스마다 고유한 status_code 가 할당
- REST API를 마늗ㄹ 때, 특히 유

##  08 장고 쉘
- SQL 출력 옵션
 - 쉘 > python manage.py shell_plus --print-sql
 - 혹은 settings.SHELL_PLUS_PRINT_SQL = True


##  09 장고 모델 (ORM)
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
    
##  10 장고 모델 필드
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
  
##  11 마이그레이션을 통한 데이터베이스 스키마 관리
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

##  12 장고 admin을 통한 데이터 관리
### django admin
- djnago.contrib.admin 앱을 통해 제공
    - 디폴트 경로: /admin/ -> 실제 서비스에서는 다른 주소로 변경 권장
- 모델 클래스 등록을 통해, 조회/추가/수정/삭제 웹UI를 제공
    - 서비스 초기에 관리도구로서 사용하기에 제격
    - 관리도구 만들 시간을 줄이고 End - User 서비스에 집중
    
##  13 모델을 통한 데이터 조회
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
    
##  14 모델을 통한 데이터 생성/수정/삭제
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

##  15 관계를 표현하는 모델 필드
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

### RDBMS이지만 DB따라 NoSQL 기능도 지원

###   

##  16 django-debug-toolbar 를 통한 SQL 디버깅
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
    
    - django.db.reset_queries() 통해서 수동 초기화도 가능
    
      
    
##  17 장고 Logging과 SQL Logging 처리
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



##  18 데이터베이스 정규화/비정규화(제외)



##  19 장고 템플릿 엔진

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



##  20 Jinja2 템플릿 언어도 같이 써보기

### 장고 초심자는 장고 템플릿 언어에 먼저 집중
- 장고 템플릿 언어 (이하 DTL) 를 통해
    - 장고 기본 기능과 수많은 써드파티 라이브러리들이 구현
- Jinja2로의 확장은 장고 초심자에게는 너무 이른 호기심

### Jinja2 템플릿 언어
- 장고 템플릿 언어의 영향을 받음
    - 문법적으로 유사하지만, 보다 유연한 문법
    - 가장 큰 차이 : 템플릿 내에서 함수 호출 시에 소괄호를 쓴다
        - 즉, 다수 인자 지정이 가능
    - File System Loader 만 지원하기에, 앱별 디렉토리에 템플릿 지정 불가
- 아직 장고에서는 Jinja2에 대해 부분적인 지원
- 필요한 라이브러리 pip install jinja2

### 장고 템플릿 언어와의 문법적인 차이 포인트
- Jinja2에서는 함수 호출시에 괄호를 사용하여 자유도를 높임

|구분|Jinja2|Django Template Language|
|------|---|---|
|함수호출|{{ post.get_comments() }}| {{ post.get_comments }}|
|필터|{{ tags join(" , ") }}|{{ tags join:" , " }}|

### django-jinja 
- 장고/Jinja2 통합 라이브러리
    - 장고 기본에서의 Jinja2 지원만으로는 부족.
- 기존 DTL 코드를 이에 맞춰 사용하기 위해서는, 마이그레이션 필요



##  21 장고가 템플릿 파일을 찾는 원리

### Django Template Loader
- 다수 디렉토리 목록에서 지정 상대경로를 가지는 템플릿을 찾아줌.
    - 다양한 로더가 지원되며, 템플릿 설정의 OPTIONS내 loader를 통해 각기 활성화
    - 우선순위 : 파일시스템 로더 > 앱 디렉토리 로더
- 다양한 템플릿 로더
    - 파일 시스템 로터
        - settings.TEMPLATES의 DIRS=[] 설정에 의존
        - 지정 경로 리스트를 리스트에 추가
    - 앱 디렉토리 로더
        - settings.TEMPLATES의 APP_DIRS=True 설정에 의존
        - 각 장고 앱 디렉토리 내, templates 경로를 리스트에 추가
    - cached 로더
        - 템플릿은 매번 파일읽기/컴파일 과정이 들어가는 데, 이를 로컬 메모리에 캐싱
        
### 템플릿 디렉토리 리스트
1. 템플릿 로더는 서버가 시작할 때마다, 템플릿 로더 설정에 기반하여 "템플릿 디렉토리 리스트"를 생성
    - 즉, 개발서버에서 settings.DEBUG = True 시에는 파이썬 소스코드가 변경될 때마다 서버를 재시작하기에, 소스코드 변경시마다
        "템플릿 디렉토리 리스트"를 새로이 생성
2. "find template" 로직 수행 시에, 이미 생성된 "템플릿 디렉토리 리스트"에서 템플릿을 순차적으로 찾음

### 디렉토리 매칭 메커니즘
- 템플릿 디렉토리 리스트 예
    - askcompany/templates/ 
    - blog/templates/ 
    - shop/templates/
- render(request, "blog/post_list.hml")를 호출할 경우, 순차적으로
    - appcompany/templates/blog/post_list.html -> 매칭 시도 시작
    - blog/templates/blog/post_list.html 
    - shop/templates/blog/post_list.html
    
### app/templates/app은 namwspace 역할
- 만약 다음과 같이 템플릿 파일이 있을 경우,
    - appcompany/templates/post_list.html
    - blog/templates/post_list.html 
    - shop/templates/post_list.html
- shop/templates/post_list.html 파일 활용을 위해
    - render(request, "post_list.html")로 호출해보지만,
    - 사용되는 것은 매번 askcompany/templates/post_list.html 입니다.
- 권장
    - 앱 내 디렉토리 배치는 app/templates/app 구조를 필히
    - 그리고 "app/파일명" 구조로 활용



##  22 템플릿 상속을 통한 중복 제거

### 템플릿 상속의 필요성
- 각 뷰에 연결된 템플릿른 독립적으로 동작
    - 그런데, 독립적으로 동작하는 템플릿은 같은 레이아웃/스타일을 가지게 된다
        - 네이버 블로그 내 각 링크들은 서로 다른 주소(장고에서는 서로 다른 뷰/템플릿) 이지만, 같은 스타일을 가진다.
    - 즉, 템플릿 코드 중복이 발생
- 이러한 코드 중복을 해결하기 위한 솔루션 -> 템플릿 상속

### 템플릿 상속의 특징
- 기본 특징
    - 상속은 여러 단계로 이뤄질 수 있다.
    - block에는 이름을 할당해야하며, 이름을 통해 구분하며, 한 템플릿 내에서 그 이름은 유일
- 부모 템플릿
    - 전체 레이아웃을 정의
    - 자식 템플릿이 비집고 들어올 수 있는 영역(block)을 다수 정의가능
        - block이 없다면, 자식 템플릿은 상속만 받을 뿐, 어떠한 변경도 수행할 수 없다.
- 자식 템플릿
    - 상속받을 부모를 1개 지정할 수 있다.
    - 상속받은 부모에서 정의한 block에 대해, block 내용을 재정의하여 그 내용을 추가/변경/제거
        - block 바깥에 정의한 내용은 모두 무시
        - 부모가 정의하지 않은 block을 재정의하여도 이는 무시
        
### 사용하는 템플릿 태그
- {% extends "부모템플릿경로" %}
- {% block 블럭이름 %} 블럭내용 {% endblock %}
    - 부모에서 사용하면, 블럭 정의
    - 자식이 사용하면, 부모의 블록 재정의
- {{ block.super }}
    - 자식 템플릿에서 사용할 때, 지정 위치에 부모 block 내용 출력
    
### 기본적으로 2단계의 상속을 추천
- 프로젝트 전반적인 레이아웃 템플릿 : askcompany/templates/layout.html
    - 각 앱 별 레이아웃 템픒릿 : app/templates/app/layout.html -> layout.html 상속
        - 템플릿#1 : app/templates/app/post_list.html -> layout.html 상속   
        - 템플릿#2 : app/templates/app/post_detail.html -> layout.html 상속   
        - 템플릿#3 : app/templates/app/post_form.html -> layout.html 상속   



## 23 자주 사용하는 템플릿 필터

### 장고 템플릿 필터
- 함수 형태로 구현하여, 템플릿에 등록
- 언제 사용하는가?
    - 템플릿 단에서 출력된 값에 대해서, 값 변환이 필요할 
    - ex) 개행 적용, 숫자에 콤마찍기, 소스코드 highlight 등

- 필터에서 취하는 인자 (1개 ~2개)
    - 인자 A : 변환할 값
    - 인자 B (옵션) : 추가 옵션
    
### add
- 정수 뿐만 아니라, 다양한 같은 타입에 대한 + 연산 지원
{{ value|add:"2" }}

### cut
{{ value|cut:" " }}

### 유용한 값 처리
- default : 값이 False 판정일 때, 인자로 지정한 디폴트 값을 사용
    - default_if_none: 값이 None 판정일 때, 인자로 지정한 디폴트 값을 사용
- filesizeformat : 숫자를 파일크기로서 단위를 붙임
    - 지원 단위 : KB, MB, GB, TB, PB
    - ex) 123456789 -> 117.7 MB
- join : 문자열 join과 유사
    - 언제 리스트를 하나로 합쳐서 표현하고자 할 때
- linebreaks : 1개 개행은 <br> 태그, 2개 개행은 <p> 태그로 변환
    - 줄바꿈 시에 유용
- linebreaksbr : 모든 개행을 <br> 태그로 변환
- pprint : pprint.pprint() 래핑. 리버깅 목적의 출력
- truncatechars : 지정 글자수 만큼을 자르고, 말줄임표(...)를 붙임.
    - truncatechars_html: 글자 단위로 html 요소를 살려서 자르기
    - truncatewords: 단어 단위로 자르기
    - truncatewords: 단어 단위로 html 요소를 살려서 자르기
    
### URL 링크 만들기
- urlize : URL과 이메일을 a 태그로 변환
    - URL은 링크 문자열이 필히 http://, https://, www. 로 시작해야함.
    - 최상위 도메인이 .com, .edu, .gov, .int, .mil, .net, .org 중 하나여야함
    - 생성된 링크에 rel="nofollow"가 추가 -> 크롤러에게 추적방지 요청
    - 보다 유연한 링크 변환을 위해, javascript 라이브러리를 사용해볼 수도.
- urlizetrunc 
    - urlize와 동일하지만, 링크 텍스트를 지정 길이로 자르기
    
### escape 처리와 SafeText
- escape : 문자열의 HTML요소를 변환 <-> safe
    - 이를 통해 사이트 개발자가 의도치않은 HTML/Javascript 수행을 방지
        - < (&lt), > (&gt), 홑따옴표(&#39), 쌍따옴표(&quot;), &(&amp;) 를 변환
        - 장고 템플릿 언어에서는 디폴트로 escape 처리
        - autoescape 태그를 통한 처리도 가능
- safe : escape 처리되지 않도록, SafeText 로 래핑
    - 파이썬 객체의 값을

### date
- 지정 포맷으로 날짜 포맷팅
- 관련 settings
    1. DATE_FORMAT : 디폴트 "N j, Y" (예: "Feb. 4, 2003")
    2. DATETIME_FORMAT : 디폴트 "N j, Y, P" (예: "Feb. 4, 2003, 4 pm")
    3. SHORT_DATE_FORMAT : 디폴트 "m/d/Y" (예: "12/31/2003")
    3. SHORT_DATETIME_FORMAT : 디폴트 "m/d/Y P" (예: "12/31/2003 4 pm")
- 위 포맷 중 택일 지정하거나, 커스텀 지정. 미지정시에 DATE_FORMAT 으로 지정
- settings.USE_L10N = True 시에는 settings.LANGUAGE_CODE에 맞춰, 번역 사용

### time
- 지정 포맷으로 시간 포맷팅
- 관련 settings
    1. TIME_FORMAT : 다폴트 "P" (예 "4 p.m")
- 커스텀 지정. 미지정시에 TIME_FORMAT 으로 지정
- settings.USE_L10N = True 시에는 settings.LANGUAGE_CODE 에 맞춰 번역 사용

### json script 필터
- 파이썬 객체를 JSON 으로의 처리
    - 파이썬 문법과 JSON 문자열 문법이 비슷한 측면이 있기에, 그대로 템플릿에 출력하여, 사용하기도 했었음.
    - django.core.serializers.json.DjangoJSONEncoder 를 통한 json 직렬화
    - 변환된 JSON 문자열에 대해서 '>', '<', '&' 문자열 ESCAPE 처리 (XSS 공격방지)
    

{{ value|json_script:"my-id" }}

<script id="my-id" type="application/json">{"hello": "world"}</script>
var value = JSON.parse(document.getElementById('my-id').textContent);



## 24. 자주 사용하는 템플릿 태그

### 장고 템플릿 태그
- 함수/클래스 형태로 구현하여, 템프릿에 등록
    - 원하는 개수 만큼의 인자를 받을 수 있습니다.
    - 템플릿에 따라 현재 템플릿 내 Context를 받을 수도 있습니다.
- 언제 사용하는가?
    - 단순 값 변환이 아닌, 다양한 처리가 필요할 때
        - ex) for/endfor, if/endif, ifchanged 등
    - 템프릿 필터보다 많은 인자 처리가 필요할 때
- 필터에서 취하는 인자 (0개 이상~)

### 기본 태그
- extends : 템플릿 상속
- load : 빌트인 템플릿태그/필터 외에 추가 로딩
    - 각 장고앱의 templatetags/ 디렉토리 내, 파일명을 지정
- include : 템플릿 가져오기
    - 현재의 context가 그대로 전달
    - with 옵션을 통해 추가 키워드 인자 전달
        - only 추가옵션을 통해 지정
- block ... endblock : 블락 영역 지정
    - 템플릿 상속을 위한 영역 이정
- comment ... endcomment : 주석 영역 지정

### 조건문 / 반복문
- if ... elif ... else ... endif : 조건문
- ifchanged ... endifchanged : 대상 값이 변경될 시에, 렌더링
    - 인자없이 사용할 경우
        - 대상 값: 해당 블락에 속한 템플릿 내역
    - 인자를 1개 이상 사용할 경우
        - 대상 값: 인자 목록
- for ... empty ... endfor : 반복문
    - empty는 해당 Iterable Object가 비었을 때, 수행
    
### 템플릿 태그(1)
- lorem: 무작위 채우기 텍스트 생성
     - {% lorem 횟수 단어_단락_선택 랜덤여부 %}
     - 횟수 : 디폴트 1
     - 단어_단락_선택 : 단어(w), HTML단락(p), PlainText단락(b, 디폴트)
- spaceless ... endspaceless
    - HTML 태그 사이의 공백을 모두 제거
- url : URL Reverse
- verbatim ... endverbatim
    - 해당 역열에 대해서 템플릿 엔진 처리를 하지 않습니다.
    
### 템플릿 태그(2)
- with ... endwith
    - 템플릿 단계에서 변수 생성 문법
    

총 {{ business.employees.count }} 명의 직원이 있습니다.
{{ business.employees.count }} 명의 직원 중에 3명이 업무 중에 있습니다.

{% with total=business.employees.count %}
    총 {{ total }} 명의 직원이 있습니다.
    {{ total }} 명의 직원 중에 3명이 업무 중에 있습니다.
{% endwith %}

## 

## 25. static 파일을 다루는 방법

### Static & Media 파일

- Static 파일
  - 개발 리소스로서의 정적인 파일( js, css, image 등)
  - 앱 / 프로젝트 단위로 저장/서빙
- Media 파일
  - FileField / ImageField  를 통해 저장한 모든 파일
  - DB 필드에는 저장경로를 저장하며, 파일은 파일 스토리지에 저장
  - 프로젝트 단위로 저장/서빙

### Static 파일,관련 settings 예시

- 각 설정의 디폴트 값
  - STATIC_URL = None
    - 각 static 파일에 대한 URL Prefix
      - 템플릿 태그 {% static "경로" %} 에 의해서 참조되는 설정
    - 항상 / 로 끝나도록 설정
  - STATICFILES_DIRS = []
    - File System Loader 에 의해 참조되는 설정
  - STATIC_ROOT = None
    - python manage.py collectstatic 명령이 참조되는 설정
    - 여러 디렉토리로 나눠진 static 파일들을 이 경로의 디렉토리로 복사하여, 서빙
    - 배포에서만 의미가 있는 설정

### 추천 settings

```python
STATIC_URL = '/static'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
  		os.path.join(BASE_DIR, 'askdjango', 'static')
]
```

### Static Files Finders

```python
STATICFILES_FINDERS = [
  'django.contrib.staticfiles.finders.FileSystemFinder'
  'django.contrib.staticfiles.finders.AppDirectoriesFinder'
]
```

- Template Loader 와 유사
  - 설정된 Finders 를 통해 , static 템플릿이 있을 디렉토리 목록을 구성
    - 장고 서버 초기 시작 시에만 1회 작성
    - 디렉토리 목록에서 지정 상대경로를 가지는 static 파일 찾기
  - 대표적인 2가지 Static Files Finders
    - APP Directories Finder
      - "장고앱/static/" 경로를 "디렉토리 목록"에 추가
    - File System Finder
      - settings.STATICFILES_DIRS 설정값을 "디렉토리 목록"에 추가

### 템플릿에서 static URL 처리 예시(1)

- 방법1) settings.STATIC_URL, Prefix 를 하드코딩하기

  - 하지만 settings.STATIC_URL 설정은 언제라도/ 프로젝트마다 변경될 수 있음. 하드코딩하는 것이 번거롭기도하고 변경이 되었을 때 하나하나 수정해줘야 함

  - 무엇보다, 배포 시에는 static_url 설정값이 변경됩니다.

    - 클라우드 저적 스토리지나 CDN 사용시

      ```html
      <img src="/static/blog/title.png" />
      ```

### 템플릿에서 static URL 처리 예시(2)

- 방법2) Template Tag를 통한 처리

  - 프로젝트 설정에 따라, 유연하게 static url prefix 가 할당됩니다.

  ```html
  {% load static %}
  <img src="{% static "blog/title.png" %}" />
  ```

### 개발환경에서의 static 파일 서빙

- 개발서버를 쓰고, and settings.DEBUG = True 일 때에만, 지원
  -  프로젝트/urls.py 에 Rule이 명시되어 있지 않아도, 자동 Rule 추가
  - 이는 순수 개발목적으로만 제공
- 개발서버를 쓰지 않거나, settings.DEBUG = False 일 때에는
  
- 별도의 static 서빙 설정을 해줘야합니다
  
- static 서빙을 하는 여러가지 방법

  1) 클라우드 정적 스토리지나 CDN 서비스를 활용

  2) apche/nginx 웹서버 등을 통한 서빙

  3) 장고를 통한 서빙

  	- whitenoise 라이브러리 활용

### collectstatic 명령

- 실 서비스 배포 전에는 필히 본 명령을 통해, 여러 디렉토리에 나눠져있는 static 파일들을 한 곳으로 복사
  - 복사하는 대상 디렉토리 : settings.STATIC_ROOT
  - 왜냐하면 여러 디렉토리에 나눠 저장된 static 파일들의 위치는 "현재 장고 프로젝트" 만이 알고있음. 외부 웹서버는 전혀 알지 못함
  - 외부 웹서버에서 finder 의 도움없이도 static 파일을 서빙하기 위함.
  - 한 디렉토리에 모두 모여있기에, finder의 도움이 필요가 없음

### 외부 웹서버에 의한 static/media 컨텐츠 서비스

- 정적인 컨텐츠는 외부 웹서버를 통해 처리하면, 효율적인 처리
- 정적 컨텐츠만의 최적화 방법 사용
  - Memcache/redis 캐시 등
  - CDN (Content Delivery Network)

### nginx  웹서버에서의 static 설정 예시

```javascript
server{
  location /static{
    autoindex off;
    alias /var/www/staticfiels;		# settings.STATIC_ROOT
  }
  location /media {
    autoindex off;
    alias /var/www/media;					# settings.MEDIA_ROOT
  }
}
```



### 배포 시에 static 처리 프로세스

1. "서비스용 settings"에 배포 static 설정

2. 관련 클라우드 스토리지 설정, 혹은 아파치/ ngix static 설정

3. 개ㄹ이 완료된 static 파일을, 한 디렉토리로 복사

   ```python
   python manage.py collectstatic --settings=서비스용 settings
   ```

   - storage 설정에 따라, 한 번에 클라우드 스토리지로의 복사를 수행되기도 함.
   - settings.STATIC_ROOT 경로로 복사됨

4. settings.STATIC_ROOT 경로에 복사된 파일들을 배포서버로 복사

   - 대상 : 클라우드 스토리지, 혹은 아파치/nginx 에서 참조할 경로

5. static 웹서버를 가리키도록 settings.STATIC_URL 수정



### static 관련 라이브러리

- Django-storages
  - Azure Storage, Amazon S3, Google Cloud Storage, FTP 등 지원
  - 

## 26. Media 파일을 다루는 방법

### Media 파일

- 실제로 문자열을 저장하는 필드(중요)

### Media 파일 처리 순서

1. HttpRequest.FILES 를 통해 파일이 전달
2. 뷰 로직이나 폼 로직을 통해, 유효성 검증을 수행하고,
3. Field/ImageFiled 필드에 "경로(문자열)"를 저장하고,
4. settings.MEDIA_ROOT 경로에 파일을 저장합니다.

### Media 파일, 관련 settings 예시

- 각 설정의 디폴트 값
  - MEDIA_URL = ""
    - 각 media 파일에 대한 URL Prefix
      - 필드명.url 속성에 의해서 참조되는 설정
  - MEDIA_ROOT = ""
    - 파일필드를 통한 저장 시에, 실제 파일을 저장할 ROOT 경로

#### 추천 settings

```python
MEDIA_URL = '/media'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### FileField 와 ImageField

- FileField
  - File Storage API를 통해 파일을 저장
    - 장고에서는 File System Storage 만 지원. Django-storages 를 통해 확장 지원
  - 해당 필드를 옵션 필드로 두고자 할 경우, blank = True 옵션 적용
- ImageField 
  - Pillow 를 통해 이미지 width/height 획득
    - Pillow 미설치 시에, ImageField 를 추가한 make migrations 수행에 실패
- 위 필드를 상속받은 커스텀 필드를 만드실 수도 있습니다.
  - Ex) PDFField, ExcelField 등

### 모델 필드 예시

```python
class Post(models.Model):
  		author_name = models.CharField(max_length=20)
  		title = models.CharField(max_length=100)
  		content = models.TextField()
      photo = models.ImageField(blank=True)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)      
```

### 사용할 만한 필드 옵션

- blank 옵션
  - 업로드 옵션처리 여부
  - 디폴트 : False
- upload_to 옵션
  - settings.MEDIA_ROOT 하위에서 저장한 파일명/경로명 결정
  - 디폴트 : 파일명 그대로 settings.MEDIA_ROOT 에 저장
    - 추천) 성능을 위해, 한 디렉토리에 너무 많은 파일들이 저장되지 않도록 조정하기
  - 동일 파일명으로 저장 시에, 파일명에 더미 문자열을 붙여 파일 덮어쓰기 방지

### 파일 업로드 시에 HTM Form enctype

- form method 는 필히  POST로 지정

  - GET의 경우 enctype이 "application/x-www-form-urlencoded"로 고정

- form enctype을 필히 "multipart/form-data" 로 지정

  - "Application/x-www.form-urlencoded"의 경우, 파일명만 전송

    ```html
    <form action="" method="post" enctype="multipart/form-data">
      {% csrf_token %}
      <table>
        	{{ form.as_table }}
      </table>
      <input type="submit" />
    </form>
    ```

### upload_to 인자

- 파일 저장 시에 upload_to 함수를 호출하여, 저장 경로를 계산
  - 파일 저장 시에  upload_to 인자를 변경한다고 해서, DB에 저장된 경로 값이 갱신되진 않습니다.
- 인자 유형
  - 문자열로 지정
    - 파일을 저장할 "중간 디렉토리 경로" 로서 활용
  - 함수로 지정
    - "중간 디렉토리 경로" 및 "파일명"까지 결정 가나ㅡㅇ

### 파일 저장경로

- travel-20181225.jpg 파일을 업로드할 경우
  - MEDIA_ROOT/travel-20181225.jpg 경로에 저자되며,
  - DB에는 "travel-20181225.jpg" 문자열을 저장합니다.

### 파일 저장 경로 / 커스텀

upload_to  옵션

- 한 디렉토리에 파일을 너무 많이 몰아둘 경우, OS 파일찾기 성능 저하. 디렉토리 Depth가 깊어지는 것은 성능에 큰 영향 없음
- 필드 별도, 다른 디렉토리 저장경로를 가지기
  - 대책1) 필드 별로 다른 디렉토리에 저장
    - phto = models.ImageField(upload_to='blog')
    - phto = models.ImageField(upload_to='blog/photo')
  - 대책2) 업로드 시간대 별로 다른 디렉토리에 저장
    - upload_to 에서 strftime 포맷팅을 지원
    - photo = models.ImageField(upload_to='blog/%Y/%m/%d')

### uuid 를 통한 파일명 정하기 예시

```python
import os
from uuid import uuid4
from django.utils import timezone

def uuid_name_upload_to(instance, filename):
  	app_label = instance.__class__._meta.app_label  # 앱 별로
    cls_name = instance.__class__._name.lower()     # 모델 별로
    ymd_path = timezone.now().strftime('%Y/%m/%d')  # 업로드하는 년/월/일 별로
    uuid_name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower() # 확장자 추출하고, 소문자로 변환
    return '/'.join([
      app_label,
      cls_name,
      ymd_path,
      uuid_name[:2],
      uuid_name + extension,
    ])
```



### 템플릿에서 media URL 처리 예시

- 필드의 .url 속성을 활용하세요.

  - 내부적으로 settings.MEDIA_URL과 조합을 처리

    - <img src="{{ post.photo.url }}" %}" />

  - 필드에 저장된 경로에 없을 경우, .url 계산에 실패함에 유의. 그러니 안전하게 필드명 저장유무를 체크

    ```python
    {% if post.phto %}
    	<img src="{{ post.photo.url }}" %}" />
    {% endif %}
    ```

- 참고
  - 파일 시스템 상의 절대경로가 필요하다면, .path 속성을 활용하세요
    - settings.MEDIA_ROOT 와 조합

### 개발환경에서의 media 파일 서빙

- static 파일과 다르게, 장고 개발서버에서 서빙 미지원

- 개발 편의성 목적을 직접 서빙 Rule 추가 가능

  ```python
  from django.conf import settings
  from django.conf.urls.static import static
  
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

### File Upload Handler

- 파일크기가 2.5MB 이하일 경우
  - 메모리에 담겨 전달
  - MemoryFileUploadHandler
- 파일크기가 2.5MB 초과일 경우
  - 디스크에 담겨 전달
  - TemporaryFileUploadHandler
- 관련 설정
  - settings.FILE_UPLOAD_MAX_MEMORY_SIZE
    - 2.5MB
    - 

## 27. 개발환경에서 static 캐싱 무효화하기

### Private browser caches 

- 브라우저 단에서는 컨텐츠를 캐싱하여, 매번 서버로 컨텐츠를 요청하지 않고 캐싱된 컨텐츠를 사용함으로서, 페이지 렌더링 시간을 단축시킵니다
- 캐싱  Key : 요청 URL
- 캐싱 만료 정책 : Cache-Control 헤더 

  

### 개발할 때에는, 쉴새없이 변경되는~

- 하지만 종종 이전 내역이 브라우저 캐싱되어 변경된 내역이 반영되지 않기도
- 이때 변경된 내역이 반영되게 하려면
  - 1) 브라우저의 캐시 내역을 강제로 비우기
  - 2) 해당 정적 파일 응답에서 cache-control 헤더 조절하기
  - 3) 해당 정적 파일의 파일명을 변경
  - 4) 해당 정적 파일, 요청 URL에 대해 Dummy QueryString을 추가
    - Query String 값이 변경되면 브라우저에서는 새로운 리소스로 인식합니다
      - 웹프론트엔드에서 같은 URL로 Ajax 요청시마다  dummy QueryString 을 붙이는 것과 같은 이치

### 커스텀 Template Tag를 통해, Dummy Query String을 붙여봅시다

```python
from time import time
from django import template
from django.conf import settings
from django.template.static import StaticNode

register = template.Library()

class FreshStaticNode(StaticNode):
  	def url(self, context):
      url = super().url(text)
      if settings.DEBUG():
        url += '?_={}'.format(int(time())) # Dummy Qeury String 추가
      return url
    
@register.tag('fresh_static')
def do_static(parser, token):
  return FreshStaticNode.handle_token(parser, token)
```



## 28. URL Reverse를 통해 유연하게 URL 생성하기

### URL Dispatcher

urls.py  변경만으로  "각 뷰에 대한 URL"이 변경되는 유연한  URL 시스템

```python
# "/blog/", "/blog/1/" 주소로 서비스하다가
urlpatterns = [
  path('blog/', blog_views.post_list, name="post_list"),
  path('blog/<int:pk>/', blog_views.post_detail, name='post_detail'),
]

# 다음과 같이 변경을 하면,
# 이제 "/weblog/", "/weblog/1/" 주소로 서비스하게 됩니다
urlpatterns = [
  path('weblog/', blog_views.post_list, name="post_list"),
  path('weblog/<int:pk>/', blog_views.post_detail, name='post_detail'),
]


```

### URL Reverse의 혜택

- 개발자가 일일이 URL을 계산하지 않아도 됩니다. 
- URL이 변경되더라도, URL Reverse 가 변경된 URL을 추척

### 직접 URL을 계산한다면 ~

1. blog앱 Post 목록을 볼려면, post_list 뷰를 호출해야하니깐,
2. Urls.py 를 뒤적뒤적거리며,  URL계산계산
3. 계산완료! -> /blog/ 주소를 쓰면 되겠네

### URL 계산은 장고에게 양보하세요

1. blog앱 Post 목록을 볼려면,  post_list 뷰를 호출해야하니깐,

### URL Reverse 를 수행하는 4가지 함수 (1)

- url 템플릿태그
  - 내부적으로 reverse 함수를 사용
- reverse 함수
  - 매핑 URL이 없으면 NoReverseMatch 예외 발생
- resolve_url 함수
  - 매핑 URL이 없으면 "인자 문자열"을 그대로 리턴
  - 내부적으로 reverse 함수를 사용
- redirect 함수
  - 매핑 URL이 없으면  "인자 문자열"을 그대로 URL로 사용
  - 내부적으로  resolve_url 함수를 사용



### URL Reverse 를 수행하는 4가지 함수 (2)

```python
{% url "blog:post_detail" 100 %}
{% url "blog:post_detail" pk=100 %}

reverse('blog:post_detail', args=[100])
reverse('blog:post_detail', kwargs={'pk': 100})

resolve_url('blog:post_datail', 100)
resolve_url('blog:post_datail', pk=100)
resolve_url('/blog/100/')

redirect('blog:post_detail', 100)
redirect('blog:post_detail', pk=100)
redirect('/blog/100/')
```

### 모델 객체에 대한 detail 주소계산

- 매번 다음과 같은 코드로 하실수도 있겠지만

  ```python
  resolve('blog:post_detail', pk=post.pk)
  redirect('blog:post_detail', pk=post.pk)
  {% url 'blog:post_detail' post.pk %}
  ```

- 다음과 같이 사용하실 수도 있습니다 어떻게?

  ```python
  resolve_url(post)
  redirect(post)
  {{ post.get_absolute_url }}
  ```

### 모델 클래스에 get_absolute_url()

- resolve_url 함수는 가장 먼저 get_absolute_url() 함수의 존재여부를 체크하고, 존재할 경우 reverse를 수행하지 않고 그 리턴값을 즉시 리턴

  ```python
  def resolve_url(to, *args, **kwargs):
      if hasattr(to, 'get_absolute_url'):
        	return to.get_absolute_url()
      try:
        	return reverse(to, args=args, kwargs=kwargs)
      except NoReverseMatch:
  ```

### resolve_url/ redirect 를 위한 모델 클래스 추가 구현

```python
from django.urls import reverse

class Post(models.Model):
  		def get_absolute_url(self):
          return reverse('blog:post_detail', args=[self.pk])
```

### 그 외 활용

- CreateView / UpdateView
  - success_url 을 제공하지 않을 경우, 해당 model instance 의 get_absolute_url 주소로 이동이 가능한지 체크하고 이동이 가능할 경우 이동
  - 생성/수정하고 나서 Detail 화면으로 이동하는 것은 자연스러운 시나리오
- 특정 모델에 대한 Detail 뷰를 작성할 경우
  - Detail 뷰에 대한 URLConf 설정을 하자마자 필히 get_absolute_url 설정을 



## 29. 장고 Form 을 쓰지 않고, 글 생성/수정 구현하기

### 장고 스타일로 Item New

```python
chrome <-> django
# GET요청
1) http://localhost:8000/shop/item/new/
				2) 빈 Form 화면을 보여줍니다.
# POST요청
3) 유저가 Form을 채우고, 작성후에 "저장"을 요청합니다
				4) 입력값 유효성 검사를 한 후에,
  			a. 검사를 통과 못했을 경우에, 다시 Form을 보여주고 재입력을 요청
    		b. 검사를 통과했을 경우에, 데이터베이스에 저장하고, 다른 주소로 이동
```

### 장고 스타일로 Item Edit

```python
chrome <-> django
# GET요청
1) http://localhost:8000/shop/item/<int:pk>/edit 페이지 방문
				2) 지정 pkdml item이 없을 경우, 404처리
						Item이 있을 경우, Item 필드로 채운 Form 화면을 보여줍니다.
# POST요청
3) 유저가 Form을 내용을 변경하고, 작성후에 "저장"을 요청합니다.
				4) 입력값 유효성 검사를 한 후에,
  			a. 검사를 통과 못했을 경우에, 다시 Form을 보여주고 재입력을 요청
    		b. 검사를 통과했을 경우에, 데이터베이스에 저장하고, 다른 주소로 이동
```











