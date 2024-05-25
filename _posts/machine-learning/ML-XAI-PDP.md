---
title: '[XAI]PDP Plot의 이해와 구현'
categories:
  - Machine Learning
date:
updated:
tags: 
  - XAI
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

## PDP plot

---
**_Concept_**

- **ICE(Indivisual Conditional Expectation)** :하나의 관측치에 대해 특정 feature의 값을 변화시킬 때 모델의 예측.
- **marginal effect** :독립변수의 변화예 따른 종속변수의 변화
- **Partial Dependence Plot** : 1개나 2개의 특성의 변화(상호작용)에 따른 모델 예측의 변화를 그린 것.

---

>The partial dependence plot (short PDP or PD plot) shows the marginal effect one or two features have on the predicted outcome of a machine learning model (J. H. Friedman 200130). A partial dependence plot can show whether the relationship between the target and a feature is linear, monotonic or more complex. 

- feature가 모델에 미치는 긍정적/부정적 영향 확인
- 특정 feture에 대해 여유분(buffer)을 함께 표시 -> feature간 독립을 보장하지 못하는 환경에서 모델에 어느정도 있을 수 있는 지를 확인할 수 있게끔 함

### 기본적인 컨셉에 대한 이해

$$\hat{f}_S(x_S)=E_{X_C}\left[\hat{f}(x_S,X_C)\right]=\int\hat{f}(x_S,X_C)d\mathbb{P}(X_C)$$

$$\hat{f}_S(x_S)=\frac{1}{n}\sum_{i=1}^n\hat{f}(x_S,x^{(i)}_{C})$$


- $X_S$는 분석하고자 하는 feature이다.
- $X_C$는 분석하고자 하는 feauture 외의 모델의 feauture들이다.
- 여기서 $f(x_{S}, x_{C}^{(i)})$ 가 하나의 ICE 곡선을 나타낸다.
- Partial Dependence는 단순히 $X_C$를 를 고정시킨 상태에서 $X_S$를 변화시키며 모델의 예측값을 계산 후 그 값을 평균한 것이다.
- **target과 관련이 있는 특성에 대한 Global한 설명이 필요할 때 사용한다.**


### ICE(Indivisual Conditional Expectation)

- ICE 곡선은 하나의 관측치에 대해 관심 특성을 변화시킴에 따른 타겟값 변화 곡선. 
- PDP는 기본적으로 여러 ICE곡선의 평균이다.
- `frac_to_plot` : 라인 수 조정 파라미터. 라인 수 혹은 비율

- **ICE와 PDF에 대한 직관적 이해** : https://twitter.com/i/status/1066398522608635904


- 부분 의존성 계산 및 PDP plot 그리기

```python

ice = pdp.pdp_isolate(
      model = clf,
      dataset = df,
      model_features=features
      feature = "feature_1" # 분석하고자 하는 feature
        )

# PDP plot

fig, axes = pdp.pdp_plot(
            ice,
            "feature_1",
            plot_line = False,
            frac_to_plot = 0.5,
            plot_pts_dist = True
                         )
```



### PDP interaction

- 두 특성간 상호작용 확인
- 등고선 그래프를 그렸을 때 특정 축에 평행할 경우 다른 축의 값에 상관없이 
  + X축에 평행할 경우 모델의 예측 X축의 변수에 보다 의존적.
  + Y축의 변수의 값에 상관없이 X축의 값에 따라 모델 예측이 결정됨 
- 해석하기에는 Grid로 그래프를 그리는 것이 더 나을 수 있다. 

- skearn으로 구현한 등고선 그래프
![ICE](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_003.png)

- pdp plot 패키지로 구현한 상호작용
  + 모델이 없이 두 feature의 상호작용에 따른 target의 값을 보여준다.

```python
from pdpbox import info_plots, get_dataset

test_titanic = get_dataset.titanic()
titanic_data = test_titanic['data']
titanic_target = test_titanic['target']

fig, axes, summary_df = info_plots.target_plot_interact(
    df=titanic_data, features=['Sex', ['Embarked_C', 'Embarked_Q', 'Embarked_S']],
    feature_names=['Sex', 'Embarked'], target=titanic_target)

```


### PDP plot에서 범주형 변수 Decoding하기

- 범주형 변수는 Ordinal Encoder나 target Encoder로 인코딩 한 후 사용된다.
- 인코딩을 하게되면 학습 후 PDP 를 그릴 때 인코딩된 값이 나오게 되어 카테고리특성의 실제 값을 확인하기 어려운 문제가 있다.

```python

import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline

df = sns.load_dataset('titanic')
df['age'] = df['age'].fillna(df['age'].median())
df = df.drop(columns='deck') # NaN 77%
df = df.dropna()

target = 'survived'
features = df.columns.drop(['survived', 'alive'])

X = df[features]
y = df[target]

# 파이프라인 생성 및 학습
pipe = make_pipeline(
    OrdinalEncoder(), 
    RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
)
pipe.fit(X, y);

# 
encoder = pipe.named_steps['ordinalencoder']
X_encoded = encoder.fit_transform(X)
rf = pipe.named_steps['randomforestclassifier']

```
 
- 범주형 변수에 대한 ice plot

```python
import matplotlib.pyplot as plt
from pdpbox import pdp
feature = 'sex'
pdp_dist = pdp.pdp_isolate(model=rf, dataset=X_encoded, model_features=features, feature=feature)
pdp.pdp_plot(pdp_dist, feature); # 인코딩된 sex 값을 확인할 수 있습니다
```

- 자동으로 PDP 카테고리 매핑

```python
# 이번에는 PDP 카테고리값 맵핑을 자동으로 해보겠습니다

feature = 'sex'
for item in encoder.mapping:
    if item['col'] == feature:
        feature_mapping = item['mapping'] # Series
        
feature_mapping = feature_mapping[feature_mapping.index.dropna()]
category_names = feature_mapping.index.tolist()
category_codes = feature_mapping.values.tolist()


pdp.pdp_plot(pdp_dist, feature)

# xticks labels 설정을 위한 리스트를 직접 넣지 않아도 됩니다 
plt.xticks(category_codes, category_names);

```

- PDP 상호작용 

```python
# 2D PDP 를 Seaborn Heatmap으로 그리기 위해 데이터프레임으로 만듭니다
pdp = interaction.pdp.pivot_table(
    values='preds', 
    columns=features[0], 
    index=features[1]
)[::-1]

pdp = pdp.rename(columns=dict(zip(category_codes, category_names)))
plt.figure(figsize=(6,5))
sns.heatmap(pdp, annot=True, fmt='.2f', cmap='viridis')
plt.title('PDP decoded categorical');
```


**References & annotation**

- https://pdpbox.readthedocs.io/en/latest/index.html
- https://christophm.github.io/interpretable-ml-book/pdp.html
- https://scikit-learn.org/stable/modules/partial_dependence.html

