- Linear Model
  - Linear Regression
  - Logistic Regression
  - Stochastic Gradient Descent
- Tree Based Model
  - Decision Tree
  - Random Forest
  - Gradient Boosting
  - XGBoost
  - LightGBM
  - CatBoost
- Probabilistic Model  
  - Naive Bayes
  - Gaussian Process
  - Bayesian Network

- KNN
- Support Vector Machine
- Neural Network(in pytorch)
  - ANN

# Linear Model

**선형모델**

회귀와 분류모델 모두 있다.

**선형모델의 학습알고리즘**

- 특정 계수와 절편의 조합이 train 데이터에 얼마나 적합한지 측정
- 어떤 방식의 규제를 사욯할 것인지 결정

**선형모델의 장점**

- **설명이 쉽다.**
- 기본적으로 변수들의 선형결합으로 설명가능하다.
- 대용량처리가 가능하다.
  + solver = sag(확률적 경사하강법) 옵션 사용
  + SDG classifier, SDGRegressor 사용

**선형모델의 단점**

- 다중공선성 문제: Feature간 연관성이 높을 경우 설명 어려움
- 선형모델은 sample에 비해 feature가 많을 때도 잘 동작하지만 저차원 데이터 셋에서는 일반화 성능이 떨어진다.-> 과적합되기 쉽다.

## Linear Regression

### Cost function

cost function이 convex function이기 때문에 어디서 초기화를 하던지 무관하게 우리는 같은 지점 혹은 거의 같은 지점의 값을 얻을 수 있다.

우리는 Gradient descent 알고리즘을 통해 가장 낮은 값의 cost function값을 가지게 하는 w, b를 찾을 수 있다. 위 3차 그래프의 극값에 이를 때까지 함수의 기울기를 구하여 기울기가 낮은 쪽으로 계속 이동시키는 것이다.

### 선형회귀 일반 개념 및 인덱스

---

**_Concept_**

- **기준모델** : 모델에서 넘어야할 최소 기준점을 설정하기 위한 모델
- **Mean Absolute Error(MAE, 평균절대오차)** 예측 error 의 절대값 평균.
- **예측값** : 만들어진 모델이 추정하는  값. 보통 y_hat이라고 한다.
- **residual** : 표본집단에서 예측값과 관측값의 차이
- **error** : 모집단에서 예측값과 관측값 차이
- **RSS(residual sum of squares) :** 잔차제곱합. SSE(Sum of Square Error)라고도 말하며 이 값이 회귀모델의 비용함수(Cost function)이다.
- **Ordinary least squares(OLS)** : 잔차제곱합을 최소화 하는 가중치 벡터를 구하는 방법
- **coefficient** : 추정된 상수항
- **intercept** : 계수가 0일때 예측값. 추정된  상후항
- **회귀선** :  RSS(residual sum of squares)를 최소화 하는 직선
- **보간** : 알려진 지점의 값 사이(중간)에 위치한 값을 알려진 값으로부터 추정하는 것
- **외삽** : 기존 데이터의 범위를 넘어서는 값을 예측하기 위한 방법

---

### 오차항에 대한 가정

잔차(residual)는 모델의 예측값과 실제 true value의 차이를 뜻한다.

따라서 다음의 3가지 가정을 전제한다.

1. 등분산성
2. 평균이 0
3. 독립성 (iid에 대한 가정)

### 정규방정식을 통한 모수추정

**ref**

- https://brunch.co.kr/@linecard/467
- https://angeloyeo.github.io/2020/08/24/linear_regression.html

### 머신러닝 관점에서의 모수추정

회귀분석에서 MSE은 비용함수이다.
-> MSE를 최소화하는 가중치와 편향을 찾은 것으로 MSE를 재정의할 수 있다.
비용함수를 최소화 하는 최적화 관점에서 머신러닝을 볼 수 있다.
기울기 업데이트를 통해 비용함수(MSE)의 최소값을 찾는다.

$$
J\left(\theta_0, \theta_1\right)=\frac{1}{2 m} \sum_{i=1}^m\left(h_\theta\left(x^{(i)}\right)-y^{(i)}\right)^2
$$

---

**_Concept_**

