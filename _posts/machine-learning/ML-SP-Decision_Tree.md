---
title: '[Algorithms]Decision Tree의 이해'
categories:
  - Machine Learning
tags:
  - Supervised Learning
  - Decision Tree
date:
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
- Preprocessing


#신경망이란 무엇인가?

https://www.youtube.com/watch?v=aircAruvnKk


#참고

https://cinema4dr12.tistory.com/1016?category=515283

https://www.kdnuggets.com/2021/07/top-python-data-science-interview-questions.html
-->

## Decision Tree의 이해

---
**_Concept_**
- **Decision Tree(결정트리)**: 질문을 던지고 답을 하는 과정을 연쇄적으로 반복해 집단을 분류하거나 예측하는 분석방법.
- **threshold** : 결정트리에서의 학습대상. 정확히는 데이터를 나누는 best feature의 best threshold를 찾는 것이 학습의 목적이다,
- **full tree** : 모든 학습데이터에 대해 분기한 상태.
- **Entropy** : Entropy 는 데이터셋의 불순도와 무질서한 정도를 나타내는 측정치
- **지니 불순도** : 데이터 집합에서 클래스 분포에 따라 무작위로 라벨이 지정된 경우 무작위로 선택한 요소들을 잘못 분류할 확률이다.(Chance of being incorrect if you randomly assign a label to an example in the same set)
- **정보 이득** : 정보 이득은 단순히 부모 노드의 불순도와 자식 노드의 불순도 합의 차이.
- **Root Node** : 초기노드. 데이터셋 혹은 샘플 전체. 
- **Leaf Node(Terminal Node)** : 자식이 없는 노드.하위노드가 없다.
- **Pure Node** : 노드의 모든 데이터포인트가 하나의 클래스에 할당되어 있을 경우. 타깃 한개로만 이루어진 Leaf Node.
- **Branch** : sub-section of an entire tree.
- **Splitting** : 특정 노드를 나눠 하위노드를 생성하는 것.
- **Pruning** : 특정 노드의 하위노드를 날리는 것(삭제).
- **Pre-prune**: When you stop growing DT branches when information becomes unreliable.
- **Post-prune**: When you take a fully grown DT and then remove leaf nodes only if it results in a better model performance. This way, you stop removing nodes when no further improvements can be made.

