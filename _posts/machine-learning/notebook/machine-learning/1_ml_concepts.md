# 머신러닝을 위한 핵심 컨셉들

여기서는 기초적인 사항에 대해 간단히 집고 넘어간다.

## Machine Learning

> "A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E"

특정 task에 T에 대해 Experience E를 통해 T에 대한 Performance P를  높이는 것이 머신러닝이다.

여기서  E는 Data에 해당한다.

![](https://www.kdnuggets.com/wp-content/uploads/michell-process-measure-improve.png)

## Supervised Learning

> 지도학습과 비지도학습의 기본적인 차이는 학습하는 패턴의 유형이다. 지도학습은 데이터를 이미 알고있는 label 로 변환시키는 패턴을 찾는 반면 비지도학습은 데이터를 잘 알려지지 않은 cluster label로 변화시키는 패턴을 찾는 것이다.

지도학습의 목적은 input x를 output label로 변환(mapping)하는 패턴을 학습하는 것이다.

input을 **이미 알고 있는** output으로 변환시키는 패턴을 찾는 것이 지도학습이다.

지도학습의 핵심적인 특징은 학습시 정답 label이 주어진다는 것이다.

지도학습은 크게 Regression과 Classification로 나뉜다.

### Regression

지도학습에서 label(output)이 Continuous한 경우 가 Regression이다.

```r
# 간단한 선형 모델 예시
library(palmerpenguins)
penguins_df <-penguins

model <- lm(body_mass_g ~ flipper_length_mm, penguins_df)
summary(model_3)

##
Call:
lm(formula = body_mass_g ~ flipper_length_mm, data = penguins_df)

Residuals:
     Min       1Q   Median       3Q      Max 
-1058.80  -259.27   -26.88   247.33  1288.69 

Coefficients:
                   Estimate Std. Error
(Intercept)       -5780.831    305.815
flipper_length_mm    49.686      1.518
                  t value Pr(>|t|)    
(Intercept)        -18.90   <2e-16 ***
flipper_length_mm   32.72   <2e-16 ***
---
Signif. codes:  
0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 394.3 on 340 degrees of freedom
  (2 observations deleted due to missingness)
Multiple R-squared:  0.759,    Adjusted R-squared:  0.7583 
F-statistic:  1071 on 1 and 340 DF,  p-value: < 2.2e-16
```

### Classification

지도학습에서 label(output)이 Categorical한 경우 분류 문제라 한다.

분류와 회귀의 가장 큰 차이점은 분류의 경우 나올 수 있는 결과가 한정적이라는 것이다.

```r
# logistic regression 예제

library(palmerpenguins)
penguins_df <-penguins
```

## Unsupervised Learning

input을 **알려지지 않은** Cluster label로 변환하는 패턴을 찾는 것이 비지도학습이다.

- 지도학습과의 차이는 label이 주어지냐의 여부이다.  

### 연관분석(Association Analysis)

주어진 데이터의 연관성을 자동탐색

### Clustering

: 기본적으로 유사한 데이터들 끼리 묶는 것

- grouping customers

### Dementionality Reduction

: input data의 특징을 유지

### Anomali Detection

: 비정상적인 데이터포인트를 찾는 것

## Reinforcement Learning

- 주어진 상황에서 보상(reward)을 최대로 만드는 액션을 찾는 문제
- **Exploration과 Exploitation 의 trade-off 문제**
- 기본적으로 target label이 주어지지 않는다.

**reference**

- https://www.kdnuggets.com/2018/12/essence-machine-learning.html

## Modeling-Taxomony

모델의 특성에 따라 여러 종류로 모델을 구분할 수 있다.

- Parametric vs Nonparametric
- Supervised vs Unsupervised



## Non-Linear Model

## optimizaiton(최적화 문제)

$\min f(x) \text{ s.t. } g(x) = c$

optimization은 모델(함수)을 데이터에 fitting시키는 과정이다. 이때, 모델을 데이터에 fitting시키려면 어떤 목적 또는 기준(fitting이 잘 되었는지 여부를 평가하기 위한)이 있어야 할텐데요, 그 목적/기준이 되는 함수가 objective function입니다. 예를 들어, 각 데이터의 fitting error를 구하고, 이들의 제곱의 합을 objective function으로 잡을 수 있을 것입니다.

https://darkpgmr.tistory.com/148

## Convexity

Convex 한 집합을 볼록집합 Convex Set이라고 부른다. Convex 집합은 집합이 이루는 공간 내의 두 점을 연결한 선분이 그 집합 안에 포함되는지, 포함되지 않는지에 따라 Convexity가 갈린다.

- convex 함수 : 경사하강법을 통해 찾을 수 있는 최저점이 전역 최적해(Global minimum) 하나만 존재
- non convex 함수 : local minimum이 여러개 존재. 어디가 전역 최적해인지 알기 어려움

이러한 관점에서 볼 때 퍼셉트론과 SVM과 같은 선형분류기는 Convex한 집합을 올바르게 분리하는 HyperPlane를 찾는 통계모델이라 볼 수 있다.

이때 심층 신경망, 딥러닝이 갖는 강점이 나타난다. 심층 신경망의 층을 한 계층씩 늘릴 때마다, 신경망이 표현 가능한 데이터의 축이 하나씩 추가되는 효과를 갖는다. 이때, 고차원 공간의 데이터 포인트는 저차원 공간에 비해 선형 분리 가능한 축의 수가 많아져서, 선형 분리가 가능할 확률이 높아진다.

즉, 신경망의 계층이 쌓일수록, 분리하기 어려워 보이는 집합을 분리하는 초평면에 가까이 갈 수 있게 된다.

**ref**

- https://ratsgo.github.io/convex%20optimization/2017/12/25/convexset/
- https://skyil.tistory.com/33
- [모두를 위한 컨벡스 최적화](https://convex-optimization-for-all.github.io/#:~:text=Convex%20Optimization%EC%9D%80%20%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D,%EC%82%AC%EB%9E%8C%EB%93%A4%EC%97%90%EA%B2%8C%20%EB%A7%A4%EB%A0%A5%EC%A0%81%EC%9D%B8%20%ED%95%99%EB%AC%B8%EC%9E%85%EB%8B%88%EB%8B%A4.)

## Loss Surface


신경망을 학습시킨다는 것은 기본적으로 고차원의 non-convex 최적화문제를 푸는 것이다. 이는 다시말하면 loss function에서 파라미터를 업데이트 해가며 global minimum을 찾는 것이다. 

신경망의 학습은 Optimizer, 가중치 초기화, 신경망

신경망의 목적함수는 고차원 함수이기때문에, 네트워크가 어떻게 학습이 되고 있는지 직관적으로 알기 어렵다. 하지만, 고차원의 목적 함수를 사람이 이해할 수 있는 3차원 공간안에 표현함으로써, 신경망의 훈련 과정을 더 잘 이해할 수 있으며, 신경망 설계에 필요한 직관을 더 얻을 수 있다.

- https://github.com/MinyeLee/RL_LossSurface
- https://medium.com/curg/%EC%83%9D%EA%B0%81%EB%B3%B4%EB%8B%A4-%EC%96%B4%EB%A0%A4%EC%9A%B4-%EC%B5%9C%EC%A0%81%ED%99%94-%ED%91%9C%EB%A9%B4-%EC%8B%9C%EA%B0%81%ED%99%94%ED%95%98%EA%B8%B0-5e6bdda500bf
- https://losslandscape.com/faq/

## ERM과 SRM

- https://datascience.stackexchange.com/questions/66729/difference-between-empirical-risk-minimization-and-structural-risk-minimization

- https://process-mining.tistory.com/143

### SRM

SRM(Structural Risk Minimization) 은 손실최소화와 복잡도의 균형을 추구하는 최적화 방식이다.

- 손실최소화 : 예측력이 좋음
- 복잡도가 낮음 : ex) 정규화 수준이 높게 이루어짐

$$
R_{\mathrm{srm}}(f)=\frac{1}{N} \sum_{i=1}^{N} L\left(y_{i}, f\left(x_{i}\right)\right)+\lambda J(f)
$$

ERM(Empirical Risk Mnimi)

## Hyperparameter

> Hyperparameter는 
