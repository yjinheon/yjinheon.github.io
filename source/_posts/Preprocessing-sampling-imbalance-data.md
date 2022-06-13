---
title: '[Sampling]Class Imbalance 다루기'
categories:
  - Preprocessing
date:
updated:
tags: 
  - Sampling
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

오버 샘플링 렉카
https://wyatt37.tistory.com/10
-->

# Dealing with Class Imbalance(클래스 불균형 다루기)
---

<!--
오버 샘플링 렉카
https://wyatt37.tistory.com/10

-->

**여기서 해결하는 문제**

- Biased predictions
- Misleading accuracy

**보통 고려하는 해결방법**

- 데이터 합성(Synthesisis of new minority class instances)
- Over-sampling 
- Under-sampling 
- class weight 조정하기(상향/하향가중치 적용)
- cost function 조정

## Random Under-Sampling
---

- **Advantages**
  + It can help improve run time and storage problems by reducing the number of training data samples when the training data set is huge.

- **Disadvantages**
  + It can discard potentially useful information which could be important for building rule classifiers.
  + The sample chosen by random under-sampling may be a biased sample. And it will not be an accurate representation of the population. Thereby, resulting in inaccurate results with the actual test data set.

### Tomeck Links

Tomek Links란 두 샘플 사이에 다른 관측치가 없는 경우를 말한다.

