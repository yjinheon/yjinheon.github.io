# 확률론 기초

표본공간에서 어떤 사건이 발생할 가능성을 확률이라고 한다.
확률은 기본적으로 면적이다.

- 프로그래머를 위한 확률과 통계

## 확률(Probability)

확률 P는 기본적으로 Event 사건과 그에 대응하는 수치에 대한 Mapping 이다.

## 표본공간 (Sample Space)

: **기본적으로 실험으로부터 나온 모든 결과를 담고있는 집합을 표본공간이라고 한다.**

## 확률변수(Random Variable)

: **표본공간의 각 요소(사건)와 값을 매핑하는 함수. 정확히는 확률적으로 발생하는 사건을 실수에 매핑하는 함수이디.**

**확률 변수는 표본공간 안에서 특정한 확률을 가지고 발생하는 사건을 실수에 매핑한 함수이다.**

<!---
a function that associates values of a sample space to a real number.
-->

동전을 2번 던지는 시행에서 표본공간은 {HH,HT,TT,TH} 이다. 이때 변수 X를 동전의 위(Head)가 나올 수 있는 경우의 수로 생각할때 X는 {0,1,2} 의 3가지 값을 가질 수 있다 이때 변수 X를 확률변수라 한다.

사건에 실수값을 매핑하는 것이 중요한 이유는 이를 통해 불확실성을 가진 확률실험의 결과를 수학적으로 연산하고 모형화 하게끔 바꿔줄 수 있기 때문이다.

확률변수는 불확실성을 가진 어떤 현상이나 실험의 결과를 숫자로 바꾸는 역할

**보통 표본을 확률변수로 간주한다.**

#### 이산확률변수(descrete random variable)

: 표본공간(Sample Space) 내에서 사건마나 매핑되는 실수 값들이 유한할 경우(Countable) 이산확률변수라고 한다.

- 모든 값의 확률이 0과 1사이에 존재한다.
- 표기시 P(X=x)와 같은 형태로 표기한다.

#### 연속확률변수 (continuous random variable)

: **구간 내의 모든 실수 값을 취하는 확률변수(random variable)이다.**

- 이산확률변수와의 가장 큰 차이는 
- **확률이 기본적으로 분포상의 특정구간의 면적에 할당된다.**

#### 확률분포와 머신러닝

회귀분석 

### 기댓값(Expected Value)

: **확률적 사건에 대한 가중평균으로 각 확률변수와 그 확률변수에 대응하는 확률을 곱한 것을 합산한 값이다. 확률변수의 기대값은 E(X)로 표기한다.**

**이산확률분포의 기댓값**
:
이산확률변수의 기댓값은 Sample Space의 각 원소의 가중평균이다.

$$
\text{E}[X]=\sum_i x_i P\left(X=x_i\right)
$$

**연속확률분포의 기댓값**

이산확률변수의 기댓값은 적분을 통해 정의할 수 있다. 

$$
\begin{align}
\text{E}[X] = \int_{-\infty}^{\infty} x f(x) dx 
\end{align}
$$

### 분산(Variance)

: **데이터가 평균으로부터 흩어진 정도**

분산은 모델의 신뢰도와 관련이 있다. 

확률변수 X의 분산은 X의 기댓값 E[X] 로부터 확률변수가 얼마나 떨어져있는지 그 정도를 제곱한 것의 기댓값과 같다

## 확률함수 (Probability funtion)

:**확률 변수가 특정한 값을 가질 확률을 나타내는 함수이다**. 아는 확률변수와 그 값이 나올 수 있는 확률을 대응시킨 것이다.(확률변수와 확률의 매핑)

기본적으로 input이 실수고 output이 그 실수에 대응하는 확률이다.

$$
p=f(Real Number)
$$

- input이 되는 확률변수의 특징에 따라 **확률질량함수(PMF)**와 **확률밀도함수(PDF)**로 나뉜다.

### PMF(Probability Mass Function)

: 확률함수의 input이 이산형일 때 **확률질량함수**라고 한다. 이산확률변수 X가 취할 수 있는 값들에 대해 각각 확률을 매핑해주는 함수이다.

$$
P(X=x_{i})=p_{i} (i=1,2,3, ... n)
$$


- 확률이 가능성의 크기로 생각하여 일종의 질량으로 간주된다.
- PMF에서 likelyhood와 probability는 개념상 같아진다. 이는 

**확률을 생성하는 함수**

### CDF(Cumulative Distribution Function)

: 

확률변수 X에 대한 확률을 p(x)라 할 경우 누적분포함수는 다음과 같이 나타난다.

$$
F_{X}(x)= p_{X}(X \leq x)
$$

- 확률변수가 이산형이던 연속형이던 상관없이 CDF로 나타낼 수 있다

### PDF(Probability Density Function)

: 확률함수의 input이 연속형일 경우 **연속확률분포**라 한다.

구체적으로는 확률 변수가 취하는 값들의 집합이 실수의 구간을 이루면 연속확률분포가 된다.

PDF에서의 확률은  f(x)dx를 구간내에서 정적분한 값이 PDF의 확률이 된다.
-> **PDF에서 확률은 어떤 구간 내의 면적으로 표현된다.**

$$
P(a\leq X \leq b) = \int_{a}^{b}f(x)dx
$$

