# [[MIT] 데이터 사이언스 기초](https://www.edwith.org/datascience/lecture/33888/)
Today I Learned

## Chapter 1. Introduction and Optimization Problems
### 계산모델 (Computation Model)
- 이제까지 일어났던 무언가를 이해하거라 매일 보는 현상들을 설명하는 모델
- 아직 일어나지 않은 미래를 예측할 수 있게 해주는 모델
- 예) 날씨 변화 모델 : 천년 동안 날씨가 어떻게 변했는지에 대한 모델과 미래에 어떻게 될지 예측하는 모델을 만들 수 있음

### 최적화 모델(Optimization Model)
- 제한 조건을 가지며 목적 함수를 최대화 또는 최소화하는 모델
- 냅색(배낭) 문제
  제한 조건 : 냅색 안에 들어갈 수 있는 양
  도둑이 가장 값비싼 물건을 훔쳐야 하는 최적화 문제
  연속 냅색 문제
    - 일부분만 가져갈 수 있는 문제(금괴가 아닌 금모래로 가져갈 수 있는 경우)
    - 탐욕 알고리즘으로도 풀 수 있고, 풀기 쉬운 편
  0/1 냅색 문제
    - 금괴를 가져가거나 아예 못 가져가는 경우
    - 한번 결정하면 그 결정이 다음 결정에 영향을 미침
    
### 최적화 문제를 푸는 방법
- 무차별 대입 알고리즘(Brute force algorithm)
    모든 경우의 수를 고려해 승자를 택하는 것
    그러나 실용적이지는 않다
- 탐욕 알고리즘 (Greedy algorithm)
    while kanpsack not full put 'best' available item in kanpsack
    여러 경우 중 하나를 결정할 때 그 순간 best 라고 생각되는 것을 선택해 나가는 방식
    가장 좋은 것 (best)의 의미는 정의에 따라 달라짐
    탐욕 알고리즘은 좋은 해를 구할수는 있어도 최적 해를 구할수는 없음
    
### 파이썬 람다 표현식
- 익명의 함수를 만들 때 사용
- (lambda 식별자 배열: 원하는 식)
- 이 파라미터들로 표현된 식을 계산하고 결과를 반환하는 함수를 만듬
- def 를 쓰는 대신에 인라인 함수로 정의

람다 함수에 대한 설명이 나와있는 문서
[점프 투 파이썬](https://wikidocs.net/64) 

## Chapter 2. Optimization Problems
### 탐욕 알고리즘(Greedy Algorithm)
결정할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 최종 답에 도달하는 방식
- 장점 : 구현하기 쉬움, 매우 빠름
- 단점 : 최적일 수도 있고 아닐수도 있는 해를 구함

### 무차별 대입 알고리즘(Brute Force Algorithm)
- 탐욕 알고리즘을 대체할 수 있는 알고리즘
- 항목의 조합 가능한 수를 열거한 후, 전체 합이 가중치를 넘어가는 것은 제거

### 동적 프로그래밍(Dynamic Programming)
- 복잡한 문제를 간단한 여러 개의 문제로 나누어 푸는 방법
- 최적 부분 구조 문제일 경우 풀 수 있는 방법
    - For x > 1, fib(x) = fib(x-1) + fib(x-2)
- 중복 부분 문제일 경우 풀 수 있는 방법
    - 최적 해를 구할 때 같은 문제를 여러 번 풀어야 하는 문제
    - fib(x)를 1번 계산하거나 여러 번 계산하는 경우
- 근사가 아닌 최적화 해법이 구해짐

## Chapter 3. Graph-theoretic Models
### 그래프(Graph)
- 그래프는 꼭짓점 혹은 노드로 이루저이고 이들은 간선 혹은 변으로 이루어짐
- 노드의 집합
    - 각 노드는 다른 노드와 관계된 정보를 담고있음
    - 예 ; 학생의 성적
- 간선, 변이
    - 노드의 쌍을 연결
    - 간선을 이용해 그래프를 만드는 2가지 방법: 무방향, 유향
- 사용 예시
    - 개체 사이의 관계 표시
        - 예 : 파리에서 런던으로 여행을 갈 때 노드는 각 도시 연결은 도시 사이 레일
- 유용한 이유
    - 세상에 존재하는 여러 관꼐는 그래프로 표현하기 적합
    - 컴퓨터 네트워크, 교통 네트워크, 금융 네트워크, 정치 네트워크, 범죄 네트워크, 사회 네트워크 등
- 그래프를 만드는 방법
    - 두 요소 사이에 연속된 간선이 있는지 확인
    - 최소 비용 혹은 최단 경로를 찾을 수 있는지 확인
    - 그래프 분할 문제로 접근
그래프 탐색
    - 한 노드에서 다른 노드로 가는 최단 경로를 구하는 방법은?
    - 최단 경로 : 시작점의 첫 간선 ~ 도착점의 마지막 간선
        - 일종의 사슬처럼 보임
    - 알고싶은 것 : 최소 단계 수
    - 1) 깊이 우선 탐색 (Depth-first Search)
        - 루트 노드에서 시작해 다음 분기로 넘어가기 전에 해당 분기를 모두 탐색하는 방법
        - 루프의 가능성이 있기 떄문에 경로를 기억해야 함
        - 이미 들렀던 노드는 가지 않음
            - 첫 간선을 따라가다 올바르게 왔는지 확인 올바르지 않으면 루프
            - 목표 노드에 도착하거나 선택지가 없어질 때까지 반복
        - 특징
            - 자기 자신을 호출하는 순환 알고리즘
            - 어떤 노드를 방문했는지를 반드시 확인
     
     [그래프 깊이 우선 탐색 ratsgo's blog](https://ratsgo.github.io/data%20structure&algorithm/2017/11/20/DFS/)            
     ```python     
    from pythonds.graphs import Graph
    class DFSGraph(Graph):
        def __init__(self):
            super().__init__()
            self.time = 0
            
        def dfs(self):
            # 모든 노드의 색상을 white, 부모노드 정보를 -1로 초기화
            for aVertex in self:
                aVertex.setColor('white')
                aVertex.setPred(-1)
            for aVertex in self:
                # 임의의 노드가 아직 방문하지 않은(white) 노드라면 해당 노드에 대해 dfsvisit 호출
                # dfsvisit은 더 이상 나아갈 엣지가 없을 떄까지 재귀적으로 수행, 수행 후에도 white인 노드가
                # 있으면 해당 노드를 시작노드로 해서 dfsvisit 반복 수행
                if aVertex.getColor() == 'white':
                    self.dfsvisit(aVertex)
        
        def dfsvisit(self, startVertex):
            # processing 이라는 의미로 시작노드의 색상을 gray로 변
              
     ```
     
    - 2) 너비 우선 탐색 (Breadth-first Search)
        - 루트 노드에서 시작해 인접한 노드를 먼저 탐색하는 방법
        - 특징
            - 루트 노드에서 목표 노드까지의 최단 거리를 보장
            

