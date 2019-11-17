
A curated list of Two Scoops of Django https://www.twoscoopspress.com/

## 코어
- Django https://www.djangoproject.com/
- django-debug-toolbar https://django-debug-toolbar.readthedocs.io/en/latest/
  - 장고 디버깅을 위한 디스플레이 패널
- django-model-utils https://pypi.org/project/django-model-utils/
  - 시계열 모델을 포함한 유용한 모델 유틸리티
- sphinx http://www.sphinx-doc.org/en/master/
  - 파이썬 프로젝트 문서화 도구

## 비동기
- celery http://www.celeryproject.org/
  - 분산 태스크 큐
- flower https://pypi.org/project/flower/
  - 셀러리 태스크 관리. 모니터링 도구
- rq https://pypi.org/project/rq/
  - 가벼우면서 간단한 백그라운드 작업 생성과 프로세싱 라이브러리
- django-rq https://github.com/rq/django-rq
  - RQ(Redis Queue)와 장고의 통합을 제공하는 간단한 앱
- django-background-tasks https://django-background-tasks.readthedocs.io/en/latest/
  - 데이터베이스 기반의 비동기 태스크 큐

## 데이터베이스
- django-db-tools https://pypi.org/project/django-db-tools/
  - 데이터베이스를 읽기 전용으로 만들거나 반대로 읽기 전용 모드에서 일반 모드로 변경하는 데 큰 도움이 된다
- psycopg2 https://pypi.org/project/psycopg2/
  - PostgreSQL 데이터베이스 어댑터
  
## 배포
- circus 
  - 다중 프로세스와 소켓을 실행하고 관리하는 프로그램. 모질라에서 이용한다. 그 복잡성 떄문에 작은 프로젝트에는 적합하지 않다
- dj-database-url
  - 허로쿠 데이터베이스 접근을 간단하게 만들어 주는 장고 유틸리티
- django-heroku-memcacheify 
  - 허로쿠용 Memcached 설정
- Fabric
  - 원격 실행과 배포를 위한 간단한 도구
- Invoke
  - Fabric과 비슷하다. 파이썬3에서도 작동
- Paver
  - 쉬운 빌드와 분산 배포를 위한 스크립트
- Supervisor http://supervisord.org/
  - 사용자가 유닉스 계열 운영 체제에서 여러 프로세스를 컨트롤하고 모니터링하게 해 주는 클라이언트/서버 프로그램
  
## 폼
- django-crispy-forms https://django-crispy-forms.readthedocs.io/en/latest/
    - 장고 폼의 렌더링 조종 도구. 기본으로 트위터 부트스트랩을 이용하나 변경할수 있음
- django-floppyforms 
  - django-crispy-forms 과 함게 쓸 수 있는 폼 필드, 위젯, 레이아웃
- django-forms-bootstrap
  - 장고 폼과 트위터 부트스트랩을 이용하기 위한 간단한 폼 필터
- django-forms-builder
  - 어드민 인터페이스에서 어드민이 스스로의 폼을 만드는 기능을 제공하는 장고의 재사용 가능한 앱
  
## 로깅
- logutils 
    - 로깅에 여러 가지 유용한 핸들러를 추가
- Sentry https://sentry.io/welcome/
    - 오픈 소스 기반의 훌륭한 에러 수집 서비스
- App Enlight https://getappenlight.com/
    - 프로젝트의 에러와 성능 이슈를 추적
- Newrelic https://newrelic.com/
    - 실시간 로깅과 수집 플랫폼
    
## 프로젝트 템플릿
- cookiecutter-django https://github.com/pydanny/cookiecutter-django
    - 샘플 프로젝트 레이아웃
- cookiecutter https://github.com/cookiecutter/cookiecutter
    - 장고에만 국한되지 않은 프로젝트와 앱 템플릿 생성용 명령행 유맅리티. 수 많은 테스트를 거쳤으며 문서화가 잘 되어 있다.    
- django-kevin https://github.com/imkevinxu/django-kevin
    - 허로쿠 배포에 최적화된 장고 프로젝트 템플릿. 이전 버전의 (1.5, 1.6) Two Scoops 프로젝트 템플릿에서 포크되었다
- django-herokuapp https://github.com/etianen/django-herokuapp
    - 장고 사이트를 허로쿠에서 돌려 주는 유틸리티와 프로젝트 템플릿

## REST API
- django-rest-framework https://www.django-rest-framework.org/
    - 실질적으로 장고의 메인 REST 패키지. 모델 리소스와 비모델 리소스 모두 RESTful API로 서비스할 수 있게 해준다.
- django-jsonview https://github.com/jsocol/django-jsonview
    - 파이썬 객체를 JSON으로 변환해 주는 간단한 데코레이터를 제공. 데코레이터를 이용한 뷰가 언제나 JSON을 반환하는지 확인하라

## 보안
- bleach 
    - 화이트리스트(whitelist, 안전목록) 기반의 HTML 검사기
- defusedxml
    - 외부에서 온 XML을 처리할 때 반드시 필요한 파이썬 라이브러리
- django-autoadmin
    - 자동 생성된 패스워드로 장고 프로젝트 어드민 사용자를 생성해 준다. 자동으로 생성된 사이트의 보안 문제를 해결
- django-admin-honeypot
    - 가짜 장고 어드민 로그인 스크린. 허용하지 않은 접근 시도에 대해 어드민에게 알려 준다.
- django-axes https://github.com/jazzband/django-axes
    - 장고 기반 사이트에 로그인 시도, 실패에 대한 감시를 해준
- django-ratelimit-backend
    - 인증 백엔드 레벨에서 로그인의 접속 제한을 한다
