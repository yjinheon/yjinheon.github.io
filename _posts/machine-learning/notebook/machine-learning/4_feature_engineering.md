다항식

# Data Transformation

## Encoding Categorical data

https://analyticsindiamag.com/a-complete-guide-to-categorical-data-encoding/

https://www.analyticsvidhya.com/blog/2020/08/types-of-categorical-data-encoding/#:~:text=This%20categorical%20data%20encoding%20method,over%20one%2Dhot%2Dencoding.

### One Hot Encoding

- basic usage

```python
from  sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(sparse=False)
print(encoder.fit_transform(df))
```

- 주요 옵션
  + sparse : default =True.희소행렬을 반환한다.  sparse=False로 설정할 경우 

### Ordinal , Label Encoding

순서형인코딩은 주의해야 할 것이 있습니다. 범주들을 순서가 있는 숫자형으로 바꾸면 원래 그 범주에 없던 순서정보가 생깁니다.

예를들어 food 특성에 ('밥', '빵') 이라는 두 범주가 있을 때 순서형 인코딩을 하면 ('1','2') 이렇게 인코딩이 됩니다. 원하지 않게 밥은 1, 빵은 2라는 순위를 매길수 있는 정보가 생겼습니다.

사실 순서형 인코딩은 범주들 간에 분명한 순위가 있을때 그 연관성에 맞게 숫자를 정해주는 것이 좋습니다. 예를들어 영화 평점과 같은 특성은 분명히 순서형 인코딩이 적절합니다.

지금까지는 OrdinalEncoder를 사용해 무작위로 수치를 인코딩 하였지만,

여러분들이 정확한 범주의 순위를 알고 있다면 `mapping` 파라미터를 사용해 지정해줄 수 있습니다. [OrdinalEncoder](https://contrib.scikit-learn.org/category_encoders/ordinal.html)

### Target Encoding

Target encoding is the process of replacing a categorical value with the mean of the target variable. Any non-categorical columns are automatically dropped by the target encoder model.

1. Feature Scaling
   1. Z표준화(standardization)
   2. 01변환(normalization)
2. variance stabilizing transformation
   1. 로그변환
   2. 제곱근변환
3. Sampling
   1. 랜덤샘플링
   2. 층화샘플링
   3. 군집샘플링
4. 범주화
   1. 이산형화
   2. 이항분포화
5. 차원축소
   1. 요인분석
   2. 주성분분석
   3. Autoencoder

## Feature Scaling

<!--

진짜 렉카

standar

- https://datascience.stackexchange.com/questions/45900/when-to-use-standard-scaler-and-when-normalizer

조건수의 의미
- https://datascienceschool.net/03%20machine%20learning/04.03%20%EC%8A%A4%EC%BC%80%EC%9D%BC%EB%A7%81.html


조건수가 크면 약간의 오차만 있어도 해가 전혀 다른 값을 가진다. 따라서 조건수가 크면 회귀분석을 사용한 예측값도 오차가 커지게 된다.

회귀분석에서 조건수가 커지는 경우는 크게 두 가지가 있다.

1) 변수들의 단위 차이로 인해 숫자의 스케일이 크게 달라지는 경우. 이 경우에는 스케일링(scaling)으로 해결한다.

2) 다중 공선성 즉, 상관관계가 큰 독립 변수들이 있는 경우, 이 경우에는 변수 선택이나 PCA를 사용한 차원 축소 등으로 해결한다.


다음의 경우

- 데이터가 편포된 경우
- 독립변수와 예측치가 비선형인 경우



https://deepinsight.tistory.com/113

-->

### Feature Scaling에서 overflow와 underflow의 의미

**no blog**

A common pre-processing step is to normalize/rescale inputs so that they are not too high or low.

However, even on normalized inputs, overflows and underflows can occur:

Underflow: Joint probability distribution often involves multiplying small individual probabilities. Many probabilistic algorithms involve multiplying probabilities of individual data points that leads to underflow. Example : Suppose you have 1000 data points, where the probability of each is < 1 lets say around 0.8, we have 0.8 ^ 1000 = 1.2302319e-97 which is close to 0. This is underflow.
A common way to combat this is to work in the log probability space: http://blog.smola.org/post/987977550/log-probabilities-semirings-and-floating-point

Overflow: Imagine you have a deep network, error gradients an keep accumulating and often become  vary large gradients. This results in an overflow where the values of the gradients become NAN. Weight regularization and gradient clipping are some common ways of dealing with this problem.

