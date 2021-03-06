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


#06. 함수
### Agenda
- positional / keyword arguments
- 가변인자
- 익명함수
- 1급객체와 1급 함수/클래스
- 고차함수

### 함수 Functions
- 함수의 구성
    - 1개의 함수명(필수) : 작업의 이름
    - 0개 이상의 인자값(옵션) : 작업에 필요한 정보
    - 1개의 반환값 (옵션) : 작업의 결과를 하나 돌려받습니다
- 코드의 중복을 제거하기 위해서 가장 필요한 문법
- 빌트인 함수 (Builtin Functions) : print, range 등
- 반환값이 없는 함수호출은 None 을 리턴합니다

### Scope (변수의 유효범위)
- 변수가 선언되어, 해당 변수가 영향을 미치는 영역
- 지역 변수 (Local Variable)
    - 함수 안에서 선언되어 함수내에서만 활용이 가능한 변수
- 전역 변수 (Global Variable)
    - 함수 밖에서 선언되어, 함수안에서도 활용이 가능한 변수
    
### 전역변수
- 코드의 가독성을 헤치므로 권장하지 않는 방법
- 주로 변수 목적으로 많이 쓰입니다. 파이썬에서는 따로 상수문법이 따로 없습니다.
    - 상수명을 대문자로 씁니다.
- 변수의 값이 변경되는 경우라면, 그 유효범위를 최소화하여 지역변수를 사용하는 것이 버그 발생확률을
  획기적으로 낮ㅊ루 수 있습니다.
  
### Arguments (인자)
 - 함수가 실행되는데에 필요한 0개 이상의 변수 목록

### Positional Arguments
- 인자의 위치에 기반한 인자

def fn_with_positional_arguments (name, age):
    print("당신의 이름은 {}이며, 나이는 {}입니다.".format(name, age))
    
fn_with_positional_arguments('Tom', 10)

### Keyword Arguments
- 인자의 이름에 기반한 인자
- 디폴트 인자 문법이 함께 적용 : 함수 호출 시에 해당 인자를 지정하지 않으면 디폴트 인자값으로 값이 자동지정

def fn_with_positional_arguments (name="", age=0):
    print("당신의 이름은 {}이며, 나이는 {}입니다.".format(name, age))

### Packing
- 인자의 갯수를 제한하지 않고, 다수의 인자를 받을 수 있음
- 다수의 Positional Arguments 를 하나의 tuple 로서 받을 수 있음 (packing)

```python
def fn2(*colors) :  # 0개 이상의 인자를 받을 수 있음
    for color in colors:
        print(color)
        
fn2()
fn2('white')
fn2('white', 'yellow')

def fn3(color1, color2, *other_colors):
    print('color1 :', color1) 
    print('color2 :', color2) 
    for color in other_colors:
        print(color)

fn3('brown', 'green') # 최소 2개의 인자 지정이 필요
```
### unPacking
- 인자를 넘길 때 Sequence Data Type (리스트/튜플 등) 을 다수의 인자인 것처럼 나눠서 전달 가능 (unpacking)

```python
colors = ['white', 'yellow', 'black']
fn2(*colors)
fn2('brown', 'pink', *colors)
```

​       

#07. 클래스

### Object Oriented Programming (OOP) 배경

- 함수는 데이터의 처리방법을 구조화했을뿐, 데이터 자체는 구조화하지 못했다.
- 큰 문제를 작게 쪼개는 것이 아니라, 먼저 작은 문제들을 해결할 수 있는 객체들을 만든 뒤, 이 객체들을 조합해서 큰 문제를 해결하는 상향식 (Bottom-up) 해결법을 도입

### OOP 주요특징

- Encapsulation (캡슐화) : 관련 특성/기능을 하나의 클래스에 결합
- Inheritance (상속) : 코드 재활용성 증대
  - 부모 클래스의 특성/기능을 자식 클래스가 물려받음
  - 자식 클래스는 물려받은 특성/기능을 활용/변경/무시/재정의
- Polymorphism (다형성, 위키피디아, 참고)
  - 다른 동작을 동일한 함수로 사용할 수 있도록 지원

#### Class 

- 단순히 <사용자 정의 데이터 타입>
  - 관련된 다수의 변수와 함수의 묶음으로 구성
- Ex) Circle 클래스, Rectangle 클래스
- Tip : 파이썬에서 함수명은 snake_case, 클래스명은 CamelCase

### 파이썬3 기본클래스는 object를 상속받아도, 안 받아도 동일

- python2에서는 object를 상속받아야 New-style Class
- python3에서는 Old-style class는 제거되고, New-style class만 남았습니다

`class Python3NewStyleClass:`
`				pass`

`class Python3NewStyleClass(object):
		pass`

### 커스텀 클래스 Circle - 훨씬 응집도 있는 처리

데이터와 함수의 통합

```python
from math import sqrt
class Circle(obejct):
  def __init__(self, x, y, radius):
    	self.x = x
      slef.y = y
      self.radius = radius
  
	def area(self):
    	return self.radius ** 2
    
  def distance(self, other):
    	return sqrt ((self.x -other.x) **2 + (self.y -other.y) **2) - (self.radius + other.radius)
    
    
    >>> circle1 = Circle(10, 20, 3)
    >>> circle1.area()
    
    >>> circle1.distance(circle2)
    
```

- 지정 클래스 타입의 변수 = 인스턴스 (Instance)
- 인스턴스 생성 문법
  -  함수를 호출하듯이, 클래스를 호출하여 인스턴스 생성
- 클래스가 호출이 될 때, 클래스내 `__init__` 함수가 자동 호출
  - 생성자(Constructor)라 하며, 해당 인스턴스를 초기화하는 역할
  - 클래스 호출 시에 넘겨진 인자는 모두 생성자의 인자로 넘겨짐.
- 인스턴스를 위한 함수/변수들을 인스턴스 함수, 인스턴스 변수



## 클래스 변수와 인스턴스 변수

### 클래스 변수와 인스턴스 변수

- 클래스 변수 (Class)
  - 클래스 공간에 저장
- 인스턴스 변수 (Instance)
  - 각 인스턴스마다 개별 공간에 저장

#### 인스턴스 변수인 것 같지만, 클래스 변수

파이썬에서는 인스턴스 변수 선언 문법은 Java의 그것과 다릅니다.

```python
class Dog:
  	tricks = [] # 이는 인스턴스 변수가 아니라, 클래스 변수
    
    def add_trick(self, trick):
        self.tricks.append(trick)
        
>>> dog1 = Dog()
>>> dog1.add_trick('roll over')

>>> dog1.tricks #['roll over', 'play dead'] 출력 -????
```

