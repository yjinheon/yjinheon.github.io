---
title: '[Deep Leearing] 학습 규제하기(Handling Overfitting)'
categories:
   - [Neural Network]
tags:
mathjax: true
date: 2021-08-02 00:00:00
updated:
---

<!--

<center>Kaggle Customer Score Dataset</center>

- Machine Learning
- Statistics , Math
- Data Engineering
- Programming
- EDA & Visualization
- Data Extraction & Wrangling

#신경망이란 무엇인가?

https://www.youtube.com/watch?v=aircAruvnKk


#참고

https://cinema4dr12.tistory.com/1016?category=515283

https://www.kdnuggets.com/2021/07/top-python-data-science-interview-questions.html
-->

**과적합 방지를 위한 기법을 규제라고 부른다.**

- [Weight Decay](#weight-decay)
- [Weight Constraint](#weight-constraint)
- [Dropout](#dropout)
- [](#)
- [\[추가\] 학습에 batch size가 미치는 영향](#추가-학습에-batch-size가-미치는-영향)
- [References](#references)

---

## Weight Decay

학습은 

$$Loss = MSE + \lambda \times  * {w}^2$$

왜 이런 조치를 하는 것이 overfitting을 줄여주는가?

어딘가에 Global minimum이 존재

하지만 이 Global minimum은 `학습한` training set에서만 적용

Regularization 항을 추가할 경우 원점에 loss surface가 하나 더 생김

Global minimum에 빠질 경우 overfitting 이 일어나는데 loss surface를 하나 더 만듦으로써 다른 training set에서도 해당 모형이 잘 적용될 수 있게끔하는 것이다.

## Weight Constraint

## Dropout

## 

## [추가] 학습에 batch size가 미치는 영향

## References

- [batch size 관련](https://medium.com/mini-distill/effect-of-batch-size-on-training-dynamics-21c14f7a716e) 
- [overfitting in deeplearing models](https://towardsdatascience.com/handling-overfitting-in-deep-learning-models-c760ee047c6e)
- [weight decay](https://towardsdatascience.com/this-thing-called-weight-decay-a7cd4bcfccab)

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