### Scaling을 하는 이유

---

feature scaling을 하는 가장 직관적인 이유는 **분석 단위(크기)를 맟줘주기 위해서이다.** 모델 학습시 각 feature의 크기를 맟줘 줌으로서 학습 시 특정 feature의 영향이 너무 커지는 것을 방지할 수 있다.

**scaling은 공분산행렬의 조건수(condition number)를 감소시킨다.**

조건수는 행렬에서 eigen value와 가장 작은 eigen value의 비율을 말한다.

$$\text{condition number} = \dfrac{\lambda_{\text{max}}}{\lambda_{\text{min}}}$$

조건수가 커질수록 약간의 오차에 대해서도 회귀방정식의 해의 오차가 민감하게 변하기 때문에 회귀식의 에러가 커진다.

조건수의 eigen value는 분산을 바탕으로 구해지기 때문에 scaling을 통해 condition number를 줄일 수 있다.

feature가 scaling이 되지 않을 경우 조건수가 커져서 에러가 증폭된다.

**scaling은 데이터의 크기와 범위를 제한해서 Gradient Explode나 Gradient Vanishing을 제한한다.**

- feature마다 
- 데이터의 범의를 줄여서 Neural network의 최적화 과정에서 수렴속도를 빠르게 한다.  
- Neural network model에서 sigmoid 활성화 함수의 `saturation`(포화) 문제를 완화한다.(Gradient Vanishing) 

**정리하면 Scaling의 핵심은 데이터가 유사한 범위를 가지도록 데이터의 범위를 제한한다는 것이다.**

1. 데이터의 범위를 제한해서 조건수를 낮춰 예측오차에 덜 민감해게끔 만든다.
2. 데이터의 범위를 제한해서 기울기 폭발,소실 문제를 완화한다.

### 어떤 경우에 Feature Scaling을 고려해야 하는가?

---

**거리 기반 모델의 경우 Scaling이 매우 중요하다**

- KNN, K-means clausturing : 유클리디안 거리를 기반으로 데이터 유사성을 결정하기 때문에 Scaling의 영향을 크게 받는다.
- SVM : margin(거리)를 최대화하는 것이 최적화 문제에 포함되어 있다 
- PCA : 알고리즘의 목적 자체가 분산이 가장 큰 방향을 가지는 고유벡터를 찾는 것이기 때문에 Scaling의 영향을 크게 받는다. 따라서 반드시 사전에 모든 수치형 변수들의 Scaling을 해줘야 한다.

**Gradient Descent 기반 모델의 경우**

신경망을 기반으로 하는 모델의 경우 loss function을 최소화 하는 방식으로 최적화를 진행한다.

이는 각 feature의 범위와 크기가 다를 경우 feature 마다 다른 step size를 적용해야 한다는 것을 뜻한다.

따라서 scaling를 통해 범위를 맞춰줄 경우 gradient descent의 수렴이 보다 빠르게 이루어진다.

**tree기반 알고리즘의 경우 Scaling에 따라 성능에 영향받지 않는다.**

대표적으로 tree기반 알고리즘에 해당하는 CART,RandomForest 등은 학습의 대상이 거리와 관련이 없기 때문에 (학습의 대상이 일종의 분기점) Scaling을 해줄 필요가 없다. Scaling을 해주는 경우가 가끔 있지만 이는 Scailng을 요구하는 다른 알고리즘과의 비교를 위해서이다.

**언제 Scaling을 하는가?**

**반드시 학습데이터와 검증 데이터를 나눈 이후에 Scaling을 시행한다.**

이는 data leakage로 인해 test data의 정보가 모델링에 포함 될 수 있기 때문이다.

- train test split 이후의 Scaling 예시

```python
normalizer = preprocessing.Normalizer().fit(X_train)


X_train = normalizer.transform(X_train) 
X_test = normalizer.transform(X_test) 
```

<!--

언제 scaling을 하는가?

렉카

https://datascience.stackexchange.com/questions/54908/data-normalization-before-or-after-train-test-split

https://stackoverflow.com/questions/49444262/normalize-data-before-or-after-split-of-training-and-testing-data


Normalization across instances should be done after splitting the data between training and test set, using only the data from the training set.

This is because the test set plays the role of fresh unseen data, so it's not supposed to be accessible at the training stage. Using any information coming from the test set before or during training is a potential bias in the evaluation of the performance.