### 올바른 인스턴스 변수 선언

인스턴스 함수 내에서 인스턴스 변수를 선언합니다

```python
class Dog:
  		def __init__(self):
      		self.tricks = []   # 이것이 인스턴스 변수입니다.
        
      def add_trick(self, trick):
        	self.tricks.append(trick)
          
          
>>> dog1 = Dog()
>>> dog1.add_trick('roll over')
>>> dog2 = Dog()
>>> dog2.add_trick('play dead')

>>> dog1.tricks # ['roll over'] : 바르게 출력
>>> dog2.tricks # ['play dead'] : 바르게 출력

```



### Data Hiding, Name Mangling

데이터 은닉과 이름 장식

- mangle : [동사] 짓이기다. 심하게 훼손하다
- 파이썬에서는 접근 제한자 미지원
- 언더스코어 2개 (__)로 시작하는 이름에 한하여 이름을 변경 (Name Mangling) 기법을 제공
  - 인스턴스 함수 에서는 이름 그대로 접근

```python
class Person:
  	def __init__(self, name):
      self.__name = name
      
    def say_hello(self):
      print('안녕 {}.'.format(self.__name)) # 인스턴스 함수 내에서는 이름 그대로 접근
      
      
      
>>> tom = Person('tom')
>>> tom.__name 
AttributeError: 'Person' object has no attribute '__name'
>>> tom._Person__name  # 외부에서는 맹글링된 이름으로 접근
'tom'
>>> tom.say_hello()
'안녕 tom.'
```

#08. 호출 가능한 객체

### 호출 가능한 (Callable) 객체

- 호출문법 : obj()
- 함수를 호출해서, 리턴값을 취한다

```python
def area(self):
	return self.radius ** 2
>>> area()
```

- 클래스를 호출해서, 인스턴스를 생성한다

- 하지만, 클래스의 인스턴스를 호출할 수는 없다

  

```python
class Calculator(object):
	def __init__(self, base):
    	self.base = base
      
calculator = Calculator(10)
print(calculator(1, 2)) # TypeError : 'Calculator' object is not callable.
```

### 인스턴스를 호출가능토록 만들기

- 인스턴스를 호출가능토록 만들려면 ```__call__ ``` 멤버함수를 구현
  - 인스턴스를 호출하면, 파이썬에서 멤버함수 ```__call__ ``` 를 호출해줍니다.

```python
class Calculator(object):
	def __init__(self, base):
    	self.base = base
      
	def __call__(self, x, y):
    	return self.base + x + y

>>> calculator = Calculator(10)
>>> calculator(1, 2)
13
>>> calculator.__call__(1, 2)
```

- 예) 상태값을 유지하는 함수

  

```python
class Calculator(object):
	def __init__(self, base):
    	self.base = base
      
	def __call__(self, x, y):
    	self.base += (x + y)
      return self.base

>>> calculator = Calculator(10)
>>> calculator(1, 2)
13
>>> calculator(1, 2)
16
>>> calculator(1, 2)
19


```

- 기존 함수와 비슷한 로직의 함수를 만들려면,

```python
import requests
from bs4 import BeautifulSoup
from collections import Counter

def word_count(url):
  html = request.get(url).text
  
  soup = BeautifulSoup(html, 'html.parser')
  words = soup.text.split()
  
  counter = Counter(words)
  
  return counter

>>> word_count('https://nomade.kr/vod/')
```



- 함수는 새로 구현할 수 밖에 없음.

```python
import requests
from bs4 import BeautifulSoup
from collections import Counter

def korean_word_count(url):
  html = request.get(url).text
  
  soup = BeautifulSoup(html, 'html.parser')
  words = soup.text.split()
  
  # 한글 단어만 추출
  words = [word for word in words if re.match(r'^[ㄱ-힣]+$', word)]
  
  counter = Counter(words)
  
  return counter

>>> word_count('https://nomade.kr/vod/')
```



### 단어수 세기(클래스 버전)

- 클래스지만 함수처럼 호출해서 쓸수 있음

```python
import requests
from bs4 import BeautifulSoup
from collections import Counter

class WordCount(object):
  def get_text(self, url):
    '문자열 수집'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
		return soup.text
  
	def get_list(self, text):
    '단어 리스트로 변환'
    return text.split()
  
	def __call__(self, url):
		  text = self.get_text(url)
      words = self.get_list(text)
		  counter = Counter(words)
  		return counter

>>> word_coutn = WordCount()
>>> word_count('https://nomade.kr/vod/')
```

### 한글 단어수 세기 (클래스 버전)

- 상속과 오버라이딩을 통해, 주요코드만 재정의

```python
import re

class KoreanWordCount(WordCount):
  def get_list(self, text):
    	'한글로만 구성된 단어만 추출'
      words = text.split()
      return [word for word in words if re.match(r'^[ㄱ-힣]+$', word)] 
    
>>> korean_word_count = KoreanWordCount()
>>> korean_word_count('https://nomade.kr/vod/')
```



## 09. 순회 가능한 객체

### 참고) Iterables vs Iterators vs Generators

- iterable : 순회 가능한 객체
- Generator : 값을 생산해내는 객체
  - generator expression : 제너레이터 표현식
  - generator function : 제너레이터 함수

### Generator 맛보기

```python
# a generator expression
>>> (i ** 2 for i in range(10))

# generator expression 으로 list 생성
>>> list(i ** 2 for i in range(10))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# a generator function
def power():
    for i in range(10):
      yield i ** 2    # 함수 내에서 return 대신에 yield, yield 시마다 값을 생산
      
>>> power()

>>> list(power())
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### 순회 가능한 (Iterable) 객체

- set, list, dict, tuple, string, generator 는 모두 순회 가능한 객체
- Custom 클래스에 대해서도 순회가능토록 만들 수있습니다
  - ```__iter__``` 멤버함수 구현 : self가 iterator로서 동작을 하기 위해 self 를 반환
  - ```__next__``` 멤버함수 구현 : iterator로서 동작
- for in 구문에서 활용 가능

```python
for ch in "hello world":
    print(ch)
```

### 사전 (dict)의 경우

```python
mydict = {'a':1, 'b':2}

for key in mydict:
    print(key, mydict[key])
for key in mydict.keys():
    print(key, mydict[key])
for value in mydict.values():
    print(value)
for (key, value) in mydict.items():
    print(key, value)
```

###  클래스를 통한 Iterable 객체 만들기

```python
class MyRange:
	    def __init__(self, start, end):
      		self.start = start
          self.end = end
      def __iter__(self):
          return self   # iterator를 요구받고, 현 instance 에서 next처리
        
      def __next__(self):
          if self.start >= self.end:
            	raise StopIteration
          value = self.start
          self.start += 1
          return value
        
