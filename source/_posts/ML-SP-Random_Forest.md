---
title: '[Tree]Random Forest의 이해'
categories:
  - Machine Learning
tags:
  - Random Forest
  - Supervised Learning
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

## Random Forest

---
**_Concept_**

- **Bagging** : 랜덤 복원추출을 통해 샘플링한 데이터를 바탕으로 피팅한 모델들의 예측결과를 다수결이나 평균을 내어 예측하는 것. 
- **weak learner** : 서로 독립적으로 만들어지며 **상관이 낮은** 약한 분류기.
- **Random Subspace Method** : Bagging과 유사하지만 Bagging에 추가로 feature를 일부 선택해서 분할하는 것. Random Forest에서 사용
- **Random Forest** : 여러 `week learner`들을 합쳐서 하나의 트리를 만드는 것. boosting에 비해 과적합이 덜되는 경향이 있다.
- **Bootstrap** : datapoint가 n개일 때 n의 크기를 가지는 표본을 복원추출하는 것. 기본적으로 데이터가 편중되지 않게끔 한다.
- **OOB** : Out of Bag. 부트스트랩에서 추출되지 않는 36.8% 의 샘플.
---

> A large number of relatively uncorrelated models (trees) operating as a committee will outperform any of the individual constituent models.

**랜덤포레스트의 핵심적인 컨셉은 위의 인용처럼 서로 상관이 낮은 약한 분류기들을을 합쳐서 강력한 하나의 모델을 만드는 것이다.**

### Bagging

<img src="https://www.researchgate.net/profile/Xiaogang_He2/publication/309031320/figure/fig1/AS:422331542708224@1477703094069/Schematic-of-the-RF-algorithm-based-on-the-Bagging-Bootstrap-Aggregating-method.png" width="700" />

배깅의 핵심적인 목표는 **의사결정 트리 사이의 분산을 줄이는 것이다.** . Bagging은 기본적으로 모델의 bias를 상승시키지 않으면서 variance를 줄이는 방법이다.이를 위해 배깅에서는 `부트스트래핑`을 통한 데이터의 서브셋을 각각 학습시켜 독립적이고 서로 상관이 낮은 여러 기본모델들을 만든다. 이렇게 만든 여러 기본모델들의 앙상블이 `랜덤 포레스트`이다. `랜덤포레스트`는 한 트리의 오류가 전파되지 않아서 노이즈(이상치)에 강하며 따라서 일반적인 의사결정나무의 약점인 과적합에 강한 모습을 보인다.

### Random Subspace method

- Bagging과 유사하지만 Bagging에 추가로 feature를 일부 선택해서 분할하는 것. Random Forest에서 사용.
- train dataset의 feature가 1개만 있다면 랜덤포레스트와 배깅의 알고리즘이 동일해진다.
- **feature를 일부 선택해서 분할하는 이유는 설명력이 높은 feature가 모든 `weak learner`에서 선택되어 모델 간의 예측값의 상관이 높아지는 것을 방지하기 위함이다.**
- 기본모델 생성시 **특성 m개 중 일부분 k개의 특성을 선택(sampling)한다** 
- k개에서 최적의(information gain이 가장 높은) 특성을 찾아내어 분할함. k개는 일반적으로 $log_2 m$ 를 사용.
- $\sqrt{m}$을 k로 활용할 수도 있다.
- k가 작아질 수록 각 트리들이 모두 다르게 구성되어 예측력이 향상.
- k가 너무 작아지면 가중치가 적은 feature가 상위노드에 들어가 불순도가 높아진다.
- k가 너무 커지면 각 트리간 상관이 높아짐(트리들이 비슷해짐).예측력이 하락한다 
- 서로 상관이 높은 feature가 많은 경우 k를 적게 하는 것이 유리하다.**

- 트리의 수가 증가해도 과적합되지 않는다. 일정 수준이상으로 많아지면 error rate는 안정되는 경향을 보인다.
![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcaLvgA%2FbtraSXTXHT3%2FT0aBmdkrhHd3FCKGsSWN9k%2Fimg.png)

**배깅과 Random subspave method의 비교**

- bagging: it is better when the training samples are sparse(결측값이 많은 경우)
- Random subspace method: it is better when the classes are compact and the boundaries are smooth.

