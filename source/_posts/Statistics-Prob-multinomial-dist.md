---
title: "[Probability]numpy와 scipy로 다항분포 간단하게 구현하기"
date: 
updated:
categories: 
        - [Statistics]
tags:
  - Probability
mathjax: true
---

<!--

진짜 ref
https://www.statology.org/multinomial-distribution-in-python/

https://boxnwhis.kr/2015/06/04/multinomial_dist_for_gachas.html

다항로지스틱 머신러닝
https://machinelearningmastery.com/multinomial-logistic-regression-with-python/

확륳함수로부터 나오는 확률들의 패턴을 확률분포라 한다

https://cinema4dr12.tistory.com/1016?category=515283

https://www.kdnuggets.com/2021/07/top-python-data-science-interview-questions.html
-->


#### Note

- 다항분포는 이항분포의 보다 일반화된 버전이다.(다항 분포에서 차원이 2인 경우 이항 분포가 된다.)
- **다항 분포는 여러 개의 값을 가질 수 있는 독립 확률변수들에 대한 확률분포로, 여러 번의 독립적 시행에서 각각의 값이 특정 횟수가 나타날 확률을 정의한다.**
다항분포의 가장 쉬운 예시 중 하나는 주사위를 N 번 던저 각 면이 나오는 횟수 집합의 분포를 구하는 것이다.

- **특정 확률변수 X가 다음의 조건을 충족할 경우 다항분포를 따른다.**
  + k개의 class(발생가능한 결과, 카테고리 등)
  + 각 trial은 독립적이다.
  + 독립적인 각각의 trial에서 i번째 class가 나타날 확률읜 $p_{i}$로 고정한다.

#### 다항분포 공식

- 다항분포의 PMF는 다음과 같이 정의된다. 식이 복잡해보이는 것은 단순히 나올 수 있는 결과의 조합이 복잡하기 때문이다.
$$f(x)=\frac{n !}{x_{1} ! \cdots x_{k} !} p_{1}^{x_{1}} \cdots p_{k}^{x_{k}}$$

- 다항분포의 기댓값 :
$$E\{X_{i}\}=np_{i}$$

- 다항분포의 분산 :
$\operatorname{Var}\left(X_{i}\right)=n p_{i}\left(1-p_{i}\right)$

#### 구현

- numpy를 활용한 시뮬레이션

두번째 인수에 tuple 형태로 각 class의 확률이 들어간다.
두번째 인수의 확률의 합은 반드시 1이여야 한다.

```python
# 주사위 10번 던지는 시뮬레이션
np.random.multinomial(10, [1/6.]*6, size=1)
array([[4, 3, 6, 5, 2, 1]]) # random

```

- scipy 예제

주머니에 6개의 노란 구슬,2개의 빨간 구슬, 2개의 파란구슬이 있을 때
복원추출로 4개의 구슬을 뽑을 경우 모든 구슬이 빨간 색일 확률은 무엇인가?


```python
from scipy import multinomial

multinomial.pmf(x=[0,4,0],n=4,p = [.6,.2,.2])

>>>0.1295999999999999

```




**References & annotation**
---
- https://youtu.be/nMsCHfrt3Cw
- https://www.statisticshowto.com/multinomial-distribution/