- CDF가 미분가능한 함수로 나타날 경우 연속확률변수이고 이를 미분한것이 PDF이다.

- dx는 여기서 x의 변화량(기울기) 이므로 구간의 아주 작은 구간을 의미한다.

- f(x)는 여기서 확률밀도(y축)을 의미한다.

- 따라서 확률이 f(x)가 아니라 f(x)dx가 된다.

- PDF의 y축은 likelyhood로 특정 데이터 포인트가 고정 되어 있을 때 이 데이터가 어떤 분포로부터 나왔을 지에 대한 확률이다.

  - $$
    L(\theta | Data)
    $$


![img](/home/jinheonyoon/workspace/ml/notebook/data/images/liklihood.png)

## 모수(parameter)

모수는 모집단(Poppulation)의 특성을 나타나는 값이다.
모수는 통계학에서 기본적으로 알 수 없는 값이며 상수이다.

## 확률분포 (Probability dis)

: **확률분포는 확률변수를 확률에 매핑하는 함수로 확률함수로부터 생성되는 확률값들의 패턴을 의미한다. 기본적으로 일정한 범위에서 어떤 확률변수(random variable)이 가질 수 있는 모든 가능한 확률값을 나열한 것이다.**



### 이산확률분포(Descrete Probability Distribution)

확률값들의 결과

이산확률분포의 기대값

이산확률분포의 분산

#### 베르누이분포

#### 이항분포(Binary Distribution)

> n번의 독립시행에서 성공 확률이 p일 때의 이산확률분포

- 확률변수 K가 n과 p를 가지는 이항분포를 따른다면, K ~ B(n,p)로 나타낸다.

- n번 시행 중에 k번 성공할 확률은 확률질량함수로 주어진다.

- 이항분포는 n이 일정수준 이상으로 커질 경우 정규분포에 근사한다.

- 보통 np >= 10일 경우 정규분포로 본다.

- **n=1일 경우 이항분포는 베르누이 시행이다.**

- 심플하게 생각하면 **성공과 실패 두 가지 결과가 있는 확률적 사건을 n번 반복했을때 성공이 몇번 나타날지를 확률분포로 나타낸것이다.**
  
  - ex) 성공확률이 주어졌을 때 특정 리뷰데이터가 나올 확률

**이항분포 공식**

- 이항분포를 따르는 확률변수 K가 있을때 n번시행에서 k번 성공할 확률을 나타내는 PMF는 다음과 같다.
  + $\binom{n}{k}$는 단순히 가능한 조합의 수를 나타낸다. 

$$
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
$$

- 이항분포의 기댓값은 다음과 같다.
  
$$
E(K) = np
$$

- 분산은 다음과 같다. 단순히 n번의 독립적인 베르누이 시행의 분산을 더한 것이다,

$$
Var(K) = np(1-p)
$$

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


![](../data/images/binary_distribution_r.png)



```r
# 이항분포가 B(10,0.5)를 따를 경우 P[X>3] 계산 
pbinom(3, 10, 0.5, lower.tail=F) # 1-pbinom(3, 10, 0.5) 과 같은 값이 나온다.
```

### 연속확률분포(Contiuous Distribution)

#### Exponential Distribution

#### Uniform Distribution

#### Gaussian Distribution

: 정규분포

$$
N(x\;|\;\mu, \sigma^2)=\dfrac{1}{(2\pi\sigma^2)^{1/2}}\exp\left\{-\dfrac{1}{2\sigma^2}(x-\mu)^2\right\}
$$

다변량 가우시안 분포

$$
N({\bf x}|{\pmb \mu}, {\pmb \Sigma})=\dfrac{1}{(2\pi)^{D/2}|{\pmb \Sigma}|^{1/2}}\exp\left\{-\dfrac{1}{2}({\bf x}-{\pmb \mu})^T{\pmb \Sigma}^{-1}({\bf x}-{\pmb \mu})\right\}
$$

$$
\hat{\theta} =  (\textrm{x}^{T} \cdot \textrm{x})^{-1} \cdot \textrm{x}^{T} \cdot\textrm{y}
$$

**Z score** 
:

- https://www.researchgate.net/figure/Various-data-types-used-for-quantitative-morphological-phenotyping-Morphological_fig3_359634115

#### Sample Distribution

정규분포가 중요한 이유는 많은 연속형 데이터가 정규분포를 따르기 때문만은 아니다. 

샘플링을 통해 표봅평균을 구해보면 그것들이 따르는 분포가 정규분포인 것이 중요하다.

이를 표본분포(통계량의 확률분포)라고 한다.

모수의 확률분포가 정규분포를 따르지 않더라도 

#### Exponential Distribution(지수분포)

#### Gamma Distribution

### 확률분포 사이의 관계

### 확률분포의 결정 방법

- 데이터는 0 또는 1 뿐이다. → 베르누이분포
- 데이터는 0과 1 사이의 실수 값이어야 한다. → 베타분포
- 데이터는 항상 0 또는 양수이어야 한다. → 로그정규분포, 감마분포, F분포, 카이제곱분포, 지수분포, 하프코시분포 등
- 데이터가 크기 제한이 없는 실수다. → 정규분포 또는 스튜던트 t분포, 코시분포, 라플라스분포 등

### Marginal Distripution

### Joint Distribution
