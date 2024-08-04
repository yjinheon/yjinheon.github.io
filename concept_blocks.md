- **결정 경계**: 서로 다른 두 데이터를 구분하는 기준선(threshold). 선형 SVM의
  결정 경계는 데이터 feature의 n차원의 초평면(hyperplane)이다.
- **초평면(hyperplane)** : flat affine subspace of p-1 (p는 데이터의 차원)
- **Support Vector** : 결정 경계와 가장 가까운 데이터 포인트. Soft Margin의 끝에
  있는 데이터포인트
- **Margin** : 결정경계와 Support Vector사이의 거리(threshold와 데이터포인트
  사이의 최소거리)
- **Support Vector Machine** : 마진을 최대화 하는 결정 경계를 찾는 알고리즘.
  - **Soft Margin** : **Allow misclassification**. outlier의 오분류를
    허용함으로써 과적합으로 인한 문제(low bias, high variance) 를 완화시키려고
    하는 것. Soft Margin은 오분류를 허용한 경우의 Margin
  - **Hard Margin**: 결정경계면이 선형이며 오분류를 허용하지 않는 Margin.
    오차항이 없는 경우의 softmargin

- **결정트리**: 질문을 던지고 답을 하는 과정을 연쇄적으로 반복해 집단을
  분류하거나 예측하는 분석방법.
- **threshold** : 결정트리에서의 학습대상. 정확히는 데이터를 나누는 best
  feature의 best threshold를 찾는 것이 학습의 목적이다,
- **full tree** : 모든 학습데이터에 대해 분기한 상태.
- **Entropy** : Entropy 는 데이터셋의 불순도와 무질서한 정도를 나타내는 측정치
- **지니 불순도** : 데이터 집합에서 클래스 분포에 따라 무작위로 라벨이 지정된
  경우 무작위로 선택한 요소들을 잘못 분류할 확률이다.(Chance of being incorrect
  if you randomly assign a label to an example in the same set)
- **정보 이득** : 정보 이득은 단순히 부모 노드의 불순도와 자식 노드의 불순도
  합의 차이이다. 정보이득이 높을수록 데이터틀 더 잘 구분할 수 있는 feature이다.
- **Root Node** : 초기노드. 데이터셋 혹은 샘플 전체.
- **Leaf Node(Terminal Node)** : 자식이 없는 노드.하위노드가 없다.
- **Pure Node** : 노드의 모든 데이터포인트가 하나의 클래스에 할당되어 있을 경우.
  타깃 한개로만 이루어진 Leaf Node.
- **Branch** : sub-section of an entire tree.
- **Splitting** : 특정 노드를 나눠 하위노드를 생성하는 것.
- **Pruning** : 특정 노드의 하위노드를 날리는 것(삭제).
- **Pre-prune**: When you stop growing DT branches when information becomes
  unreliable.
- **Post-prune**: When you take a fully grown DT and then remove leaf nodes only
  if it results in a better model performance. This way, you stop removing nodes
  when no further improvements can be made.

![](https://miro.medium.com/max/888/1*FYEZGG-gEijSb87KuxSE_Q.png)

- **Bagging** : 랜덤 복원추출을 통해 샘플링한 데이터를 바탕으로 피팅한 모델들의
  예측결과를 다수결이나 평균을 내어 예측하는 것.
- **weak learner** : 서로 독립적으로 만들어지며 **상관이 낮은** 약한 분류기.
- **Random Subspace Method** : Bagging과 유사하지만 Bagging에 추가로 feature를
  일부 선택해서 분할하는 것. Random Forest에서 사용
- **Random Forest** : 여러 `week learner`들을 합쳐서 하나의 트리를 만드는 것.
  boosting에 비해 과적합이 덜되는 경향이 있다.
- **Bootstrap** : datapoint가 n개일 때 n의 크기를 가지는 표본을 복원추출하는 것.
  기본적으로 데이터가 편중되지 않게끔 한다.
- **OOB** : Out of Bag. 부트스트랩에서 추출되지 않는 36.8% 의 샘플.

**커널** :

**커널** :