>>> iterable = MyRange(0, 3)
>>> for i in iterable:
  			print(i)
# object가 iterator가 아닐 경우, iterator(반복자)를 요구받음 - 인스턴스일 경우 __iter__ 호출
# for 루프를 돌며, iterator에 다음 요소를 요구 - 인스턴스일 경우 __next__ 호출              
              
              
```



## 10. 코루틴 및 제너레이터

### Python2 에서의 range & xrange

- python3 에서는 range 가 제거되고 xrange가 range로 변경됨
- 차이
  - range : 가용값들을 미리 생성하고 시작하느냐 (+메모리 공간)
  - xrange : 값의 범위만 정해두고, 값을 그떄 그때 생성해내느냐 (+ CPU 연산)

#### Python2에서의 range

- 한 리스트 300,000,000 개를 구성하고 나서, 첫 값을 출력하고, break

  

#### Python2에서의 xrange

- 첫 값을 생산하자마자 출력하고 break

### range, xrange 개념 구현

```python
def myrange(start, end, step):
    mylist = []
    while start < end:
        mylist.append(start)
        start += step
    return myslit

def myxrange(start, end, step): # 코루틴 생성
    while start < end:
        yield start # generator 문법
        start += step
```

### Co-Routine (코루틴)

- Sub Routine : 일반적인 함수
  - 진입점이 하나이며, 부모/자식의 종속적인 관계가 성립
  - 매 호출시마다, Routine 내 context가 초기화

- Co Routine : 코루틴
  - 진입점이 여럿이며, 병렬(Concurrency, not Parallelism) 수행
  - 호출부와 대등한 관계
  - 여러번 호출이 되어도, Routine 내 Context 가 유지

### Generator 문법으로 간편히 코루틴 구현

```python
def sub_routine():
    return 10
  
def co_routine():
    yield 10
    yield 20
    yield 30
    
>>> sub_routine()
10

>>> generator1 = co_routine()
>>> generator1

>>>next(generator1) # 이제서야 루틴이 실행 => 첫 yield까지 수행
>>>10
>>>next(generator1) # 이어서, 다음 yield 까지 수행
>>>20
>>>next(generator1) # 이어서, 다음 yield 까지 수행
>>>30

>>>next(generator1) # 더 이상 생산(yield)할 수 없으므로, stopIteration 예외 자동 발생 
>>>stopIteration
```

### Generator

- generator 는 항상 iterator 입니다.
- 연속된 (Sequence) 값들을 생산해내는 함수
- 함수에 yield 키워드가 여지면 Generator
- yield한 값들이 순차적으로 생산됩니다
- Generator 에서 return문을 만나더라도 종료만 될 뿐, 리턴값이 사용되지는 않습니다.
- 추가 yield가 없으면, StopIteration 예외 자동발생
  - for 루프는 StopIteration 예외 자동으로 처리
  - 직접 StopIteration 예외를 발생시켜도 됩니다

```python
def myxrange(start, end):
    while start < end:
      yield start
      start += 1
```

### 중첩된 Generator는 Pipeline

- 매 Generator가 완료된 후에, 다음 Generator가 수행되는 것이 아니라 한 Generator에서 값이 생산될 때마다 다음 Generator로 값이 전달

```python
>>> gen1 = (i**2 for i in range(10))
>>> gen2 = (j+10 for j in gen1)
>>> gen3 = (k*10 for k in gen2)

>>> for i in gen3:  #첫 번째 값을 받아올 때, 그제서야 gen1에서 값 생산 시작
    print(i, end= ' ')
```

- 데이터가 아무리 많아도, 첫 스타트업 시작이 짧습니다
- 그렇기에, 가급적이면 Generator를 그대로 써주세요. list/tuple 로 변환하지마세요.

```python
>>> t1 = tuple(i**2 for i in range(10)) # 모든 값을 tuple 로 생성
>>> t2 = tuple(j+10 for j in gen1)
>>> t3 = tuple(k*10 for k in gen2)

>>> for i in t3:  # 이미 생성된 tuple값에 대해서 순회
    print(i, end= ' ')
```



### iterator로 tuple/list 생성하기

```python
def to_3():
    yield 1
    yield 2
    yield 3
    
numbers_list = list(to_3())
numbers_tuple = tuple(to_3())
```

### tuple/list/iterator 를 dict 으로 변환

```python
mylist = [['a', 1], ['b',2 ]]
dict(mylist) # {'a':1, 'b':2}

# key가 중복이 되면, 마지막 key/value가 남습니다.
mylist = [['a', 1], ['b',2 ], ['a',3]]
dict(mylist) # {'a':3, 'b':2}


```

### Generator로 피보나치 수열 생산하기

- 소비하는 만큼만 생산 (좀 더 범용적으로 활용이 가능)

```python
def fib():
  x, y = 1, 1
  while True:
    	yield x
      x, y = y, x +y
      
>>> count = 0
		for x in fib():
    		print(x, end= ' ')
        count += 1
        if count >= 10:
            break
            
>>> from itertools import islice
>>> islice(fib(), 10)
>>> tuple(islice(fib(), 10))
```



### List/set/dict Comprehension

- 순회가능한 객체를 조작하여, 필터링/새로운 리스트/사전/집합을 만들 수 있는 아주 간편한 방법
- tuple comprehension은 없어요. 필요하다면 tuple(순회가능한 객체)



```python
# list comprehension
[표현식 for 변수 in 순회가능한객체 if 필터링조건]
[i**2 for i in range(5) if i%2 == 0]

# dict comprehension
{Key:표현식 for 변수 in 순회가능한객체 if 필터링조건}
{i:i**2 for i in range(5) if i%2 == 0}

# set comprehension
{표현식 for 변수 in 순회가능한객체 if 필터링조건}
{i%5 for i in range(20) if i%2 == 0}
```



### Generator Expression (제너레이터 표현식)

- 문법비교 list comprehension : 한번에 list를 생성

```python
>>> [i**2 for i in range(100)]
[0,1,4,9,16,25,36,49,64, ...]

# generator expression : 값을 그때그때 생성하여 yield
>>> (i**2 for i in range(100))

# 제너레이터 표현식으로 list/tuple 만들기
>>> list(i**2 for i in range(100))
[0, 1,4,9,16, ...]
>>> tuple(i**2 for i in range(100))
(0, 1,4,9,16, ...)
```



## 11. 빌트인 함수, 정렬

### sorted : 정렬된 리스트를 반환

``` python
sorted_list = sorted(iterable, key=None, reverse=False )

