cross validation

grid search

evaluation



# Model Evaluation and Optimization(평가지표와 성능향상)

- 편향-분산 트레이드오프와 모델 일반화
- 교차검증
- 과적합 방지를 위한 규제
- 평가지표(회귀,분류)

## 편향-분산 트레이드오프와 모델 일반화

---

**_Concept_**

- **분산(Variance)** : 모델을 여러번 훈련했을 때 특정 샘플에 대한 **예측의 일관성 문제**. 모델이 무작위성에 얼마나 민감한지(robustness)를 측정
- **편향(Bias)** : **모델 자체의 구조적 에러의 문제**.다른 훈련 데이터 셋에서 여러번 훈련했을 때 예측이 참값에서 얼마나 벗어나 있는지를 측정
- **일반화(generalization)** : 모델을 연구실 밖의 데이터에 적용시킬 수 있냐의 문제.
- **과적합(Overfitting)** : **분산이 큰 것**.모델이 훈련데이터의 특징을 과하게 학습해 일반화를 못해 테스트데이터에서 오차가 커지는 것
- **과소적합(Underfitting)** : **편향이 큰 것**. 훈련데이터에 과적합도 못하고 일반화 성질도 학습하지 못해, 훈련/테스트 데이터 모두에서 오차가 크게 나오는 경우
- **학습 곡선(Learning Curve)** : 훈련/검증 데이터의 양에 대해 모델의 성능 변화(loss,accuracy)를 차트화한 것.

---

### 편향-분산 트레이드오프(Bias-Variance tradeoff)

- 분산은 모델을 여러 데이터에 대해 적용했을 때의 **신뢰도**의 문제이다.

- 편향은 모델 자체의 **타당도**의 문제이다.

- 편향과 분산은 기본적으로 트레이드 오프 관계에 있다.

- Variance는 특정 input에 대한 모델의 

