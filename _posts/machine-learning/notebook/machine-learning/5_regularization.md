# Regularization 이해

**_Concept_**

- 과적합을 줄이는 세 가지 방법
  + **Regularizaiton** : **과적합을 줄이기 위해** 파라미터에 패널티를 주는것. 
    + cost function에  Regulariazation을 적용한다는 것은 기본적으로 학습과정에서 local noise의 영향을 줄이고
  + **Feature Selection(Reduce number of Features)** : **과적합을 줄이기 위해** 불필요한 Feature들을 제거하는 것.
  + **데이터의 수를 늘이기** : 가장 단순하지만 일반적으로 가장 효과적인 방법.
- $\lambda$ (lambda) : learning rate 같은 hyperparameter의 일종
- + 
- **L1 norm** : 모델의 가중치 벡터의 각 요소들의 절대값의 합. 여기다가 $\lambda$를 곱하면 lasso 회귀의 규제항이 됨
  - L1 규제의 경우 절대값을 적용하기 때문에 크기가 작은 가중치는 0으로 만들어버리는 특성이 있어 일부 특성들을 제거하려고 할 때 유용하다.
  - 에러 값에 현재 가중치 크기의 **일정 값** 을 추가로 반영함. 따라서 특정 가중치 W는 0이 될 수 있다.
- **Ridge** : 
  + **일정한 비율로 패널티를 적용**
- **Lasso** :
  + 변수들의 부분 집합만을 포함하는 모델을 생성하여 더 간단하고 해석 가능하다는 점이 Ridge와 비교하여 주된 장점
  + **일정한 양으로 패널티를 적용**
- **Elastic Net** :
  + lambda_1, lambda_2는 각각 Ridge와 Lasso 속성에 대한 강도를 조절하는 것이다. 이를 통해,Ridge의 정규화 속성과 Lasso의 변수축소 속성을 모두 갖는 모델이다.
  + Lasso는 상관관계가 있는 다수의 변수들 중 하나를 무작위 선택하여 계수를 축소하는 반면, Elastic-Net은 상관성이 높은 다수의 변수들을 모두 선택하거나 제거한다.
  + 이러한 방식을 통해 group effect를 유도한다. 따라서 **다수의 변수간에 상관관계가 존재할 때 유용하다**. 

---



https://github.com/greyhatguy007/Machine-Learning-Specialization-Coursera/blob/main/C1%20-%20Supervised%20Machine%20Learning:%20Regression%20and%20Classification/week3/C1W3A1/C1_W3_Logistic_Regression.ipynb

## 과적합

머신러닝에서 과적합(overfitting)은 모델이 학습 데이터에 과도하게 적합하게 훈련되어 새로운 데이터(테스트 데이터)에 대해서 성능이 나오지 않는 것을 의미한다

## 과적합을 줄이는 방법들

과적합을 줄이는 방법으로 보통 아래와 같은 방법들을 사용한다. 

여기서는 

1. 데이터 늘리기 : 과적합은 일반적으로 모델이 충분한 데이터를 학습하지 못했기 때문에 발생한다.

2. Feature Selection : **과적합을 줄이기 위해** 불필요한 Feature들을 제거하는 것. `bias-variance tradeoff` 와 직접적으로 관련이 있으며

3. Reqularization : 모델 학습시 모수에 패널티를 추가해서 특정 feature에 모델

4. cross validation : cross validation은 1번의 데이터를 늘리는 방식의 일종이다. 데이터를 k개의 subset으로 나누고 모든 subset을 학습 및 평가에 사용해 vud

     - 평가에 사용되는 데이터 편중을 막을 수 있다. 

   (특정 평가 데이터 셋에 overfit 되는 것을 방지할 수 있다.) 

5. Ealry Stopping : validation set의 성능이 더 나아지지 않을 경우 학습을 중단하는 방법

6. Data aumentation : input data 에 일부러 변형을 가해서 패턴을 학습하게끔 하는 것

## Regularization

:**Regularization은 모델 복잡도를 줄이고 일반화 성능을 높이기 위해 학습과정에서  모수의 일정비율(양)의 패널티를 부여 하는 것이다.**

- 결과적으로 모수($\theta_0, \theta_1, \theta_2, ..., \theta_n$)의 영향을 줄이는 것이다.

- cost function에  Regulariazation을 적용한다는 것은 기본적으로 학습과정에서 local noise의 영향을 줄이고 이상치의 영향을 덜 받게 하겠다는 것이다.

## Norm

norm은 베ㅂ

$$
L_p = (\sum_i^n |x_i|^p)^{\frac{1}{p}}
$$




##  L2 norm

:**L2 norm**은 



- **L2 norm** : 모델의 가중치 벡터의 유클리디안 거리. 여기다가 $\lambda$를 곱하면 Ridge 회귀의 규제항이 된다
  + L2 norm은 가중치 파라메터의 크기(거리)를 의미하기 때문에, 에러 값에 현재 가중치 크기의 **일정 비율**을 추가로 반영시킴으로써 갱신이 이루어질때, 현 시점의 가중치를 일정비율로 깎아내린 다음에 오차에서 계산된 기울기를 갱신을 해주는 것
  + L2 규제의 경우 가중치(파라미터)의 제곱 을 사용하기 때문에 가중치의 크기가 클수록 규제를 많이 받게 되고 따라서 큰 가중치를 제한하는데 효과적으로 사용할 수 있다.
- 이상치에 민감하다.



## L1 norm

: L1 norm은 벡터의 각 데이터포인트에 대한 절대값의 합니다.



- ㅇ라ㅓ

라소

![](../data/images/L1L2norm.png)

비교
![l2 norm l1 norm 비교](https://amitrajan012.github.io/img/Linear%20Model%20Selection%20and%20Regularization_files/lasso.png)



Ridge regression shrinks every dimenion of the data by same proportion.

Lasso shrinks every coefficient towards 0 by same amount and the smaller coefficients are shrinken all the way to 0.



출처 위키피디아

## Elastic Net



## 구현







## Reference

https://towardsdatascience.com/l1-and-l2-regularization-methods-ce25e7fc831c
https://deepapple.tistory.com/6
https://todayisbetterthanyesterday.tistory.com/12

