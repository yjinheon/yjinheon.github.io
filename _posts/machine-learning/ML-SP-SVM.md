---
title: '[SVM]서포트벡터머신의 이해'
categories:
  - - Machine Learning
    - Supervised Learning
date:
updated:
tags:
  - SVM
  - hyperplane
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

<!--
진짜 ref
https://excelsior-cjh.tistory.com/165


진짜 가장중요한 ref
https://www.baeldung.com/cs/svm-hard-margin-vs-soft-margin

-->

---
**_Concept_**

- **결정 경계**: 서로 다른 두 데이터를 구분하는 기준선(threshold). 선형 SVM의 결정 경계는 데이터 feature의 n차원의 초평면(hyperplane)이다.
- **초평면(hyperplane)** : flat affine subspace of p-1 (p는 데이터의 차원) 
- **Support Vector** : 결정 경계와 가장 가까운 데이터 포인트. Soft Margin의 끝에 있는 데이터포인트
- **Margin** : 결정경계와 Support Vector사이의 거리(threshold와 데이터포인트 사이의 최소거리)
- **Support Vector Machine** : 마진을 최대화 하는 결정 경계를 찾는 알고리즘.
  + **Soft Margin** : **Allow misclassification**. outlier의 오분류를 허용함으로써 과적합으로 인한 문제(low bias, high variance) 를 완화시키려고 하는 것. Soft Margin은 오분류를 허용한 경우의 Margin을 뜻한다.
  + **Hard Margin**: 결정경계면이 선형이며 오분류를 허용하지 않는 Margin. 오차항이 없는 경우의 soft margin 을 hard margin이라 한다.
---

### Note
---
- 데이터가 p차원일 경우 분류기(Support Vector Classifier)는 p-1차원의 subspace에 존재한다. 이를 hyperplane이라 한다.
- 기본적인 컨셉은 margin을 최대화 하는 결정경계를 찾는 것이다.
- margin을 크게 할 수록 일반화 성능이 좋아진다.(과적합이 덜 된다.)
- 마진이 커질경우 일반화 성능이 좋아지지만 bias가 상승한다,
- 패널티 항을 추가해서 생각하면 SVM에서의 최적화는 결국 마진을 크게 하는 것과 에러에 대한 페널티를 크게 하는 것의 균형으로 볼 수 있다.
  + maximizing the margin and minimizing the loss