## Chapter 4. Stochastic Thinking
### 확률론적 사고(Stochastic Thinking)
- 세계를 본질적으로 예측가능할 수 없다고 취급하는 것이 나을 수 있음
    - 세상엔 불확실성(무작위성)이 너무 많아 이해하기 어려움
    - 무작위성을 위해 확률론적 사고를 할 필요성이 있음
    
- 확률에 대한 3가지 기본 사실
    - 확률은 항상 0 ~ 1
    - 분모 : 가능한 모든 사건의 수 분자 : 부분 집한인 관심을 갖는 사건
    - 어떤 사건이 일어날 확률이 p라면 일어나지 않을 확률은 1-p
    
- 중요한 법칙 (곱의 법칙)
    - 사건이 서로 독립적이라면 모든 사건이 일어날 확률은 각 사건이 일어날 확률을 곱한 것과 같음
    - A가 일어날 확률이 0.5고 B가 일어날 확률이 0.4라면 A,B가 이러날 확률은 0.2
    - 그러나 이런 법칙은 독립적인 경우에만 적용
    - 하나의 결과가 다른 결과에 영향을 주지 않는다면 두 사건은 독립적
    - 사람들은 자주 독립성이 없는 경우에도 독립적임을 가정하고 확률을 계산하니 주의가 필요

### 시뮬레이션 모델(Simulation Model)
- 시스템이 가능한 행동에 대한 정보를 제공하는 계산을 나타내는 프로그램
    - 시뮬레이션을 작성하고, 그 사건이 드물게 발생하면 추정된 확률을 믿기 전에 더 많은 시도를 하는 것이 좋음
        - 드물게 발생하는 사건의 좋은 추정을 얻기 위해선 많은 시도가 필요
        - 항상 실제 확률과 헷갈리지 않도록 추정된 확률이라는 것을 알고 있어야 함
- 시뮬레이션을 사용하는 이유는?
    - 복잡한 확률 계산을 하는 대신 확률적인 질문에 대한 답을 얻기 위해 시뮬레이션을 사용하는 주된 이유
- 초반에 본 최적화 모델(1~3강)과 다른 점
    - 최적화 모델은 규범적
    - 어떻게 배낭에서 최대의 가치를 얻는지
    - 어떠헥 A에서 B로 가는 최단 거리로 가는지
    - 반면 시뮬레이션 모델은
        - 이런 결과가 나타난다는 것을 말해줌
        - 어떻게 그 일을 일어나게 해주는지 말해주지 않음
        - 현실의 근사치일뿐임
        - 수학적으로 접근하기 힘든 문제를 풀 경우 시뮬레이션을 사용하면 유용
        - 다양한 조건을 쉽게 조절하면서 진행할 수 있기 떄문에 잘 사용함
        
- random.choice 함수
    - 실제로 무작위적이지 않음 의사 난수라는 것을 생성함 (pseudo random)
        - 연속된 수에서 한 숫자가 다음 숫자를 생성하는 알고리즘이 있음(seed)
        - 컴퓨터의 클럭을 가지고 읽음
        - random.seed 를 사용해 같은 시작점에 대해 같은 무작위적인 값을 얻음
    - 해당 원소 중 하나를 추출
    - p 파라미터에 확률값을 넣어서 사용할 수 있음
                  
    
## Chapter 5. Random Walks
### 무작위 행보(Random Walks)
- 많은 영역에서 중요
    - 주식 시장에서 가격의 움직임을 입증하는데 가장 좋은 모델
    - 현대의 많은 포트폴리오 분석이 기반을 두고 있음
    - 전파를 모델링할 때도 랜덤 워크를 사용, 열 전파나 분자의 전파
- 우리 주변의 세계를 이해하기 위해 시뮬레이션을 어떻게 사용할지에 대한 좋은 사례를 제공
- 추상적인 것들을 다루면서 프로그래밍과 소프트웨어 엔지니어링을 같이 진행
- 예시) 술 취한 사람의 걸음과 편향성을 가진 술 취한 사람의 걸음 차이를 파악

### 위생 검사 (Sanity Check)
- 시뮬레이션을 생성핧 땐 위생 검사가 필요
- 시뮬레이션이 실제로 말이 되는지 확인하는 과정
    - 의심을 가져야 함
    - 코드에 버그가 있을 수 있음!

