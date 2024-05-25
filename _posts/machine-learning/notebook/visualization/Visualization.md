# 문서 분리 기준

- H1 기준으로 문서 분리
- 번호 붙일 것


# 이 문서에 넣을 것들

- 시각화 코드 전부
- toobox에 visualization에도 전부 넣기
  --

EDA는 기본적으로 데이터를 처음 받았을 때 하는 일들이다.
데이터 전처리랑 겹치는 부분이 있다.
EDA는 시각화와 관련이 있다.

시각화는 분석전후에도 쓰인다.

여기에는 시각화 관련 전반적인 내용과 시각화 중심의 EDA를 기록한다,

**무지성카피**

# 데이터를 보고나서 해야할 것

**long 형태로 바꿀 수 있는 데이터라면 반드시 long 형태로 바꾼다.**

# 분석과정중의 시각화

## 사전작업

## **pandas 함수들 (pandas utility)**

> 주요 pandas 함수 기능 정리

- shape : DF 차원 파악

#### Visualization(나중에 옮길것)

- plot
- plot.area
- plot.bar
- plot.barh
- plot.box
- plot.density
- plot.hexbin
- plot.hist
- plot.kde
- plot.line
- plot.pie
- plot.scatter

### 한글폰트 설정하기

- 한글폰트 시각화 관련

```python
# 다른 노트북 작성할 때도 이 셀만 떼서 사용 가능하다.
import matplotlib.pyplot as plt 
import platform                

# 웬만하면 해주는 것이 좋다.
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus']= False

if platform.system() == 'Darwin': # 맥os 사용자의 경우에
    plt.style.use('seaborn-darkgrid') 
    rc('font', family = 'AppleGothic')

elif platform.system() == 'Windows':# 윈도우 사용자의 경우에
    path = 'c:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=path).get_name()
    plt.style.use('seaborn-darkgrid') # https://python-graph-gallery.com/199-matplotlib-style-sheets/
    rc('font', family=font_name)
```

- colab 한글폰트 시각화 관련

```shell
# 이후 런타임 재시작
!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf
```

이후 폰트를 나눔폰트로 바꾼다.

```python
import matplotlib.pyplot as plt

plt.rc('font', family='NanumBarunGothic') 
```

## plotting

## x범주형 y

### bar chart

### correlation plot

### raincloudplot

- **기본적으로 분포를 보기위한 차트**

**tools**

- https://mjskay.github.io/ggdist/

- https://github.com/pog87/PtitPrince # 파이썬 버전

- https://github.com/RainCloudPlots/RainCloudPlots

- 기본 베이스는 이거고 여기서 옵션 조절해가며 그릴 것

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="darkgrid")
sns.set(style="whitegrid")
sns.set_style("white")
sns.set(style="whitegrid",font_scale=2) # 조절 가능
import matplotlib.collections as clt
import ptitprince as pt # raincloud function

dx="group"; dy="score"; dhue = "gr2"; ort="h"; pal = "Set2"; sigma = .2
f, ax = plt.subplots(figsize=(12, 5)) # 조절가능

ax=pt.RainCloud(x = dx, y = dy, hue = dhue, data = df, palette = pal, bw = sigma, width_viol = .7,
                ax = ax, orient = ort , alpha = .65, dodge = True, pointplot = True, move = .2)

plt.title("Figure P18\n Shifting the Rain with the Move Parameter")
```

# 분석 이후의 시각화

## 예측

### 회귀 시각화

- 신뢰구간을 포함한 단순선형회귀

```python
import seaborn as sns
sns.regplot(x=train['GrLivArea'], y=train['SalePrice']).set_title('Housing Prices');
```

- 2d 선형회귀직선과 제곱오차(squared errors)를 확인하기 위한 함수.

```python
from IPython.display import display
from matplotlib.patches import Rectangle

def eval_metrics(df, feature, target, slope, intercept):
    """
    2d 선형회귀직선과 제곱오차(squared errors)를 확인하기 위한 함수
    df : Pandas 데이터프레임
    feature : 특징 열
    target : 타겟 열
    slope : 선형방정식의 기울기
    intercept : 선형방정식의 y 절편
    """

    x = df[feature]
    y = df[target]

    # plot 데이터
    ax = plt.axes()
    df.plot.scatter(feature, target, ax=ax)

    # 예측
    y_pred = slope * x + intercept

    # plot 예측
    ax.plot(x, y_pred)

    # Plot 제곱오차(MSE)
    x_left, x_right = ax.get_xlim() # x-axis view limits
    y_bottom, y_top = ax.get_ylim()
    scale = (x_right - x_left) / (y_top - y_bottom)

    for f, t, p in zip(x, y, y_pred):
        xy = (f, min(t, p))
        h = abs(t - p)
        w_scaled = h * scale
        ax.add_patch(Rectangle(xy=xy, width=w_scaled, height=h, alpha=0.2))

    # 회귀방정식 평가지표
    mse = mean_squared_error(y, y_pred)
    mae = mean_absolute_error(y, y_pred)
    rmse = mse ** 0.5
    r2 = r2_score(y, y_pred)

    display(pd.DataFrame([['MSE', mse],['MAE', mae],['RMSE', rmse],['R2', r2]], columns=['Metric', 'Score']))