- django-passwords 
    - 패스워드 안정성에 대한 검증 기능을 제공하는 재사용 가능한 장고 앱
- django-secure
    - 보안 전문가들의 실제 경험을 통해 축적한 사항들로 사이트를 더욱 안전하게 해 준다. 많은 기능이 장고 SecurityMiddleware 클래스에 포함되어 있다.
- django-two-factor-auth
    - 장고용 이중 인증기능
- django-user-sessions
    - 장고 세션을 사용자의 외부 키로 연결한다.
- peep
    - 파이썬 패키지 인덱스로 업로드할 때 사용자의 민감한 정보를 보호하기 위해 인증된 TLS만 이용
- Twine

## 테스팅
- coverage https://coverage.readthedocs.io/en/v4.5.x/
    - 얼마나 많은 코드가 테스트로 커버되고 있는지 체크해 준다.
- django-test-plus https://github.com/revsys/django-test-plus
    - 장고 기본 테스트에 유용한 추가 기능을 제공해 주는 패키지. 
- factor boy
    - 모델 테스트 데이터를 생성해 주는 패키지
- model mommy
    - 모델 테스트 데이터를 생성해 주는 또 다른 패키지
- mock
    - 장고뿐 아니라 여러 환경에서 이용. 시스템을 목 객체로 대체하여 이용하게 해준다.
- pytest https://docs.pytest.org/en/latest/
    - 파이썬과 장고 프로젝트에서 매우 유용하게 쓰이는 검증된 다양한 기능의 파이썬 테스팅 도구
- pytest-django https://pytest-django.readthedocs.io/en/latest/
    - 장고 애플리케이션과 프로젝트를 테스트하는 유용한 도구를 지원하는 py.test의 플러그인
- tox https://tox.readthedocs.io/en/latest/
    - 셀에서 간단한 명령을 실행해 다양한 파이썬 버전으로 프로젝트를 테스트하게 해주는 virtualenv 관리와 테스트 명령행 도구

## 사용자 등록
- django-allauth https://django-allauth.readthedocs.io/en/latest/
    - 범용 사용자 등록.인증 도구. 이메일, 트위터, 페이스북, 깃허브, 구글 등 다양한 방법을 지원
- python-social-auth https://python-social-auth.readthedocs.io/en/latest/
    - 트위터, 페이스북, 깃허브, 구글 등 다양한 방법을 포함한 소셜 미디어 등록.인증 도구
    
## 뷰
- django-braces
    - 장고의 클래스 기반 뷰를 더욱 강력하게 만들어 주는 드롭인 믹스인
- django-extra-views
    - 장고에서 지원하는 것 이외에 여러 추가적인 클래스 기반 뷰를 지원
- django-vanilla-views http://django-vanilla-views.org/
    - 상속 관계를 간단히 함으로써 장고의 클래스 기반 뷰들을 간단하게 처리

## 시간
- python-dateutil
    - 파이썬 datetime 모듈에 강력한 기능을 추가
- pytz
    - 올슨 tz 데이터베이스를 파이썬에서 이용하게 해 준다. 시간 계산이 정확하고 플랫폼에 구애받지 않고 이용할 수 있는 장점을 제공한다. 일광 절약 시간의 마지막 날 등
    여러 민감한 문제를 해결해 준다.
    

## 기타
- awesome-slugify
    - 유연한 slugify(빈칸이나 특수 문자로 이루어진 문장을 대시 등을 이용하여 한 단어로 이어 묶어 주는 것) 함수
- dj-stripe
    - 장고와 스트라이프를 쉽게 사용하게 해준다.
- django-compressor
    - 링크 또는 인라인 자바스크립트나 CSS 파일을 압축된 하나의 캐시된 파일로 만들어준다.
- django-extensions
    - 셀에 추가적인 관리 명령과 여러 유틸리티를 제공
- django-haystack
    - SOLR, 엘라스틱서치 등과 함께 이용 가능한 풀 텍스트 검색기능
- django-pipeline
    - CSS와 자바스크립트 압축해 준다. cssmin과 jsmin 패키지와 함께 이용한다
- django-htmlmin
    - 장고용 HTML 소형화 도구
- django-reversion
    - 장고 웹 프레임워크의 종합적인 버전 관리 기능을 제공해 주는 확장 기능
- django-watson https://github.com/etianen/django-watson
    - SQL 데이터베이스 기능을 이용한 다중 테이블에 대한 풀 텍스트 검색 애플리케이션
- envdir
    - daemontools와 envdir 을 파이썬으로 이식한 것
- flake8
    - PyFlakes, pop8, 여타 도구들을 이용한 코드 체커
- pathlib
    - 객체 지향형 파일 경로. 파이썬 릴리스 3.4부터 파이썬에 합쳐졌다
- pip-tools
    - 원하는 파이썬 의존성 라이브러리, 도구들을 설치, 관리해 주는 도구 모음
- pyyaml
    - 파이썬용 YAML 파서와 생성기
- requests
    - 파이썬의 urlib2 라이브러리를 대체하는 쉽게 이용할 수 있는 HTTP 라이브러리
- silk https://github.com/jazzband/django-silk
    - 장고 프레임워크의 라이브 프로파일링과 인스펙션 도구, HTTP 요청과 데이터베이스 쿼리를 사용자에게 보여주기 이전에
    가로채 저장하여 좀 더 자세한 분석을 가능하게 해준다.
- unicode-slugify https://github.com/mozilla/unicode-slugify
    - 모질라에서 지원하는 유니코드 문자를 지원하는 slugifier
- Unipath
    - os/os.path/shutil 의 객체 지향형 대안
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  
  
  
  
  
  
  
  
  
  
  
  
  
      
  
  
  
  
  
  
  