### 정리
- 랜덤 워크를 하는 요점은 시뮬레이션 모델이 아닌 어떻게 만드는지에 관한 것
- 클래스를 정의하는 것부터 한번의 시도와 여러 번의 시도에 대응하는 함수를 만들고 결과를 보는 과정
- 시뮬레이션에 점진적 변화를 줘서 다른 문제를 조사할 수 있음
- 처음엔 간단한 시뮬레이션으로 시작해 잘 되지 않는 이유를 알고 Sanity check로 잘못된 것을 체크
- plot 스타일로 그래프를 그림

## Chapter 6. Monte Carlo Simulation
### 몬테 카를로 시뮬레이션(Monte Carlo Simulation)
- 추리통게학을 이용해 알 수 없는 값을 추정하는 방법
- 핵심 개념은 모집단
    - 모집단 : 가능한 예시들의 전체 집합
    - 모집단으로부터 적당한 부분 집합을 뽑음
        - 표본의 통계를 통해 모집단을 추론
        - 일반적으로 표본을 추출하면 그 표본이 모집단과 동일한 특성을 갖는 경향이 있음
        - 우리가 취할 수 있는 수많은 랜덤워크, 만개를 보지않고 100개 추출해서 평균 계산한 후 기대값 계산
        - 표본 추출이 무작위어야 함! 무작위로 뽑은 표본이 아니면 모집단과 같은 특성을 가질 것이라고 기대할 수 있는 근거가 없음

### 큰 수의 법칙 또는 베르누이의 법칙
- 실제 확률이 동일한 독립사건이 반복되면 실행 횟수가 무한대로 갈수록 p와 다른 결과가 나오는 횟수의 비율이 0으로 수렴
- 공정한 룰렛 휠을 무한번 돌리면 기댓값이 0이 됨

### 도박사의 오류
- 잘못된 결과의 오류
- 도박사의 오류에 의하면 사람들은 기대와 다른 이변이 일어나면 미래에 다시 정상으로 돌아올 것이라고 믿음
- 서로 영향을 끼치지 않는 일련의 확률적 사건들에서 상관 관계를 찾는 오류를 발생

### 평균으로의 회귀
- 부모가 둘 다 평균보다 키크면 자식이 부모보다 작은 가능성이 높다
- 역으로 부모가 평균보다 작으면 자식은 평균보다 클 가능성이 높다
- 도박사의 오류와 미묘하게 다름
- 극단적인 사건 다음에 오는 사건은 덜 극단적인 경향이 있다
- 공정 룰렛 휠을 10번 돌려 빨간색이 나온다면(극단적 사례) 10번에서는 빨간색이 10보다 적게 나온다는 개념. 덜 극단적인 사건이다
- 극단적인 결과보다는 20번 돌린 것의 평균 결과가 50% 빨간색이라는 평균값에 더 가까울 것
- 더 많은 표본을 취할수록 평균에 더 가까워짐

### 분산과 표준편차
- 기저 확률의 변이성에 따라 필요한 표본의 수가 달라짐
- 데이터의 변이성을 알기 위해 알아야 되는 개념 : 분산
    - 평균으로부터 모두의 거리를 구하여 단순히 다 더함
    - 마지막으로 집합의 크기(전체 항목) 개수로 나눔
    - 단지 항목의 개수가 많다는 이유로 분산이 높아지는 것을 막기 위해서, 항목의 개수로 정규화함
    - 제곱을 하는 이유 :
        - 차이가 양수든 음수든 상관이 없다는 것. 평균으로부터 어느 쪽에 있는지보다 근처에 있지 않다는 것이 중요함
        - 거리를 제곱해 이상치를 특별히 강조함(장점이자 단점)
- 표준편차
    - 분산의 제곱근
    - 표준편차 그 자체로는 의미없는 숫자
    - 항상 평균을 고렿애 생각해야 함
- 신뢰구간
    - 우리는 종종 평균만 가지고 예측하려고 함
    - 값을 모르는 매개변수를 설명할 때 기댓값과 같은 특정 값을 주는 것보다 신뢰 구간으로 표현하는 것이 좋음
    - 신뢰구간은 모르는 값이 포함될 가능서이 높은 구간과 그 구간에 존재할 확률을 알려줌
    - 결과가 -1%과 +1% 사이일 것이라 예측하고 전체 게임 중 95%는 이 예측이 맞을 것이라고 기대하는 것
- 신뢰 구간은 어떻게 계산할까?
    - 경험적인 규칙을 사용
    - 데이터를 얻어 평균을 찾고 표준편차를 계산하면 데이터의 58%는 평균값 앞뒤로 1 표준편차 범위 이내에 있음
- 경험적인 규칙을 적용하기 위한 가정
    - 평균 추청 오차가 0
        - 높게 예측할 가능성과 낮게 예측할 가능성이 같아야 함
        - 이런 류의 실험과 시뮬레이션에선 타당한 가정
        - 오차에 편향이 없다는 가정
    - 오차의 분포가 정규분포
        - 가우스 분포, 정규분포
    - 이 두 가정하에 경험적 규칙은 항상 유효
    
### 확률분포
- 확률 분포 : 확률 변수가 서로 다른 값을 가지는 상대적 빈도를 나타내는 개념
- 확률 변수
    - 이산 확률 변수
        - 유한 집합의 값들을 가짐
        - 동전을 던지면 앞면과 뒷면이란 2개의 값만 나옴
    - 연속 확률 변수
        - 확률밀도함수 (PDF)를 사용
        - 두 값 사이 어딘가에 존재할 확률을 알려줌  
        
        