![](https://blog.dominodatalab.com/hubfs/Imported_Blog_Media/machine-learning-challenges-for-automated-prompting-in-smart-homes-23-638-2.jpg)

Tomek Links 방법은 Tomeck links 중에 major에 속하는 데이터포인트를 제거하는 undersampling 기법의 일종이다. 이 경우 데이터 불균형을 해결하면서 클래스 간 거리가 확보 되지만 여전히 정보 자체를 잃어버린다는 단점은 남는다.

```python
from imblearn.under_sampling import TomekLinks

tomek = TomekLinks(random_state = 123)

X_tm, y_tm = tomek.fit_sample(X, y)
```

## Random Over-Sampling
---

minor class의 데이터를 반복적으로 replace하는 것

단순히 부트스트래핑을 통한 업샘플링의 변형이다.

- **Advantages**
  + no information loss
- **Disadvantages**
  + prone to overfitting due to copying same information 

```python
X_samp, y_samp = RandomOverSampler(random_state=0).fit_sample(X_imb, y_imb)

plt.subplot(121)
classification_result2(X_imb, y_imb)
plt.subplot(122)
model_samp = classification_result2(X_samp, y_samp)


```

- 부트스트래핑을 직접 구현할 경우

```python

def bootstrap(X, n = None, iterations = 1):
    if n == None:
        n = len(X)
        X_resampled = np.random.choice(X, size = (iterations, n), replace = True)
    return X_resampled

```

### SMOTE(Synthetic Minority Oversample Technique)


임의의 마이너 클래스 데이터 포인트와 근접한 마이너 클래스 데이터 포인트 사이에 새로운 데이터 포인트를 생성하는 것

**반드시 training set에 대해서만 SMOTE 시행. 이는 data leakage 문제와 관련이 있다.**

$$syntetic = x_{minor} + u * (x_{nn}-x_{minor})$$

synthetic 합성 값은 minor class의 데이터 포인트와 근접한 minor class의 데이터포인트의 차이에 uniform distribution을 곱한 뒤 minor class의 데이터포인트를 더해준 값이다.


<!--
- Process
  + Identify the feature vectore and its nearest neighbor
  + take the the difference between the two
  + multiply the difference with a random number between 0 and 1
  + identify a new point on the line segment by adding the randomg number to feature vector
  + repeat the process of identified feature vectors

- 절차
-->

- numpy로 SMOTE 구현하기

알고리즘을 구현하는 것 자체는 어렵지 않지만 실제로 작업을 할때는 `imblearn` 모듈에서 제공하는 SMOTE함수를 사용하는 것이 훨씬 낫다.

```python
import random
import numpy as np

# SMOTE

def euclidean_dist(x1,x2):
    return np.sqrt(sum((x1-x2)**2))


def get_neighbors(X, x, k):
  """
  minor 클레스 데이터에 대해서 k개의 nearest neighbor를 구한다
  """
    X_len = len(X)
    euclidean_dist = [euclidean_dist(X[i],x) for i in range(X_len)]
    euclidean_dist = np.sort(euclidean_dist)
    neighbors = euclidean_dist[:k]
    
    return neighbors

def SMOTE(X,k):
  """
  smote algorithm 적용한 합성 데이터 생성
  """
    X_len = len(X)
    synthetic = []
    for i in range(0,X_len):
        w = 0
        while w == 0:
            w = np.random.uniform(0,1)
        add = get_neighbors(X,X[i],k)
        rand_idx = random.randint(0,k-1)
        add = add[rand_idx]
        
        diff = X[i] - add
        
        synthetic.append(X[i] + w*diff)

    return np.array(synthetic)

```

- imblearn을 활용한 target resampling


```python
from imblearn.over_sampling import SMOTE

rs = SMOTE(random_state=123)

X_new, y_new = rs.fit_sample(X, y)

```

### Borderline-SMOTE

: major와 minor를 구분하는 경계선에 있는 Borderline에 속하는 데이터데 대해 SMOTE을 적용하는 것

Minor class data X와 근접한 K개의 데이터포인트의 클래스의 수에 따라 SMOTE 적용 여부를 결정

- 0 <= K' <= K/2 : Safe

- K = K' : Noise

- K/2 < K' < K : Danger : 이 경우에 SMOTE을 적용한다.

```python
# Borderline-SMOTE

bsmote = BorderlineSMOTE(random_state = 1234, k_neighbors=3, m_neighbors=10)
X, y_new = bsmote.fit_resample(X, y)

print('Original_y %s' % Counter(y))
print('BorderlineSMOTE_y %s' % Counter(y_new))
```

### ADASYN

: Adaptive Synthetic Sampling

- 가중치를 적용해 SMOTE을 다르게 진행
- 인접한 major class의 비율에 따라 SMOTE을 다르게 적용하는 것

```python
X_samp, y_samp = ADASYN(random_state=0).fit_sample(X_imb, y_imb)

```

## 모델링과 평가 단계에서 Class Imbalance 다루기
---

샘플링 단계가 아니라 모델링과 평가단계에서 Class Imbalance 문제를 처리한다.

### Change the performance metric

class weight에 영향을 덜 받게끔 평가지표 자체를 바꿀 수 있다.

다른 방법보다 품이 덜 들어서 의외로 괜찮은 방법이다.


- **Confusion Matrix**: a table showing correct predictions and types of incorrect predictions.

- **Precision**: the number of true positives divided by all positive predictions. Precision is also called Positive Predictive Value. It is a measure of a classifier’s exactness. Low precision indicates a high number of false positives.

- **Recall**: the number of true positives divided by the number of positive values in the test data. The recall is also called Sensitivity or the True Positive Rate. It is a measure of a classifier’s completeness. Low recall indicates a high number of false negatives.

- **F1**: Score: the weighted average of precision and recall.

- **Area Under ROC Curve (AUROC)**: AUROC represents the likelihood of your model distinguishing observations from two classes.
In other words, if you randomly select one observation from each class, what’s the probability that your model will be able to “rank” them correctly?


### Penalize Algorithms(class_weight)

- Cost-Sensitive Training
- minority class로의 오분류에 대한 패널티를 크게 만듦

```python
# load library
from sklearn.svm import SVC

# class weight 
svc_model = SVC(class_weight='balanced', probability=True)

svc_model.fit(x_train, y_train)

svc_predict = svc_model.predict(x_test)# check performance
print('ROCAUC score:',roc_auc_score(y_test, svc_predict))
print('Accuracy score:',accuracy_score(y_test, svc_predict))
print('F1 score:',f1_score(y_test, svc_predict))

```
- sklearn를 활용한 구현

```python

# Classweight  계산 
from sklearn.utils.class_weight import compute_class_weight
classes = np.unique(y_train)
weights = compute_class_weight(class_weight='balanced', classes=classes, y=y_train)
class_weights = dict(zip(classes, weights)) # 모델의 인수로 들어간다.
```

- R 을 활용한 구현

대출연체가 minor이기에 연제에 대한 가중치를 1/p로 적용.
p는 연체의 확률값


```R
# wt 가중치 벡터 만들기
wt <- ifelse(loan_all_data$outcome == 'default',
             1/mean(loan_all_data$outcome == 'default'),1)

clf <- glm(outcome ~ payment_inc_ratio+purpose_+home_+emp_len,
           data= loan_all_data,
           weight =wt, family="binomial")

```

### Novelty Detection(단일클래스 분류기법)

- 단일클래스 분류기법
- Minor를 무시하고 Major class 에 속하는 데이터를 결정하는 일종의 바운더리를 생성하고 그 바운더리에 들어가냐 들어가지 않냐의 boolen으로 클래스를 결정한다.
- outlier 를 판별하는 알고리즘


**Reference & annotation**
---
- https://towardsdatascience.com/methods-for-dealing-with-imbalanced-data-5b761be45a18
- **Class weight를 적용하는 방식이 minor를 oversampling하거나 major를 undersampling하는 방법을 대체할 수 있다.(Practical Statistics for Data Scientist)**
- https://www.analyticsvidhya.com/blog/2020/07/10-techniques-to-deal-with-class-imbalance-in-machine-learning/
