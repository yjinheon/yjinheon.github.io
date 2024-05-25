

**일반선형모델 들어갈 내용**
generalized linear model의 파라메터는 convex optimization 기법으로 구한다. generalized linear model은 다음 두 가지 속성이 있다.

최적 generalized linear model의 예측 평균은 학습 데이터 정답의 평균과 같다.
최적 로지스틱 회귀 모델이 예측한 확률의 평균은 학습 데이터 정답의 평균과 같다.
generalized linear model의 예측력은 피처에 의해 제한된다. 딥러닝 모델과 달리 generalized linear model은 (학습데이터에 없는)새로운 피처를 학습할 수 없다.

https://www.kdnuggets.com/2019/06/main-approaches-machine-learning-models.html



# Parameter Estimation

## Method of Moment

## Maximum Likelyhood Estimation

: Maximum Likelyhood estimation

데이터 분석에 있어서 가장 핵심적인 컨셉 중의 하나는 우리가 관측한 데이터들이 기본적으로 특정한 확률분포를 따르는 표본(sample)이라는 것이다.
여기서 특정한 확률분포의 특성을 나타내는 값을 모수(Parameter)라고 부르고 보통 $\theta$ 라고 쓴다.

최대우도추정이란 

### 합의 법칙

합의 법칙 예시

### 곱의 법칙

$P(O|\theta)$

가능도 값을

$L(\theta|O) = P(O|\theta)$

$$
L(\theta \; ; y_1 ,y_2,\cdots ,y_n) = \prod_{i=1}^n f(\theta \; | \; y_1 ,y_2,\cdots ,y_n )
$$

### Maximum Likelihood

가능도를 최대화 한

**MLE는 기본적으로 확률분포의의 추론이다.**

MLE는 관측된 데이터가 나타날 확률을 최대화 하는 $\theta$(모수) 를 찾는 것이 목적이다.

어떤 데이터를 선택했을 때 그 데이터가 어떤 확률분포로 부터 추출되었을 지를 추정하는 것이다.

$$
\widehat{\theta}=\operatorname{argmax}_{\theta} P(D \mid \theta)
$$

### MLE Calculation

$$
\theta=\arg \max P(D \mid \theta)=\operatorname{argm} a x_{\theta} \theta a_{n}(1-\theta)^{a_{T}}
$$

log함수는 단조증가(monotonic)하기 때문에 log를 취한 $\widehat{\theta}$ 의 P를 최대화 하는 $\theta$와 log를 취하지 않은 $\widehat{\theta}$의 P를 최대화하는 $\theta$는 결국 같게 된다.

따라서 수식을 아래와 같이 표현할 수 있다.

이후 최적화 문제를 풀기위해 미분을 통해 극점(0이되는 지점)을 찾는다.

$$
\frac{d}{d \theta}\left(a_{H} \ln \theta+a_{T} \ln (1-\theta)\right)=0$$ $$ \frac{a_{H}}{\theta}-\frac{a_{T}}{1-\theta}=0
$$

$$
\theta=\frac{a_{H}}{a_{T}+a_{H}}
$$

- $\theta$는 최종적으로 앞면이 나온 횟수/동전을 던진 횟수가 된다.

**Simple Error Bound**

$$
P\left(\left|\hat{\theta}-\theta^{*}\right| \geq \varepsilon\right) \leq 2 e^{-2 N \varepsilon^{2}}
$$

## MAP

: # Maximum a posteriori estimation

주어진 관측결과와 사전지식(Prior)를 사용해서 

> MLE과 MAP의 차이는 기본적으로 사전확률(Prior)을 

**references**

- https://en.wikipedia.org/wiki/Maximum_a_posteriori_estimation

- edwith 문일철교수님 머신러닝 강의





# Parameter Estimation Concept

**모수를 추정한다는 것의 의미**
: 통계학에서의 모수는 보통 알 수 없는 값이기 때문에 모집단의 일부인 표본(Sample)을 통해 모집단의 특성을 파악한다. 다시말하면 표본의 통계량을 이용해 모수의 추정치를 정의한다.

## Moment

적률과 적률생성함수

### 적률

### 적률생성함수

## Central Limit Theory

sample size가 일정 수준 이상 커질 경우 표본평균의 분포는 정규분포에 근사한다.

표본평균의 적률생성함수가 n이 무한대일 때 생성되는 분포가 정규분포를 따름

https://m.blog.naver.com/mykepzzang/220851280035



<p align="center">
<img src="https://datasciencebook.ca/img/population_vs_sample.png" alt="drawing" width="600"/>
</p>

<center><b>모비율 추정의 예시</b></center>

통계학에서는 보통 $\theta$로 표현된다.
머신러닝에서의 모수는 보통 Weight라고 부른다.

### Parametric Model

특정 확률분포를 가정하고 이를 바탕으로 모수를 추정할 경우 Parametric Model(모수적 모델) 이라 한다.
선형모델의 경우 모델링 과정에서 정규분포를 가정하기 때문에 Parmetric  Model에 속한다.

### Non-Parametric Model

**Unsupervised Parametric Model**