## Chapter 7. Confidence Intervals
경험적인 규칙의 전제
- 지난 강의에서 나온 경험적인 규칙의 전제
    - 평균 추정 오차는 0
    - 오차의 분포는 정규분포 (가우스 분포)  
    
### 확률밀도함수(PDF)
- 분포는 확률밀도함수로 정의
    - 이 함수로 어떤 확률변수가 임의의 두 값 사이에 있을 확률을 구할 수 있음
    - 이것은 최소부터 최대값 사이에 놓여있는 x축의 값을 가진 곡선으로 정의
    - 두 값 사이의 곡선 아래의 넓이가 그 범위안에 속해있을 확률을 도출
- 누적분포함수의 도함수
- 구하려는 것 : 어떠한 값이 표시한 범위 내에 해당할 확률을 구하고 싶으면 확률은 이 곡선 하단의 면적이자 적분 값

### 중심 극한 정리 (CLT, central limit theorem)  
- 동일한 확률분포를 가진 독립 확률 변수 n개의 평균의 분포는 n이 적당히 크다면 정규분포에 가까워진다는 정리
- 우리의 현실은 모든 분포가 정규분포는 아님
- 충분한 표본을 가지고 있다면 표본의 평균값은 대략적으로 정규 분포
- 원래 값의 분포도 모양은 상관이 없음
    - 충분히 큰 표본의 평균을 측정한다면 CLT(중심극한정리)는 신뢰구간을 계산하는데 경험적인 규칙을 사용할 수 있도록 함
- 원주율 구하는 예시
    - 원의 둘레를 지름으로 나눈 값
    - 많은 바늘들을 임의로 떨어트림
    - 어디에 떨어졌는지 보고 몇개는 정사각형 안이지만 원 안에 떨어지는 것도 있음
    - 원 안의 바늘과 정사각형 안의 바늘의 비율은 정사각형의 면적과 원의 면적의 비율과 정확하게 일치할 것
    - 파이는 정사각형의 넓이를 정사각형 안의 바늘의 갯수로 나눈 값
    - 논리 : 많은 바늘을 떨어뜨린 후, 떨어진 위치를 보고 더하여 그 값으로 신기하게도 실제 파이 값을 알 수 있음
    - 1의 확률로 실제 파이의 값이 두 값 사이에 있는 말은 사실
    - 0.95의 확률로 실제 파이의 값은 두 값 사이에 있다는 말도 사실
        - 시뮬레이션을 통해서만 알 수 있음        
            
## Chapter 8. Sampling and Standard Error
- 1개 이상의 임의 표본을 조사하여 모집단을 추정하는 것
- 몬테 카를로 시뮬레이션으로 매우 많은 임의 표본을 생성학 그것을 이용해 신뢰 구간을 계산할 수 있음
- 만약 시뮬레이션으로 표본을 생성할 수 없다면
    - 표분 추출을 사용해야 함
### 표본 추출(Sampling)
- 모집단에서 하나 이상의 무작위로 추출된 표본을 보는 것
- 시뮬레이션을 하지 않을 때 표본 추출을 어떻게 하는가?
    - 확률 표본 추출
    - 모집단의 모든 요소들은 표본으로 추출될 수 있는 0이 아닌 확률을 가지고 있음
        - 시간 전부를 단순 임의 추출에 적용
            - 모집단의 각 요소들은 표본으로 추출될 확률이 모두 같음, 편향이 없음
            - 항상 적절한 것은 아님
        - 층화 추출(stratified sampling)
            - 모집단을 세부 그룹으로 나눈 후 각 세부 그룹에서의 단순 임의 추출
            - 세부 그룹의 크기와 비율을 동일하게 적용
            - 세부 그룹이 있을 때 사용
            - 모집단의 크기에 따라 비율적으로 대표
            - 이 방법은 표본의 필요한 크기를 줄이는 데에도 사용할 수 있음
- 중심 극한 정리 복습
    - 표본 집합에 있는 표본들의 평균(표본평균)은 거의 정규분포를 따름
    - 이 정규분포의 평균은 모집단의 평균에 가까움
    - 표본평균의 분산은 모집단의 분산을 표본의 크기로 나눈 값에 가까움
    - 평균의 표준편차(SME, SE) 계산
        - SE = σ/√​n
​
### 왜도(Skewness)
- 확률 분포도의 비대칭 정도를 측정
    - 왜도가 클수록 좋은 근사치를 얻기 위해 더 많은 표본이 필요함
    - 모집단이 아주 기울어지고 분포도가 아주 비대칭이면 더 많은 표본이 필요
    - 만약 아주 균등하다면 적은 표본이 필요
- 얼마나 많은 표본이 필요할지 정할 때에 모집단의 왜도의 추정치가 필요함

### 단일 표본으로부터 평균 추정
1) 모집단의 왜도 추정값에 따라 표본의 크기 결정
2) 모집단으로부터 임의 표본 추출
3) 표본의 평균과 표준편차 계산
4) 표본의 표준편차를 이용해 표준오차 추정
5) 표준오차 추정값을 통해 표본평균 주변의 신뢰구간 생성

### 표준편차 (SD) & 표준오차 (SE)
표준편차 (SD, Standard Deviation)
- 점수집합 내에서 점수들 간의 상이한 정도를 나타내는 산포도 측정 도구
- 표준편차가 클수록 평균값에서 이탈한 것
- 표준편차가 작을수록 평균값에 근접한 것
- 변수값이 평균값에서 어느 정도 떨어져 있는지를 알 수 있음  
  
