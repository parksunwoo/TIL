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
 
 
 
 
 
        
    
    
    
    
    
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 






































