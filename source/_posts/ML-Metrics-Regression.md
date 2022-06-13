---
title: '[Metrics]회귀모델의 평가지표'
categories:
  - [Machine Learning]
tags:
  - Regression
  - Metrics
date:
updated:
---

<!--

<center>Kaggle Customer Score Dataset</center>

- Machine Learning
- Statistics , Math
- Data Engineering
- Programming
- EDA & Visualization
- Preprocessing


#신경망이란 무엇인가?

https://www.youtube.com/watch?v=aircAruvnKk


#참고

https://cinema4dr12.tistory.com/1016?category=515283

https://www.kdnuggets.com/2021/07/top-python-data-science-interview-questions.html
-->

**회귀모델의 평가지표 정리**

### 회귀모델의 평가지표

- $R^2$ 외에, MAE는 단위 유닛이 같으므로 보다 해석에 용이함.
- MSE는 제곱을 하기 때문에 특이값에 보다 민감. 
- RMSE는 MSE를 실제값과 유사한 단위로 변화시켜줌.
- 회귀문제에서 RMSE가 일반적으로 선호되는 방법이지만, 상황에 맞는 다른 방식을 사용. 특이값이 많은 경우에는 MAE를 사용.

---
**_Concept_**

* MSE (Mean Squared Error) = 
$\frac{1}{n}\sum_{i=1}^{n}(y_{i} - \hat{y_{i}})^{2}$
* MAE (Mean absolute error) = $\frac{1}{n}\sum_{i=1}^{n}\left | y_{i} - \hat{y_{i}} \right |$
* RMSE (Root Mean Squared Error) = 
$\sqrt{MSE}$
* R-squared (Coefficient of determination) = 
$1 - \frac{\sum_{i=1}^{n}(y_{i} - \hat{y_{i}})^{2}}{\sum_{i=1}^{n}(y_{i} - \bar{y_{i}})^{2}} = 1 - \frac{SSE}{SST} = \frac {SSR}{SST}$

* MAPE = $\frac { \sum \vert \frac { y - \hat y}{y} \vert }{n}*100\%$

- 참고
    - SSE(Sum of Squares `Error`, 관측치와 예측치 차이): $\sum_{i=1}^{n}(y_{i} - \hat{y_{i}})^{2}$
    - SSR(Sum of Squares due to `Regression`, 예측치와 평균 차이): $\sum_{i=1}^{n}(\hat{y_{i}} - \bar{y_{i}})^{2}$
    - SST(Sum of Squares `Total`, 관측치와 평균 차이): $\sum_{i=1}^{n}(y_{i} - \bar{y_{i}})^{2}$ , SSE + SSR

---

#### MSE

- 모델의 예측값과 실제값 차이의 면적의 합.
- 특이값이 존재할 경우 수치가 많이 늘어남

#### MAE

- MSE 보다 특이치에 robust
- 절대값을 취하기 때문에 매우 직관적

#### RMSE

- MSE의 제곱근. 
- 큰 오류값에 대해 패널티를 주기 때문에 보통 이걸 사용

#### R-squared

- 설명량
- $R^2$ 값이 1에 가까울 수록 데이터를 잘 설명하는 모델이 됨

#### MAPE

```python
def MAPE(y_true, y_pred): 
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

```
- MAE를 퍼센트 변환한 것.
- MAE와 마찬가지로 MSE보다 특이치에 robust하다.
- 모델에 대한 편향이 존재.
- 0 근처의 값에서는 사용하기 어렵습니다.

#### MPE

```python
def MAPE(y_true, y_pred): 
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

```
- MAPE를 퍼센트 변환한 것.
- 절대값을 제외했기 때문에 overperformance인지 underperformance인지 쉽게 알 수 있다.


## References


- https://www.dataquest.io/blog/understanding-regression-error-metrics/
- https://machinelearningmastery.com/regression-metrics-for-machine-learning/