표준오차 (SE, Standard Error)
- 표본추출의 과정에서 발생하는 오차와 연관된 것으로 추정량의 정도를 나타내는 측정 도구
- 표본이 모집단으로부터 얼마나 떨어져 있는지를 나타내는 것
- 각 표본들의 평균과 전체 평균 간의 간격
- 표준오차가 작을수록 표본의 대표성이 높다
- 표본평균의 표준편차
- 시그마 = 표준편차
- 시그마 제곱 = 분산

## Chapter 9. Understanding Experimental Data (cont.)
### 실험으로 데이터를 얻는 경우
- 실험 과학과 통계가 만남
- 데이터를 얻음녀 무엇을 할 수 있을까?
    - 데이터 및 모델이 어떤 연관성이 있느지
    - 미래 기대치에 대해 무엇을 말해주는지
    - 데이터를 통해 예상할 수 있는 다른 결과는 무엇인지
    - 사회적으론 응답에 대해 어떻게 생각하는지, 다음 선거에서 누구를 뽑을지 등
    - 세번째로 데이터 관련 문제에 답을 위한 계산을 설계
- 추가적인 실험을 위해 계싼을 어디에 사용할지?

### 데이터에 곡선 피팅
- 데이터에 곡선을 맞추는 것은 도긻 변수를 종속 변수의 추정값에 관련시키는 방법을 찾는 것
- 어떤 곡선이 데이터에 얼마나 잘 맞는지를 결정하려면, 적합도를 측정하는 방법, 즉 목적 함수가 필요함
    - 목적 함수가 얼마나 정확한지를 측정해줄거임
- 목적 함수를 정의하고 나면, 그것을 최소화하는 곡선(선)을 찾아야함
    - 최소화하는 선: 추세선
- 측정점들까지의 거리의 합에 관한 함수가 최소화되는 직선을 찾아야 함
    - 측정값들의 거리 합이 최소화가 되는 곳을 찾기  
### 거리 측정
- 점을 찍어보면 일직선은 아님
- 직선을 찾기 위해
    - 측정값과 잡음을 고려
    - 독립 변수인 x축을 종속 변수 y축에!!!
    - 직선이 있더라도 얼마나 적절한지 측정해야 함
- 목적 함수가 필요
    - 얼마나 정확한지 측정해줄거임
    - 목적 함수를 정의하고 나면 최소화하는 선을 찾음
    - 최적의 선, 목적 함수를 최소화하는 선을 찾음!
        - 이게 추세선
- 직선에서 측정값들의 거리의 합이 최소화가 되는 곳을 찾기
    - 종속 값을 예측하려고 함
    - 차이, 불확실성은 수직 변위임
### 추세선의 적합성을 파악하는 방법
- 그냥 서로 비교
- 절대적인 값을 구하기
- 우린 하려고 하는 것
    - 독립 변수에 대한 종속 변수의 함수를 구함
    - 독립 변수가 주어졌을 때 예측을 가능하게 하는 것
    - 어떤 추세선이 더 나은 추정값을 반환하는지 알고싶음
    - 추세선의 적절성을 측정하는 방법을 찾으려 함
    - 결정 계수 (R^2) 사용
### 결정계수
- 분자는 추세선에서 오차를 구하고 분모는 데이터 자체의 편차를 나타냄
    - 분모는 데이터가 얼마나 변화하는지
    - 분자는 오차 값들이 얼마나 퍼져있는지
    - 표본의 수로 나누면 meanError
- 의미
    - 데이터에서 얼마만큼의 범위가 저 모델에 의해 설명되는지?
    - 선형 회구로 추세선을 만들면 R square 는 0 ~1
    - 1은 모든 데이터를 설명할 수 있다는 뜻
        - 데이터의 변동성을 모델로 완벽히 예측할 수 있음
    - 0이면 아무 의미가 없음
        - 실제값과 추정값 사시에 어떤 연관성도 없음
    - 높은 값을 가져서 반드시 사용해야되는 건 아님
    
## Chapter 10. Understanding Experimental Data (cont.)
### 높은 차수의 모델을 사용하지 않는 이유
- 새로운 행동을 얼마나 잘 예상하는지 궁금
    - 여기서 보는 것은 훈련 오차인데, 모델이 학습한 데이터를 잘 표현하는 것
    - 검증 또는 교차 검증(Cross Validate)을 통해 학습한 데이터가 아닌 새로운 데이터를 얼마나 잘 파악하는지 보고 싶음
- 높은 차수 모델은 가능한 차수에 대한 자유도가 너무 높음
    - 정해지지 않은 모수가 너무 많음
    - 노이즈도 포함
- 왜 지수에 자유도를 높일 때 결과가 좋을까?
    - 사실 더 높은 지수를 추가하면 영향을 끼치지 않음
        - 완벽한 데이터를 가지면 계수가 0일듯
        - 추세선에 영향을 끼치지 않음
    - 그러나 노이즈가 많으면 모델은 노이즈도 추세에 포함
        - 더 나은 추세선은 아님
- 모델이 간단하고 데이터를 잘 설명할 수 있는 중간의 모델을 원함
- 알맞는 모델을 어떻게 구하는 방법
    - 낮은 차수의 그래프부터 시작
    - 차수를 높이세요
    - 반복하세요
    - 정확도가 떨어지기 시작할 때가 적합한 모델을 찾았다는 신호

### 모형 검증
- 예측 모형의 최종 성능을 객관적으로 측정하려면 모수 추정 즉 트레이닝에 사용되지 않은 새로운 데이터, 즉 테스트 데이터를 사용해야한다.
모형의 모수 갯수를 증가시킨다든가 커널 모형, 신경망 모형과 같은 비선형 모형을 사용하게 되면 트레니이 데이터에 대한 예측 성능을 얼마든지 높일 수 있기 때문이다.
이러한 방법에 의해 과최적화가 일어나면 트레니이 데이터에 대해서는 예측이 잘되지만 테스트 데이터에 대해서는 예측 성능이 급격히 떨어지는 현상이 발생한다.
    