[Precision thanks to Neil's comment] When normalizing the test set, one should apply the normalization parameters previously obtained from the training set as-is. Do not recalculate them on the test set, because they would be inconsistent with the model and this would produce wrong predictions.


Gradient Descent의 의미

Gradient descent is an iterative optimisation algorithm that takes us to the minimum of a function.
Machine learning algorithms like linear regression and logistic regression rely on gradient descent to minimise their loss functions or in other words, to reduce the error between the predicted values and the actual values.
Having features with varying degrees of magnitude and range will cause different step sizes for each feature. Therefore, to ensure that gradient descent converges more smoothly and quickly, we need to scale our features so that they share a similar scale.
Check out this video where Andrew Ng explains the gradient descent algorithm in more detail.


Data leakage와 싸우기 위한 5가지 팁!



-일시적 제거 : 관찰이 일어난 시간보다 사실이나 관찰에 대해 배운 시간에 초점을 맞추어 관심 이벤트 직전의 모든 데이터를 제거하십시오.

-소음 추가. 입력 데이터에 임의의 노이즈를 추가하여 누출 가능성이있는 변수의 영향을 부드럽게합니다.

-누출 변수를 제거하십시오. 간단한 규칙 기반 모델을 평가하려면 OneR에 계좌 번호 및 ID 등과 같은 변수를 사용하여 이러한 변수가 누출인지 확인하고 누락 된 경우이를 제거하십시오. 변수가 누설 된 것으로 의심되면 제거하는 것을 고려하십시오.


-파이프 라인을 사용하십시오. R의 caret 패키지 및 scikit-learn의 파이프 라인과 같은 교차 검증 폴드 내에서 일련의 데이터 준비 단계를 수행 할 수있는 파이프 라인 아키텍처를 많이 사용합니다.

-데이터를 따로 보유하십시요. validation데이터 셋을 따로 보유한후 마지막에 최종적으로 모델을 평가하는데 사용하면 됩니다.


-->

### Scaler의 종류

---

Scaling 대표적인 기법

- **Normalization(정규화)**

보통 값을 0,1 사이로 고정시킨다.

- **Standardization(표준화)**

#### MinMaxScaler

- 대부분의 Scaler가 그런 것 처럼 이상치에 민감하다.
- 데이터가 가우시안 분포가 아니고 사이즈가 작을 경우 유용하다.

```python
# 직접 구현

def minmax(x):
    return (x-min(x))/(max(x)-min(x))


# sklearn 에서 제공하는 MinMazScaler
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

X_train_new = scaler.fit_transform(X_train)
```

#### Robust Scaler

- 중앙값과 IQR을 사용해 이상치의 영향을 줄인 Scaler

```python
# sklearn 구현
from sklearn.preprocessing import RobustScaler
rbs = RobustScaler()
rbs.fit_transform(X_train)
```

#### StandardScaler

- 기본적으로 정규분포를 가정한다.
- 평균을 0, 분산은 1인 분포로 feature를 변환
- 이상치의 영향이 크기 때문에 이상치가 많을 경우 사전에 제거해주거나 다른 Scaler를 고려해야함
- 데이터의 최소 최대를 모르는 경우 사용

```python
# 직접구현
import numpy as np

def get_standard(x):
    mean = np.mean(x)
    rescale = x-mean/np.std(x)

    return rescale

# sklearn
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X_train_new = scaler.fit_transform(X_train)
```

#### Normalizer

- column-wise가 아니라 row wise로 정규화를 적용
- 최적화 과정에서 gradient exlosion이나 gradient vanishing을 막기 위해 사용

###### Reference & reference

- [condition number의 의미](https://www.quora.com/What-are-condition-numbers-and-poor-conditioning-How-are-they-related-to-deep-learning)
- [importance of feature scaling](https://towardsdatascience.com/gradient-descent-the-learning-rate-and-the-importance-of-feature-scaling-6c0b416596e1)
- `saturation`은 sigmoid 활성화 함수의 특정구간에서 gradient가 0에 가까워지는 것이다.(Gradient Vanishing 문제)
- https://www.youtube.com/watch?v=F6GSRDoB-Cg&t=74s

## Transformation

사실 이 부분은 매우 어려우며 통계쪽에서 구체적으로 다루는 편이 낫다

### 로그변환(log transformation)

Data transformation is the process of taking a mathematical function and applying it to the data. In this section we discuss a common transformation known as the log transformation. Each variable x is replaced with , where the base of the log is left up to the analyst. It is considered common to use base 10, base 2 and the natural log .
This process is useful for compressing the y-axis when plotting histograms. For example, if we have a very large range of data, then smaller values can get overwhelmed by the larger values. Taking the log of each variable enables the visualization to be clearer. An example of this is the number of ports on a system. There are 65,535 ports available on a system, if we are attempting to visualize traffic to all of them, then this visualization could hide values on the lower range of ports while attempting to display higher ports.
Log transformation also de-emphasizes outliers and allows us to potentially obtain a bell-shaped distribution. The idea is that taking the log of the data can restore symmetry to the data.
A log transformation is not always essential to analyzing the data. It can depend on the statistical analysis we are performing. If we are looking for outliers in our data, then a process that de-emphasizes them is not useful. If we use the transformation correctly, then we can illuminate structures in the data we may not have seen. However, we have to be careful on the data that we apply it to. If the distance between each variable is important, then taking the log of the variable skews the distance. Always carefully consider the log transformation and why it is being used before applying it.

**왜 로그변환을 하는 가?**

- **단위문제(Scaling)** : 집값, 재산보유액 같이 숫자가 큰 데이터를 **정규분포 형태로 바꾸기** 위해 로그 변환을 한다. 
  
  + 단위가 너무 큰 값의 경우 로그를 취해서 회귀분석을 시행한다.
  + feature와 타겟의 변화관계에서 절대량이 아닌 비율을 확인한다.

- **선형변환문제** : 비선형 관계를 선형관계로 바꾸기 위해 자연로그를 취한다.

**로그변환을 판단하는 시점**

- 보통은 EDA 이전에 수치가 가지는 의미만 확인해도 로그변환을 할지 안할지 각이 나온다.
- 검정 방법을 통해 데이터의 정규성을 확인한다.[데이터의 정규성을 확인하는 6가지 방법](https://towardsdatascience.com/6-ways-to-test-for-a-normal-distribution-which-one-to-use-9dcf47d8fa93)
  + Histogram
  + QQ plot
  + 
- QQ 정규성 검정

- SQL 코드

- Python 코드

```python
np.log10(100)
2.0
np.log2(16)
4.0
np.log(1000)
6.907755278982137
```

![](https://t1.daumcdn.net/cfile/tistory/2249D13F55BCB67C17)

# Dimension Reduction(Feature Extraction)

- 

# Feature Selection

Encoding과 기본적인 Scaling 이후의 작업을 다룬다.

https://machinelearningmastery.com/feature-selection-with-real-and-categorical-data/



## 상호작용과 다항식

### Polynomial Regrssion



## 일변량비선형 변환과 로그변환

## Feature 수 줄이기

### 일변량 통계(SelectKbest)

일변량통계는 그냥 ANOVA이다



# Pipeline

## Pipeline Neat

https://towardsdatascience.com/how-to-use-sklearn-pipelines-for-ridiculously-neat-code-a61ab66ca90d

- column datatype 별 pipeline 생성

```python
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.pipeline import Pipeline

numeric_pipeline = Pipeline(steps=[
    ('impute', SimpleImputer(strategy='mean')),
    ('scale', MinMaxScaler())
])

categorical_pipeline = Pipeline(steps=[
    ('impute', SimpleImputer(strategy='most_frequent')),
    ('one-hot', OneHotEncoder(handle_unknown='ignore', sparse=False))
])
```

- numeric pipeline을 활용한 변환

```python
numeric_pipeline.fit_transform(X_train.select_dtypes(include='number'))
```

- ColumnTransformer

```python
from sklearn.compose import ColumnTransformer

full_processor = ColumnTransformer(transformers=[
    ('number', numeric_pipeline, numerical_features),
    ('category', categorical_pipeline, categorical_features)
])
```

### Pipeline for NLP

https://towardsdatascience.com/getting-the-most-out-of-scikit-learn-pipelines-c2afc4410f1a

<!--stackedit_data:
eyJoaXN0b3J5IjpbNzEwODQ0ODcwXX0=
-->

## Utility functions

#### dataframe

```python
# input - df: a Dataframe, chunkSize: the chunk size
# output - a list of DataFrame
# purpose - splits the DataFrame into smaller chunks
def split_dataframe(df, chunk_size = 10000): 
    chunks = list()
    num_chunks = len(df) // chunk_size + 1
    for i in range(num_chunks):
        chunks.append(df[i*chunk_size:(i+1)*chunk_size])
    return chunks
```