```

## 트리

### dtreeviz를 활용한 tree시각화

-[깃허브 링크](https://github.com/parrt/dtreeviz)

**Code from TowardDS**

- setup

```python
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris, load_boston
from sklearn import tree

from dtreeviz.trees import *


# load the two data sets  
iris = load_iris()
boston = load_boston()
```

- old way

```python
# prepare the data
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# fit the classifier
clf = tree.DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X_train, y_train)


tree.plot_tree(clf); # this old way
```

- Decision Tree의 Class Labeling (색칠하기)

```python
tree.plot_tree(clf,
               feature_names = iris.feature_names, 
               class_names=iris.target_names,
               rounded=True, 
               filled = True);
```

- dtreeviz in action

```python
viz = dtreeviz(clf, 
               x_data=X_train,
               y_data=y_train,
               target_name='class',
               feature_names=iris.feature_names, 
               class_names=list(iris.target_names), 
               title="Decision Tree - Iris data set")
viz
```

![](https://miro.medium.com/max/1050/1*iiYZWUlZyCvvNahmcVT1XA.png)

- highlight the path of first obervation of the test set

```python
viz = dtreeviz(clf, 
               x_data=X_train,
               y_data=y_train,
               target_name='class',
               feature_names=iris.feature_names, 
               class_names=list(iris.target_names),
               title="Decision Tree - Iris data set",
               [[orientation]]="LR", 
               X=X_test[0])  
viz
```

- Regression example
- 회귀분석

```python
# prepare the data
X = boston.data
y = boston.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# fir the regressor
reg = tree.DecisionTreeRegressor(max_depth=2, random_state=42)
reg.fit(X_train, y_train)

# plot the tree
viz = dtreeviz(reg,
               x_data=X_train,
               y_data=y_train,
               target_name='price',
               feature_names=boston.feature_names,
               title="Decision Tree - Boston housing",
               show_node_labels = True)
```

![](https://miro.medium.com/max/1050/1*XN54CVrnWqtn4GRs_ij2yQ.png)

#### Regression_Tree

- Wine Dataset Regression Visualization

```python
features = wine.drop('quality',axis=1)
target = wine['quality']

# Regression tree on Wine data
fig = plt.figure(figsize=(25,20))
regr= tree.DecisionTreeRegressor(max_depth=3)  
regr.fit(features, target)
viz = dtreeviz(regr,
               features,
               target,
               target_name='wine quality',
               feature_names=features.columns,
               title="Wine data set regression",
               fontname="Arial",
               colors = {"title":"purple"},
               scale=1.5)
viz
```

![](https://miro.medium.com/max/1050/1*qzLs2IBAYSEJwycZ0rc7mg.png)

#### Classification_Tree

- Wine Dataset Classification Visualization

```python
fig = plt.figure(figsize=(25,20))
clf = tree.DecisionTreeClassifier(max_depth=3)
clf.fit(features, target)
# pick random X observation for demo
X = features.iloc[np.random.randint(0, len(features)),:].values
viz = dtreeviz(clf,
               features,
               target,
               target_name='wine quality',
               feature_names=features.columns,
               title="Wine data set classification",
               class_names=['5', '6', '7', '4', '8', '3'],
               scale=1.3,
               X=X)
viz
```

#### Prediction Path

```python
regr = tree.DecisionTreeRegressor(max_depth=2)  # limit depth of tree
diabetes = load_diabetes()
regr.fit(diabetes.data, diabetes.target)
X = diabetes.data[np.random.randint(0, len(diabetes.data)),:]  # random sample from training

viz = dtreeviz(regr,
               diabetes.data, 
               diabetes.target, 
               target_name='value', 
               orientation ='LR',  # left-right orientation
               feature_names=diabetes.feature_names,
               X=X)  # need to give single observation for prediction

viz.view()  
```

If you want to visualize just the prediction path, you need to set parameter show_just_path=True

```python
dtreeviz(regr,
        diabetes.data, 
        diabetes.target, 
        target_name='value', 
        orientation ='TD',  # top-down orientation
        feature_names=diabetes.feature_names,
        X=X, # need to give single observation for prediction
        show_just_path=True     
        )
```

**Explain Prediction Path**

```python
X = dataset[features].iloc[10]
print(X)
Pclass              3.0
Age                 4.0
Fare               16.7
Sex_label           0.0
Cabin_label       145.0
Embarked_label      2.0