### 교차 검증
- 모형 성능을 정상적으로 검사하려면 테스트 데이터가 별도로 있어야 하기 때문에 현실에서는 확보한 데이터 중 일부를 떼어내어 테스트 데이터로 사용.
테스트 데이터를 어떻게 골라내느냐에 따라 모형의 성능이 달라지므로 한 개의 테스트 데이터만 사용하는 것이 아니라 각기 다른 방법으로 서로 다른 테스트 데이터를 여러번 골라내서 복수의 테스트를 실시하는 것이 일반적.
교차 검증을 통한 모형성능은 보통 다음과 같은 두 가지 값으로 나타낸다.
    - 오차평균 : 트레이닝에 사용되지 않은 테스트 데이터에 대해서 평균 오차의 크기가 얼마나 작은가?
    - 오차분산 : 트레이닝에 사용되지 않은 테스트 데이터에 대해 오차의 크기가 얼마나 달라지는가?
이 중에서 오차 분산을 계산하려면 테스트 데이터 셋이 최소한 세 개 세트가 있어야 한다.

- 하나의 데이터셋으로 모델을 생성한 후, 다른 데이터셋으로 모델 검증
    - 검증 오차가 훈련 오차보다 클 것
    - 학습 오차보다 일반성을 더 잘 나타냄
- 상황별 교차 검증
    - 데이터 세트가 작다면 Leave one out cross validation(LOOCV)을 사용
        - 데이터 세트 크기만큼 반복하고 데이터 셋 혹은 복사본 표본 중 하나를 버림
        - 버리고 훈련 데이터 셋으로 모델을 만든 후 평균
    - 데이터 세트가 크다면 k-fold 교차 검증
        - 데이터 세트를 k 크기의 작은 세트로 분할하고 나머지를 이용해 모델 생성
    - 반복 무작위 추출법
- 왜 여러 개의 데이터 세트로 검증해야 할가?
    - 편차가 클 수 있음
    - 다른 결론에 도달할 수 있음
    - 각 실행에 대한 통계 값을 얻을 수 있음

### 정리
- 선형 회귀를 이용하여 데이터에 곡선을 피팅할 수 있음
    - 독립 변수를 종속 변수로 연결시키기
- 그 곡선은 우리가 본 적 없는 독립 변수 값(표본에 없는 데이터)에 대한 값을 예측하는 데 사용될 수 있는 모델
- R2은 모델을 평가하는 데 사용됨
    - 과대 적합의 위험성이 있으므로 높다고 항상 "더 좋은" 모델은 아님
- 모델의 복잡도를 선택하는 기준
    - 데이터의 구조에 관한 이론
    - 교차 검증
    - 단순성                 
    
## Chapter 11. Introduction to Machine Learning
### 머신러닝
- 자연어 처리, 계산생물학, 컴퓨터 비전, 로보틱스 모두 머신러닝에 의존
    - 얼굴 인식 기술: 얼굴을 감지하고 또 식별할 때 사용
    - IBM Watson의 암 진단법
- 경험을 통해서 학습하는 프로그램 -> 새로운 사실을 예측하고 싶음
- 컴퓨터가 명시적으로 프로그래밍 되지않고 학습하게 만드는 연구 분야
- 프로그램을 통해 인풋 -> 출력
- 머신러닝은 프로그램에게 원하는 것의 예시를 제공
    - 컴퓨터 할 일은 주어진 출력과 데이터에 대한 정의로 프로그램을 생성
- 일반화
    - 데이터의 내적 패턴으로부터 정보를 유추하는 프로그램을 작성하는 것에 관심을 가짐
- 머신러닝 모델의 종류
    - 선형 회귀
        - 머신러닝에서 대표적인 모델
        - 데이터에 적합한 모델을 유추할 떄 도와줌
        - 데이터의 최적선을 찾음
    - 군집분석 : 레이블화된 데이터가 없을 때 유용
- 머신러닝 알고리즘의 분류
    - 지도 학습
        - 훈련 데이터로 제공하는 모든 새로운 예시마다 레이블이 존재
        - 레이블을 예측할 규칙을 찾아내 보지 못했던 입려의 레이블을 찾아냄
    - 비지도 학습
        - 각각의 레이블을 알수 없음
        - 자연스러운 방법을 찾아서 모델 생성

### Feature Engineering (특성 공학)
- 어떤 특성들을 측정해 조합을 만들고 어떻게 가중치를 둘 것인지 결정하는 것, 모델의 성능을 높이기 위해 모델에 입력할 데이터를 만들기 위해 주어진 초기 데이터로부터 특징을 가공하고 생성하는 전체 과정을 의미
- 모델 성능에 미치는 영향이 크기 떄문에 머신러닝 응용에 있어서 굉장히 중요한 단계이며, 전문성과 시간과 비용이 많이 드는 작
- 특성을 어떻게 선택할까?
    - 신호 대 잡음비는 최대화
    - 가장 많은 정보를 가진 특성을 최대화하고 그렇지 않은 것을 제거
- 방법적인 측면
    - 특징 선택 : 특징랭킹 또는 특징 중요도
    - 차원 감소 : 관측 데이터를 잘 설명할수 있는 잠재공간을 찾는 것
    - 특징 생성 ,구축 : 데이터에 대한 도메인 전문성을 바탕으로 데이터를 합치거나 쪼개는 등의 작업을 거쳐 새로운 특성생