- **Gradient Descent** : 함수의 기울기(즉, gradient)를 이용해 x의 값을 어디로 옮겼을 때 함수가 최소값을 찾는지 알아보는 방법. 함수값을 최소화 하는 독립변수를 찾는 방법
- **learning rate** : 학습을 한 내용을 다음 학습에 얼마나 반영할지의 문제. 정확히는 Loss 값을 가중치벡터로 편미분하여 얻어낸 값에 얼마나 수정을 해야 할 지를 결정하는 하이퍼파라미터 
  - learning rate가 너무 크다면 최적점에 도달하지 못하고 모델이 발산할 수 있다.
  - learning rate가 너무 작다면 최적점에 도달하지 못하고 학습이 끝날 수 있다.
- **iteration** : 학습(가중치 업데이트)의 반복횟수
- **weight** : 경사하강법을 통해 업데이트 되는 feature의 가중치
- **bias** : 활성함수에서 활성화가 잘 될지 안될지를 조절하는 hypterparameter의 일종.기본적으로 function curve 자체를 조정한다.(선형 비선형 상관없이)

---

#### Cost function of Linear Regression

- Cost Function은  (가설함수-target) 인 오차 제곱합에 대해 평균을 취한 것이다.
- Cost Function을 최소화 하는 w와 b를 찾는 것이 머신러닝에서의 학습의 목적이 된다.
- 이를 아래와 같이 일반화 할 수 있다.

$$cost(w, b) = \frac{1}{n} \sum_{i=1}^{n} \left[y^{(i)} - H(x^{(i)})\right]^2$$

- 단순선형회귀의 경우 아래와 같이 나타낼 수 있다.

$$f(w,b) =  \frac{1}{N} \sum_{i=1}^{n} (y_i - (wx_i + b))^2$$

#### Gradiant Descent

<!--
경사하강법은 미분 가능한 convex한 함수, 즉 y=x2과 같은 오목 함수에서 y가 최소값 갖게 하는 x를 찾기 위한 알고리즘입니다. (위의 그림에서는 x가 w로 표시돼 있네요!) 이를 위해 Gradient Descent는 함수의 기울기 혹은 경사 (gradient)를 구하여 기울기가 낮은 쪽으로 x값을 계속 이동시켜서 y가 극소값을 갖도록 반복합니다.
-->

- Gradiant Descent(경사하강법)은 Cost Function을 최소화하는 최적화 알고리즘의 일종이다.
- 오차가 낮아지는 방향으로 이동할 목적으로 현재 위치를 미분한다.
- **경사하강법의 원리는 반복적인 미분을 통한 w값의 업데이트를 통해 w, cost 지점의 경사(기울기)가 0이 되도록 만드는 것이다.** 

