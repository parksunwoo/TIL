
A curated list of Two Scoops of Django

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
-   
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
      
  
  
  
  
  
  
  