### 평가 방법
- 오차 행렬(confusion matrix)
    - 정확도
        - 전체 샘플 중 맞게 예측한 샘플 수의 비율
    - PPV (positivie predictive value = true positive/ (true positive + false positive))
        - 정밀도, 긍정 표시한 것들 중 얼마나 진실인지?
    - 민감도 (sensitivity) = true positive / (true positive + false negative)
        - 재현율, 단순히 올바르게 맞춘 비율
        - TPR : True Positive Rate
    - 특정성 (specificity) = true negative / (true negative + false positive)
        - 올바르게 제외한 비율, 1 - 위양성률
    - F점수
        - 정밀도와 재현율의 가중조화평균을 F점수라고 한다. 정밀도에 주어지는 가중치를 베타라고 한다. 베타가 1인 경우를 특별히 F1점수라고 한다.
    - ROC
        - 위에서 설명한 각종 평가 점수 중 재현율과 위양성률은 일반적으로 양의 상관관계. 재현율을 높이기 위해서는 양성으로 판단하는 기준(threshold)을 낮추어 약간의 증거만 있어도 양성으로 판단하도록 하면된다.
          그러나 이렇게 되면 음성임에도 양성으로 판단되는 표본 데이터가 같이 증가하게 되어 위양성율이 동시에 증가한다. ROC(receiver operator characteristic) 커브는 크래스 판별 기준값의 변화에 따른
          위양성률(fall-out)과 재현율(recall)의 변화를 시각화한 것이다.
       ​​              
## Chapter 12. Clustering
### 군집화 (Clustering)
- 군집화는 최적화 문제
    - 지도 학습도 최적화 문제. 군집화는 지도 학습보다 더 간단한 형태
    - 변이성 (variability)
        - 군집의 평균과 군집에 포함된 각 샘플 사이의 거리를 모두 합한 것의 제곱
    - 비유사성(dissimilarity)
        - 모든 변이성을 더하고 크기로 나눔
    - 정규화의 장점과 단점
        - 정규화 : 큰 군집에 대한 패널티
        - 정규화를 하지 않으면 크기가 크고 분산이 높은 군집에 더 높은 패널티를 줄 수 있음
    - 목표함수
        - 각 군집들은 서로 최소한 거리를 가져야 함
        - 제약 조건 : 군집의 개수를 제한  
        
### 위계적 군집화 (Hierarchical clustering)
- 각 샘플을 각각의 군집에 할당
    - 그리고 가장 비슷한 두 개의 군집을 찾음
    - 그리고 이 둘을 하나의 군집으로 합침
    - 이제 군집의 수가 N개에서 N-1개
    - 이 과정을 계속 반복!
        - 특정 부분에서 반복을 멈출 수 있음
- 덴드로그램을 만들 수 있음
    - 각 단계에서 어떤 것들이 합쳐졌는지 보여줌
- 신경 써야하는 것
    - 거리의 정의
        - 어떤 것을 측정하냐에 따라 다양한 대답이 나올 수 있음
    - 단일 연결(Single linkage)
        - 한 쌍의 군집 사이의 거리
        - 한 군집에 포함된 샘플과 다른 굱비에 포함된 샘플 사이의 최소 거리
    - 완전 연결(Complete-linkage)
        - 두 군집 사이의 거리를 각 샘플간의 최대 거리라고 정의
    - 평균 연결
        - 한 집단과 다른 집단 사이의 모든 요소 간의 평균 거리를 두 집단 사이의 거리라고 정의
- 단점
    - 너무 결정론적
    - 주어진 연결 방법에 대해 항상 같은 결과
    - 무작위적인 결과는 만들어지지 않음
    - 이 겨로가가 최적의 결과는 아닐수 있음
    - 매우 느림

### K 평균 군집화(K-means clustering)
- k : 필요한 군집의 개수
- 초기 상태에서 k개의 샘플을 무작위로 선택
    - 그리고 K 개의 군집을 생성할 때 각 샘플을 각 가까운 중심에 할당
    - 그리고 k 개의 새로운 중심을 계산
    - 각 군집에 포함된 샘플들의 평균을 이용
    - 중심이 안바뀔때까지 계속 반복!
    - 중심이 안바뀌면 converge
- 단점
    - k를 잘못 설정하면 무의미한 결과가 나올 수 있음
    - 이미 알고있는 지식(도메인 지식)으로 K를 설정
    - 다양한 K를 시도하고 결과의 품질을 확인하며 K를 찾기
    - 각 결과는 초기 방법에 따라 다름 -> 샘플링, 반복 횟수에 따라 다름
      잘못하면, 중심점과 점간의 거리가 Global optimum 인 최소 갑승ㄹ 찾는게 아니라 중심점이 Local optimum에 수렴하여 잘못된 분류를 할 수 있다는 취약점을가지고 있다
   
- Z Scaling
    - 평균 0 표준편차는 항상 1
    - 보간법을 사용하기도 함
        - 가장 작은 값을 0, 큰 값 1으로 하고 선형 보간
    - 스케일링하면 모델이 차이가 날 수 있음
    - 데이터를 다룰 때 생각을 많이해야 하는 이유
        - 값 넣고 정답 얻기까지 기다릴 수 없음. 미리 생각하고 행동!
                      
## Chapter 13. Classification
### 지도학습
- 특성 벡터에 대한 특정한 수를 예측하는 회귀
  - 주어진 특성에 대한 특정 지점을 예측하는 방법
  - 다차원으로 일반화하는 것
- 분류는 회귀보다 더 자주 사용됨
  - 이산값을 계산하는 것이 목표

