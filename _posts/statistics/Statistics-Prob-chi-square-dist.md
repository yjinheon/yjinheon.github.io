---
title: '[Probability]Python을 활용한 카이스퀘어 검정 구현'
categories:
  - Statistics
date:
updated:
tags:
  - Probability
mathjax: true
---

### 카이스퀘어 분포

#### Note

- 감마분포의 특수한 형태이다.
- 표준정규분포로부터 얻은 랜덤 변수들을 제곱해서 더한 것이다.
- 자유도 수 만큼 표준정규분포에서 변수를 뽑고 그 값들을 제곱해서 더한다.
- **데이터의 분산이 퍼저있는 정도를 분포로 보여준다는 것이 핵심이다.**
  + 모분산을 추정할 수 있다 -> goodness of fit
  + 두 분포의 차이를 확인할 수 있다 -> Chi-square test of independence

#### 공식

- k개의 정규분포를 따르는 확률변수 X_1 ,..., X_k를 정의하면 아래와 같이 자유도 k의 카이스퀘어 분포를 나타낼 수 있다.

$$Q = \sum_{i=1}^{k} X_i^2$$


- 독립성 검정(independence test)과 적합성 검정(goodness of fit)을 위하 사용하는 피어슨 카이스퀘어 통계량
  + $\frac{(O_i - E_i)^2}{E_i}$는 정규분포를 따르고 데이터가 충분히 많다면 이를 합한 피어슨 카이스퀘어 통계량은 카이스퀘어 분포를 따른다.

$$\sum_i \frac{(O_i - E_i)^2}{E_i}$$


#### 적합성 검정(goodness of fit) 구현

적합성 검정은 기본적으로 샘플 데이터가 특정 분포를 따르는지(정규분포) 확인할 때 사용한다.
이 검정이 중요한 이유는 회귀분석 모델링에서 요구하는 오차의 정규성 가정을 확인하는데 쓸 수 있기 때문이다.

**관측한 데이터(샘플)의 분포가 기대되는 어떤 분포(보통 정규분포)를 따르는지 확인한다는 것이 핵심이고 로직 자체는 아래의 독립성 검정과 유사하다.**
```python
import scipy.stats as stats

obs = [20, 40, 30, 10, 50]
exp = [20, 20, 20, 20, 20]

#Goodness of Fit Test
# f_exp 인자로 로 기대되는 데이터 value를 넣을 수 있다. 
stats.chisquare(f_obs=obs,f_exp=exp)

>>>Power_divergenceResult(statistic=33.333333333333336, pvalue=1.020735571764047e-06)

```

#### 독립성 검정(Chi-square test of independence)

- **두 범주형 변수 사이의 관계를 파악한다.**
- 독립성 검정을 시행하려면 교차표의 각 셀의 기대빈도가 5 이상이여 한다는 조건이 붙는다.
- 각 셀의 기대빈도가 5 이상일 경우 $\chi^2$ 는 근사적으로 기대빈도가 n-1인 카이스퀘어 분포를 따른다.
- 보통 범주형 독립변수와 범주형 종속변수의 관계가 있는지 확인할 때 사용한다.

귀무가설은 두 범주형 변수가 독립적이라는 것이다.
귀무가설이 성립하려면 교차표의 각 셀의 관측빈도와 기대빈도의 차이는 0에 가까워야 한다.
두 범주형 변수의 빈도의 범주간 차이가 기댓값에서 유의미하게 벗어나는지 검정한다.

카이스퀘어 통계량이 유의수준을 넘어서면 귀무가설을 기각한다.

```python 
from scipy.stats import chi2_contingency

# 교차표 자체는 pandas에서 제공하는 crostab함수를 통해 df로 만들 수도 있다.
table = [[20, 40, 30, 10], [20, 42 ,15,  30]]

# 카이 , p-value, 자유도, 기대빈도
stat, p, dof, expected = chi2_contingency(table)
# 유의수준 설정
alpha = 0.05
# 가설수용/기각

print('significance=%.3f, p=%.3f' % (alpha, p))
if p <= alpha:
    print('Variables are associated (reject H0)')
else:
    print('Variables are not associated(fail to reject H0)')

```


**References & annotation**
---

- https://youtu.be/2QeDRsxSF9M
- https://towardsdatascience.com/chi-squared-test-for-feature-selection-with-implementation-in-python-65b4ae7696db
- 기대빈도가 5미만일 경우 피셔의 적합검정을 고려한다.
- 제대로 쓰려면 헬퍼함수를 따로 만들긴 해야할 것 같다.
