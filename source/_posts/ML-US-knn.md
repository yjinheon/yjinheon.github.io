---
title: '[Unsupervised Learning]KNN을 활용한 분류'
categories:
    - [Machine Learning]
tags:
  - KNN
  - Unsupervised Learning
date:
updated:
---

<!--

- ML
- Statistics , Math
- Data Engineering
- Programming
- EDA & Visualization
- Data Extraction & Wrangling


#참고

https://cinema4dr12.tistory.com/1016?category=515283

https://www.kdnuggets.com/2021/07/top-python-data-science-interview-questions.html
-->

---

## 간단한 컨셉

**KNN**

- 새로운 데이터에 대해 기존 데이터 가운데 가장 가까운 K개 이웃의 정보로 새로운 데이터를 예측하는 방법론.
- 회귀문제와 분류문제 해결에 모두 사용되는 지도학습
- 하이퍼파라미터는 기본적으로 거리측정방법과 탐색할 이웃 수 2가지 이다.
- **K(이웃)을 적게 사용하면 모델 복잡도가 높아지고 많이 사용하면 복잡도가 낮아진다(K의 수를 늘릴수록 결정경계가 부드러워진다.).**
- KNN은 회귀분석에도 쓰이며 여러개의 K를 사용할 경우 이웃들의 종속변수의 평균이 예측된다.
- 거리측정방법
    + 유클리디안 거리 : 데이터포인트 사이 직선 최단거리
    + 마할라노비스 거리 : 공분산을 고려해 거리를 계산한다. 변수간 상관관계를 고려한 거리지표.
    + 맨해튼 거리 : 각 좌표축 방향으로만 이동할 경우 계산된다. 격자모양의 길을 따라간다.
- 주의점
    + 기본적으로 거리기반이기 때문에 KNN을 돌리기 전 반드시 변수를 정규화 해야 한다.
    + 불균형 데이터의 분류문제를 풀 경우 학습데이터 범주의 사전확률(Prior Probability)를 고려해야핟다.

- 장단점
    +   장점 : 학습 데이터 내 노이즈의 영향들 덜받음. 학습데이터가 많으면 효과적 
    +   단점 : 어떤 거리척도가 분석에 적랍한지 불분명. 계산시간이 오래 걸림 


## 구현

- 유클라디안 거리를 활용한 KNN 구현

```python
import numpy as np
from collections import Counter


def euclidean_distance(x1,x2):
    return np.sqrt(np.sum((x1-x2)**2))

class KNN:

    self __init__(self, k=3):
        self.k = k 

    def fit(self, X, y): # triain sample and label
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predicted_labels = [self._predict(x) for x in X]
        return np.array


    def _predict(self,x):
        """
        1. 거리 계산하기

        2. k nearest sample

        3. majority vote, get most common class

        """

        distances = [euclidean_distance(x,x_train) for x_train in X_train]

        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]

        most_common = Counter(k_nearest_labels).most_common(1)

        return most_common[0][0]

```


## 분류문제 풀이

- iris 데이터를 바탕으로 분류문제 풀이

```python
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn.model_selection import train_test_split

cmap = ListedColormap(["#FF0000", "#00FF00", "#0000FF"])

def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy

iris = datasets.load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1234
    )

k = 3
clf = KNN(k=k)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
print("KNN classification 정확도", accuracy(y_test, predictions))

```


```bash
$KNN classification accuracy 1.0

```

- sklearn에서도 knn 분류기가 구현되어 있다.
    + irsis data load까지는 동일하게 진행된다.

```python
from sklearn.neighbors import KNeiborsClassifier

clf = KNeiborsClassifier(n_neighbors =3)
clf.fit()

pred = clf.predict(X_test)
print("KNN classification 정확도", clf.score(X_test,y_test))


```


## K값과 모델 복잡도의 관계

- 위스콘신 유방암데이터로 구현한다.
- k의 수가 1개일 때는(적을 때는) train 데이터에 대해서만 예측력이 높고 test에서는 낮은 과적합된 모습을 보인다.
- k의 수가 많을 수록 모델이 단순해지고 train 데이터의 정확도는 줄어든다.
- k의 수가 10개일 때는 모델이 너무 단순해 train과 test모두에서 예측력이 낮은 모습을 보인다.
- 중간정도의 범위에서 k의 수를 선정할 필요가 있다.

```python
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt

cancer = load_breast_cancer()
X_train , X_test , y_train , y_test = train_test_split(cancer.data,
                                                       cancer.target,
                                                       stratify = cancer.target, # stratify 값을 target으로 지정해주면 각각의 class 비율(ratio)을 train / validation에 유지해준다. (한 쪽에 쏠려서 분배되는 것을 방지)
                                                       random_state=42)

train_acc = []
test_acc = []


k_indices = range(1,11)

for k in k_indices:
    clf = KNeiborsClassifier(n_neighbors=k)
    clf.fit()
    train_acc.append(clf.score(X_train,y_train))
    test_acc.append(clf.score(X_test,y_test))

plt.plot(neighbors_settings, training_accuracy, label="훈련 정확도")
plt.plot(neighbors_settings, test_accuracy, label="테스트 정확도")
plt.ylabel("정확도")
plt.xlabel("n_neighbors")
plt.legend(

```


![](https://tensorflowkorea.files.wordpress.com/2017/06/2-7.png?w=1024)

## References

- https://docs.python.org/3/library/collections.html
- [파이싼 라이브러리를 활용한 머신러닝](https://tensorflow.blog/%EA%B0%9C%EC%A0%95%ED%8C%90-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D/)
- https://ratsgo.github.io/machine%20learning/2017/04/17/KNN/