print(explain_prediction_path(tree_classifier, X, feature_names=features, explanation_type="plain_english"))
2.5 <= Pclass 
Age < 36.5
Fare < 23.35
Sex_label < 0.5
```

#### Regression with univariate feature-target space

```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from dtreeviz.trees import *

df_cars = pd.read_csv("cars.csv")
X, y = df_cars[['WGT']], df_cars['MPG']

dt = DecisionTreeRegressor(max_depth=3, criterion="mae")
dt.fit(X, y)

fig = plt.figure()
ax = fig.gca()
rtreeviz_univar(dt, X, y, 'WGT', 'MPG', ax=ax)
plt.show()
```

![](https://user-images.githubusercontent.com/178777/49105092-9b264d80-f234-11e8-9d67-cc58c47016ca.png)

#### Regression bivariate feature-target space

<img src="https://user-images.githubusercontent.com/178777/49104999-4edb0d80-f234-11e8-9010-73b7c0ba5fb9.png" width="30%">

```python
from mpl_toolkits.mplot3d import Axes3D
from sklearn.tree import DecisionTreeRegressor
from dtreeviz.trees import *

df_cars = pd.read_csv("cars.csv")
X = df_cars[['WGT','ENG']]
y = df_cars['MPG']

dt = DecisionTreeRegressor(max_depth=3, criterion="mae")
dt.fit(X, y)

figsize = (6,5)
fig = plt.figure(figsize=figsize)
ax = fig.add_subplot(111, projection='3d')

t = rtreeviz_bivar_3D(dt,
                      X, y,
                      feature_names=['Vehicle Weight', 'Horse Power'],
                      target_name='MPG',
                      fontsize=14,
                      elev=20,
                      azim=25,
                      dist=8.2,
                      show={'splits','title'},
                      ax=ax)
plt.show()
```

#### Regression bivariate feature-target space heatmap

<img src="https://user-images.githubusercontent.com/178777/49107627-08d57800-f23b-11e8-85a2-ab5894055092.png" width="30%">

```python
from sklearn.tree import DecisionTreeRegressor
from dtreeviz.trees import *

df_cars = pd.read_csv("cars.csv")
X = df_cars[['WGT','ENG']]
y = df_cars['MPG']

dt = DecisionTreeRegressor(max_depth=3, criterion="mae")
dt.fit(X, y)

t = rtreeviz_bivar_heatmap(dt,
                           X, y,
                           feature_names=['Vehicle Weight', 'Horse Power'],
                           fontsize=14)

plt.show()
```

=======

Highlights the decision nodes in which the feature value of single observation passed in argument X falls. Gives feature values of the observation and highlights features which are used by tree to traverse path.

```python
regr = tree.DecisionTreeRegressor(max_depth=2)  # limit depth of tree
diabetes = load_diabetes()
regr.fit(diabetes.data, diabetes.target)
X = diabetes.data[np.random.randint(0, len(diabetes.data)),:]  # random sample from training

viz = dtreeviz(regr,
               diabetes.data, 
               diabetes.target, 
               target_name='value', 
               orientation ='LR',  # left-right orientation
               feature_names=diabetes.feature_names,
               X=X)  # need to give single observation for prediction

viz.view()  
```

If you want to visualize just the prediction path, you need to set parameter show_just_path=True

```python
dtreeviz(regr,
        diabetes.data, 
        diabetes.target, 
        target_name='value', 
        orientation ='TD',  # top-down orientation
        feature_names=diabetes.feature_names,
        X=X, # need to give single observation for prediction
        show_just_path=True     
        )
```

**Explain Prediction Path**

```python
X = dataset[features].iloc[10]
print(X)
Pclass              3.0
Age                 4.0
Fare               16.7
Sex_label           0.0
Cabin_label       145.0
Embarked_label      2.0

print(explain_prediction_path(tree_classifier, X, feature_names=features, explanation_type="plain_english"))
2.5 <= Pclass 
Age < 36.5
Fare < 23.35
Sex_label < 0.5
```

#### Regression with univariate feature-target space

```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from dtreeviz.trees import *

df_cars = pd.read_csv("cars.csv")
X, y = df_cars[['WGT']], df_cars['MPG']

dt = DecisionTreeRegressor(max_depth=3, criterion="mae")
dt.fit(X, y)

fig = plt.figure()
ax = fig.gca()
rtreeviz_univar(dt, X, y, 'WGT', 'MPG', ax=ax)
plt.show()
```

![](https://user-images.githubusercontent.com/178777/49105092-9b264d80-f234-11e8-9d67-cc58c47016ca.png)

#### Regression bivariate feature-target space

<img src="https://user-images.githubusercontent.com/178777/49104999-4edb0d80-f234-11e8-9010-73b7c0ba5fb9.png" width="30%">

```python
from mpl_toolkits.mplot3d import Axes3D
from sklearn.tree import DecisionTreeRegressor
from dtreeviz.trees import *

