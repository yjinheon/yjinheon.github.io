---
title: '[Classification]로지스틱 회귀와 크로스엔트로피'
categories:
  - [Machine Learning]
tags:
  - Logistic Regression
  - Cross Entropy
  - Supervised Learning
date:
updated:
---

<!--

<center >Kaggle Customer Score Dataset</center>

- Machine Learning
- Deep Learning
- Statistics , Math
- Data Engineering
- Programming
- EDA & Visualization
- Data Extraction & Wrangling


#신경망이란 무엇인가?

https://www.youtube.com/watch?v=aircAruvnKk


#참고

https://cinema4dr12.tistory.com/1016?category=515283

https://www.kdnuggets.com/2021/07/top-python-data-science-interview-questions.html
-->


## Logistic Regression


**로지스틱회귀의 파라미터 추정은 Feature X에 대한 선형회귀모델을 X에 대한 target의 log odds에 Fitting하는 것이다.**

**Fitting의 방식**

Maximum Likelyhood를 최대화하는 것 = 이항편차(binary deviance)를 줄이는 것 = cross entropy loss 를 줄이는 것

MLE(Maximum Likelyhood Estimation)를 통해 이해할 수도 있지만 여기서는 Cross Entropy를 통한 최적화 관점에서의 Logistic 회귀를 주로 다룬다.

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
  + – MLE관점에서 볼때 로지스틱회귀는 x와 w가 주어졌을 때 y의 확률. y의 확률이 나올 수 있는 w의 최대값을 구하는 문제이다.
- 우도함수 :  가능도함수는 모수가 $\theta$일 때, 특정 표본 x 가 나타날 함수.
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
  + p(x)는 true label의 분포를 one-hot encoding 형식으로 나타낸 것이다.
  + q(x)는 현재 예측모델의 추정값의 분포이다.
- 모형이 예측한 확률분포들 중 정답에 해당하는 위치의 뉴런에 -log를 취한 것이 출력값이 된다.
- `-log` 를 취하는 이유는 출력값이 0,1 사이의 확률값으로 나와하 하기때문이다.

![크로스 엔트로피 수식](https://i.stack.imgur.com/gNip2.png)

- MSE을 비용함수로 사용할 경우 국소 최소값에 빠질 가능성이 있어 크로스 엔트로피 함수를 사용한다.
- **정답에 해당하는 뉴런값의 오차만 계산에 들어간다는 것이 특징이다.**

- 정답에 해당하는 위치의 뉴런이 0에 가까워 질수록 y값이 exponential하게 증가하게 된다.
- Best case는 모델이 예측한 분포와 타겟의 분포가 같은 경우. 이 경우 오차가 0이된다.
- worst case는 target 위치의 뉴런 값이 0인 경우이며 이 때 Cross Entropy 오차는 무한히 증가한다. 

![크로스 엔트로피 오차](https://ml-cheatsheet.readthedocs.io/en/latest/_images/y1andy2_logistic_function.png)

- 크로스 엔트로피 구현

```python
import numpy as np

p = np.array([0, 1, 0])             # True probability (one-hot)
q = np.array([0.228, 0.619, 0.153]) # Predicted probability

cross_entropy_loss = -np.sum(p * np.log(q))
print(cross_entropy_loss)
# 0.47965000629754095
```

- 크로스 엔트로피 비용함수를 통해 로지스틱 회귀 모형의 목적함수를 정의할 수 있다.
  + $\lambda \rVert W \rVert_2$ 는 l2 규제항이다.
  + $\lambda$ 가 0이 되면 규제항이 없는 단순 로지스틱회귀가 된다. 
  + $\lambda$가 커질수록 W가 줄어든다.($\lambda$가 무한대로 가면 가중치는 0으로 수렴)
  + $\lambda$ 수치를 조정함으로서  fit과 magnitude 사이에서 균형을 맞출 수 있다.
  + C는 $\lambda$ 역수로 sklearn에서 hyperparameter로 쓰인다.

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

- 식 자체는 단순하게 `probability = exp(value) / sum v in list exp(v)` 로 나타낼 수 있다. `n번째 일 확률 / 전체 확률` 로 생각하면 된다. 
- [지수함수(exp)가 식에 포함된 이유](https://gooopy.tistory.com/53)

- softmax 구현
```python
In [3]: from numpy import exp
   ...:
   ...: 
   ...: def softmax(vector):
   ...:   e = exp(vector)
   ...:   return e / e.sum()
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


## References

- [Cross Entropy](https://stackoverflow.com/questions/41990250/what-is-cross-entropy/41990932)
- [Logistic Regression](https://youtu.be/yIYKR4sgzI8?list=PLblh5JKOoLUKxzEP5HA2d-Li7IJkHfXSe)
- [로지스틱 회귀 구현](https://ml-cheatsheet.readthedocs.io/en/latest/logistic_regression.html)
- [소프트맥스](https://developers.google.com/machine-learning/crash-course/multi-class-neural-networks/softmax)
