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
                                          
#03. 기본 자료구조
## 기본 데이터 타입 (int, float, str)
### container
- 여러 원소들을 가지고 있는 자료 구조
  - list, deque
  - set, fronzensets
  - dict, defaultdict, OrderedDict, Counter
  - Tuple, namedtuple
  - **str
- in 연산자로 멤버쉽 테스트를 지원
>>> 'hello' in 'hello world'

### list
- 생성문법 : [], list(), list(iterable)
- 여러 값을 순차적을 저장, 순서를 보장
- 리스트를 한 줄로 쓸 때에는 대개 끝에 쉼표를 쓰지 않으며,
- 여러 줄로 나눠쓸 때에는 끝에 쉼표를 씁니다. 항목 추가/삭제가 용이하기 때문입니다
numbers = [1,3,5,7,9]
names = [
    'Tom',
    'Steve',
    'Min',
]
- 색인(index) 지원 : 0부터 시작하여 1씩 증가
  - 음수 색인 지원: 끝에서부터 역으로 -1부터 1씩 감소
- 다른 타입의 값들로도 구성 가능
- 한 List에 서로 다른 데이터타입의 값을 넣을 수 있지만, 가급적 같은 타입으로 맞춰 주는 것이 보다 알기 쉬운 코드가 됩니다
    numbers = [1,3,5,7]
    print(7 in numbers)
    print(numbers[0], numbers[-3])
    print(len(numbers))
    for i in numbers:
        print(i)
    
    bad_values = [10, 'Tom', (1,2,3)] # bad

- 범위 밖의 색인(index) 을 참조하는 경우, IndexError 예외가 발생
>>> numbers = [1,3,5,7]
>>> print(numbers[10])
IndexError : list index out of range

### 데이터 변수
numbers = [1,3,5,7,5]
numbers[0] = 10
numbers.append(9)
numbers.pop(3)
numbers.remove(5)
numbers.insert(1, 11)

## 값을 잘라내기(slice)
>>> numbers = [1,2,3,4,5,6,7,8,9,10]
>>> print(numbers[1:])
[2,3,4,5,6,7,8,,9,10]
>>> print(numbers[1:7])
[2,3,4,5,6,7]
>>> print(numbers[1:7:2])
[2,4,6]
>>> print(numbers[::-1])
[10,9,8,7,6,5,4,3,2,1]

## 리스트 합치기
>>> numbers1 = [1,3,5,7]
>>> numbers1 = [2,4,6,8]
>>> print(numbers1 + numbers2)
[1,3,5,7,2,4,6,8]

## List Comprehension
>>> numbres1 = [1,3,5,7]
>>> numbres2 = [2,4,6,8]
>>> print([i + j for (i, j) in zip(numbers1, numbers2)])
[3, 7, 11, 15]

## tuple
    - 생성문법 : (), tuple(), tuple(iterable)
    - list와 유사하지만 변경 불가능(Immutable) 한 특성
>>> numbers = (1,3,5,7,5)
>>> numbers[0] = 10
TypeError : 'tuple' object does not support item assignment

>>> numbers.append(9)
AttributeError : 'tuple' object has no attribute 'append'

- 소괄호는 때에 따라, 우선순위 연산자 혹은 튜플로 쓰인다
    - 설정값으로서 튜플을 쓰실때, 헷갈리시몀ㄴ 리스트를 쓰세요. 기능 차이는 거의 없습니다. 코드오류가 나지 않는 것이 중요
>>> tuple1 = (1 + 3)
>>> tuple2 = (1 + 3,)
>>> tuple3 = (3)
>>> tuple4 = (3,)

>>> list1 = [1 + 3]
>>> list2 = [1 + 3,]
>>> list3 = [3]
>>> list4 = [3,]

- Packing / Unpacking : list/ tuple에 동일하게 적용
- unpacking 시에 갯수가 맞지 않으면 ValueError
>>> numbers = (1,2,3,4,5,6,7,8,9,10)
>>> v1, v2, v3, v4, v5, v6, v7, v8, v9, v10 = numbers

>>> v1, v2, v3, v4 = numbers[:4]
>>> v1, v2, v3, v4 *others = numbers

>>> *others, v8, v9, v10 = numbers
>>> v1, v2, *others, v9, v10 = numbers
>>> v1, v2, v3, *others = numbers

>>> v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13 = (*numbers, 11, 12, 13)
- swap : list/ tuple 에 동일하게 적용
>>> x,y = 1, 2
>>> x,y = y, x

### set (집합형)
- 중복을 허용하지 않는 데이터의 집합
    - list/tuple 에서 중복을 제거코자 할 때, set을 활용하면 유용
- list/ Tuple 과 다르게 추가된 순서를 유지하지 않음

>>> set_numbers = {1,2,3,4,5, 1,4,3,1 }
>>> set_numbers = {1,3,4,5}

>>> list_numbers = [1,1,2,1,1,2,2,3,1,2,3]
>>> list_numbers = list(set(list_numbers))
>>> list_numbers [1,2,3]

