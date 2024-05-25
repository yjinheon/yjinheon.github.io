# 어딘가 집어넣을 것들

## n211

#### 기준모델

- [Always start with a stupid model, no exceptions](https://blog.insightdatascience.com/always-start-with-a-stupid-model-no-exceptions-3a22314b9aaa)

#### Scikit-Learn

- [Python Data Science Handbook, Chapter 5.2: Introducing Scikit-Learn](https://jakevdp.github.io/PythonDataScienceHandbook/05.02-introducing-scikit-learn.html#Basics-of-the-API)
- [2.4.2.2. Supervised Learning](https://ogrisel.github.io/scikit-learn.org/sklearn-tutorial/tutorial/text_analytics/general_concepts.html#supervised-learning-model-fit-x-y)
- [sklearn.linear_model.LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
- [sklearn.metrics.mean_absolute_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html)

#### 읽어보세요

- [Art of Choosing Metrics in Supervised Models](https://towardsdatascience.com/art-of-choosing-metrics-in-supervised-models-part-1-f960ae46902e)
- [The Discovery of Statistical Regression](https://priceonomics.com/the-discovery-of-statistical-regression/)

#### 최소제곱법

- [수학산책-최소제곱법](https://terms.naver.com/entry.nhn?cid=58944&docId=3569970&categoryId=58970)

#### (참고) 더 세련된 시각화툴: Plotly

- [Plotly Express](https://plot.ly/python/plotly-express/)
- [plotly_express.scatter](https://www.plotly.express/plotly_express/#plotly_express.scatter)

#### ipywidgets interact

- [Using Interact](https://ipywidgets.readthedocs.io/en/stable/examples/Using%20Interact.html#Using-Interact)

### 210624

https://velog.io/@tobigs_xai/1%EC%A3%BC%EC%B0%A8-XAI-%EA%B8%B0%EB%B3%B8%EA%B0%9C%EB%85%90-xgboost # 오늘 건진것중 가장 중요(아마)

#### ADABoost

- https://ko.wikipedia.org/wiki/%EC%97%90%EC%9D%B4%EB%8B%A4%EB%B6%80%EC%8A%A4%ED%8A%B8
- https://jungsooyun.github.io/statistics/Adaboost_weight/
- https://assaeunji.github.io/ml/2020-08-14-adaboost/

#### shell scipt

- https://vaert.tistory.com/103
- https://devhints.io/bash
- https://www.educative.io/blog/bash-shell-command-cheat-sheet

### 210622

#### misc

- https://m.blog.naver.com/onevibe12/222003789290 [[파이썬]] vim 설정

#### 프로젝트 관련데이터사이트

- https://data.world/
- https://researchguide.cau.ac.kr/c.php?g=549836&p=3774670
- https://bigdata.seoul.go.kr/main.do
- https://rstudio-pubs-static.s3.amazonaws.com/594440_b5a14885d559413ab6e57087eddd68e6.html

#### 웜업

- 클래스 불균형시의 분류문제
  : 과학저술의 99.99는 노벨상이 되지 않는다. 라고 할때 정확한 분류기를 얻을 수 있다.

- Relative cost of false positive/false negative
  
  - 이 경우 상대적인 Cost는 False postive(false alarm)이 더 크다.
  - Hyper Plane(Decision Boundary)를 그릴때 threshold를 크게 하는것이 중요하다.
  - 상대적인 Cost가 FP가 더 크기때문에 Precision이 아닌 Recall에 더 가중치를 준다
  - 따라서 F-beta score에서 beta의 가중치는 줄인다

- 고전적인 비교
  
  - Medical diagnosis & investment opportunities

##### Choos ML Problems

- 예측문제 정의 : 예측타겟 선택
- 정보의 누수(Data Leakage) : 두 가지 경우 :
  - 타겟변수 외에 예측시점에 사용할 수 없는 데이터가 포함되어 학습이 이뤄질 경우
  - 훈련데이터와 검증데이터를 완전히 분리하지 못했을 경우 -> 답안이 유출된것, 어쩔 수 없이 과적합이 일어난다.
    - 정보의 누수가 과적합을 일으키고 실제성능을 떨어트린다.
    - 불균형클래스 : 타겟특성의 클래스 비율이 차이가 많이 날 경우가 존재
      - 대부분의 scikit-learn 분류기들은 class_weight와 같은 클래스의 밸런스를 맞추는 파라미터를 가지고 있음
        1. 데이터가 적은 범주 데이터의 손실을 계산할 때 가중치를 더 곱하여 데이터의 균형을 맞추기
        2. 적은 범주 데이터를 추가샘플링 하거나 반대로 많은 범주 데이터를 적게 샘플링 하는 방법이 있다.
    - 오버샘플링, 언더샘플링

##### 테크블로그

- https://tech.kakao.com/2020/04/29/kakaoarena-3rd-part2/ # 카카오
- https://woowabros.github.io/study/2018/08/01/linear_regression_qr.html # 우아한 형제들 

##### Information Leakage

- https://machinelearningmastery.com/data-leakage-machine-learning/
- https://towardsdatascience.com/data-leakage-in-machine-learning-6161c167e8ba

##### 왜도 관련

- https://ko.wikipedia.org/wiki/%EB%B9%84%EB%8C%80%EC%B9%AD%EB%8F%84 # 왜도 위키피디아
- https://cceeddcc.tistory.com/14
- https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=istech7&logNo=50154573592
- https://medium.com/@ODSC/transforming-skewed-data-for-machine-learning-90e6cc364b0

#### 210621 스프린트 정리

- 결정트리
  
  + 파이프라인
  + 사이킷런 결정트리
  + 특성 중요도
  + 결정트리 모델의 장점을 이해하고 선형회귀모델과 비교

- Random Foreset
  
  + ensemble : 성능을 높이기 위해 여러 모델을 합친다
  + 랜덤포레스트 :  
  + 배깅 : 단순히 부트스트래핑(복원추출)하고 합친것
  + 파라미터
    * n_estimators : 기준모델의 수
    * max_depth : 나무 깊이

- Confusion Matrix
  
  + Recall : 초기암진단 : 민감도 : 기본적으로 Type2 error(Miss), False Negative를 피하는 것이 중
  + Precision : 스팸메일 : 정밀도: 모델이 예측한 True 중 실제 True의 비율,Type1 error(False Alarm), False Positive를 피하는 것이 중요

- Model Selection
  
  + CV는 기본적으로는 데이터 양이 적어서 학습세트를 늘리려고 만든것이다.
  + Train-valid-test로 나누는 홀드아웃 검정의 경우 하이퍼파라미터 튜닝할 때 데이터의 일부에 튜닝할 수 있는 단점이 있다.예컨대 
    valid set에 관한 검증 결과 확인 후 모델 파라미터 튜닝을 하는 작업을 반복하게 되면 모델이 valid set에 대해 overfit 될 가능성이 높다는 것이 단점이다
  + Taget encoder : 성능향상에 도움이되는 인코더, 사용시 정보의 누수가 일어나지 않도록 주의

- 하이퍼파라미터 튜닝
  
  + 기본적으로 트리가 커질수록 과적합 가능성이 높아진다.
  + Max depth를 어느지점에서 결정할 지 validation cureve를 활용해야한
  + fold는 보통 5-fold이상

##### CrossValidation 사용이유와 용법

- https://modern-manual.tistory.com/20?category=902149
- https://m.blog.naver.com/ckdgus1433/221599517834

##### Git bash Conda 사용하기

https://azanewta.tistory.com/29

##### Fit과 교차검증의 관계

##### 교차검증의 전단계에서 Fit은 끝나있다.

- 교차검증은 기본적으로 검증만 하는것
- 모든 fold에 대해 valid set이 될 기회를 끝나있다.

##### 관련있는 피처 ->통합 유의미한 피처

- 설명력 강화와 차원축소를 위해 합친다

##### random forest

- oob score는 보통 거의 쓰지 않는다.

##### Crossvalidation

- https://teddylee777.github.io/scikit-learn/grid-search-%EB%A1%9C-hyperparameter%EC%B5%9C%EC%A0%81%ED%99%94
- https://learnaday.kr/open-course/tfcert
- https://github.com/koni114/TIL/blob/master/Machine-Learning/contents/ML%EC%83%81%EC%8B%9D%EC%A0%95%EB%A6%AC.md

#### 210617

- 중요 : 민감도 특이도 정밀도
- https://sumniya.tistory.com/26 # 개념암기용 우선
- https://towardsdatascience.com/demystifying-confusion-matrix-29f3037b0cfa # 이해용 
- https://towardsdatascience.com/machine-learning-an-error-by-any-other-name-a7760a702c4d# # 헷갈리는 명칭들
- https://towardsdatascience.com/classification-metrics-thresholds-explained-caff18ad2747
- https://towardsdatascience.com/demystifying-confusion-matrix-29f3037b0cfa
- http://seb.kr/w/F1_%EC%8A%A4%EC%BD%94%EC%96%B4
- https://en.wikipedia.org/wiki/F-score
- https://youtu.be/j-EB6RqqjGI
- https://www.youtube.com/watch?v=4jRBRDbJemM
- https://newsight.tistory.com/53 # ROC, AUC, 민감도, 특이도
- https://www.kaggle.com/nappon/animation-confusion-matrix-and-roc-interplay
- https://darkpgmr.tistory.com/162
- https://eunsukimme.github.io/ml/2019/10/21/Accuracy-Recall-Precision-F1-score/ # 블로그 참고
- https://en.wikipedia.org/wiki/F-score
- https://stats.stackexchange.com/questions/221997/why-f-beta-score-define-beta-like-that

##### multilabel classification problem

##### Visualize

- Recall(Sensitivity)
- https://rafalab.github.io/dsbook/inference.html
- https://github.com/reiinakano/scikit-plot
- https://morioh.com/p/2298e2750226 # 개쩌는 레퍼런스

#### 210616

- articles
  + https://www.analyticsvidhya.com/blog/2016/12/detailed-solutions-for-skilltest-tree-based-algorithms/?utm_source=blog&utm_medium=4-ways-split-decision-tree

중요

- 노드와 피처는 다르다!!

- 노드는 기본적으로 TF로 나누어질 수있는 Statement이다.

- 랜덤포레스트

- 배깅 : 부트스트랩을 통해 모델을 학습을 하고 합치는 과정
  
  + 원본 데이터의 개수만큼 복원추출을 하는 것을 부트스트탭 샘플링이라 한다
  + 부트스트랩에서 추출되지 않는 36.8% 의 샘플을 OOB 샘플이라고 하며 이를 통해 모델을 검증한다.

- Ordinal encoding 하는 이유
  
  + 범주형 자료를 모델에서 사용하고자 할때 Ordinal 
  + 트리모델에서는 구조상 중요한 특성들이 상위노드에서 선택됨
  + 중요한 범주형 특성이 원핫인코딩을 하게되면 제대로 쓰일 수없다
  + 원핫인코딩에서는 한 피처가 여러 특성으로 나눠지기 때문에..

- 기본적으로 노드가 중요할수록 불순도가 크게 감소한다.

- 지니인덱스가 낮으면 불순도가 낮기 때문에 루트노드에 올 가능성이 높아진다.

- 잘 나누는 기준은 나눴을 때 덜 섞이는 것

- 만들어진 결정트리를 보니 어떤 특성이 중요하다 로 이해하면 된다.

#### 210615

- https://wikidocs.net/744
- https://soohee410.github.io/iml_tree_importance
- https://www.math.snu.ac.kr/~hichoi/machinelearning/lecturenotes/CART.pdf

#### Post-Pruning : 해볼 것

https://scikit-learn.org/stable/auto_examples/tree/plot_cost_complexity_pruning.html

https://christophm.github.io/interpretable-ml-book/tree.html

https://ko.wikipedia.org/wiki/%EA%B2%B0%EC%A0%95_%ED%8A%B8%EB%A6%AC_%ED%95%99%EC%8A%B5%EB%B2%95

- 파이프라인 : Python,ML
  
  + 기타 레퍼런스
  + https://spark.rstudio.com/guides/pipelines/ 

- 의사결정트리
  
  + 전반적으로 확인 https://blog.naver.com/ehdrndd/221158124011
  
  + 목적
  
  + 수식
    
    * IG
    * df
  
  + terminology
    
    * root node
    * leaf node
    * pure node 
  
  + 목적함수
  
  + 하이퍼파라미터
    
    * max_depth : 일반화 성능관련, 끝까지 학습환런
    * min_sample_splite
    * max_feature : 최대 피처 사용수
    * random_state : random state
    * class_weight : 가중치 balance 맟추기
  
  + 특징
    
    * Scale의 영향을 받지 않는다.

- 결정트리구현-python
  
  + 시각화 : graphviz 확인
  + 혼동행렬
  + Post-Pruning
    수식
    https://en.wikipedia.org/wiki/Decision_tree_learning
    https://zephyrus1111.tistory.com/124?category=858748
    https://towardsdatascience.com/the-mathematics-of-decision-trees-random-forest-and-feature-importance-in-scikit-learn-and-spark-f2861df67e3
    https://youtu.be/yLh-UiqMC04?list=PLJN246lAkhQiEc-QvvGzUneCWuRnCNKgU

#### input이 continuous 한 경우의 의사결정 트리

- 매우 매우 매우 매우 매우 매우 매우 중요
- https://www.youtube.com/watch?v=v26lXTcAicw&t=13s
- https://www.youtube.com/watch?v=OD8aO4ovIBo # input이 continuous 고

#### Feature Engineering

#### 재귀적인 이진분리의 수행

#### 크로스 엔트로피

- https://3months.tistory.com/436
- http://melonicedlatte.com/machinelearning/2019/12/20/204900.html

OLS회귀 랑 sklearn의 결과다른 이유 : dk

#### graphviz 그래프 시각화

```python
from sklearn.tree import export_graphviz
export_graphviz(model, out_file='cancer_tree_self.dot', class_names=cancer.target_names,
                feature_names=cancer.feature_names,
                filled=True)
```

```python
import os
import graphviz
from IPython.display import display
with open(r'cancer_tree_self.dot', encoding='utf-8') as f:
    dot_graph = f.read()
display(graphviz.Source(dot_graph))
```