df_cars = pd.read_csv("cars.csv")
X = df_cars[['WGT','ENG']]
y = df_cars['MPG']

dt = DecisionTreeRegressor(max_depth=3, criterion="mae")
dt.fit(X, y)

figsize = (6,5)
fig = plt.figure(figsize=figsize)
ax = fig.add_subplot(111, projection='3d')

t = rtreeviz_bivar_3D(dt,
                      X, y,
                      feature_names=['Vehicle Weight', 'Horse Power'],
                      target_name='MPG',
                      fontsize=14,
                      elev=20,
                      azim=25,
                      dist=8.2,
                      show={'splits','title'},
                      ax=ax)
plt.show()
```

#### Regression bivariate feature-target space heatmap

<img src="https://user-images.githubusercontent.com/178777/49107627-08d57800-f23b-11e8-85a2-ab5894055092.png" width="30%">

```python
from sklearn.tree import DecisionTreeRegressor
from dtreeviz.trees import *

df_cars = pd.read_csv("cars.csv")
X = df_cars[['WGT','ENG']]
y = df_cars['MPG']

dt = DecisionTreeRegressor(max_depth=3, criterion="mae")
dt.fit(X, y)

t = rtreeviz_bivar_heatmap(dt,
                           X, y,
                           feature_names=['Vehicle Weight', 'Horse Power'],
                           fontsize=14)

plt.show()
```

> > > > > > > 2392348623ab026ecc187a8b50d9619895c682ae

#### Classification univariate feature-target space

<img src="https://user-images.githubusercontent.com/178777/49105084-9497d600-f234-11e8-9097-56835558c1a6.png" width="30%">

```python
from sklearn.tree import DecisionTreeClassifier
from dtreeviz.trees import *

know = pd.read_csv("knowledge.csv")
class_names = ['very_low', 'Low', 'Middle', 'High']
know['UNS'] = know['UNS'].map({n: i for i, n in enumerate(class_names)})

X = know[['PEG']]
y = know['UNS']

dt = DecisionTreeClassifier(max_depth=3)
dt.fit(X, y)

ct = ctreeviz_univar(dt, X, y,
                     feature_names = ['PEG'],
                     class_names=class_names,
                     target_name='Knowledge',
                     nbins=40, gtype='strip',
                     show={'splits','title'})
plt.tight_layout()
plt.show()
```

#### Classification bivariate feature-target space

<img src="https://user-images.githubusercontent.com/178777/49105085-9792c680-f234-11e8-8af5-bc2fde950ab1.png" width="30%">

```python
from sklearn.tree import DecisionTreeClassifier
from dtreeviz.trees import *

know = pd.read_csv("knowledge.csv")
print(know)
class_names = ['very_low', 'Low', 'Middle', 'High']
know['UNS'] = know['UNS'].map({n: i for i, n in enumerate(class_names)})

X = know[['PEG','LPR']]
y = know['UNS']

dt = DecisionTreeClassifier(max_depth=3)
dt.fit(X, y)

ct = ctreeviz_bivar(dt, X, y,
                    feature_names = ['PEG','LPR'],
                    class_names=class_names,
                    target_name='Knowledge')
plt.tight_layout()
plt.show()
```

#### Classification boundaries in feature space

- https://github.com/parrt/dtreeviz/blob/master/README.md

```python
clfviz(rf, X, y, feature_names=['x1', 'x2'], markers=['o','X','s','D'], target_name='smiley')
```

![](https://user-images.githubusercontent.com/178777/113516349-a12c4780-952e-11eb-86f3-0ae457eb500f.png)

## XAI

# 그래프 관련 이슈들

## 컬러 팔레트

- https://blog.datawrapper.de/which-color-scale-to-use-in-data-vis/

- https://seaborn.pydata.org/tutorial/color_palettes.html

- https://www.omnisci.com/blog/12-color-palettes-for-telling-better-stories-with-your-data

- 차트에 컬러 팔렛 적용하기
  
  ```python
  
  ```

import seaborn as sns
import matplotlib.pyplot as plt

five_thirty_eight = [
    "#30a2da",
    "#fc4f30",
    "#e5ae38",
    "#6d904f",
    "#8b8b8b",
]

sns.set_palette(five_thirty_eight)
sns.palplot(sns.color_palette())
plt.show(




### Categorical Palettes

### Sequential Palettes

### Diverging Palettes


## 축 이슈

### 축에 있는 label 겹칠경우(overlapping) 해결법(seaborn)


https://stackoverflow.com/questions/42528921/how-to-prevent-overlapping-x-axis-labels-in-sns-countplot



```