```

- 
- key : 정렬기준값을 생성할 함수를 지정. iterable 객체의 각 원소마다 key함수가 호출되고 그 리턴값으로 정렬을 수행

``` python
>>> def sort_fn(value):
  return value % 10 # 1의 자리수로서 정렬을 수행하려면

>>> sorted_list = sorted([19, 25, 32, 45], key=sort_fn, reverse=True)
>>> sorted_list =[19, 25, 32, 45]
```



### filter : 지정함수 필터링된 결과를 생산할 Iterator를 반환

- 각 원소마다 지정함수가 호출되어, 리턴값이 True 판정될 경우 통과

``` python
iterator = filter(필터링여부를 결정할 함수, iterable)

>>> def judge_fn(value):
        return value % 2 == 0 # 짝수만 통과
>>> iterator = filter(judge_fn, [1,2,3,4,5,6])
>>> list(iterator)
[2,4,6]
```

### map : 지정함수 리턴값을 반환할 Iterator를 반환

``` python
iterator = map(값을변환할함수, iterable)

>>> def power_fn(value):
        return value ** 2
>>> iterator = map(power_fn, [1,2,3,4,5])
>>> list(iterator)
[1,4,9,16,25]
```



### max / min : Iterable 에서 key 함수를 거친 결과값 중에 가장 큰 결과값의 원래값을 반환

``` python
최대값 = max(iterable, [, default=obj][, key=값을변환할함수])
최소값 = min(iterable, [, default=obj][, key=값을변환할함수])

>>> max([], default=0)
0
>>> max([1,2,3], default=0)
3
```

- Iterable 이 비었을 경우, default 값을 반환
- 디폴트값을 지정하지 않고 Iterable 객체가 비었을 경우, ValueError: max() arg is an empty sequence 예외가 발생



### list의 sort 멤버함수

- sorted : 다양한 iterable 객체를 정렬한 새로운 리스트를 리턴
  - 원본 <iterable 객체>의 순서는 변경하지 않음
- list는 자체적으로 sort 함수를 지원
  - list 자체의 순서를 변경
  - sorted 와 다르게 리턴값이 없습니다. 즉 None 을 리턴합니다



### 임의 기준으로 정렬하기

- sorted, mylist.sort 함수에 key 함수를 제공하여, 임의 기준으로 정렬

### 대소비교

- 정렬을 위해서는 각 값들 간에 대소비교가 가능해야합니다.

  - 대소비교가 지원되지 않으면, 정렬이 불가

    0 < 'a'
    TypeError: unorderable types : int() < str()

- 한 문자끼리 비교는 각 문자에 매핑된 문자코드를 따라 비교

-  'a' < 'b' # True

- 문자열끼리의 비교는 첫번째 인덱스부터 대소비교가 판가름이 날떄까지 같은 인덱스의 문자끼리 비교

- 'abcdef' < 'axab' # True 0번 인덱스 (무승부) 1번인덱스 (우항이크다)

- list / tuple 끼리의 비교도 문자열 비교와 동일

  [9] < [0] # False

  [0,9]  < [9] # True



## 12. 모듈, 팩키지

### import

- 다른 파이썬 소스파일 내 함수/클래스등을 현재의 공간으로 가져오기
- import 시점에서 해당 코드가 실행됩니다

``` python
module.py
pkg1
-- __init__.py
-- pkg2
----- __init__.py

import module					# module.py
module.some_fn()			# module.py 내 some_fn

from module import some_fn # module.py 내 some_fn
some_fn()

import pkg1						# pkg1/__init__.py
import pkg1.pkg2			# pkg1/pkg2/__init__.py
pkg1.pkg2.some_fn()		# pkg1/pkg2/__init__.py 내 some_fn
some_fn()

import pkg1						# pkg1/__init__.py
import pkg1.pkg2			# pkg1/pkg2/__init__.py
pkg1.pkg2.some_fn()		# pkg1/pkg2/__init__.py 내 some_fn

from pkg1 import pkg2	# pkg1/pkg2/__init__.py
pkg2.some_fn()


import mymodle1 			# mymodule1.py 내 사항을 가져옴
mymodle1.mysum(1,2)		# mymodule1.py 내 mysum 함수

import pkg1.pkg2 			# pkg1/pkg2/__init__.py 사항을 가져옴
pkg1.pkg2.mysum(1,2)	# pkg1/pkg2/__init__.py 내 mysum 함수

import pkg1.pkg2.모듈 			# pkg1/pkg2/모듈.py 내 사항을 가져옴
pkg1.pkg2.mysum(1,2)	# pkg1/pkg2/모듈.py 내 mysum 함수
```

## modules (모듈)

- 다수의 함수/클래스들을 정의해둔 파이썬 소스코드 파일

``` python
# mymodule.py
def mysum(x , y):
    return x + y
  
mymultiply = lambda x, y : x * y

>>> import mymodule
>>> mymodule.mysum(1, 2)
3
>>> mymodule.mymultiply(1, 2)
2

>>> from mymodule import mysum, mymultiply
>>> mysum(1, 2)
3
>>> mymultiply(1, 2)
2
```

## packages (팩키지)

- 파이썬 소스코드가 들어있느 디렉토리
- 해당 디렉토리에는 필히 ```__init___``` 파일이 있어야 파이썬 팩키지로서 인식합니다. (파이썬 3.3 이상에서는 없어도 인식)
- 팩키지를 import 할 때에는 ```__init_.py``` 가 import 대상이 됩니다

``` python
mylib
-- __init__.py
---- mysum4 임포트된 함수
-- math.py
---- mysum4 함수

# mylib/__init_-.py
from .math import mysum4

# mylib/math.py
def mysum4(a, b, c, d):
  return a + b + c + d

#가져와서 쓰기
>>> from mylib import mysum4
>>> mysum(1, 2, 3, 4)
10

>>> from mylib.math import mysum4
>>> mysum( 1, 2,3,4)4
10

```

### import 해서, 이름을 변경해서 쓰기

- import 시에 as를 통해 원하는 이름으로 변경

## Relative import

- 팩키지 내에서 다른 모듈/팩키지 가져오기

``` python
main.py
pkg1
-- __init__.py
----- mysum 임포트된 함수
-- math.py
----- mysum 함수

# pkg1/math.py
def mysum(x, y):
    return x + y
  
# pkg1/__init__.py
from .math import mysum # mysum 함수를 현재 이름공간(name)으로 가져옴