**경사하강법의 원리**
![](https://i.ytimg.com/vi/b4Vyma9wPHo/maxresdefault.jpg)

일단 비용함수인 MSE부터 시작한다.

$$
f(w,b) =  \frac{1}{N} \sum_{i=1}^{n} (y_i - (wx_i + b))^2
$$

미분할 경우 아래와 같이 변하며

$$
(y_i - (wx_i + b))^2 = A(B(w,b))
$$

$$
A(x) = x^2
$$


$$
\frac{df}{dx} = A'(x) = 2x
$$

따라서 아래와 같이 미분할 수 있다.

$$
B(m,b) = y_i - (wx_i + b) = y_i - wx_i - b \\~\\
$$
$$
\frac{dx}{dw} = B'(w) = 0 - x_i - 0 = -x_i \\~\\
$$

$$
\frac{dx}{db} = B'(b) = 0 - 0 - 1 = -1 
$$

미분의 `Chain Rule` 을 활용하여 가중치와 편향의 미분값을 구할 수 있다.

$$
\frac{df}{dw} = \frac{df}{dx} \frac{dx}{dw} \\~\\
$$

$$
\frac{df}{db} = \frac{df}{dx} \frac{dx}{db}
$$

가중치와 절편에 Chain Rule을 적용해 미분을 하면 아래와 같다.

$$
\frac{df}{dm} = A'(B(m,f)) B'(m) = 2(y_i - (wx_i + b)) \cdot -x_i \\~\\
$$

$$
\frac{df}{db} = A'(B(m,f)) B'(b) = 2(y_i - (wx_i + b)) \cdot -1 
$$

따라서 비용함수(MSE)의 Gradiant를 아래과 같이 유도할 수 있다.

$$
\begin{align}
  f'(w,b) =
    \begin{bmatrix}
      \frac{df}{dm}\\
      \frac{df}{db}\\
    \end{bmatrix}
  &=
    \begin{bmatrix}
      \frac{1}{N} \sum -x_i \cdot 2(y_i - (wx_i + b)) \\
      \frac{1}{N} \sum -1 \cdot 2(y_i - (wx_i + b)) \\
    \end{bmatrix}\\
  &=
    \begin{bmatrix}
       \frac{1}{N} \sum -2x_i(y_i - (wx_i + b)) \\
       \frac{1}{N} \sum -2(y_i - (wx_i + b)) \\
    \end{bmatrix}
  \end{align}
$$

**가중치 업데이트 방식은 Learning Rate(학습률)와 기울기(Gradient)를 곱한 값을 기존 가중치에서 빼서 새로운 가중치로 설정하는 것을 반복하는 것이다.**

**따라서 최적화하고자 하는 함수 f(x)에 대해 아래와 같이 정리할 수 있다.**

$$
x_{i+1} = x_i - \alpha \frac{df}{dx}(x_i)
$$

**기본적으로 반복횟수가 많아질수록 오차가 줄어들어야 한다.**

![](https://ml-cheatsheet.readthedocs.io/en/latest/_images/linear_regression_training_cost.png)

#### Gradiant Descent를 활용한 선형회귀 구현

- dw는 비용함수인 MSE를 가중치 W에 대하여 편미분한 것이다.
- db는 비용함수인 MSE를 편향 b에 대하여 편미분한 것이다.

```python
import numpy as np

def r2_score(y_true, y_pred):
    corr_matrix = np.corrcoef(y_true, y_pred)
    corr = corr_matrix[0, 1]
    return corr ** 2


class LinearRegression:

  def __init__(self, lr = 0.001, n_iters = 1000):
    self.lr = lr
    self.n_iters = n_iters
    self.weigts = None
    self.bias = None


  def fit(self,X,y):

    # init paremeters : 시작지점을 초기화 한다.
    n_samples , n_features = X.shape
    self.weigts = np.zeros(n_features)
    self.bias = 0

    for _ in range(self.n_iters):
      y_pred = np.dot(X,self.weigts) + self.bias

      dw = (1/n_samples) * np.dot(X.T,(y_pred - y)) # 가중치의 기울기(Gradiant)(미분값) 
      db = (1/n_samples) * np.sum(y_pred - y) # 편향의 기울기. 

      self.weigts -= self.lr * dw # 기울기 업데이트
      self.bias -= self.lr * db # 편향 업데이트



  def predict(self,X):
    y_pred = np.dot(X,self.weigts) + self.bias

    return y_pred
```

**ref**

- [경사하강법과 회귀](https://angeloyeo.github.io/2020/08/24/linear_regression.html)
- [ML from scratch](https://youtu.be/4swNt7PiamQ?list=PLqnslRFeH2Upcrywf-u2etjdxxkL8nl7E)

### MARS(Multivariate Adaptive Linear Splines)

### LOESS(Locally Estimated Scatterplot Smoothing)

## Logistic Regression

MLE(Maximum Likelyhood Estimation)를 통해 이해할 수도 있지만 여기서는 Cross Entropy를 통한 최적화 관점에서의 Logistic 회귀를 주로 다룬다.


- 회귀를 위한 선형 모델에서는 y_hat이 feature의 선형함수라면 분류용 선형모델은 결정 경계가 입력의 선형함수이다.
- 선형 분류기는 선,평면,초평면(3차원 이상) 을 사용해서 두 클래스를 구분하는 분류기이다.
- **결정경계는 기본적으로 선형 함수이고 이를 기준으로 클래스가 구분된다는 것이 중요하다.**

---

**_Concept_**

- **Cross Entropy** :두 개의 확률분포 p와 q에 대해 하나의 사건 X가 갖는 정보량
  + **Cross Entropy** 는 기본적으로 **추정된 분포가 실제의 분포와 열마나 가까운지** 를 결정한다. 
- **sigmoid** : input을 0과 1사이로 조정하여 반환하는 활성화 함수의 일종
- **softmax** : 로지스틱 회귀를 다중 클래스 분류로 확장할때 사용하는 활성화 함수.분류될 클래스가 n개라 할 때, n차원의 벡터를 입력받아, 각 클래스에 속할 확률을 추정한다.
- **모수(Parameter)** : 머신러닝에서 파라미터는 **모델의 형태를 결정하는 값**으로 정의할 수 있다. 예를 들어 y = wx+b라는 모델이 주어졌을 때 w,b가 모델의 모수가 된다.
- **우도** : 확률 분포의 모수가, 어떤 확률변수의 표집값과 일관되는 정도를 나타내는 값. **관측값이 고정되어있을 때** 그 관측치가 어떤 확률분포에서 나왔는가의 문제 
- **최대우도추정(Maxium Likelyhood Estimation)** :얻어진 데이터를 토대로 그 확률변수의 모수를 구하는 방법이다. 어떤 모수가 주어졌을 때, 원하는 값들이 나올 우도함수를 최대로 만드는 **모수를 선택하는 방법**이다.
  + **관측값(데이터) 가 주어진 상태에서 그 관측값이 나올 우도함수 **
  + MLE관점에서 볼때 로지스틱 회귀는 x와 w가 주어졌을 때 y의 확률. y의 확률이 나올 수 있는 w의 최대값을 구하는 문제이다.
- 우도함수 :  가능도함수는 모수가 $\theta$일 때, 특정 표본 x 가 나타날 함수. 즉, $\theta$가 주어졌을 때, x가 나타날 확률을 나타낸다.

---

**정리**

- Linear regression 에서는 연속적인 값을 출력하는 반면 Logistic regression에서 기본적으로 기대되는 output은 확률이다.
- **오차함수의 기본적인 검증 방식이 0이나 1로부터 예측값이 얼마나 떨어져 있는 지를 측정하는 것이다**
- 확률을 도출하기 위해 **선형모델에 sigmoid 함수를 적용**한다.
- 기본적으로 L2규제를 적욯하기 때문에 규제를 강하게 하면 계수가 0에 가깝게 되지만 완전히 0이 되지는 않는다.
- 설명하기 쉬운 모델을 원한다면 특성의 개수를 제한하는 L1규제를 사용한다. 
  + L1규제는 0이 많은 sparse data에 적합하다.
- Hyperparameter C를 통해 규제의 강도를 결정한다.
- C는 Ridge나 Lasso에서의 규제강도인 alpha($\lambda$)의 inverse이다. 다시말해 **C 값이 높을 수록 규제가 감소하고 C값이 낮으면 계수 벡터가 0에 가까워진다**.(피쳐의 영향이 줄어든다.)
- 이는 C의 값이 낮다면 데이터 포인트를 다수에 맞추려고 하는 반면 C의 값이 높다면 개개의 데이터 포인트를 명확하게 분류하고자 하는 알고리즘으로 볼 수 있다.

#### Cost function in Logistic Regression (Cross Entropy)

- **Cross Entropy는 두 개의 확률분포 p와 q에 대해 하나의 사건 X가 갖는 정보량이다**. 즉, 서로 다른 두 확률분포에 대해 같은 사건이 가지는 정보량을 계산한 것이다.
- 기본적으로 **추정된 분포가 실제의 분포와 열마나 가까운지** 를 결정한다.
  + **추정된 분포가 실제와 가까울 수록  오차가 0에 가까워진다.**
  + p(x)는 true label의 분포를 one-hot encoding 형식으로 나타낸 것이다.
  + q(x)는 현재 예측모델의 추정값의 분포이다.
- 모형이 예측한 확률분포들 중 정답에 해당하는 위치의 뉴런에 -log를 취한 것이 출력값이 된다.
- `-log` 를 취하는 이유는 출력값이 0,1 사이의 확률값으로 나와야 하기때문이다. -> 


- 크로스 엔트로피는 실제값과 예측값이 맞는 경우에는 0으로 수렴하고, 값이 틀릴경우에는 값이 커지기 때문에, `예측값과 실제 값의 차이를 줄이기 위한 엔트로피`라고 보면 된다.

![크로스 엔트로피 수식](https://i.stack.imgur.com/gNip2.png)

- MSE을 비용함수로 사용할 경우 국소 최소값에 빠질 가능성이 있어 크로스 엔트로피 함수를 사용한다.

- **정답에 해당하는 뉴런값의 오차만 계산에 들어간다는 것이 특징이다.**

- 정답에 해당하는 위치의 뉴런이 0에 가까워 질수록 y값이 exponential하게 증가하게 된다.

- Best case는 모델이 예측한 분포와 타겟의 분포가 같은 경우. 이 경우 오차가 0이된다.

- worst case는 target 위치의 뉴런 값이 0인 경우이며 이 때 Cross Entropy 오차는 무한히 증가한다. 

![크로스 엔트로피 오차](https://ml-cheatsheet.readthedocs.io/en/latest/_images/y1andy2_logistic_function.png)


#### Cross Entropy from Coursera

#### -log



- 크로스 엔트로피 구현

```python
import numpy as np

p = np.array([0, 1, 0])             # True probability (one-hot)
q = np.array([0.228, 0.619, 0.153]) # Predicted probability

cross_entropy_loss = -np.sum(p * np.log(q))
print(cross_entropy_loss)
# 0.47965000629754095
```

- 크로스 엔트로피 함수

```python

def cross_entropy(actual,pred):
    loss = -np.sum(actual * np.log(pred))
    return loss

```


- 크로스 엔트로피 비용함수를 통해 로지스틱 회귀 모형의 목적함수를 정의할 수 있다.
  + $\lambda \rVert W \rVert_2$ 는 l2 규제항이다.
  + $\lambda$ 가 0이 되면 규제항이 없는 단순 로지스틱회귀가 된다. 
  + $\lambda$가 커질수록 W가 줄어든다.($\lambda$가 무한대로 가면 가중치는 0으로 수렴)
  + $\lambda$ 수치를 조정함으로서  fit과 magnitude 사이에서 균형을 맞출 수 있다.
  + C는 $\lambda$ 역수로 sklearn에서 hyperparameter로 쓰인다.
  + **C 값이 높을 수록 규제가 감소하고 C값이 낮으면 계수 벡터가 0에 가까워진다**

$$J(w) = -\frac{1}{m} \sum_{i=1}^{m} [y^{(i)}logH(x^{(i)}) + (1-y^{(i)})log(1-H(x^{(i)}))]+\lambda \rVert W \rVert_2$$

아래와 같이 보다 간소화 해서 작성할 수 있다.

$$J(w)=\frac{1}{m} \sum_{i=1}^{m} \operatorname{Cost}\left(h\left(x^{(i)}\right), y^{(i)}\right)+\frac{\lambda}{2 m} \sum_{j=1}^{n} w_{j}^{2}$$

이 경우 업데이트 시 **Gradiant를** 아래아 같이 작성할 수 있다.

$$\frac{\partial}{\partial w_{i}} J(w)=\frac{1}{m}\left[\sum_{j=1}^{m}\left(h\left(x^{(j)}\right)-y^{(j)}\right) x_{i}^{(j)}+\lambda w_{i}\right]$$

#### Sigmoid Function

- input을 0과 1사이로 조정하여 반환하는 활성화 함수의 일종.
- 기준점인 0.5를 기준으로 출력값을 결정한다.
- w가 커질수록 기울기가 커진다.
- b의 크기에 따라 함수 자체가 이동한다.

```python
# 시그모이드 구현
def sigmoid(x):
    return 1/(1+np.exp(-x))

# sigmoid non-convex logistic least squares cost function
# convex 한것은 비용함수가 구불구불해서 국소 최저점이 존재하는 것

def sigmoid_least_squares(w):
    cost = 0
    for p in range(y.size):
        x_p = x[:,p]
        y_p = y[:,p]
        cost += (sigmoid(w[0] + w[1]*x_p) - y_p)**2
    return cost/y.size
```

![](https://jermwatt.github.io/machine_learning_refined/mlrefined_images/superlearn_images/sigmoid.png)

### Softmax

- 로지스틱 회귀를 다중클래스 분류로 확장한 것.
- 분류하고자 하는 클래스가 n개일 때, n차원의 벡터를 입력받아서 모든 벡터 원소의 값을 0과 1사이의 값으로 값을 변경하여 다시 k차원의 벡터를 리턴한다.
- 소프트맥스 함수는 분류될 클래스가 n개라 할 때, n차원의 벡터를 입력받아, 각 클래스에 속할 확률을 추정한다.

![](https://www.gstatic.com/education/formulas2/397133473/en/softmax_function.svg)

- **확률의 총합이 1이다.**

- 식 자체는 단순하게 `probability = exp(value) / sum v in list exp(v)` 로 나타낼 수 있다. `v번째 일 확률 / 전체 확률` 로 생각하면 된다. 

- [지수함수(exp)가 식에 포함된 이유](https://gooopy.tistory.com/53)

- softmax 구현
  
  ```python
  In [3]: from numpy import exp
   ...:
   ...: 
   ...: def softmax(vector):
   ...:     e = exp(vector)
   ...:     return e / e.sum()
   ...:
   ...: 
   ...: data = [1, 3, 2]
   ...: # convert list of numbers to a list of probabilities
   ...: result = softmax(data)
   ...: # report the probabilities
   ...: print(result)
   ...: # report the sum of the probabilities
   ...: print(sum(result))
  [0.09003057 0.66524096 0.24472847]
  1.0
  ```

```python
### 구현

- numpy를 활용한 구현
```python
# 정확도를 측정하기 위한 accuracy 함수
def accuracy(y_true,y_pred):
    accuracy = np.sum(y_true==y_pred)/len(y_true)

    return accuracy


import numpy as np

class LogisticRegression:

    def __init__(self,lr=0.001,n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weigts = None
        self.bias = None


    def fit(self,X,y):
        # init parameters

        n_samples, n_features = X.shape

        self.weigts = np.zeros(n_features)
        self.bias =0

        # gradient descent

        for _ in range(self.n_iters):
            linear_model = np.dot(X,self.weigts)+self.bias

            y_pred = self._sigmoid(linear_model) # 선형모델에 sigmoid 적용


            dw = (1/n_samples) * np.dot(X.T,(y_pred-y)) # W에 대해 편미분
            db = (1/n_samples) * np.sum(y_pred-y)


            self.weigts = -= self.lr * dw
            self.bias = -= self.lr*db


    def predict(self,X):
        linear_model = np.dot(X,self.weigts)+self.bias
        y_pred = self._sigmoid(linear_model) # 0~1 사이의 float을 반환

        y_pred_class = [1 if i > 0.5 else 0 for i in y_pred] # 값을 0,1로 고정

        return y_pred_class


    def _sigmoid(self,x):
        return 1/(1+np.exp(-x))
```

- sklearn을 활용한 구현

```python
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
X, y = load_iris(return_X_y=True)
clf = LogisticRegression(random_state=0).fit(X, y)
clf.predict(X[:2, :])

clf.predict_proba(X[:2, :]) # 확률 출력


clf.score(X, y)
```

- tensorflow를 활용한 구현

```python
# keras 를 활용한 
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers


x = np.array([0.42264594, 0.4524148 , 0.93797131, 0.36534474, 0.40276151,0.29153749, 0.05982402, 0.24713247, 0.91650771, 0.45207763])
y = np.array([0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]) 

model = Sequential()
model.add(Dense(1, input_dim=1, activation='sigmoid'))

sgd = optimizers.SGD(lr=0.001)
model.compile(optimizer=sgd ,loss='binary_crossentropy', metrics=['binary_accuracy'])
model.fit(x, y, epochs=200)
```

**ref**

- [Cross Entropy](https://stackoverflow.com/questions/41990250/what-is-cross-entropy/41990932)
- [Logistic Regression](https://youtu.be/yIYKR4sgzI8?list=PLblh5JKOoLUKxzEP5HA2d-Li7IJkHfXSe)
- [로지스틱 회귀 구현](https://ml-cheatsheet.readthedocs.io/en/latest/logistic_regression.html)
- [소프트맥스](https://developers.google.com/machine-learning/crash-course/multi-class-neural-networks/softmax)



## Perceptron



