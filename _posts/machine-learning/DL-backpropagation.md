---
title: '[Neural Network]역전파 알고리즘(backpropagation)'
categories:
  - [Neural Network]
tags:
date: 2021-09-28 16:59:23
updated:
mathjax: true
---

<!--

<center>Kaggle Customer Score Dataset</center>

- Machine Learning
- Statistics , Math
- Data Engineering
- Programming
- EDA & Visualization
- Data Extraction & Wrangling

https://edgeaiguru.com/Feedforward-and-Backpropagation
https://www.youtube.com/watch?v=aircAruvnKk
#참고

https://cinema4dr12.tistory.com/1016?category=515283
https://www.kdnuggets.com/2021/07/top-python-data-science-interview-questions.html
-->

**순전파가 입력층에서 신호를 받아 은닉층의 가중치(+bias)와 연산을 한 뒤 출력층에서 벡터를 출력하는 과정이라면
역전파는 예측값과 실제값의 차이(에러)를 줄이기 위해  손실함수가 최소가 되도록 출력층으로부터 순전파의 역방향으로 편미분을 통해 가중치를 업데이트 하는 것이다. 간단히 역전파의 컨셉을 알아보자.**

---
## 역전파 알고리즘

**순전파가 입력층에서 신호를 받아 은닉층의 가중치(+bias)와 연산을 한 뒤 출력층에서 벡터를 출력하는 과정이라면 역전파는 예측값과 실제값의 차이(에러)를 줄이기 위해  손실함수가 최소가 되도록 출력층으로부터 순전파의 역방향으로 편미분을 통해 가중치를 업데이트 하는 것이다.**

역전파 알고리즘에서 가중치를 업데이트 한다는 것은 가중치 매개변수의 기울기(Graidant)를 예측값을 바탕으로 다시 계산한다는 것이다.


기본적으로 **타겟과 예측값의 차이를 줄이기 위해** 가중치를 업데이트한다.

$$
 y = activiate(\sum(\theta_{1}x_{1} + \theta_{2}x_{2} + ... + \theta_{n}x_{n}) + bias)
$$


타겟과 예측값의 차이는 `loss function(cost function)`이라고 볼 수 있다.

비용함수는 수식으로 나타내면 아래와 같다.

$$
J(\theta) = y - h_\theta(x)
$$

여기서 $h_\theta(x)$ 는 가설함수(모형)이다.

역전파(backward Propagation)는 예측값의 국소적 미분값을 순전파(Forward Propagation)의 반대방향으로 곱한 후 다음노드로 전달하는 것이다.

비용함수의 편미분을 통해 기울기를 구하는 이유는 **기울기가 비용함수의 값을 최소화 하는 방향을 제시하기 때문이다.**