# main.py : 아래 2가지 mysum을 모두 사용가능
from pkg1 import mysum
from pkg1.math import mysum
```

### import 경로

- import 를 수행할때, sys.path 경로에서 모듈/팩키지 탐색
  - 환경변수 PATH 개념과 유사
- sys.path 는 list 이기 때문에, 자유롭게 추가/수정/삭제 가능
  - 수정된 내용은 현재 프로세스에서만 유효
  - 관리성이 나빠지기 떄문에 권장하는 방법은 아님
- 현재 디렉토리와 sys.path 경로에서 지정 모듈/ 팩키지를 찾지 못했을 경우 Import Error 발생

## 파이썬 소스코드 내 __file__

- 해당 파이썬 소스코드 파일 경로
- pkg1/helloworld.py 일 경우
  - "Users/askdjango/pkg1/helloworld.py"
- 참고 : 장고프로젝트/setings.py 내 BASE_DIR

``` 
from os.path import abspath, dirname
BASE_DIR = dirname(dirname(abspath(__file__)))
```

### 파이썬 소스코드 내 __name__

- 해당 파이썬 소스코드 파일명

  - pkg1/helloworld.py 일 경우 : "helloworld"

- 비교

  - 최초 진입소스 코드일 경우: ```__main___``` 으로 변경되어 실행
  - import 된 소스코드 : 본래 ``` __name__``` 이 유지된 채로 실행

- 이를 통해, import 시에는 실행되지 않고, 최초 진입시에만 실행될 코드를 지정가능

  

``` python
def main():
  print('본 스크립트가 최초 진입 소스코드 경우에만 실행됩니다.')
 
if ```__name__``` == '__main__':
  main()
  
if ```__name__``` == '__main__':
  코드에 의해 import 될때에는 실행되지 않습니다.
  
```



## 13. 문자열 인코딩과 유니코드

### bit and byte

- 컴퓨터 데이터의 크기를 나타내는 단위
- 1 bit : 0과 1, 2가지 데이터를 표현 가능
- 1 byte : 8bit, 256 가지 데이터를 표현 가능

### character Encoding (문자 인코딩)

- 문자나 기호들의 집합을 부호화(인코딩) 하는 방법 (위키피디아)
- 인코딩의 2가지 의미
  - 변환하는 방법: ascii, cp949, utf8, utf16, utf32 등
  - 변환하는 행위
- 하나의 동영상을 avi, mp4, mkv 등으로 변환(인코딩)할 수 있듯이, 하나의 문자열도 다양한 인코딩으로 변환할 수 있습니다.
- 각 인코딩마다 표현가능한 글자와 범위가 다름

### Encoding & Decoding

- 일반적인 인코딩 의미: 어떠한 값을 특정 룰에 맞춰 다른 형식으로 변환
  - 디코딩 : 역변환
- 파이썬 유니코드 문자열(str) 열에서의 인코딩 의미
  - 하나의 문자를 한의 숫자로서 표현하는 다양한 Mapping Rule (인코딩마다 Rule이 다름)
  - 해당 Mapping Rule에 맞춰 변환하는 것
- 파이썬 바이트(bytes) 에서의 디코딩 의미
  - 해당 바이트를 유니코드로 디코딩할수 있음을 알고있다
  - 해당 바이트가 인코딩된 인코딩에 따라, 디코딩을 수행하여 유니코드 문자열(str) 을 획득

### 다양한 인코딩

- ascii : 7비트를 사용한 인코딩
- utf8, utf16, utf32 : 유니코드를 따르는 인코딩 방식
- code page 949 : Microsoft 의 한국어 문자 인코딩
- code page 932 : Microsoft 의 일본어 문자 인코딩



### Unicode (유니코드)

- 기존 코딩의 한계를 극복하고 전 세계의 모든 문자를 일관되게 표현할 수 있도록 설계된 산업표준
- UTF-8
  - 모든 유니코드 글자 표현 가능
  - 가변 길이 문자 인코딩 방식 : 1바이트 ~ 4바이트

### Unicode 이해의 다양한 단계들

### 5. 특정 글자셋을 사용하는 문자(열)을 바이트열로 인코딩하는 방식이 인코딩이며,

UTF-8이 곧 Unicode 가 아니라는 것을 아는 사람. Python에서 unicode 타입과 str 타입이 왜 함께 있는지 이해하며 잘 사용한다

- 부연설명
  - Python 2 : unicode타입(유니코드) 과 str타입(특정 인코딩)
  - Python 3 : str 타입(유니코드) 과 bytes 타입(특정 인코딩)

### ascii code

- 7비트를 사용한 인코딩

  ``` python
  >>> for i in range(128):
  				print(i, repr(chr(i)))
  ```

### 파이썬에서의 인코딩/디코딩

- 유니코드 문자열(str타입) > 인코딩 > bytes 타입 문자열
- Bytes 타입 문자열 > 디코딩 > 유니코드 문자열(str 타입)

``` python
unicode_string = '가'
utf8_string = unicode_string.encode('utf-8') # bytes type
cp949_string = unicode_string.encode('cp949') # bytes type
unicode_string = cp949_string.decode('cp949') # str type
```

- 참고 : 바이너리 데이터를 파이썬으로 읽어들이면, bytes 타입
  - PSD, PNG, JPG, XLSX, 세이브 데이터 등
- 엉뚱한 인코딩으로 인코딩하면 UnicodeDecodeError



## 파이썬에서의 인코딩/디코딩 Tip

- 파이썬 코드 안에서는 모두 유니코드로 처리
  - 유니코드로 문자열을 처리하면, 한글처리에 불편함이 없습니다. 글자수 세기도 쉬움

``` python
unicde_ga = '가나다'
utf8_ga = unicode_ga.encode('utf-8')

print(len(unicode_ga)) 	# 3 : 글자수
print(len(utf8_ga)) 		# 9 : 바이트 수