- 합집합, 교집합, 차집합, 여집합 연산 지원
>>> set_numbers1 = {1, 3, 4, 5, 1, 4, 3, 1}
>>> set_numbers2 = {1, 3, 4, 11, 13, 14, 15, 11, 14, 13, 11}
>>> print(set_numbers1 - set_numbers2)
{5}
>>> print(set_numbers1 | set_numbers2)
{1,3,4,5,11,13,14,15}
>>> print(set_numbers1 & set_numbers2)
{1,3,4}
>>> print(set_numbers1 ^ set_numbers2) # 여집합
{5, 11, 13, 14, 15}

- dict (사전형)
 - Key와 Value 의 쌍으로 구성된 집합
 - Key 중복을 허용하지 않음.
 - 중과홀 내에 콜론(:) 으로 Key/Value를 구분
 
 dict_values = {'blue':10, 'yellow':3, 'blue':9, 'red':7}
 - in 연산자로 멤버쉽 체크 지원 (Key의 등록 여부)
 - 순회 시에는 key 목록만 순회
 - 멤버함수
    - .keys(): key 목록
    - .values(): value 목록
    - .items(): (key, value) 목록
    
>>> print(dict_values['blue'])
10
>>> dict_values['black'] = 30
>>> del dict_values['black'] 
    
- in 연산자로 지정 Key 의 등록여부를 확인
>>> dict_values = {'blue':10, 'yellow':3, 'red':7}
>>> print('blue' in dict_values)
>

- for 루프 순회
>>> dict_values = {'blue':10, 'yellow':3, 'red':7}
>>> for key in dict_values:
    print(key)
red
>yellow
>blue
>
>
>
>
>>> for (key, value) in dict_values.items():
    print(key, value)
red 7
yellow 3
blue 10
>
>

#04. 블록문 들여쓰기 주석
### 블록문 (Block Statement)
- 블록문 (Block Statement) : 연속된 코드 묶음
- 코드는 다수의 블록 으로 구성. 블로문 안에 다수의 블록문 중첩
- 블록구분 : 들여쓰기 (Indent), 다른 언어에서는 중괄호 ({})

### 들여쓰기(Indentation)
- 들여쓰기는 Tabs 또는 Spaces로 입력
 - Github 코드 저장소에성늬 Tabs/Spaces 사용 통계
- 파이썬 언어 특징중에서 가장 호불호가 갈리는 기능
 - 코드의 가독성 증대
- 하나의 들여쓰기는 Python Style Guide #Indentation 에 따라, 공백 4칸을 권장

### IndentationError
- 일관된 들여쓰기를 지키지 않는다 IndentationError 발생
- Tab과 Space는 엄연히 다른 글자입니다. 필히 하나로 통일 ~ !!!
max = 10
result = 0
for i in range(max+1):
result = result +i # 들여쓰기(Indentation) 가 빠졌어요.
print("result = %d" % result)

### 탭 > 스페이스, 자동변환 기능
- 요즘 대개의 소스코드 편집기에서 자동변환 기능을 제공
- visual studio code : 디폴트 활성화
- sublime text3 : 아래 설정이 필요

### 주석 (Comments)
- 파이썬에서의 주석 문법은 "1줄 주석" 문법만 지원
    - "여러 줄 주석" 문법은 "문자열"로서 표기

### PEP8: Style Guide for Python Code
- PEP : Python Enhancements Proposals
- 일관성있는 코드 스타일을 위한 코드 스타일 제안
- 주요 스타일
    - 들여쓰기는 공백 4칸 (구글은 공백 2칸)
- [파이썬 코딩 컨벤션 by spoqa](https://spoqa.github.io/2012/08/03/about-python-coding-convention.html)

#05. 흐름 제어 (조건문, 반복)
### 조건문, if문
- 한 if statement 에서 if/ else 는 1회만 쓸수 있으나, elif 는 원하는 조건의 수만큼 쓸 수 있음

### 반복문 : for
- Iterable Object 로부터 가져올 값들을 모두 가져올때까지 반복
for 변수 in 리스트:
    매 항목마다 수행할 코드 블록
for 내에서 break 문을 지나면 해당 반복문 종료

for i in range(20):
    print(i)
    if i > 10:
        break
         
### 중첩 반복문을 한번에 종료시키기
예외발생이나 함수 내에서 return 문을 통해 중첩 반복문을 한번에 종료가능

>>> def gugu():
    for i in range(2, 10):
        for j in range(1, 10):
            print(i, j)
            return None
>
### 내장함수 range 
- range (stop) : 0부터 stop 미만의 범위에서 1씩 증가시킨 값으로 리스트를 구성
    - 문법적으로는 리스트가 아니라, 순회가능한 (Iterable) 객체
- range (start, stop[, step]) : start 값 이상, stop 값 미만의 범위에서 step 씩 증가시킼ㄴ 값을 리스트를 구성

### 반복문 : while
- 조건이 만족하는 동안에 반복문 수행
while 조건:
    매 항목마다 수행할 코드 블록
while 내에서 break 문을 만나면 해당 반복문 종료

### 무한루프 
- <반복문조건>이 항시 True 일 때
i = 10
while i < 13:
    print(i)
    i -= 1
    
for 에서는 itertools.count 함수를 통해 가능
from itertools import count
for i in count(1):
    print(i)






    
    













    
    
    
    
    












