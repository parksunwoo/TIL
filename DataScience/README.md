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
            
            
            
            
            
            




