![](https://jakevdp.github.io/PythonDataScienceHandbook/figures/05.03-validation-curve.png)

### 머신러닝의 일반화

> 기본적으로 이상적인 모델은 학습데이터의 패턴을 정확하게 잡아내면서도 학습되지 않은 데이터를 잘 일반화할 수 있는 모델이다.

**일반화(generalization)** 

- 훈련데이터와 테스트 데이터 모두 좋은 성능을 내는 모델은 **일반화가 잘 된 모델**이라고 부른다.
- 테스트데이터에서 만들어내는 오차는 **일반화** 오차이다.

### 학습곡선

- 학습곡선(learning curve)은 훈련 데이터의 양에 대해, 모델의 성능 변화를 플롯
  즉, 훈련 데이터에 대한 모델의 성능과 검증 데이터에 대한 모델의 성능이 훈련 데이터의 양에 따라 어떻게 변화해가는지를 표시한 그래프.

The learning curve is a great tool that you should have in your machine learning toolkit. It can be used to see **how much your model benefits from adding more training data. Sometimes, adding more data will benefit the model to generalize to new input data.** Generally, the cross-validation procedure is taken into effect when plotting the learning curve to avoid the effect of the random data splitting process.

#### 학습곡선의 해석

- Overfitting

- Underfitting
  Underfitting occurs when the model is not able to obtain a sufficiently low error value on the training set.

- Good fit

#### 학습곡선 그리기

- [yellowbrick package](https://towardsdatascience.com/plotting-the-learning-curve-with-a-single-line-of-code-90a5bbb0f48a)

```python
# yellowbrick 
# learning curve
# RandomForest Classifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from yellowbrick.model_selection import learning_curve

cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

rfc = RandomForestClassifier(n_estimators=100, max_depth=3, random_state=0)
print(learning_curve(rfc, X, y, cv=10, scoring='accuracy'))
```

- [sklearn 버전의 학습곡선 그리기](https://scikit-learn.org/stable/auto_examples/model_selection/plot_learning_curve.html)

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit

def plot_learning_curve(
    estimator,
    title,
    X,
    y,
    axes=None,
    ylim=None,
    cv=None,
    n_jobs=None,
    train_sizes=np.linspace(0.1, 1.0, 5),
):
    """
    Generate 3 plots: the test and training learning curve, the training
    samples vs fit times curve, the fit times vs score curve.

    Parameters
    ----------
    estimator : estimator instance
        An estimator instance implementing `fit` and `predict` methods which
        will be cloned for each validation.

    title : str
        Title for the chart.

    X : array-like of shape (n_samples, n_features)
        Training vector, where ``n_samples`` is the number of samples and
        ``n_features`` is the number of features.

    y : array-like of shape (n_samples) or (n_samples, n_features)
        Target relative to ``X`` for classification or regression;
        None for unsupervised learning.

    axes : array-like of shape (3,), default=None
        Axes to use for plotting the curves.

    ylim : tuple of shape (2,), default=None
        Defines minimum and maximum y-values plotted, e.g. (ymin, ymax).

    cv : int, cross-validation generator or an iterable, default=None
        Determines the cross-validation splitting strategy.
        Possible inputs for cv are:

          - None, to use the default 5-fold cross-validation,
          - integer, to specify the number of folds.
          - :term:`CV splitter`,
          - An iterable yielding (train, test) splits as arrays of indices.

        For integer/None inputs, if ``y`` is binary or multiclass,
        :class:`StratifiedKFold` used. If the estimator is not a classifier
        or if ``y`` is neither binary nor multiclass, :class:`KFold` is used.

        Refer :ref:`User Guide <cross_validation>` for the various
        cross-validators that can be used here.

    n_jobs : int or None, default=None
        Number of jobs to run in parallel.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    train_sizes : array-like of shape (n_ticks,)
        Relative or absolute numbers of training examples that will be used to
        generate the learning curve. If the ``dtype`` is float, it is regarded
        as a fraction of the maximum size of the training set (that is
        determined by the selected validation method), i.e. it has to be within
        (0, 1]. Otherwise it is interpreted as absolute sizes of the training
        sets. Note that for classification the number of samples usually have
        to be big enough to contain at least one sample from each class.
        (default: np.linspace(0.1, 1.0, 5))
    """
    if axes is None:
        _, axes = plt.subplots(1, 3, figsize=(20, 5))

    axes[0].set_title(title)
    if ylim is not None:
        axes[0].set_ylim(*ylim)
    axes[0].set_xlabel("Training examples")
    axes[0].set_ylabel("Score")

    train_sizes, train_scores, test_scores, fit_times, _ = learning_curve(
        estimator,
        X,
        y,
        cv=cv,
        n_jobs=n_jobs,
        train_sizes=train_sizes,
        return_times=True,
    )
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    fit_times_mean = np.mean(fit_times, axis=1)
    fit_times_std = np.std(fit_times, axis=1)

    # Plot learning curve
    axes[0].grid()
    axes[0].fill_between(
        train_sizes,
        train_scores_mean - train_scores_std,
        train_scores_mean + train_scores_std,
        alpha=0.1,
        color="r",
    )
    axes[0].fill_between(
        train_sizes,
        test_scores_mean - test_scores_std,
        test_scores_mean + test_scores_std,
        alpha=0.1,
        color="g",
    )
    axes[0].plot(
        train_sizes, train_scores_mean, "o-", color="r", label="Training score"
    )
    axes[0].plot(
        train_sizes, test_scores_mean, "o-", color="g", label="Cross-validation score"
    )
    axes[0].legend(loc="best")

    # Plot n_samples vs fit_times
    axes[1].grid()
    axes[1].plot(train_sizes, fit_times_mean, "o-")
    axes[1].fill_between(
        train_sizes,
        fit_times_mean - fit_times_std,
        fit_times_mean + fit_times_std,
        alpha=0.1,
    )
    axes[1].set_xlabel("Training examples")
    axes[1].set_ylabel("fit_times")
    axes[1].set_title("Scalability of the model")

    # Plot fit_time vs score
    axes[2].grid()
    axes[2].plot(fit_times_mean, test_scores_mean, "o-")
    axes[2].fill_between(
        fit_times_mean,
        test_scores_mean - test_scores_std,
        test_scores_mean + test_scores_std,
        alpha=0.1,
    )
    axes[2].set_xlabel("fit_times")
    axes[2].set_ylabel("Score")
    axes[2].set_title("Performance of the model")

    return plt


fig, axes = plt.subplots(3, 2, figsize=(10, 15))

X, y = load_digits(return_X_y=True)

title = "Learning Curves (Naive Bayes)"
# Cross validation with 100 iterations to get smoother mean test and train
# score curves, each time with 20% data randomly selected as a validation set.
cv = ShuffleSplit(n_splits=100, test_size=0.2, random_state=0)

estimator = GaussianNB()
plot_learning_curve(
    estimator, title, X, y, axes=axes[:, 0], ylim=(0.7, 1.01), cv=cv, n_jobs=4
)


title = r"Learning Curves (SVM, RBF kernel, $\gamma=0.001$)"
# SVC is more expensive so we do a lower number of CV iterations:
cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)
estimator = SVC(gamma=0.001)
plot_learning_curve(
    estimator, title, X, y, axes=axes[:, 1], ylim=(0.7, 1.01), cv=cv, n_jobs=4
)

plt.show()
```

- [keras를 이용한 신경망의 학습곡선 그리기](https://machinelearningmastery.com/display-deep-learning-model-training-history-in-keras/)

```python
# Visualize training history
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import numpy
# load pima indians dataset
dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]
# create model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
history = model.fit(X, Y, validation_split=0.33, epochs=150, batch_size=10, verbose=0)

def plot_history(history):
    hist = history.history

    fig = plt.figure(figsize=(12,5))
    ax = fig.add_subplot(1,2,1) # 1행 2열의 1번째
    ax.plot(hist['loss'],label='Train')
    ax.plot(hist['val_loss'],label='Val')
    ax.set_xlabel('Epoch')
    ax.set_title('Loss')
    ax.tick_params(axis='both',which='major',labelsize=14)


    ax = fig.add_subplot(1,2,2)
    ax.plot(hist['accuracy'],label='Train')
    ax.plot(hist['val_accuracy'],label='Val')
    ax.set_xlabel('Epoch')
    ax.set_title('Accuracy')
    ax.tick_params(axis='both',which='major',labelsize=14)
    plt.tight_layout()
    return plt

plot_history(history)
plt.show()
```

- greed search validatiaon curve
  + [참조](https://matthewbilyeu.com/blog/2019-02-05/validation-curve-plot-from-gridsearchcv-results)

```python
def plot_grid_search_validation_curve(grid, param_to_vary,
                                      title='Validation Curve', ylim=None,
                                      xlim=None, log=None):
    """Plots train and cross-validation scores from a GridSearchCV instance's
    best params while varying one of those params."""

    df_cv_results = pd.DataFrame(grid.cv_results_)
    train_scores_mean = df_cv_results['mean_train_score']
    valid_scores_mean = df_cv_results['mean_test_score']
    train_scores_std = df_cv_results['std_train_score']
    valid_scores_std = df_cv_results['std_test_score']

    param_cols = [c for c in df_cv_results.columns if c[:6] == 'param_']
    param_ranges = [grid.param_grid[p[6:]] for p in param_cols]
    param_ranges_lengths = [len(pr) for pr in param_ranges]

    train_scores_mean = np.array(train_scores_mean).reshape(*param_ranges_lengths)
    valid_scores_mean = np.array(valid_scores_mean).reshape(*param_ranges_lengths)
    train_scores_std = np.array(train_scores_std).reshape(*param_ranges_lengths)
    valid_scores_std = np.array(valid_scores_std).reshape(*param_ranges_lengths)

    param_to_vary_idx = param_cols.index('param_{}'.format(param_to_vary))

    slices = []
    for idx, param in enumerate(grid.best_params_):
        if (idx == param_to_vary_idx):
            slices.append(slice(None))
            continue
        best_param_val = grid.best_params_[param]
        idx_of_best_param = 0
        if isinstance(param_ranges[idx], np.ndarray):
            idx_of_best_param = param_ranges[idx].tolist().index(best_param_val)
        else:
            idx_of_best_param = param_ranges[idx].index(best_param_val)
        slices.append(idx_of_best_param)

    train_scores_mean = train_scores_mean[tuple(slices)]
    valid_scores_mean = valid_scores_mean[tuple(slices)]
    train_scores_std = train_scores_std[tuple(slices)]
    valid_scores_std = valid_scores_std[tuple(slices)]

    plt.clf()

    plt.title(title)
    plt.xlabel(param_to_vary)
    plt.ylabel('Score')

    if (ylim is None):
        plt.ylim(0.0, 1.1)
    else:
        plt.ylim(*ylim)

    if (not (xlim is None)):
        plt.xlim(*xlim)

    lw = 2

    plot_fn = plt.plot
    if log:
        plot_fn = plt.semilogx

    param_range = param_ranges[param_to_vary_idx]
    if (not isinstance(param_range[0], numbers.Number)):
        param_range = [str(x) for x in param_range]
    plot_fn(param_range, train_scores_mean, label='Training score', color='r',
            lw=lw)
    plt.fill_between(param_range, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1,
                     color='r', lw=lw)
    plot_fn(param_range, valid_scores_mean, label='Cross-validation score',
            color='b', lw=lw)
    plt.fill_between(param_range, valid_scores_mean - valid_scores_std,
                     valid_scores_mean + valid_scores_std, alpha=0.1,
                     color='b', lw=lw)

    plt.legend(loc='lower right')

    plt.show()
```

**ref**

### Validation Curve

- https://towardsdatascience.com/validation-curve-explained-plot-the-influence-of-a-single-hyperparameter-1ac4864deaf8

- Single Hyperparameter 의 영향을 검증하는 곡선

- Single Hyperparameter

Validation curve is a great tool that you should have in your machine learning toolkit. **It can be used to plot the influence of a single hyperparameter.** It should not be used to tune the model. Use a grid search or randomized search instead. When creating the curve, the cross-validation method should be considered. The interpretation is different according to the evaluation metric you select. I recommend you use the Yellobrick Python library when creating the validation curve. It is much easy to use and save a lot of time in coding. Then use that time to interpret it!

#### Validation Curve 구현

- yellowbrick
  
  ```python
  # Importing libraries
  import numpy as np
  import pandas as pd
  from sklearn.utils import shuffle
  from sklearn.ensemble import RandomForestClassifier
  from yellowbrick.model_selection import validation_curve 
  ```

df = pd.read_csv("heart_disease.csv") # Loading the data
df = shuffle(df, random_state=3) # Shuffling the data

X = df.iloc[:,:-1] # Feature matrix in pd.DataFrame format
y = df.iloc[:,-1] # Target vector in pd.Series format

# Making a Random Forest Classifier object

rf = RandomForestClassifier(n_estimators=100, criterion='gini',
                           max_depth=None, n_jobs=-1, random_state=42)

```
- [yellowbrick package](https://towardsdatascience.com/plotting-the-learning-curve-with-a-single-line-of-code-90a5bbb0f48a)

```python
# yellowbrick 
# learning curve
# RandomForest Classifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from yellowbrick.model_selection import learning_curve

cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

rfc = RandomForestClassifier(n_estimators=100, max_depth=3, random_state=0)
print(learning_curve(rfc, X, y, cv=10, scoring='accuracy'))
```

- [sklearn 버전의 학습곡선 그리기](https://scikit-learn.org/stable/auto_examples/model_selection/plot_learning_curve.html)

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit

def plot_learning_curve(
    estimator,
    title,
    X,
    y,
    axes=None,
    ylim=None,
    cv=None,
    n_jobs=None,
    train_sizes=np.linspace(0.1, 1.0, 5),
):
    """
    Generate 3 plots: the test and training learning curve, the training
    samples vs fit times curve, the fit times vs score curve.

    Parameters
    ----------
    estimator : estimator instance
        An estimator instance implementing `fit` and `predict` methods which
        will be cloned for each validation.

    title : str
        Title for the chart.

    X : array-like of shape (n_samples, n_features)
        Training vector, where ``n_samples`` is the number of samples and
        ``n_features`` is the number of features.

    y : array-like of shape (n_samples) or (n_samples, n_features)
        Target relative to ``X`` for classification or regression;
        None for unsupervised learning.

    axes : array-like of shape (3,), default=None
        Axes to use for plotting the curves.

    ylim : tuple of shape (2,), default=None
        Defines minimum and maximum y-values plotted, e.g. (ymin, ymax).

    cv : int, cross-validation generator or an iterable, default=None
        Determines the cross-validation splitting strategy.
        Possible inputs for cv are:

          - None, to use the default 5-fold cross-validation,
          - integer, to specify the number of folds.
          - :term:`CV splitter`,
          - An iterable yielding (train, test) splits as arrays of indices.

        For integer/None inputs, if ``y`` is binary or multiclass,
        :class:`StratifiedKFold` used. If the estimator is not a classifier
        or if ``y`` is neither binary nor multiclass, :class:`KFold` is used.

        Refer :ref:`User Guide <cross_validation>` for the various
        cross-validators that can be used here.

    n_jobs : int or None, default=None
        Number of jobs to run in parallel.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    train_sizes : array-like of shape (n_ticks,)
        Relative or absolute numbers of training examples that will be used to
        generate the learning curve. If the ``dtype`` is float, it is regarded
        as a fraction of the maximum size of the training set (that is
        determined by the selected validation method), i.e. it has to be within
        (0, 1]. Otherwise it is interpreted as absolute sizes of the training
        sets. Note that for classification the number of samples usually have
        to be big enough to contain at least one sample from each class.
        (default: np.linspace(0.1, 1.0, 5))
    """
    if axes is None:
        _, axes = plt.subplots(1, 3, figsize=(20, 5))

    axes[0].set_title(title)
    if ylim is not None:
        axes[0].set_ylim(*ylim)
    axes[0].set_xlabel("Training examples")
    axes[0].set_ylabel("Score")

    train_sizes, train_scores, test_scores, fit_times, _ = learning_curve(
        estimator,
        X,
        y,
        cv=cv,
        n_jobs=n_jobs,
        train_sizes=train_sizes,
        return_times=True,
    )
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    fit_times_mean = np.mean(fit_times, axis=1)
    fit_times_std = np.std(fit_times, axis=1)

    # Plot learning curve
    axes[0].grid()
    axes[0].fill_between(
        train_sizes,
        train_scores_mean - train_scores_std,
        train_scores_mean + train_scores_std,
        alpha=0.1,
        color="r",
    )
    axes[0].fill_between(
        train_sizes,
        test_scores_mean - test_scores_std,
        test_scores_mean + test_scores_std,
        alpha=0.1,
        color="g",
    )
    axes[0].plot(
        train_sizes, train_scores_mean, "o-", color="r", label="Training score"
    )
    axes[0].plot(
        train_sizes, test_scores_mean, "o-", color="g", label="Cross-validation score"
    )
    axes[0].legend(loc="best")

    # Plot n_samples vs fit_times
    axes[1].grid()
    axes[1].plot(train_sizes, fit_times_mean, "o-")
    axes[1].fill_between(
        train_sizes,
        fit_times_mean - fit_times_std,
        fit_times_mean + fit_times_std,
        alpha=0.1,
    )
    axes[1].set_xlabel("Training examples")
    axes[1].set_ylabel("fit_times")
    axes[1].set_title("Scalability of the model")

    # Plot fit_time vs score
    axes[2].grid()
    axes[2].plot(fit_times_mean, test_scores_mean, "o-")
    axes[2].fill_between(
        fit_times_mean,
        test_scores_mean - test_scores_std,
        test_scores_mean + test_scores_std,
        alpha=0.1,
    )
    axes[2].set_xlabel("fit_times")
    axes[2].set_ylabel("Score")
    axes[2].set_title("Performance of the model")

    return plt


fig, axes = plt.subplots(3, 2, figsize=(10, 15))

X, y = load_digits(return_X_y=True)

title = "Learning Curves (Naive Bayes)"
# Cross validation with 100 iterations to get smoother mean test and train
# score curves, each time with 20% data randomly selected as a validation set.
cv = ShuffleSplit(n_splits=100, test_size=0.2, random_state=0)

estimator = GaussianNB()
plot_learning_curve(
    estimator, title, X, y, axes=axes[:, 0], ylim=(0.7, 1.01), cv=cv, n_jobs=4
)

title = r"Learning Curves (SVM, RBF kernel, $\gamma=0.001$)"
# SVC is more expensive so we do a lower number of CV iterations:
cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)
estimator = SVC(gamma=0.001)
plot_learning_curve(
    estimator, title, X, y, axes=axes[:, 1], ylim=(0.7, 1.01), cv=cv, n_jobs=4
)

plt.show()
```

- [keras를 이용한 신경망의 학습곡선 그리기](https://machinelearningmastery.com/display-deep-learning-model-training-history-in-keras/)

```python
# Visualize training history
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import numpy
# load pima indians dataset
dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]
# create model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
history = model.fit(X, Y, validation_split=0.33, epochs=150, batch_size=10, verbose=0)

def plot_history(history):
    hist = history.history

    fig = plt.figure(figsize=(12,5))
    ax = fig.add_subplot(1,2,1) # 1행 2열의 1번째
    ax.plot(hist['loss'],label='Train')
    ax.plot(hist['val_loss'],label='Val')
    ax.set_xlabel('Epoch')
    ax.set_title('Loss')
    ax.tick_params(axis='both',which='major',labelsize=14)


    ax = fig.add_subplot(1,2,2)
    ax.plot(hist['accuracy'],label='Train')
    ax.plot(hist['val_accuracy'],label='Val')
    ax.set_xlabel('Epoch')
    ax.set_title('Accuracy')
    ax.tick_params(axis='both',which='major',labelsize=14)
    plt.tight_layout()
    return plt

plot_history(history)
plt.show()
```

- greed search validatiaon curve
  
  + [참조](https://matthewbilyeu.com/blog/2019-02-05/validation-curve-plot-from-gridsearchcv-results)
    
    ```python
    def plot_grid_search_validation_curve(grid, param_to_vary,
                                    title='Validation Curve', ylim=None,
                                    xlim=None, log=None):
    """Plots train and cross-validation scores from a GridSearchCV instance's
    best params while varying one of those params."""
    
    df_cv_results = pd.DataFrame(grid.cv_results_)
    train_scores_mean = df_cv_results['mean_train_score']
    valid_scores_mean = df_cv_results['mean_test_score']
    train_scores_std = df_cv_results['std_train_score']
    valid_scores_std = df_cv_results['std_test_score']
    
    param_cols = [c for c in df_cv_results.columns if c[:6] == 'param_']
    param_ranges = [grid.param_grid[p[6:]] for p in param_cols]
    param_ranges_lengths = [len(pr) for pr in param_ranges]
    
    train_scores_mean = np.array(train_scores_mean).reshape(*param_ranges_lengths)
    valid_scores_mean = np.array(valid_scores_mean).reshape(*param_ranges_lengths)
    train_scores_std = np.array(train_scores_std).reshape(*param_ranges_lengths)
    valid_scores_std = np.array(valid_scores_std).reshape(*param_ranges_lengths)
    
    param_to_vary_idx = param_cols.index('param_{}'.format(param_to_vary))
    
    slices = []
    for idx, param in enumerate(grid.best_params_):
      if (idx == param_to_vary_idx):
          slices.append(slice(None))
          continue
      best_param_val = grid.best_params_[param]
      idx_of_best_param = 0
      if isinstance(param_ranges[idx], np.ndarray):
          idx_of_best_param = param_ranges[idx].tolist().index(best_param_val)
      else:
          idx_of_best_param = param_ranges[idx].index(best_param_val)
      slices.append(idx_of_best_param)
    
    train_scores_mean = train_scores_mean[tuple(slices)]
    valid_scores_mean = valid_scores_mean[tuple(slices)]
    train_scores_std = train_scores_std[tuple(slices)]
    valid_scores_std = valid_scores_std[tuple(slices)]
    
    plt.clf()
    
    plt.title(title)
    plt.xlabel(param_to_vary)
    plt.ylabel('Score')
    
    if (ylim is None):
      plt.ylim(0.0, 1.1)
    else:
      plt.ylim(*ylim)
    
    if (not (xlim is None)):
      plt.xlim(*xlim)
    
    lw = 2
    
    plot_fn = plt.plot
    if log:
      plot_fn = plt.semilogx
    
    param_range = param_ranges[param_to_vary_idx]
    if (not isinstance(param_range[0], numbers.Number)):
      param_range = [str(x) for x in param_range]
    plot_fn(param_range, train_scores_mean, label='Training score', color='r',
          lw=lw)
    plt.fill_between(param_range, train_scores_mean - train_scores_std,
                   train_scores_mean + train_scores_std, alpha=0.1,
                   color='r', lw=lw)
    plot_fn(param_range, valid_scores_mean, label='Cross-validation score',
          color='b', lw=lw)
    plt.fill_between(param_range, valid_scores_mean - valid_scores_std,
                   valid_scores_mean + valid_scores_std, alpha=0.1,
                   color='b', lw=lw)
    
    plt.legend(loc='lower right')
    
    plt.show()
    ```

**ref**

### Validation Curve

- https://towardsdatascience.com/validation-curve-explained-plot-the-influence-of-a-single-hyperparameter-1ac4864deaf8

- Single Hyperparameter 의 영향을 검증하는 곡선

- Single Hyperparameter

Validation curve is a great tool that you should have in your machine learning toolkit. **It can be used to plot the influence of a single hyperparameter.** It should not be used to tune the model. Use a grid search or randomized search instead. When creating the curve, the cross-validation method should be considered. The interpretation is different according to the evaluation metric you select. I recommend you use the Yellobrick Python library when creating the validation curve. It is much easy to use and save a lot of time in coding. Then use that time to interpret it!

#### Validation Curve 구현

- yellowbrick
  
  ```python
  # Importing libraries
  import numpy as np
  import pandas as pd
  from sklearn.utils import shuffle
  from sklearn.ensemble import RandomForestClassifier
  from yellowbrick.model_selection import validation_curve 
  ```

df = pd.read_csv("heart_disease.csv") # Loading the data
df = shuffle(df, random_state=3) # Shuffling the data

X = df.iloc[:,:-1] # Feature matrix in pd.DataFrame format
y = df.iloc[:,-1] # Target vector in pd.Series format

# Making a Random Forest Classifier object

rf = RandomForestClassifier(n_estimators=100, criterion='gini',
                           max_depth=None, n_jobs=-1, random_state=42)

# Plot the validation curve

print(validation_curve(rf, X, y, param_name="max_depth", n_jobs=-1,
      param_range=np.arange(1, 11), cv=10, scoring="accuracy"))

```
![](https://miro.medium.com/max/794/1*osvSbNCDc1alpiWGZDygyA.png)


- Underfitting: Accuracy scores of both train and test sets are low. This indicates that the model is too simple or has been regularized too much. At the max_depth values of 1 and 2, the random forests model is underfitting.
- Overfitting: The training accuracy score is very high and the accuracy score of the test set is low. The model fits very well for the training data, but it fails to generalize to new input data. For max_depth values of 4, 5, …, 10, the model is highly overfitted.
- Just-right: No overfitting or underfitting. At the max_depth value of 3, the model is just right. The model fits the training data very well and it is also generalizable to new input data. That’s what we want!

- Be careful: When you use an evaluation metric such as MSE, the overfitting condition happens when the training MSE is very low (not high) and the MSE of the test set is high (not low). This is because here we consider an error (Mean Squared Error).
- Be careful: **Here, you got the optimal max_depth hyperparameter value of 3. Keep in mind that this is what we got when we consider only the max_depth hyperparameter. When we consider several hyperparameters at a time as in Grid Search or Randomized Search, the optimal max_depth hyperparameter value will not be 3.** -> 사실상 쓸모가 없음

# Plot the validation curve
print(validation_curve(rf, X, y, param_name="max_depth", n_jobs=-1,
      param_range=np.arange(1, 11), cv=10, scoring="accuracy"))
```

![](https://miro.medium.com/max/794/1*osvSbNCDc1alpiWGZDygyA.png)

- Underfitting: Accuracy scores of both train and test sets are low. This indicates that the model is too simple or has been regularized too much. At the max_depth values of 1 and 2, the random forests model is underfitting.

- Overfitting: The training accuracy score is very high and the accuracy score of the test set is low. The model fits very well for the training data, but it fails to generalize to new input data. For max_depth values of 4, 5, …, 10, the model is highly overfitted.

- Just-right: No overfitting or underfitting. At the max_depth value of 3, the model is just right. The model fits the training data very well and it is also generalizable to new input data. That’s what we want!

- Be careful: When you use an evaluation metric such as MSE, the overfitting condition happens when the training MSE is very low (not high) and the MSE of the test set is high (not low). This is because here we consider an error (Mean Squared Error).

- Be careful: **Here, you got the optimal max_depth hyperparameter value of 3. Keep in mind that this is what we got when we consider only the max_depth hyperparameter. When we consider several hyperparameters at a time as in Grid Search or Randomized Search, the optimal max_depth hyperparameter value will not be 3.** -> 사실상 쓸모가 없음

## Cross Validation

하는 이유

- 과적합 방지
- 하이퍼 파라미터를 찾기 위해 사용
- 모든 데이터를 학습데이터로 사용 할 수 있다는 것이 장점

**CrossValidation 사용이유와 용법**

- https://modern-manual.tistory.com/20?category=902149

- https://m.blog.naver.com/ckdgus1433/221599517834

- Model Selection
  
  + Cross Validation는 기본적으로는 데이터 양이 적은 경우 학습세트를 늘리기 위한 기법이다.
  + Train-valid-test로 나누는 홀드아웃 검정의 경우 하이퍼파라미터 튜닝할 때 데이터의 일부에 튜닝할 수 있는 단점이 있다.예컨대 valid set에 관한 검증 결과 확인 후 모델 파라미터 튜닝을 하는 작업을 반복하게 되면 모델이 valid set에 대해 overfit 될 가능성이 높다는 것이 단점이다
  + Taget encoder : 성능향상에 도움이되는 인코더, 사용시 정보의 누수가 일어나지 않도록 주의

- 하이퍼파라미터 튜닝
  
  + 기본적으로 트리가 커질수록 과적합 가능성이 높아진다.
  + Max depth를 어느지점에서 결정할 지 validation cureve를 활용해야한
  + fold는 보통 5-fold이상

### K-fold

### Random Search

### Greedy Search

**그리디서치와 랜덤서치의 차이**

포인트를 정해주는것-grid seach
포인트가 포함되는 범위를 정해주는 것-random search

랜덤은 일정 범위안에서 랜덤으로 서치하는방법, 
그리드 서치는 일정 부분을 그리드처럼 지정해주어서 각각의 경우의 수만큼 찾는 방법

## HyperParameter Tuning

**읽어볼만한 자료**

- [Grid Search Hyperparameters for Deep Learning](https://machinelearningmastery.com/grid-search-hyperparameters-deep-learning-models-python-keras/)

- [Hyperparameters Optimization for Deep Learning Models](https://blog.floydhub.com/guide-to-hyperparameters-search-for-deep-learning-models/)

- [Dropout Regularization in Deep Learning](https://machinelearningmastery.com/dropout-regularization-deep-learning-models-keras/)

- [Weight Constraints in Deep Learning](https://machinelearningmastery.com/introduction-to-weight-constraints-to-reduce-generalization-error-in-deep-learning/)

- [Number of Layers and Nodes in a Neural Network](https://machinelearningmastery.com/how-to-configure-the-number-of-layers-and-nodes-in-a-neural-network/)

- [Batch Normalization](https://shuuki4.wordpress.com/2016/01/13/batch-normalization-%EC%84%A4%EB%AA%85-%EB%B0%8F-%EA%B5%AC%ED%98%84/)
+ 추가 자료
  [Hyperparameter Tuning: A Practical Guide and Template](https://towardsdatascience.com/hyperparameter-tuning-a-practical-guide-and-template-b3bf0504f095)

**Check**
Part1 : 각각에 대해서 설명할 수 있는 지, 이해되지 않은 것들은 없는지 확인해 봅시다.
    - Activation Functions
    - Optimizer
    - Number of Layers
    - Number of Neurons
    - Batch Size
    - Dropout
    - Learning Rate
    - Number of Epochs
    - and many more
Part2 : 실험 추적 프레임워크를 구현을 스스로 해볼 수 있는 지 점검합시다
    - Weights & Biases
    - Comet.ml
    - By Hand / GridSearch

Part3 : Keras Tuner 활용 파라미터 튜닝

### Keras Tuner를 활용한 튜닝

### Hyperops를 활용한 튜닝

### HyperParmeter Tuning Tips

**계속 추가할것**

- 활성화 함수로는 ReLU를 먼저 사용하는 것이 좋다.
- 가중치 초기화는 Sigmoid일 경우 Xavier, ReLU일 경우 He 초기값을 사용하는 것이 좋다.

## 평가지표(Evaluation Metrics)

### Cost Function에 대한 이해

- [Cost Function](https://www.analyticsvidhya.com/blog/2021/02/cost-function-is-no-rocket-science/)

**평균제곱계열**

- mean_squared_error (MSE) = $\frac{1}{n}\sum_{i=1}^{n}(y_{i} - \hat{y_{i}})^{2}$
- RMSE (Root Mean Squared Error) = 
  $\sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_{i} - \hat{y_{i}})^{2}}$
- mean_absolute_error (MAE) = $\frac{1}{n}\sum_{i=1}^{n}\left | y_{i} - \hat{y_{i}} \right |$
- R-Squared (coefficient of determination) = $1 - \frac{\sum_{i=1}^{n}(y_{i} - \hat{y_{i}})^{2}}{\sum_{i=1}^{n}(y_{i} - \bar{y_{i}})^{2}} = 1 - \frac{SSE}{SST} = \frac {SSR}{SST}$
  - SSE, SST, SSR: Sum of Squared `Error`, `Total`, `Regression`($\sum_{i=1}^{n}(\hat{y_{i}} - \bar{y_{i}})^{2}$)
- mean_absolute_percentage_error = $ \frac {1}{n}\sum _{i=1}^{n}\left|{\frac {y_{t}-\hat{y_{i}}}{y_{i}}}\right| $
- mean_squared_logarithmic_error = $\frac{1}{n} \sum_{i=1}^n (\log(\hat{y_i} + 1) - \log(y_i+1))^2 $

**엔트로피계열**

- binary_crossentropy = $ -\sum_{c=1}^{C} q(y_c) log(q(y_c)), \hspace{2em} q(y_c) \in (1, -1)$
- categorical_crossentropy = $ -\sum_{c=1}^{C} q(y_c)log(q(y_c)) $

### 회귀모델의 평가지표

- $R^2$ 외에, MAE는 단위 유닛이 같으므로 보다 해석에 용이함.
- MSE는 제곱을 하기 때문에 특이값에 보다 민감. 
- RMSE는 MSE를 실제값과 유사한 단위로 변화시켜줌
- 회귀문제에서 RMSE가 일반적으로 선호되는 방법이지만, 상황에 맞는 다른 방식을 사용. 특이값이 많은 경우에는 MAE를 사용

---

**_Concept_**

* MSE (Mean Squared Error) = 
  $\frac{1}{n}\sum_{i=1}^{n}(y_{i} - \hat{y_{i}})^{2}$
* MAE (Mean absolute error) = $\frac{1}{n}\sum_{i=1}^{n}\left | y_{i} - \hat{y_{i}} \right |$
* RMSE (Root Mean Squared Error) = 
  $\sqrt{MSE}$
* R-squared (Coefficient of determination) = 
  $1 - \frac{\sum_{i=1}^{n}(y_{i} - \hat{y_{i}})^{2}}{\sum_{i=1}^{n}(y_{i} - \bar{y_{i}})^{2}} = 1 - \frac{SSE}{SST} = \frac {SSR}{SST}$
* MAPE = \frac { \sum \vert \frac { y - \hat y}{y} \vert }{n}*100\%
- 참고
  - SSE(Sum of Squares `Error`, 관측치와 예측치 차이): $\sum_{i=1}^{n}(y_{i} - \hat{y_{i}})^{2}$
  - SSR(Sum of Squares due to `Regression`, 예측치와 평균 차이): $\sum_{i=1}^{n}(\hat{y_{i}} - \bar{y_{i}})^{2}$
  - SST(Sum of Squares `Total`, 관측치와 평균 차이): $\sum_{i=1}^{n}(y_{i} - \bar{y_{i}})^{2}$ , SSE + SSR

---

#### MSE

- 모델의 예측값과 실제값 차이의 면적의 합.
- 특이값이 존재할 경우 수치가 많이 늘어남

#### MAE

: mean absolute error

- MSE 보다 특이치에 robust
- 절대값을 취하기 때문에 매우 직관적

#### RMSE

- MSE의 제곱근. 
- 큰 오류값에 대해 패널티를 주기 때문에 보통 이걸 사용

#### R-squared

> R 제곱은 모델의 의해 설명된 target의 분산의 percentage를 뜻한다. 즉, 모든 데이터포인트에 대해 모델과의 거리를 제곱해서 모델로 설명되는 분산의 비율을 측정한다.

- 설명량. target(종속변수)의 전체 분산 중 feature(독립변수)로 인해 설명되는 부분
- 1 - (unexplained variance/total variance)
- $R^2$ 값이 1에 가까울 수록 데이터를 잘 설명하는 모델이 됨

#### MAPE

```python
def MAPE(y_true, y_pred): 
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
```

- MAE를 퍼센트 변환한 것.
- MAE와 마찬가지로 MSE보다 특이치에 robust하다.
- 모델에 대한 편향이 존재.
- 0 근처의 값에서는 사용하기 어렵습니다.

#### MPE

```python
def MAPE(y_true, y_pred): 
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
```

- MAPE를 퍼센트 변환한 것.
- 절대값을 제외했기 때문에 overperformance인지 underperformance인지 쉽게 알 수 있다.

**ref**

- https://www.dataquest.io/blog/understanding-regression-error-metrics/
- https://machinelearningmastery.com/regression-metrics-for-machine-learning/

### 분류모델의 평가지표

no blog

- yellowbrick library를 통한 시각화
- https://www.scikit-yb.org/en/latest/api/classifier/index.html
  + Classification Report: A visual classification report that displays precision, recall, and F1 per-class as a heatmap.
  + Confusion Matrix: A heatmap view of the confusion matrix of pairs of classes in multi-class classification.
  + ROCAUC: Graphs the receiver operating characteristics and area under the curve.
  + Precision-Recall Curves: Plots the precision and recall for different probability thresholds.
  + Class Balance: Visual inspection of the target to show the support of each class to the final estimator.
  + Class Prediction Error: An alternative to the confusion matrix that shows both support and the difference between actual and predicted classes.
  + Discrimination Threshold: Shows precision, recall, f1, and queue rate over all thresholds for binary classifiers that use a discrimination probability or score.

다중분류문제 참고

- https://moons08.github.io/datascience/classification_score_basic/

**evaluation metrics of classification model**

![](https://miro.medium.com/max/1400/1*UVP_xb4F6J-M-xH3haz5Jw.png)

#### Confustion Matrix

- 이진분류문제에 사용

![](https://miro.medium.com/max/1400/1*N6I3pi0prhiJ_Y85HAx4wA.png)

- True Positive (Hit)
- False Negative (Miss)
- True Negative  (Correct Rejection)
- False Positive (False Alarm)

#### Signal Detection Theory를 통한 이해


- **푸는 문제의 성격에 따라 사용하는  Metric이 달라진다.**

#### Accuracy

- `TP+TF/(TP)`

#### Recall

- `TP/(TP+FN)`
- How many relevent are selected
- 민감도(Sensitivity) : 기본적으로 Type2 error(Miss), False Negative를 피하는 것이 중요
- Criterion을 낮출 경우 민감도가 올라가지만 False Alarm의 확률도 동시에 올라간다.
- ex) 초기 암진단

#### Precisision

- `TP/(TP + FP)`
- How many selected are relevent
- 정밀도: 모델이 예측한 True 중 실제 True의 비율.
- 오분류의 리스크가 클 경우 사용가능한 metric
- Type1 error(False Alarm), False Positive를 피하는 것이 중요
- ex) 스팸 메일

**오분류 리스크 관점에서의 Precision과 Accuracy 비교**

![](https://www.researchgate.net/publication/336786839/figure/fig3/AS:817696958582785@1571965555479/Relative-benefits-of-risk-averse-control-based-on-model-accuracy-precision-given-an.ppm)

#### 특이도

- `TN/(FN+TN)`
- 특이도

#### F1 Score

- 민감도와 특이도의 조화평균
- F1 Score는 F_beta Score의 General 한 버전이다.
  + beta를 통해 precision 대비 recall의 비중을 정한다.
  + F1 Score는 beta가 1이기에 민감도와 특이도의 비중을 같게 버전의 F_beta Score이다.

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/136f45612c08805f4254f63d2f2524bc25075fff)

Type1,2 에러 측면에서 보면 식을 아래와 같이 바꿀 수 있다.

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/6fbeb471033fdd63a2c2ca7830afc7abdf8b8134)

fla

F-Measure provides a single score that balances both the concerns of precision and recall in one number. **A good F1 score means that you have low false positives and low false negatives**, so you’re correctly identifying real threats, and you are not disturbed by false alarms. An F1 score is considered perfect when it’s 1, while the model is a total failure when it’s 0.

#### ROC Curve

A ROC curve plots the true positive rate (tpr) versus the false positive rate (fpr) as a function of the model’s threshold for classifying a positive. Given that c is a constant known as decision threshold, the below ROC curve suggests that by default c=0.5, when c=0.2, both tpr and fpr increase. When c=0.8, both tpr and fpr decrease. In general, tpr and fpr increase as c decrease. In the extreme case when c=1, all cases are predicted as negative; tpr=fpr=0. On the other hand, when c=0, all cases are predicted as positive; tpr=fpr=1.

**ref**

- https://en.wikipedia.org/wiki/F-score