![](https://i.imgur.com/Olxv64J.png)

<center><b>그림 1. Gradiant Boosting을 통한 global optimum 찾기</b></center>


만약 모형의 loss function이 MSE(Mear Sqared Error)일 경우, 비용함수는 아래와 같이 나타낼 수 있다. (m은 sample의 수를 의미)


$$
J(\theta)=\frac{1}{2 m} \sum_{i=1}^{m}\left(y^{(i)}-\hat{y}^{(i)}\right)^{2}
$$


이를 미분할 경우 직접 계산하기 어렵거나 불가능하기 때문에 Chain Rule을 사용한 합성함수의 편미분을 통해 구한다.


아래와 같은 신경망이 있고 output node의 활성화함수는 sigmoid라고 할 경우


![](https://i.imgur.com/bGCvYVJ.png)

<center><b>그림 2. 신경망으로 나타낸 backpropagation</b></center>

하나의 가중치에 대한 Gradiant를 아래와 같이 나타날 수 있다.

$$
Gradiant=\frac{\partial J(\theta)}{\partial \theta_{i}}=\frac{\frac{1}{2 m} \sum_{i=1}^{m}\left(y^{(i)}-\hat{y}^{(i)}\right)} {\partial \theta_{i}}
$$

이 때 분자는 가중치 $\theta_i$에 대해 미분할 수 없기 때문에 아래와 같이 `Chain Rule` 을 사용해서 Gradiant를 도출한다.

$$
\frac{\partial J(\theta)}{\partial \theta_{i}} =\frac{\partial J(\theta)}{\partial z_{2}} \times \frac{\partial z_{2}}{\partial s_{2}} \times \frac{\partial s_{2}}{\partial \theta_{i}}
$$

**chain rule(연쇄법칙)**
chain rule은 합성함수의 미분규칙이며 역전파과정에서 Gradiant를 도출할 때 사용된다.

기본적으로 바깥함수의 도함수에 안쪽함수를 인자로 넣어주고 안쪽함수의 도함수를 곱해주면 된다.

![](https://i.imgur.com/4eSVZW0.png)


<center><b>그림 3. Chain Rule 예시</b></center>


**가중치 업데이트**

도출된 값을 learning rate와 곱해서 기존 가중치에서 빼주면 새로운 가중치는 다음과 같이 나타낼 수 있다.

$$
\theta_{j}=\theta_{j}-\eta \frac{\partial}{\partial \theta_{j}} J(\theta)
$$


**결국 순전파와 역전파를 통해 가중치와 편향을 훈련데이터에 적응하도록 조정하는 과정이  기계학습에서의 `학습`이라는 것을 알 수 있다.**


### 신경망 학습 알고리즘 절차 정리

퍼셉트론과 역전파 알고리즘에 대한 이해를 바탕으로 지금까지의 절차를 아래와 같이 정리할 수 있다.

1. 학습할 신경망 구조를 선택
    - 입력층 유닛의 수 = Feature 수 (input layer)
    - 출력층 유닛의 수 = target class 수 (output layer)
    - 은닉층 수, 각 은닉층의 노드 수 (hidden layer)
      - hyperparameter의 영역이다. 
      - sqrt(input layer 수 * output layer 수 ) 로 구해줄 수 있지만 방식이 정해진 것은 아니다.
  
2. 가중치 초기화
3. 순방향 전파를 통해 $h_{\theta}(x^{(i)})$(출력층 y값) 을 모든 입력 $x^{(i)}$에 대해 계산
   - 입력벡터와 가중치벡터의 내적을 산출 
   비용함수 $J(\theta)$를 계산
4. 역방향 전파를 통해 편미분 값들 $\frac{\delta}{\delta\theta_{jk}^{l}}{J(\theta)}$ 을 계산
5. optimizer를 통해 loss function을 최소화
6. 어떤 중지 기준을 충족하거나 비용함수를 최소화 할 때까지 단계 2-5를 반복한다.
   - 한번 학습할때의 sample의 size 를 `batch` 라고 한다.
   - 전체 sample에 대해 2-5 의 과정을 반복한 것을 `epoch`라고 한다.
   - `iteration`은 batch 기준으로 학습의 횟수를 카운팅 한 것이다. 100개의 sample의 batch가 50이고 epoch를 50으로 할 경우 전체 iteration의 수는 100이 된다.


### 머신러닝에서의 학습

미분은 순간의 변화율을 구하는 것이다.
**역전파는 모형에서 계산한 예측값과 실제값의 차이를 바탕으로 미분을 통해 가중치를 보정하는 것을 최대한 반복해서 수행하는 것이다.** 
구체적으로는 손실함수의 국소적 미분값(local deravitive)를 구해서 학습률과 곱한 값을 기존 파라미터에서 빼주는 것을 손실함수가 최소가 될 때까지 반복하는 것이다.
`손실함수의 각 피처에 대한 편미분을 벡터로 묶은 것을 그래디언트(Gradient)라고 부른다.`
결국 역전파는 gradient를 조정하는 것을 반복하는 것이라고 볼 수 있다.
결국 순전파와 역전파를 통해 가중치와 편향을 훈련데이터에 적응하도록 조정하는 과정이  기계학습에서의 `학습`이라는 것을 알 수 있다.


## 신경망 학습 알고리즘 절차 정리

퍼셉트론과 역전파 알고리즘에 대한 이해를 바탕으로 지금까지의 절차를 아래와 같이 정리할 수 있다.

0. 학습할 신경망 구조를 선택
    - 입력층 유닛의 수 = Feature 수 (input layer)
    - 출력층 유닛의 수 = target class 수 (output layer)
    - 은닉층 수, 각 은닉층의 노드 수 (hidden layer)
      - hyperparameter의 영역이다. 
      - sqrt(input layer 수 * output layer 수 ) 로 구해줄 수 있지만 방식이 정해진 것은 아니다.
  
1. 가중치 초기화
2. 순방향 전파를 통해 $h_{\theta}(x^{(i)})$(출력층 y값) 을 모든 입력 $x^{(i)}$에 대해 계산
   - 입력벡터와 가중치벡터의 내적을 산출 
   비용함수 $J(\theta)$를 계산
4. 역방향 전파를 통해 편미분 값들 $\frac{\delta}{\delta\theta_{jk}^{l}}{J(\theta)}$ 을 계산
5. optimizer를 통해 loss function을 최소화
6. 어떤 중지 기준을 충족하거나 비용함수를 최소화 할 때까지 단계 2-5를 반복한다.
   - 한번 학습할때의 sample의 size 를 `batch` 라고 한다.
   - 전체 sample에 대해 2-5 의 과정을 반복한 것을 `epoch`라고 한다.
   - `iteration`은 batch 기준으로 학습의 횟수를 카운팅 한 것이다. 100개의 sample의 batch가 50이고 epoch를 50으로 할 경우 전체 iteration의 수는 100이 된다.

## References

- https://towardsdatascience.com/understanding-backpropagation-algorithm-7bb3aa2f95fd
- https://edgeaiguru.com/Feedforward-and-Backpropagation