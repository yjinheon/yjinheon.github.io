---
title: "[Probability]이항분포의 이해"
date: 
updated: 
categories:
  - - Statistics
tags:
  - Probability
  - Distribution
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

### 이항분포(Binary Distribution)

  

> n번의 독립시행에서 성공 확률이 p일 때의 이산확률분포

  

- 확률변수 K가 n과 p를 가지는 이항분포를 따른다면, K ~ B(n,p)로 나타낸다.

- n번 시행 중에 k번 성공할 확률은 확률질량함수로 주어진다

- 이항분포는 n이 일정수준 이상으로 커질 경우 정규분포에 근사한다.

- **n=1일 경우 이항분포는 베르누이 시행이다.**

  

- 심플하게 생각하면 **성공과 실패 두 가지 결과가 있는 확률적 사건을 n번 반복했을때 성공이 몇번 나타날지를 확률분포로 나타낸것이다.**

- ex) 성공확률이 주어졌을 때 특정 리뷰데이터가 나올 확률

  

**이항분포 공식**

  

- 이항분포를 따르는 확률변수 K가 있을때 n번시행에서 k번 성공할 확률을 나타내는 PMF는 다음과 같다.

+ $\binom{n}{k}$는 단순히 가능한 조합의 수를 나타낸다.

+ n이 6이고 k가 2일 경우 2번 성공하고 n-k번 실패할 확률를 곱해서 계산한다.(독립시행)
 
  

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

  
- 이항분포의 기댓값은 다음과 같다.

  

$E(K) = np$

  

- 분산은 다음과 같다. 단순히 n번의 독립적인 베르누이 시행의 분산을 더한 것이다,

  

$Var(K) = np(1-p)$

  

**이항분포의 PMF**

  

<p align="center">

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbtoZzt%2FbtqVdebL4pt%2FmrdViwxudFPtOMDqVmyb2K%2Fimg.png" alt="drawing" width="500"/>

</p>

  

**이항분포 구현**

  

R에서 제공하는 dbinom() 함수를 사용하여 이항분포를 구현할 수 있다.

  
  

- dbinom(k,n,p) : 이항분포의 확률값

- pbinom(k,n,p) : 이항분포의 누적확률 값

- qbinom(p,size,prob) : 이항분포의 백분위수. pbinom의 역수

- rbinom(n,size,prob) : 이항분포를 따르는 난수생성

  

```r

# 주사위를 10번 던져서 원하는 값이 2번 나올 확률

df <- data.frame(dice = 1:10, prob = dbinom(x = 1:10, size = 10, prob = 1/6))

df %>%

mutate(Dice = ifelse(dice == 2, "2", "other")) %>%

ggplot(aes(x = factor(dice), y = prob, fill = Dice)) +

geom_col() +

geom_text(

aes(label = round(prob,2), y = prob + 0.01),

position = position_dodge(0.9),

size = 3,

vjust = 0

) +

labs(title = "Probability of X = 2 successes.",

x = "Successes",

y = "probability")

  

```

  

![](images/binary_distribution_r.png)

  

```r

# 이항분포가 B(10,0.5)를 따를 경우 P[X>3] 계산

pbinom(3, 10, 0.5, lower.tail=F) # 1-pbinom(3, 10, 0.5) 과 같은 값이 나온다.

```

**References & annotation**
---
- https://youtu.be/nMsCHfrt3Cw
- https://en.wikipedia.org/wiki/Binomial_distribution#