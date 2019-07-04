# [하버드] 확률론 기초: Statistics 110 : https://www.edwith.org/harvardprobability
Today I Learned

## 1강- 확률과 셈 원리 (Probability and Counting)
## 2강- 해석을 통한 문제풀이 및 확률의 공리 (Story Proofs, Axioms of Probability)
## 3강- Birthday Problem과 확률의 특성 (Birthday Problem, Properties of Probability)
## 4강- 조건부 확률 (Conditional Probability)
## 5강- 조건부 확률과 전확률정리 (Conditioning Continued, Law of Total Probability)
## 6강- Monty Hall 문제와 심슨의 역설 (Monty Hall, Simpson's Paradox)
## 7강- 도박꾼의 파산 문제와 확률변수 (Gambler's Ruin and Random Variables)
## 8강- 확률변수와 확률분포 (Random Variables and Their Distributions)
## 9강- 기댓값, 지시확률변수와 선형성 (Expectation, Indicator Random Variables, Linearity)
## 10강- 기댓값 (Expectation Continued)
## 11강- 포아송분포 (The Poisson distribution)
### 포아송분포 X ~ Pois(λ)
의미: 굉장히 여러 번의 시행을 하지만 성공의 확률은 매우 낮을 때 성공 횟수 세기
ex) 한 시간 동안 오는 이메일의 갯수

PMF:  -> λ 는 속도를 나타내는 모수로, λ > 0 인 상수이다.

### 포아송근사(poisson approximation)
어떤 큰 숫자 n에 대하여 A1,..., An의 사건들이 각각 P(Aj) = pj 라는 낮은 확률로 발생하고,
각 사건은 독립(이거나 weakly dependent) 일 떼, 발생하는 사건(Aj)의 수는 Pois(λ)의 분포를 따른다
  
또한 X ~ Bin(n,p)는  n → ∞ , p → 0 하고 np = λ 가 상수로 유지될 때 (n과 p가 증가하는 속도가 같음)
이항확률변수 X의 분포는 포아송에 근사하게 된다.

ex)길바닥에 빗방울이 떨어지는 횟수 또한 포아송 근사로 설명할 수 있다. 각 사각형에 빗방울이 떨어지는 사건은 이항분포이지만, 그 사건은 서로 독립이다. 빗방울은 많이 떨어지지만 한 사각형 안에 떨어질 확률은 작기 때문에 포아송 분포로도 볼 수 있다.

Birthday Problem(3강) 확장하기
: n명 중에서 생일이 같은 세 명의 사람을 찾을 확률?

## 12강- 이산, 연속, 균등분포 (Discrete vs. Continuous, the Uniform)
### 이산확률변수 vs 연속확률변수
이산확률변수는 확률변수 x가 가질수 있는 값의 가지수가 유한개 or 무한개가 존재해서 하나씩 셀 수 있을 떄의 변수이다
연속확률변수는 확률변수 x가 어떤 구간에서 실수값을 가질때의 변수이다

## 13강- 정규분포 (Normal Distribution)
연속균등분포는 연속 확률 분포로, 분포가 특정 범위 내에서 균등하게 나타나 있을 경우를 가리킨다. 이 분포는 두 개의 매개변수 a,b를 받으며, 이때 [a,b] 범위에서 균등한 확률을 가진다 보통 기호로 u(a,b)로 나타낸다.

### 확륣변수의 독립
확률변수 X1, X2, ..., Xn 가 모든 x1,x2, ..., xn에 대하여

-> 완전한 독립. 쌍으로 독립(pairwise independence) 보다 '센 개념'. (쌍으로 독립이라고 완전히 독립은 아니다)
    ex) X1, X2 ~ iid Bern(1/2) 한 동전 던지기 시행이고
    X3 = 1 (x1 = x2 일 때; otherwise 0) 이라고 하자
        -> (X1, X2), (X2, X3),(X3, X1)는 쌍으로 독립이지만 (X1,X2,X3)은 독립이 아니다 (X1,X2 값이 정해지면 X3 값이 정해진다)

### 정규분포 (Normal Distribution) N(u,σ^2)


## 14강- 위치, 척도 및 무의식적인 통계학자의 법칙(Location, Scale, and LOTUS)
![statistics_14_1](../img/statistics_14_1.png)
![statistics_14_2](../img/statistics_14_2.png)
![statistics_14_3](../img/statistics_14_3.png)



15강- Midterm Review
16강- 지수분포(Exponential Distribution)
17강- 적률생성함수(Moment Generating Functions)
18강- 적률생성함수_2 (MGFs Continued)
19강- 결합, 조건부, 주변 확률질량함수(Joint, Conditional, and Marginal Distributions)
20강- 다항분포 및 코시분포(Multinomial and Cauchy)
21강- 공분산과 상관계수(Covariance and Correlation)
22강- 변수변환과 합성곱(Transformations and Convolutions)
23강- 베타분포(Beta disctribution)
24강- 감마분포와 포아송 과정(Gamma distribution and Poisson process)
25강- 순서통계량과 조건부 기댓값(Order Statistics and Conditional Expectations)
26강- 조건부 기댓값_2(Conditional Expectation Continuted)
27강- 조건부 기댓값_3(Conditional Expectation given an R.V.)
28강- 부등식(Inequalities)
29강- 큰 수의 법칙과 중심극한정리(Law of Large Numbers and Central Limit Theorem)
30강- 카이제곱분포, t분포, 다변량정규분포(Chi-Square, Student-t, Multivariate Normal)
31강- 마코프 체인(Markov Chains)
32강- 마코프 체인_2(Markov Chains Continued)
33강- 마코프 체인_3(Markov Chains Continued Further)
34강- A Look Ahead