# 처음 2글자만 보기
print(unicode_ga[:2])
print(utf8_ga[:6])			# 인코딩따라서 참조하는 인덱스가 다름
```

- 현재 파이썬 프로그램 밖과 문자열 데이터를 주고 받을 때에는
  - 줄 때 : 최대한 늦게 특정 인코딩으로 인코딩한 후에 전송
  - 받을 때 : 최대한 빨리 특정 인코딩으로 디코딩하여, 유니코드로 처리

- 어떤 경우?
  - 문자열을 파일에 저장 & 읽어오기
  - 데이터베이스 통신
  - Android & iOS 앱과 통신
  - 그 외, 다수 상황

 

## 14. 파일 객체

### 파일에 저장하고 읽어오기

### 데이터를 영속성있게 저장할려면???

- 메모리 내 데이터는 프로세스가 종료되면, bye bye ~
- 영속성있게 저장할려면 파일에 저장해야합니다.
  - 파이썬에서는 open 함수를 통해 파일 읽기/쓰기 지원

### 파일 모드 (Read, Write, Append)

- [모드 R] 기존 파일 일기
- [모드 W 혹은 A] 새 파일 생성해서 쓰기
- [모드 W] 기존 파일 내용 제거하고, 처음부터 쓰기
- [모드 A] 기존 파일에 추가하기

### 파일의 종류

- TEXT : 문자열 데이터
  - 자동 인코딩/디코딩이 있으면, 더 편리하겠죠?
- BINARY : 바이너리 데이터
  - 자동 인코딩/디코딩을 구지 수행하지 않습니다.
  - 대개 문자열이 아닌, 이미지/PDF/XLS 포맷 등
  - TEXT 데이터여도 BINARY로 열수도 있겠죠.

### open(파일 쓰기/읽기 함수)

``` python
file_obj = open(파일경로, mode='r', encoding=None, 그외옵션생략)
readed_data = file_obj.read() 	# 파일 내용 처음부터 끝까지 모두 읽기
File_obj.close() 
```

- file object 주요 멤버함수
  - .write 함수 : 파일에 쓰기
  - .read 함수 : 파일 읽기
  - .close 함수 : 파일 닫기

### encoding 옵션

- 자동 인코딩/디코딩 인코딩 옵션
- text mode 시에만 지정 가능. binary 모드에서는 지정불가
- 미지정시에 OS 설정에 따라, 다른 인코딩이 지정
  - locale.getpreferredencoding(False)
  - 한글 윈도우 : cp949
  - 맥/리눅스 : 대개 utf-8
  - 가급적이면 모든 파일은 utf-8 인코딩으로 생성
- 요즘 소스코드 편집기의 디폴트 인코딩은 UTF-8
- 다양한 인코딩이 혼재하면, 정신건강에 좋지 않아요
- 특별히 cp949 인코딩이 필요한 경우가 아니라면, utf-8 로 대동단결!!!
  - ex) 한글 윈도우 엑셀에서 쓸 csv 파일 만들기
  - (utf-8 인코딩으로도 할 수는 있어요... -BOM 사용)

### 파일을 열때, 5가지 모드

- r(read ), w(wrtie), a (append)
- 인코딩 모드
  - t(text) : 자동 인코딩/디코딩 모드
    - read() 반환타입은 str
    - write() 인자로 str 타입 필요
  - b(binary) : 바이너리 모드
    - read() 반환타입은 bytes
    - write() 인자로  bytes 타입 필요
- 지정 예
  - rt(read + text), rb, wt, wb, at, ab

### r (read)

```python
filecontent_unicode = open('filepath.txt', 'rt', encoding='utf8').read()
```

- 지정 경로에 파일이 없을 경우  IOError 예외 발생
- 지정 경로의 파일에 대해 읽기권한이 없을 경우 PermissionError 예외 발생

### w (wrtie)

```python
open('filepath.txt', 'wt', encoding='utf8').write('가나다') # 유니코드 문자열(str)
```

- 지정 경로 파일이 없을 경우, 해당 내용으로 새 파일 생성
- 지정 경로의 파일이 존재하지만, 쓰기 권한이 없을 경우
  - PermissionError 예외 발생
- 지정 경로 내에 없는 디렉토리가 지정된 경우, FileNotFoundError 예외 발생

### a ( append)

```python
open('filepath.txt', at, encoding='utf8').write('가나다') # 유니코드 문자열 (str)
```

- w (wrtie) 와 유사

### t (text)

```python
with open('filepath.tx', 'wt', encoding='utf8') as f :
  f.write('가나다')
```

- 지정 encoding 으로 자동 인코딩/디코딩과 함께 파일 쓰기/읽기

### b (binary)

```python
with open('filepath.txt', 'wb') as f:
  	f.write('가나다'.encode('utf8'))
```

- 자동 인코딩/디코딩없이 파일 쓰기/읽기
- encoding 옵션 지정 불가
- 문자열이 아닌 파일을 읽어들일 때에는 인코딩/디코딩을 수행하면 안 되므로,  필히 binary 모드를 지정

```python
with open('myphoto.jpg', 'rb') as f:
  		photo_data = f.read() # bytes 타입
```

### 파일에 접근하는 다양한 방법

```python
f = open('sample.txt', 'rt', encoding='utf8')
print(f.read())
f.close()

f = open('sample.txt', 'wt', encoding='utf8')
f.wirte('hello')
print('world', file =f)
f.close()


```

- 닫고 싶어도 닫기 전에 예외가 발생하면 닫을수가 없다...
- 다음과 같이 예외처리르 통해, 꼭 닫아줘야 합니다

```python
f = open('sample.txt', 'wt', encoding='utf8')
try:
		f.write('hello  ')
    1/0								# ZeroDivisionError 예외 발생
finally:							# 예외 발생여부에 상관없이 무조건 실행
  	f.close()
    print('file closed')
```

### with 절

- 특정 block을 with 절을 통해, 해당 block 의 실행전/실행후/예외발생시의 처리를 with 절을 통해 처리가능
- open 함수에서 with 절을 지원하지만, with 절을 한번 만들어보자
- class를 통한 with절 지원도 가능

```python
from contextlib import contextmanager

@contextmanager
def myopen(filepath, mode, encoding):
    f = open(filepath, mode, encoding)
    try:
      	yield f				# with 절의 as에 넘겨짐
    finally:
      	f.close()
        
with myopen('helloworld.txt', 'wt', 'utf8') as f :
     f.write('hello ')
     f.write('world ')
      
      
# open 함수에서의 with절 지원
with open('sample.txt', 'rt') as f :
     file_content = f.read()

print(file_content)
```

### File object 순회 가능한 객체

- 줄 단위로 순회

```python
with open('sample.txt', 'rt', encoding='utf8') as f :
     for line in f:
      		print(line)
```

### 소스파일 저장은 필히 UTF-8로 

- 요즘 소스코드 에디터의 디폴트 인코딩은  UTF-8
- 파이썬에서는 각 소스파일 최상단 소스코드 자체의 인코딩 지정가능
  - python3 : 디폴트 utf-8
  - python2 : 디폴트 ascii (이 디폴트 인코딩이 원흉!!!)
- 파이썬은 소스코드를 실행하기 전에 소스파일의 내용을 먼저 디코딩
- 소스코드 인코딩을 파이썬에게 잘못알려주면, SyntaxError 예외 발생
- 이는 주석이라고 해서 예외가 없습니다. 파일 내 모든 문자열이 해당



## 15. 오버로딩과 오버라이딩

### 오버로딩(Overloading)

- 이름은 같지만, 인자와 리턴타입이 다른 멤버 함수를 여럿 정의하는 것.
- 파이썬에서는 미지원

### 오버라이딩(Overriding)

- 클래스 상속에서 사용되는 개념
- 상위 클래스가 가지고 있는 메소드를 하위 클래스가 재정의

### Sample.py

- 대신, 디폴트인자를 통한 처리가 가능합니다

```python
class Sample:
     def calculate(self, x, y, z=1):
      		return (x+y) * z
      