![](https://miro.medium.com/max/888/1*FYEZGG-gEijSb87KuxSE_Q.png)

---

### Note
---

- SVM처럼 **분기점(threshold)을 학습한다.**
- 기본적으로 정보이득량이 가장 커지는 방식으로 반복적으로 분할을 진행(recursive partitioning)한다.
- **분기의 기준이 정보이득이라는 것이 핵심이다.**
- 과적합을 방지하기 위해 pruning이 필요하다.
- 선형모델과 달리 비선형(non-linear), 비단조(non-monotonic), 특성상호작용(feature interactions) 특징을 가지고 있는 데이터 분석에 용이하다.
- 특성을 해석하기 좋아 많이 쓰임
- **샘플에 민감해 트리 고저가 자주 바뀐다.**
- 앙상블 방법의 기초가 된다.
- **결정트리를 학습한다는 것은 정답에 가장 빨리 도달하는 예/아니오 질문 목록을 학습한다는 것이다. 이러한 질문들을 test라고 한다.**
- 학습 데이터셋에 과대적합되는 경향이 있다.
- 결정트리의 트리를 제어하지 않으면 트리는 무한정 깁어지고 복잡해진다.(일반화 성능이 낮아진다.)
- 따라서 사전/사후 가지치기를 통해 과대적합을 방지한다.
- 알고리즘 특성상 feature scaling이 필요하지 않지만 주로 다른 알고리즘과의 비교(시각화)를 위해 scaling을 해주는 경우도 있다.

### 불순도 지표
---

#### Entropy
---

[엔트로피 중요개념](https://www.analyticsvidhya.com/blog/2020/11/[]entropy-a-key-concept-for-all-data-science-beginners/)

[매우중요](https://towardsdatascience.com/entropy-how-decision-trees-make-decisions-2946b9c18c8)

- Entropy 는 데이터셋의 불순도와 무질서한 정도를 나타내는 측정치이다.(measure disorder)
- 0~1의 값을 가진다.
    + 클래스가 완전히 균일하게 분포되어있을 경우(0.5) Entropy가 최대인 1이된다. 
    + 데이터셋의 요소의 분포가 특정 클래스에 치우쳐있을수록 Entropy가 0에 가까워진다.
- 트리를 만들때 알고리즘은 가능한 모든 테스트에서 타깃값에 대해 가장 많은 정보를 가진 것을 고른다. -> 엔트로피가 최소화되는 방향으로 학습을 진행한다.

<p align="center">
<img src="https://miro.medium.com/max/750/1*M15RZMSk8nGEyOnD8haF-A.png" alt="drawing" width="400"/>
</p>

- **정보이득은 엔트로피의 변화량으로 계산된다.(1-엔트로피)**
- N은 범주의 개수
- $p_{i}$ 는 p 영역에 속한 데이터 중 i 범주에 속하는 데이터의 비율.

$$\text { Entropy }(p)=-\sum_{i=1}^{N} p_{i} \log _{2} p_{i}$$


#### 지니불순도
---

- **잘못 분류될 확률을 최소화하기 위한 기준이다.**
  - 정확히는 `데이터 집합에서 클래스 분포에 따라 무작위로 라벨이 지정된 경우 무작위로 선택한 요소들을 잘못 분류할 확률이다.(Chance of being incorrect if you randomly assign a label to an example in the same set)`
  - 기본적으로 Single Node에 대해 계산한 값이다,
- 클래스의 비율이 완벽히 균등할 때 최대가 된다.
- 기본적으로 노드가 중요할수록 불순도가 크게 감소한다.
- 범주형데이터가 라벨이라면 카디널리티가 적을 수록 불순도는 낮아진다.
- **Entropy와 지니불순도의 차이는 불순도의 max가 Entopy가 보다 높다는 것이다.**
- **지니불순도가 가장 낮은 Feature statement를 의사결정 트리의 가장 위에 놓는다.**(지니인덱스가 낮으면 불순도가 낮기 때문에 루트노드에 올 가능성이 높아진다.)
  - 불순도가 낮다는 것은 해당 Feature statement로 인한 정보이득이 높다는 것이다.
- 최초 노드의 impurity(unsertainty)에서 마지막 노드의 uncertainty를 뺀 값이 information Gain 이다.
- Entropy와 달리 식에 log가 없어 계산시 약간 유리하다.
- Gain이 가장 큰쪽으로 가지치기를 반복하는 것이 기본적인 의사결정 트리 알고리즘이다.


$$\text{Gini Impurity}=\sum_{i=1}^{N} p(i) *(1-p(i))$$


#### information Gain
---


- leaf의 결과는 기본적으로 majority 를 반환한다.
- **정보 이득은 단순히 부모 노드의 불순도와 자식 노드의 불순도 합의 차이이다.**
  - 이진트리의 경우 자식트리인 왼쪽,오른쪽 트리의 불순도의 합을 부모노드에서 뺀다.
- Information Gain is calculated for a split by subtracting the weighted entropies of each branch from the original entropy. When training a Decision Tree using these metrics, the best split is chosen by maximizing Information Gain.

$$IG(Parent,Children) = E(Parent) - E(Parent | Children)$$

- **자식 노드의 불순도가 낮을수록 정보 이득이 커진다.** 
- 보통 모듈에서 이진 결정 트리를 사용하므로 부모노드는 두 개의 자식 노드로 나눠진다.


$$\text {E(parent)} - [\text {weighted average}] * E(children)$$

![](https://tensorflowkorea.files.wordpress.com/2018/03/overview-plot.png)

- 엔트로피보다 지니 불순도 방식이 불순도 값을 줄이기 위해 더 클래스 확률을 낮추어야 한다.
- 엔트로피를 불순도 지표로 사용할 경우 지니불순도를 사용하는 것보다 더 균형잡힌 트리를 만들 가능성이 높다.



### 결정트리의 최적화 문제
---


- [최적화 원리와 코드](https://data-notes.co/decision-trees-how-to-optimize-my-decision-making-process-e1f327999c7a)

**Training algorithm**

- **기본적으로 Best Threshold를 찾는 문제이다**
- Start at the top node and at each node select the best split based o the best information gain
- Greedy Search : Loop over all features and over all thresholds (**all possible feature values**)
- Save the best split features and split threshold at each node
- Build the tree recursively
- Apply some stopping criteria to stop growing
    + maximum depth
    + minimum samples
    + etc..

- When we have a leaf node, store the most common class label of this node


**Predict := Traverse tree**
- Traverse the tree recursively.
- At each node look at the best split feature of the test feature vector x and go left or right **depending on x[feature idx] <= threshold**
- When we reach the leaf node we return the stored most common class label


### Pruning
---

**Put limits in How trees grow**

#### PrePruning
---

- 트리의 최대 깊이 제한하기(max_depth)
- 리프의 최대 개수 제한하기
- 노드가 분할하기 위한 데이터 포인트의 최소 개수 지정

- sklearn에서 제공하는 관련 Hyperparameter
    + max_depth : 일반화 성능관련. 트리의 최대깊이
        * min_sample_splite
        * max_feature : 최대 피처 사용수
        * random_state : random state
        * class_weight : 가중치 balance 맟추기

#### PostPruning
---

Post-pruning is also known as backward pruning. In this, first generate the decision tree and then remove non-significant branches. Post-pruning a decision tree implies that we begin by generating the (complete) tree and then adjust it with the aim of improving the accuracy on unseen instances. There are two principal methods of doing this. One method that is widely used begins by converting the tree to an equivalent set of rules. Another commonly used approach aims to retain the decision tree but to replace some of its subtrees by leaf nodes, thus converting a complete tree to a smaller pruned one which predicts the classification of unseen instances at least as accurately. There are various methods for the post pruning.



### Feature Importance in Decision Tree
---


### More to learn
---

- Pruning
- Handling missing data
- Building Trees for regression
- Using trees to explore datasets

**more**

- Gini-Index is providing us with the highest accuracy with max depth = 6.
- Entropy and Gini-index can behave similarly with appropriately selected min_weight_fraction_leaf.
- With min_samples_split as 7, Entropy is outperforming Gini for a rudimentary assumption that More samples will provide more information gain and tend to skew the Gini index as the impurity increases.

Therefore with taking the criteria as Gini and max_depth = 6, we obtained the accuracy as 32% which is an 18% increase from without using parametric optimization. Hence, Optimizing the parameter rightfully, will increase the model accuracy and provide better results.


**결정트리의 장점**

- 설명가능성


**결정트리의 단점**
- 과적합

### 구현
---

- numpy로 구현
- **기본적으로 Best Split Threshold를 찾는 것이 목적이다.**


```python

import numpy as np
from collections import Counter


def entropy(y):
    """
    Compute the entropy of a label vector
    :param y: label vector
    :return: entropy
    """
    
    hist = np.bincount(y) # class distribution # 0부터 max까지 class label의 빈도
    ps = hist / len(y) # probability of each class
    
    return -np.sum([p * np.log2(p) for p in ps if p != 0]) # 음수에 대해서는 정의하지 않음


class Node:
    def __init__(self,feature=None,threshold=None,left=None,right=None,*,value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value
        
    def is_leaf(self):
        return self.value is not None # leaf node의 경우 value가 있다.
    
class DecisionTree:
    def __init__(self, min_samples_split=2, max_depth=100, n_feats = None):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.n_feats = n_feats
        self.root = None
        
    def fit(self, X, y):
        # grow tree
        # X.shape[1] : feature의 개수
        
        self.n_feats = X.shape[1] if not self.n_feats else min(self.n_feats, X.shape[1])
        # if not self.n_feats -> n.feats가 정의되있지 않을 경우  min(self.n_feats,X.shape[1]) 
        # input의 feature 수보다 n_feats기 커지지 않게끔하는 
        self.root = self._grow_tree(X, y)
        
    def _grow_tree(self, X, y, depth=0):
        n_sample, n_feats = X.shape
        n_labels = len(np.unique(y))
        
        # stopping criteria # 더 이상 분류할 수 없는 경우 혹은 pruning 기준에 도달한 경우
        
        if (
            depth >= self.max_depth 
            or n_labels == 1 
            or n_sample < self.min_samples_split
        ):
            leaf_value = self._most_common_label(y)
            return Node(value=leaf_value)
        
        feat_idxs = np.random.choice(n_feats, self.n_feats, replace=False)
        
        # calculate information gain
        best_feat, best_threshold = self._best_criteria(X, y, feat_idxs)
        
        # grow the children that result from splitting on the best feature
        
        # 정보이득을 계산한 best_feature와 best threshold 기준으로 분할
        left_idxs , right_idxs = self._split(X[:,best_feat], best_threshold)
        left = self._grow_tree(X[left_idxs,:], y[left_idxs], depth+1) # depth+1
        right = self._grow_tree(X[right_idxs,:], y[right_idxs], depth+1)
        
        return Node(best_feat, best_threshold, left, right) 
        
    def _best_criteria(self,X,y,feat_idxs):
        """
        Find the best criteria to split the data
        :param X: input data
        :param y: label
        :param feat_idxs: indices of features to consider
        :return: best feature index, best threshold
        """
        best_gain = -1
        
        split_idx, split_threshold = None, None
        
        for feat_idx in feat_idxs:
            X_col = X[:,feat_idx] # X의 각 feature
            thresholds = np.unique(X_col) # 각 feature의 cardianlity
            for threshold in thresholds:
                gain = self._information_gain(y,X_col,threshold) # 각 feuture의 모든 threshold에 대해서 gain을 계산
                
                if gain > best_gain:
                    best_gain = gain
                    split_idx = feat_idx
                    split_threshold = threshold
                    
        return split_idx, split_threshold
    
    
    def _information_gain(self,y,X_column,split_threshold):
        """
        Calculate information gain
        E(parent) - [weight average] * E(Children)
        """
        
        # parent entropy
        
        parent_entropy = entropy(y)
        
        
        # generate split
        left_idxs, right_idxs = self._split(X_column, split_threshold)
        
        # 더이상 분할이 안될 경우 정보이득이 0
        if (len(left_idxs) == 0) or (len(right_idxs)) == 0:
            return 0

        # compute the weighted avg. of the loss for the children
        n = len(y)
        n_l, n_r = len(left_idxs), len(right_idxs)
        e_l, e_r = entropy(y[left_idxs]), entropy(y[right_idxs])
        child_entropy = (n_l / n) * e_l + (n_r / n) * e_r

        # information gain is difference in loss before vs. after split
        ig = parent_entropy - child_entropy
        return ig
        
    def _split(self, X_column, split_threshold):
        """
        Split data according to the threshold
        :param X_column: input data
        :param split_threshold: threshold to split
        :return: left and right indices
        """
        # np.argwhere을 사용 조건에 해당하는 인덱스 반환.
        left_idxs = np.argwhere(X_column <= split_threshold).flatten()
        right_idxs = np.argwhere(X_column > split_threshold).flatten()
        return left_idxs, right_idxs
    
    def _most_common_label(self, y):
        """
        Find the most common label in the dataset
        :param y: labels
        :return: most common label
        """
        counter = Counter(y)
        # counter.most_common(1) -> [(label, count)] # 리스트 안에 튜플
        most_common = counter.most_common(1)[0][0]
        return most_common # Counter(y) : Counter({0: 2, 1: 2}) #value과 count중 value만 반환 

    def predict(self, X):
        # traverse the tree
        return np.array([self._traverse_tree(x,self.root) for x in X]) # X의 각 데이터포인트에 대해서 트리를 순회하며 각 데이터포인트에 대한 결과를 반환
    
    
    def _traverse_tree(self, x, node):
        """
        Traverse the tree from the root
        :param x: input data
        :param node: root node
        :return: label
        """
        if node.is_leaf(): # check if leaf node
            return node.value
        
        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        else:
            return self._traverse_tree(x, node.right)
    
    
if __name__ == '__main__':
    from sklearn import datasets
    from sklearn.model_selection import train_test_split
    
    def accuracy(y,y_pred):
        acc = np.sum(y == y_pred) / len(y)
        return acc
    
    data = datasets.load_breast_cancer()
    X, y = data.data, data.target

    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    clf = DecisionTree(max_depth=10)
    clf.fit(X_train, y_train)
    
    y_pred = clf.predict(X_test)
    acc = accuracy(y_test, y_pred)
    
    print(f"Accuracy : {acc}")
```

**References & annotation**
---

- [결정트리의 최적화 문제](https://www.kdnuggets.com/2020/01/decision-tree-algorithm-explained.html)
- [정보이득](https://machinelearningmastery.com/information-gain-and-mutual-information/)
- [지니불순도](https://victorzhou.com/blog/gini-impurity/)
- [불순도 지표들](https://tensorflow.blog/tag/%EC%A7%80%EB%8B%88-%EB%B6%88%EC%88%9C%EB%8F%84/)
- [Post_Pruning](-https://xzz201920.medium.com/post-pruning-techniques-in-decision-tree-4be56636172b)