### Random Forest 알고리즘

- m개의 feature와 n개의 데이터포인트가 있는 학습데이터에서 부트스트래핑을 통해 서브셋을 추출한다.
- m개의 feature에서 각각 k개의 feature를 추출한 서브셋을 가지고 학습해 약한 분류기를 여러개 만든다. 
- 각각의 약한 분류기로 결과를 예측한다.
- 각 분류기의 예측결과를 모아 최종결과를 도출한다.
  + 분류 문제일 경우 다수결을 통해 최종 결과를 도출한다
  + 회귀 문제일 경우 평균을 통해 최종결과를 도출한다.

### Random Forest 주요 hyperparameter

[Randomforest Hyperparameter](https://www.analyticsvidhya.com/blog/2015/06/tuning-random-forest-model/)
sklearn에서 제공하는 하이퍼파라미터 기준으로 정리

- max_featuers : 기본트리에 사용되는 feature의 수. default는 전부 사요하는 것.
- n_estimators : 기본트리 수. 커질수록 퍼포먼스가 좋아지지만 학습시간이 오래걸린다.
- min_sample_leaf : 리프노드 샘플의 최소값. 작을 수록 학습데이터의 이상치를 잡기 어려워진다. 보통 50이상으로 놓는다.
- oob_score : boolen 값. cross validation이랑 비슷. oob sample을 바탕으로 평가를 수행하는 것.

```python
# 보통 고려하는 것들
{'bootstrap': True,
 'criterion': 'mse',
 'max_depth': 3, # depth가 3일때까지만 split
 'max_features': 'auto',
 'max_leaf_nodes': 4, # leaf node가 4개일때까지만 split
 'min_impurity_decrease': 0.0,
 'min_impurity_split': None,
 'min_samples_leaf': 3, # 생성될 노드들의 샘플 수가 3개 이상이여만 split 
 'min_samples_split': 5, # 5개 이상의 샘플만 split
 'min_weight_fraction_leaf': 0.0,
 'n_estimators': 10,
 'n_jobs': 1,
 'oob_score': False,
 'random_state': 42,
 'verbose': 0,
 'warm_start': False}
```

### Random Forest 장단점

**장점**

- 과적합에 강하다.
- 이상치에 크게 영향받지 않는다.
- Scaling이 필요가 없다.
- 결측값에 크게 영향받지 않는다.

**단점**

- 고차원의 희소한 데이터에 대해 성능이 저하된다.
- training 속도 느림(메모리 소모)
- 개별 트리 분석이 어럽다.



### Random Forest 구현

- sklearn을 활용한 구현

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=1000, n_features=4,
                            n_informative=2, n_redundant=0,
                            random_state=0, shuffle=False)

clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(X, y)
RandomForestClassifier(...)
print(clf.predict([[0, 0, 0, 0]]))

```


- numpy를 활용한 구현

```python
from collections import Counter

import numpy as np

from .decision_tree import DecisionTree


def bootstrap_sample(X, y):
    n_samples = X.shape[0]
    idxs = np.random.choice(n_samples, n_samples, replace=True)
    return X[idxs], y[idxs]


def most_common_label(y):
    counter = Counter(y)
    most_common = counter.most_common(1)[0][0]
    return most_common


class RandomForest:
    def __init__(self, n_trees=10, min_samples_split=2, max_depth=100, n_feats=None):
        self.n_trees = n_trees
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.n_feats = n_feats
        self.trees = []

    def fit(self, X, y):
        self.trees = []
        for _ in range(self.n_trees):
            tree = DecisionTree(
                min_samples_split=self.min_samples_split,
                max_depth=self.max_depth,
                n_feats=self.n_feats,
            )
            X_samp, y_samp = bootstrap_sample(X, y)
            tree.fit(X_samp, y_samp)
            self.trees.append(tree)

    def predict(self, X):
        tree_preds = np.array([tree.predict(X) for tree in self.trees])
        tree_preds = np.swapaxes(tree_preds, 0, 1)
        y_pred = [most_common_label(tree_pred) for tree_pred in tree_preds]
        return np.array(y_pred)


```


## References


- https://towardsdatascience.com/understanding-random-forest-58381e0602d2
- https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