### k-최근접 이웃방법
- 간단한 접근! 점이 나오면 어디에 제일 근접한지를 확인
  - 몇가지 최근접 이웃을 찾고(보통 홀수를 찾음) 가장 많은 것을 고름
  - k의 크기를 고민! 분류의 크기에 따라 영향을 받을 수 있음
  - 훈련 세트와 테스트 세트로 데이터를 나누고 훈련 세트만 선택해서, 훈련 셋과 데이터 셋으로 다시 나눔
    - 다양한 k로 시도
    - 교차검증
- 장점
  - 빠르게 학습
  - 모든 부분을 기억
  - 방법과 결과를 설명하기 쉬움
- 단점
  - 메모리가 많이 필요할 수 있음, 백만개 샘플이 있으면 모두 저장해야 함
  - 예측에 필요한 시간이 길어질 수 있음
  - 무차별 대입법을 이용하면 k근접 이웃의 근사값을 구할 수 있지만 그렇게 빠르진 않음
  - 어떤 과정으로 데이터가 생성되는지 배우지 않고, 데이터의 모델이 어떠한지 알 수 없음

### 로지스틱 회귀(Logistic regression)
- 선형 회귀와 비슷해보일 수 있지만 차이점 있음
  - 선형 회귀는 어떤 사건에 대한 확률을 구하려고 함
    - 종속 변수는 유한한 개수의 값
    - 사망할 확률이 0.5면? 절반만 사망한 상태를 의미하진 않음
- 각 특성에 대한 가중치를 계산
  - 절대적 값은 상관관계의 강도
- 해당 레이블이 가질 확률값을 계산
- 각 변수에 대한 정보를 제공            
            
## Chapter 14. Classification and Statistical Sins
### ROC(Receiver Operating Characteristic)
- FPR와 TPR을 각각 x,y 축으로 놓은 그래프
  - TPR : True Positive Rate
  - FPR : False Positive Rate
  - TPR과 FPR의 여러가지 상황을 고려해 성능을 파악해야할 떄, 한눈에 볼 수 있게 시각화한 그래프
- AUC
  - AUROC(the Area Under a ROC Curve)
  - ROC 커브의 밑면적을 구한 값
  - 1에 가까울수록 성능이 좋음  

### 통계적 죄악
- 데이터에 대한 통계는 데이터 그 자체와 같지않음
  - 따라서 적절한 시각화를 통해 데이터를 파악해야 함
- 축의 라벨이 없는 경우 파악해야 함
  - 차이를 실제보다 크게 해서 속이는 경우 존재
- 데이터가 분석할 가치가 있는지 파악하기
  - Garbage In, Gabage Out
  - 불량 데이터의 분석은 위험한 결론에 도출할 수 있음
  - 표본 추출할 때
- 샘플이 무작위이고 독립적이지 않을 경우
  - 평균과 표준편차를 구할 수는 있지만, 거기서 결론을 도출해서는 안됨
  - 데이터가 어떻게 수집되었는지 이해하고 분석에 사용된 가정이 만족되었는지 확인  

# Chapter 15. Statistical Sins and Wrap Up
### 통계적 죄악
- y축이 0부터 시작하지 않는 차트를 조심하기
  - y축을 축소해서 의미없는 값들을 제거
  - 실제와 다르게 보이도록 범위를 줄이면 안되고 속일 의도로 너무 늘려서도 안됨
- 변동과 경향을 혼동하지 말기
  - 연속적인 데이터에서 우리가 보는 것은 항상 변동이 있음
  - 현상이 나타날 만큼의 간격을 설정해야 함
  - 숫자를 볼 때 어떤 맥락에 넣어보기
- 분모를 모를 떄에는 확률적인 변화에 조심하기  
 
### 강의의 주제
- 최적화 문제
- 확률론적 사고
- 세상의 측면을 모델링하는 것
- 더 나은 프로그래머 되기
  - 파이썬의 추가 기능과 유용한 라이브러리
  - 연습, 연습, 또 연습  

### 강의 정리
- 탐욕 알고리즘 : 유용하지만 자주 최적해를 찾지 못함
- k평균 군집화
  - 군집을 찾기 위한 효율적 방법
  - 최적의 군집 세트를 반드시 찾진 못함
- 동적 계획법
  - 빠른 해답을 가져다주기도 함
  - 근사 해가 아닌 정확한 해를 제공
- memorization 은 아주 유용한 기술
  - 공간을 시간으로 줄임
- 최적화 문제
  - 배낭문제
  - 그래프 문제
  - 곡선 맞춤
  - 군집화
  - 로지스틱 회귀
- 세상이 확률적이라고 생각하고 세상을 모델링하려고 하면 확률적 프로그램을 작성할 방법이 필요
- 무작위 계산
  - 전혀 무작위성을 가지지 않는 문제에도 유용하게 쓰이는 계산 기법
  - 파이값을 찾기 위해 사용, 적분에도 쓰일 수 있음
- 통계적 모델
  - 시뮬레이션 모델
  - 몬테카를로 시뮬레이션
  - 표본 추출에 기반한 모델
  - 시뮬렝션에 대해 이야기할 때 결과가 얼마나 신뢰성이 있는지 체크하기
  - 신뢰구간과 신뢰수준
    - 두 변수를 통해 답이 얼마나 믿을만한지 설명
  - 중심 극한 정리와 다른 분포
- 머신러닝 통계 모델
  - 비지도 학습
    - 군집화
      - 계층적 군집화
      - K평균 군집화
  - 지도 학습
    - 선형 회귀
    - 분류
    - K-최근접 이웃
    - 로지스틱 회귀  


