>>> sample = Sample()
>>> sample.calculate(1, 2), sample.calculate(1, 2, 3)

(3, 9)
```

​	

### 클래스 주요 오버라이딩 멤버함수

- ```__init__(self[, ...])``` : 생성자 함수

- ```__repr__(self)``` : 시스템이 해당객체를 인식할수있는 Official 문자열
  - 대개 디버깅을 위해 사용
  - 출력 문자열을 통해, 바로 인스턴스를 생성할 수 있도록, 인스턴 생성
- ```__str__(self)``` : Informal 문자열. str(obj) 시에 호출
- ```__getitem__(self, key)``` : self[key] 를 구현
- ```__setitem__(self, key, value)``` : self[key] = value 를 구현

### 클래스 주요 오버라이딩 멤버함수 - 연산자 재정의

- Binary Arthmetic Operations
  - +,-,*,@,/,//,%, divmod, pow, **, <<, >>, &, ^, |
  - ex) x + y 는 ```x.__add__(y)``` 함수를 호출

- Augmented Arithmetic Assignments
  - +=,-=,*=,@=,/=,//=,%=, **=, <<=, >>=, &=, ^=, |=
  - ex) x += y 는 ```x.__iadd__(y)``` 함수를 호출
- Unary Arthmetic Operations : -, +, abs, ~
  - ex)-obj는 ```obj.__neg__()``` 함수를 호출
- Built-in functions : complex, inf, float, round
  - ex) complex(obj)는 ```obj.__complex__()``` 함수를 호출
- Rich comparison : <, <=, ==, !=, >, >=
  - ex)  x < y 는 ```x.__lt__(y)``` 함수를 호출

### 예외 : ```__add__, __iadd__ ``` 구현하기

```python
class Person:
     def __init__(self, name, age):
         self.name = name
         self.age = age
     def __add__(self, value):
      	 return Person(self.name, self.age + value)
     def __iadd__(self, value):
				 self.age += value
      	 return self
     def __repr__(self):
      	 return "Person('{}', {})".format(self.name, self.age)
      
>>> tom = Person('Tom', 10)
>>> tom + 10
Person('Tom', 20)

>>> tom += 20
>>> tom 
Person('Tom', 30)
```



### 클래스 주요 오버라이딩 멤버함수 - with절 지원

- ```__enter__(self)```
- ```__exit__(self, exctype, excvalue, traceback)```
  - exc_type : 예외 (Exception) 클래스 타입
  - exc_value : 예외 인스턴스
  - traceback : Traceback 인스턴스
  - 예외가 발생하지 않았다면, 인자 3개 모두 None 으로서 호출

### 예외 : 클래스를 통한 with절 지원

```python
class File:
   def __init__(self, path, mode):
      self.path = path
      self.mode = mode
   def __enter__(self):
      self.f = open(self.path, self.mode, encoding='utf-8')
      return self.f    
   def __exit__(self, exc_type, exc_value, traceback):
      # 예외 발생여부에 상관없이 파일을 닫음
      self.f.close()
      
with File('filepath.txt', 'wt') as f:
  f.write('hello world')
```



## 16. 클래스 상속과 MRO

### 상속 (Inheritance)

- 코드 중복을 최소화하기 위한 목적으로 등장
- 파이썬 클래스는 최상위클래스인 object 를 상속
  - 파이썬2에서는 object 상속유무에 따라 old/new style class로 분리
  - 파이썬3에서는 old-style  class가 제거
- 클래스 간에 상속관계에 놓이게 되면, 부모/자식 관계가 성립 
- 자식 클래스는 부모 클래스의 모든 내역을 물려받음
- 다중상속 지원 : 직계 부모가 다수

### 상속으로 해결

- 사람과 관련된 코드는 모두 Person 으로 집결!!!

  ```python
  class Person(object):
    def __init__(self, name):
        self.name = name
        
    def run(self):
        print("뜁니다.")
        
    def eat(self, food):
        print('{}을 먹습니다.'.format(food))
        
    def sleep(self):
        print('잠을 잡니다.')
        
    def study(self, target):
        print('{}을 열심히 공부합니다.'.format(target))
  ```

- 코드가 보다 간결해졌습니다.

- 상속을 받고, 클래스 개별 코드만 구현합니다.

```python
class Doctor(Person):
  def research(self):
    	print('열심히 연구합니다.')
      
class Programmer(Person):
  def coding(self):
      print('열심히 개발합니다.')

class Designer(Person):
  def design(self):
      print('열심히 디자인을 합니다.')      
```



### MRO (method resolution order)

- 파이선의 클래스 탐색순서는 MRO를 따릅니다.
  -  Class.mro 를 통해 확인 가능
- MRO 가 꼬이도록 클래스를 설계할 수는 없습니다.
  - TypeError : Cannot create a consistent method resolution order (MRO)

### 부모의 함수 호출

- 내장함수 super를 통해 부모의 함수 호출
  - D의 mro 순서는 D > B > C > A
  - D().fn()의 실행결과로서 A, C, B, D 가 출력
- super 호출 시에  MRO 에 기반하여 호출

```python
class A:
  	def fn(self, arg):
      print('A', arg)
      
class B(A):
  	def fn(self, arg):
      print('B', arg)
      
class C(A):
  	def fn(self, arg):
      print('C', arg)      

class D(B, C):
  	def fn(self, arg):
      print('D', arg)            
      
>>> print (D.__mro__)
(__main__.D, __main__.B, __main__.C, __main__.A, object)
>>> print (D().fn('python'))
A python
C python
B python
D python
```

## 17. 예외처리

### 예외(Exceptions)

- 프로그램이 처리되는 동안 특정한 문제(예외)가 일어났을 때 진행중인 루틴을 중단하고, 콜스택을 거슬러 올라가, 예외를 전파하는 메커니즘
  - 이 예외를 처리할 수 있는 핸들러를 찾아, 함수 호출 역순으로 거슬러 올라가, 본 예외를 처리할 수 있는 핸들러를 찾아내면 그 곳에 처리를 맡긴다
  - 예외를 처리하는 핸들러를 찾을 수 없다면, 그 즉시 파이썬 프로그램이 비정상종료되며, 그 예외 내역에 대한 StackTrace 를 출력

```python
print('line 1')
value = int('a') + 1
print('line 2')

