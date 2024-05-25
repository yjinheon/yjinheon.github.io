> 모델 성능 최적화 관련 내용 

옵티마이저

가중치초기화

## Regulargization(과적합 방지를 위한 규제)

- n413

**학습을 어떻게 효율적으로 할 것인가?**

[매우 핵심적인 참고논문](https://https://openaccess.thecvf.com/content_CVPR_2019/papers/He_Bag_of_Tricks_for_Image_Classification_with_Convolutional_Neural_Networks_CVPR_2019_paper.pdf)
Bag of Tricks for Image Classification with Convolutional Neural Networks

**과적합 방지를 위한 기법을 규제라고 부른다.**

- [Weight Decay](#weight-decay)
- [Weight Constraint](#weight-constraint)
- [Dropout](#dropout)
- [[추가] 학습에 batch size가 미치는 영향](#추가-학습에-batch-size가-미치는-영향)
- [References](#references)

---

**_Concept_**

- **batch size**: Total number of training examples present in a single batch.
- **Iteration** : number of batches needed to complete one epoch.
- **epoch** : One Epoch is when an ENTIRE dataset is passed forward and backward through the neural network only ONCE.

---

- https://towardsdatascience.com/epoch-vs-iterations-vs-batch-size-4dfb9c7ce9c9

### Weight Decay

기본적인 컨셉은 오차를 일부 허용하더라도 오버피팅을 막겠다

weight decay를 하는이유:
가중치가 너무 커져서 과적합 되는 것을 방지하기 위하여 가중치를 인위적으로 더해서 가중치가 무한히 발산하는 것을 막아준다

L1 작은 가중치는 0이 되고 나머지는 가져감 (절대값 사용)
L2 아무리 작은 가중치도 제곱이 되기 때문에 일부는 남게됨

$$Loss = MSE + \lambda \times  * {w}^2$$

왜 이런 조치가 overfitting을 줄여주는가?

어딘가에 Global minimum이 존재

하지만 이 Global minimum은 `학습한` training set에서만 적용

Regularization 항을 추가할 경우 원점에 loss surface가 하나 더 생김

Global minimum에 빠질 경우 overfitting 이 일어나는데 loss surface를 하나 더 

더 만듬으로써 다른 training set에서도 해당 모형이 잘 적용될 수 있게끔하는 것이다.

### Weight Constraint

### Dropout

### Weight Initialize

https://excelsior-cjh.tistory.com/177 (가중치 초기화부분 정)

우리는 처음에 망의 가중치 초기화를 어떻게 하는지에 따라 결과에 얼마나 큰 영향을 끼치는지 봤습니다. 가중치 초기화 모드는 매우 다양합니다 (아래에 종류를 적어놨습니다). 모든 것을 써볼 일은 아마 없겠지만 어떤 것을 선택하는지에 따라 모델의 초기 정확도에 큰 영향을 끼칩니다. 우리가 가중치를 잘 초기화하면 훨씬 적은 epoch으로 모델을 위한 최적의 가중치를 찾을 수 있습니다.

> 가중치 표준편차를 1인 정규분포로 초기화를 할 때 활성화 값의 분포

<img src="https://t1.daumcdn.net/cfile/tistory/994C2F3C5AB623C526" width=600/>

> 가중치의 편차를 1/sqrt(n) 으로 초기화한 Xavier 초기값의 활성화 값의 분포

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbuwPPz%2FbtquO7Wq9Rp%2Fylz2Qsc0fi9m0TaQNXBYDK%2Fimg.png" width=580/>

> 가중치 표준편차를 sqrt(2/n)으로 초기화한 He 초기값의 활성화 값의 분포

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcKBoWH%2FbtquO7B8MfF%2FMs5LyROpCV89EbCFNXja4k%2Fimg.png" width=580/>

c.f. Activation function에 따른 초기값 추천
① Sigmoid  ⇒  Xavier 초기화를 사용하는 것이 유리 
② ReLU  ⇒  He 초기화 사용하는 것이 유리

https://machinelearningmastery.com/weight-initialization-for-deep-learning-neural-networks/

### [추가] 학습에 batch size가 미치는 영향

### 기울기 소실과 폭주

https://wikidocs.net/61375

### References

- [batch size 관련](https://medium.com/mini-distill/effect-of-batch-size-on-training-dynamics-21c14f7a716e) 
- [overfitting in deeplearing models](https://towardsdatascience.com/handling-overfitting-in-deep-learning-models-c760ee047c6e)
- [weight decay](https://towardsdatascience.com/this-thing-called-weight-decay-a7cd4bcfccab)
- [batch size와 number of iteration의 tradeoff](https://stats.stackexchange.com/questions/164876/what-is-the-trade-off-between-batch-size-and-number-of-iterations-to-train-a-neu)

<!--

- [L1 & L2 Regularization](https://www.youtube.com/watch?v=_sz3KTyB9Lk&t=1063s)
- [가중치 초기화 관련](https://youtu.be/ScWTYHQra5E)
- [Dropout](https://www.youtube.com/watch?v=ajeliDMD86U)
- [Ng 교수님의 하이퍼파라미터 설명](https://www.youtube.com/watch?v=wKkcBPp3F1Y)
- [parameter와 hyperparameter 차이](https://youtu.be/Kh06wgGbi78?t=12)
- [학습 규제 방식에 대한 설명 강의](https://youtu.be/_sz3KTyB9Lk?t=1005)
- [L1/L2-regularization](https://towardsdatascience.com/l1-and-l2-regularization-methods-ce25e7fc831c)
  -->

- [L1 & L2 용어정리](https://light-tree.tistory.com/125)



## Optimizers

- 하이퍼파라미터 옵션들 중 하나이다.
- 기본적으로 오차함수를 최소화하기 위한 가중치 업데이트 알고리즘이다.
- 대표적인 옵티마이저로 Gradient Descent가 있다.

---

**_Concept_**

- **Optimizers** : 손실함수(loss function)를 최소화하는 최적의 가중치 (weight)를 업데이트 하는 방법

---

![옵티마이저의 종류](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbQ934t%2FbtqASyVqeeD%2FozNDSKWvAbxiJb7VtgLkSk%2Fimg.png)

- https://ganghee-lee.tistory.com/24

- https://wiserloner.tistory.com/1032

- https://www.youtube.com/watch?v=4qJaSmvhxi8&t=320s (ref)

- [옵티마이저의 종류](https://www.slideshare.net/yongho/ss-79607172)

- 옵티마이저 종류 논문

### Gradiant Boost

- 최적화 관점에서의 회귀 링크

### Stochastic Gradient descent

### Momentum

### AdaGrad

### Adam

### RMSProp
