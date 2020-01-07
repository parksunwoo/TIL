# TIL
Today I Learned

- 가상환경 라이브러리 -venv   
    - 파이썬3에서는 venv 라이브러리가 기본 제공
    
```bash
$ python3 -m venv ./myvenv      # 가상환경 디렉토리 생성
$ source ./myvenv/bin/activate  # 맥/리눅스 가상환경 활성화
$ pip install <package>         # 가상환경 안에서 개발
$ deactivate                    # 현재 가상환경 비활성 
```
    
    - 파이썬3 명령어로 생성한 가상환경이므로 pip로 실행해도 무관함 
    - virtualenv : 파이썬3에서는 굳이 사용할 필요없음, 파이썬2에서 사용하기위함
    
#02. 데이터 타입
## 기본 데이터 타입 (int, float, str)
### 변수 (Variables)
- 프로그램이 실행되면서 필요한 데이터를 임시로 저장하는 공간
- 효율성을 높이기 위해 적절한 크기/ 용도의 변수에 값을 담아서 처리
- 하나의 소프트웨어가 동작하면서, 로직에 따라 수많은 새로운 변수가 생겨나고 변경되며 제거

### 데이터 타입 (Data Types)
- 변수는 하나의 데이터를 담아두는 공간. 그릇 개념
- 효율성을 위해, 그릇도 목적(크기/용도)에 따라 다양한 그릇이 필요
    - 물을 담아두는 다양한 용기 : 물병, 양동이, 물탱크, 소방차 등
- 자원은 유한합니다.
    - 자원이 귀한 줄 알고, 아껴써야 합니다 (CPU, 메모리, 디스크 등)
    
### Numeric Type(숫자)
- 정수형 : int
- 실수형 : float
- 사칙연산 (+,-,*,/), 몫 (//), 나머지 (%), 지수 승 (**) 연산자
- int/log/float/double( python2), int/float( python3) 통합ㅎ
- 수의 범위 제한이 없음

### boolean type ( 참/거짓)
- 참은 True, 거짓은 False (Java는 true/ false)
- 비교 연산자의 결과는 Boolean Type
    - <, <=, >, >=, ==, !=
    - is, is not : 참조 비교
- 논리 연산자
    - or, and, not

### 다른 타입에서의 Boolean 판단
- 숫자 0 False, 그 이외에는 True
- 빈 문자열은 False, 그 이외에는 True
- 빈 list/tuple/set/dict 은 False, 그 이외에는 True

### String Type(문자열)
- 문자열을 홀따옴표(')로 감싸거나, 쌍따옴표(")로 감싸기
    name1 = 'python'
    name2 = "python"
    
- 홑(쌍)따옴 1개 감싼 문자열 안에 (쌍)따옴표를 문자열로 처리하고자 할 경우, 해당 홑(쌍)따옴표를 ESCAPE 처리
- 파이썬은 여러 줄 문자열 문법을 지원합니다. 홑(쌍) 따옴표 3개로 감싸주는 방법
lyrics = '''The now glows white on the mountain tonight Now a footprint'''

- 문자열 형식 지정자
 - 문자열 내에 "{}"와 같은 헝태로 슬롯을 만르고, format 함수를 통해 슬롯에 중요한 데이터를 넘깁니다
 - format 함수에 함수인자로서 슬롯을 지정하는 방법
    - 위치(Positional), 키워드(Keyword)
    
- 함수 위치 인자 (Positional Arguments)
 >>> '{0}, {1}, {2}'.format('a', 'b', 'c')

- 함수 키워드 인자 (keyword Arguments)
 >>> 'Coordinates : {lat}, {lng}'.format(lat='37.24N', lng='-115.81W')

- NameError
    - 정의되지 않은 변수에 접근 시에 발생
    >>> print(a)
    NameError : name 'a' is not defined
                                          
    
    
    
    
    
    