# 위 코드를 실행하면 ValueError 예외가 발생하며, 코드 실행이 중단

line1
------------------------------------------------------
ValueError 																		Traceback ( most recent call last)
------> 1 value = int('a') + 1

ValueError : invalid literal for int() with base 10 : 'a'
```

### 예외 잡기

```python
print('line 1')
try:
		value = int('a') + 1
except ValueError as e :
		print(e)
print('line 2')
```

실행결과 : 예외를 정확하게 잡아서 처리했기 때문에, 다음 루틴이 이어서 계속 실행

```python
line 1
invalid literal for int() with base 10: 'a'
line 2
```

### 호출한 함수 내에서 발생한 예외도 잡을 수 있습니다.

```python
def fn1(x, y):
  	return x + y

def fn2(x, y):
  	return 10 * fn1(a, b)

try:
  print(fn2('a', 10))
except TypeError as e :
  print(e)
  
실행결과

must be str, not int
  
```

### 흔히 만나는 빌트인 예외

- Exception: 최상위 예외 클래스
- Stoplteration
  - Iterator 내에서 더 이상 생산할 Item이 없을 때
  - for in 구문에서 이 예외를 통해 반복문 중단을 처리
- AttributeError : Attribite  참조 실패 혹은 설정이 실패한 경우
- ImportError : 지정 모듈/팩키지를 import 하지 못한 경우
- NotImplementedError : 구현하지 않은 부분임을 명시할 때, 개발자가 직접 본 예외를 발생 (raise)
- IndexError : 범위 밖의 인덱스 참조시
- KeyError : 존재하지 않는 Key에 접근시
- NameError : local/global name 을 차지못한 경우
- TypeError : 부적절한 연산/함수를 적용했을 때, ex) 1 + '1'
- ValueError : ex) int('a')
- IndentationError : 소스코드 내에 부적절한 들여쓰기가 있을 때

### NotImplementedError 예시

아직 구현하지 않은 부분임을 명시

```python
class Person:
  	def run(self):
    		raise NotImplementedError
      
class Doctor:
  	pass

class Developer(Person):
  	def run(self):
      	print('개발자는 오늘도 뜁니다')
        
Doctor().run()		# NotImplementedError 발생. 자식 클래스에게 run 함수구현 (Overriding)을 강제하는 효과
Developer().run() # 예외없이 정상적으로 수행
```

### 

### 예외처리

- tuple로 예외를 다수 지정할 수 있습니다.
- as  를 통해 예외 인스턴스를 획득 가능
- else : 예외가 발생하지 않았을 때 호출되는 블럭
- finally : 예외 발생 유무에 상관없이 호출되는 블럭

```python
try:
  	some_code()
    some_code()
    some_code()
except ValueError:
    print('ValueError 가 발생했어요.')
except (KeyError, TypeError):
    print('VaueError/TypeError 중에 하나가 발생')
except ZeroDivisionError as e:
    print('0으로 나누지마세요. : {}'.format(e))
else:
    print('예외가 발생하지 않았어요.')
finally:
  	print('예외발생 유무에 상관없이 호출됩니다.')
```



### 사용자 예외 정의 (2)

- 손쉬운 예외 분류를 위해 사용자 예외 정의

  ```python
  class TooBigNumberException(ValueError):
      def __init__(self, value):
        	self.value = value
      
      def __str__(self):
          return 'too big number {}.'.format(self.value)
  
  class TooSmallNumberException(ValueError):
      def __init__(self, value):
        	self.value = value
      
      def __str__(self):
          return 'too small number {}.'.format(self.value)
        
  def fn(i):
      if i > 100:
          raise TooBigNumberException(i)
      elif i < -100:
          raise TooSmallNumberException(i)
      return i * 10
    
  try:
      fn(200)
  except TooSmallNumberException as e:
      print(e)
  except TooBigNumberException as e:
      print(e)
  
  
  ```

  

  ## 18. 장식자

  ### 장식자 (Decorator)

  - 어떤 함수를 감싸는 (Wrapping ) 목적의 함수
  - (잠깐) 1급 함수 : 함수를 동적으로 생성 가능, 반환값으로 전달 가능

  ```python
  def base_10(fn):
    	def wrap(x, y):
        	return x + y + 10
      return wrap
  
  def mysum(x, y):
      return x + y
  mysum = base_10(mysum)
  
  >>> mysum(1, 2)
  13
  
  @base_10
  def mysum(x, y)
  		return x + y
  
  >>> mysum(1, 2)
  13
  
  #Example : memoize
  import time
  
  def memoize(fn):
      cached = {}
      def wrap(x, y):
          key = (x , y)
          if key not in cached:
            	cached[key] = fn(x, y)
          return cached[key]
      return wrap
    
  def long_mysum1(x, y)
  		time.sleep(1)
      return x + y
    
  @memoize
  def long_mysum2(x, y)
  		time.sleep(1)
      return x + y
    
  for i in range(3):				# 실제 소요시간 약 3초
      print(long_mysum1(1, 2)) # memoize 미적용
  
  for i in range(3):				# 실제 소요시간 약 1초
      print(long_mysum2(1, 2)) # memoize 적용
      
  ```

  ### 장식자에 인자 지원

  ```python
  def base(base_i):
      def outer(fn):
        def wrap(x, y):
           return x + y + base_i
        return wrap
      retrun outer
      
  @base(20)
  def mysum2(x, y):
      return x + y
  
  @base(30)
  def mysum3(x, y, z):
      return x + y + z
  
  >>> mysum2(1, 2)
  23
  >>> mysum3(1, 2, 3)
  36
  
  # filter_fn을 통과하지 못하는 인자는 alter_value 값으로 대체하기
  def myfilter(filter_fn, alter_valeu):
    	def wrap(fn):
      		def inner(*args):
            	raise NotImplementedError('구현해주세요.')
          return inner
      return wrap
    
  @myfilter(lambda i : i%2==0, 0)
  def mysum(a, b, c, d, e):
      return a + b + c + d + e
    
  @myfilter(lambda i : i%2==0, 1)
  def mymultiply(a, b, c, d, e):
      return a + b + c + d + e
  
  >>> mysum(1, 2, 3, 4, 5)  
  6
  
  >>> mymultiply(1, 2, 3, 4, 5)  
  8
    
  ```

  





