![](https://www.baeldung.com/wp-content/uploads/sites/4/2021/03/svm-all.png)

margin이 최대화 하려면 결정경계에 해당하는 wx+b=0이 되게끔 하는 w를 찾아야 한다.
이는 `wx+b=0`에 수직인 벡터(법선벡터)인 $\frac{2}{\|\boldsymbol{w}\|}$ 최대화 하는 것이다.(w의 유클리드 norm에 대해 2를 곱해준 것)
따라서 $\frac{2}{\|\boldsymbol{w}\|}$ 를 최대화 하는 것이 SVM의 기본적인 목적이 된다.
Graidient 계산을 보다 용이하게 하기 위해 $\frac{2}{\|\boldsymbol{w}\|}$을 최대화하는 문제를 아래와 같이 치환할 수 있다.

$$\min _{\boldsymbol{w}, b} \frac{1}{2}\|\boldsymbol{w}\|^{2} \equiv \min _{\boldsymbol{w}, b} \frac{1}{2} \boldsymbol{w}^{T} \boldsymbol{w}$$

class label을 각각 1,-1로 가정할 때 데이터포인트를 정하게 분류하기 위해 다음과 같은 제약조건이 필요하다.

- **양성 plane 보다 위에 있는 관측치는 1보다 커야하고 음성 plane 보다 아래 있는 관측치들은 -1 보다 작아야 한다.**

이를 모두 만족하는 제약식은 아래와 같다.

$\quad y_{i}\left(\boldsymbol{w}^{T} \boldsymbol{x}_{i}+b\right) \geq 1$


따라서 최적화 문제를 최종적으로 아래와 같이 정리 할 수 있다.


$$\min _{\boldsymbol{w}, b} \frac{1}{2} \boldsymbol{w}^{T} \boldsymbol{w}$$

$$\text { s.t. } \quad y_{i}\left(\boldsymbol{w}^{T} \boldsymbol{x}_{i}+b\right) \geq 1$$

### Soft Margin
---

소프트마진은 분류기에 오차를 나타내는 slack variable $\zeta$ 를 목적함수에 추가한다. 

hyperparameter C를 통해 loss에 대한 비용을 조정할 수 있다. C가 클 수록 분류오차에 민감해진다. 즉 C값이 커질 경우 마진이 커진다.

반대로 C값을 줄일 경우 bias가 늘어나는 대신 variance가 줄어든다.

소프트 마진 SVM의 최적화 함수는 다음과 같다.

아래의 제약조건을 포함해 생각하면 slack vairable $\zeta$가 0>인 경우를 최소화하고 margin을 최대화 하는 hyperplane을 찾는 것이  Soft Margin SVM의 목적이 된다.

$$\min \frac{1}{2}\|\mathbf{w}\|^{2}+C \sum_{i=1}^{m} \zeta_{i}$$

{% raw %}

$$\quad y_{i}\left(\mathbf{w}^{T} \mathbf{x}_{i}+b\right) \geq 1-\zeta_{i} \quad i=1, \ldots, n, \quad \zeta_{i} \geq 0$$

{% endraw %}

### Hinge Loss
---

max(0, 1−yi(wTxi − b)) 는 SVM의 loss function으로 기능한다.

SVM의 loss function은 `hinge loss` 라고 불리는 데 yi(wTxi − b)이 safety margin인 1보다 크면 loss를 0으로 두고 1보다 작을수록 loss가 크도록 유도한 것이다.

SVM의 hyperparmeter C 는 단순히 hinge loss에 대한 계수이다.

결정경계로 부터의 거리가 0보다 작을 경우 hinge loss가 커지고 이는 데이터포인트가 결정경계의 잘못된 부분에 있는 것을 의미한다.

결정경계로 부터의 거리가 0 과 1 사이에 있는 경우에도 기본적인 loss가 존재하지만 기본적으로 결정경계로부터의 거리가 0보다 커질 경우  loss는 0으로 수렴한다.

![](https://miro.medium.com/max/1150/1*PGqpYm7o5GCbDXxXErr2JA.png)

### 구현

- iris data set에 대해 soft margin 구현

사실 직접 구현보다는 그냥 잘 만들어진 프레임워크를 쓰는 것이 훨씬 낫다.
```python
from sklearn.svm import svc
linear_svm = SVC(kernel='linear',C=1.0, random_state=42)

linear_svm.fit(X_train,y_train)
```

- numpy로 직접구현


```python
# numpy로 svm구현

import numpy as np

class SVM:

    def __init__(self,learning_rate=0.0001,lambda_param =0.01,n_iter =1000):
        self.lr = learning_rate
        self.lambda_param = lambda_param
        self.n_iters = n_iters
        self.w = None
        self.b = None

    def fit(self,X,y):
        y_ = np.where(y<=0 ,-1, 1)
        n_samples = X.shape

        self.w = np.zeros(n_features) # 가중치 초기화
        self.b = 0 # 편향 초기화

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                """
                current index, data point
                """
                condition = y_[idx] * (np.dot(x_i,self.w)) >= 1 # 제약조건 구현

                # 가중치 업데이트(hinge loss의 gradient update)

                if condition:
                    self.w -= self.lr * (2 * self.lambda_param * self.w)
                else:
                    self.w -= self.lr * (2 * self.lambda_param * self.w - np.dot(x_i,y_[idx]))


    def predict(self,X):
        linear_output = np.dot(X,self.w) - self.b
        return np.sign(linear_output) # numpy 부호 판별 함수 부호에 따라 -1,1,0 중 하나를 반환

# weight가 주어졌을 경우 SVM을 시각화하는 함수
def visualize_svm():
    def get_hyperplane_value(x, w, b, offset):
        return (-w[0] * x + b + offset) / w[1]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    plt.scatter(X[:, 0], X[:, 1], marker="o", c=y)

    x0_1 = np.amin(X[:, 0])
    x0_2 = np.amax(X[:, 0])

    x1_1 = get_hyperplane_value(x0_1, clf.w, clf.b, 0)
    x1_2 = get_hyperplane_value(x0_2, clf.w, clf.b, 0)

    x1_1_m = get_hyperplane_value(x0_1, clf.w, clf.b, -1)
    x1_2_m = get_hyperplane_value(x0_2, clf.w, clf.b, -1)

    x1_1_p = get_hyperplane_value(x0_1, clf.w, clf.b, 1)
    x1_2_p = get_hyperplane_value(x0_2, clf.w, clf.b, 1)

    ax.plot([x0_1, x0_2], [x1_1, x1_2], "y--")
    ax.plot([x0_1, x0_2], [x1_1_m, x1_2_m], "k")
    ax.plot([x0_1, x0_2], [x1_1_p, x1_2_p], "k")

    x1_min = np.amin(X[:, 1])
    x1_max = np.amax(X[:, 1])
    ax.set_ylim([x1_min - 3, x1_max + 3])

    plt.show()


```



**Reference & Annotaion**

- https://youtu.be/efR1C6CvhmE
- https://en.wikipedia.org/wiki/Support-vector_machine
- https://towardsdatascience.com/a-definitive-explanation-to-hinge-loss-for-support-vector-machines-ab6d8d3178f1
- 데이터가 비선형일 경우 커널 트릭을 활용한 고차원 매핑을 시행한다.
- 법선벡터를 최대화 하는 문제를 최적화 문제로 바꾸는 변환에 주의할 것.