# 조건부 확률(Conditional Probability)

: Bayes theorem

조건부확률



$$
P(\theta|D)=\frac{P(D| \theta) P(\theta)}{P(D)}
$$



$$
P(w_ i|x) = \frac {P(x|w_ i)P(w_ i)}{\sum_ {j} {P(x|w_ j)P(w_ j)}}
$$

---

**_Concept_**

- **사전확률(Prior)** : 
- **사후확률(Posterior)** : 사건
- **가능도(likelyhood)** : 데이터가 

---

### 조건부 확률의 개념

: 조건부확률

$$P(B|A)=\frac{P(B|A) P(B)}{P(B)}$$

### 확률분포와 확률

우리가 확률이라고 하는 것은 보통  특정 확률분포 하에서 특정데이터가 나타날 가능성을 뜻한다.
예를 들어 호수에서 물고기를 낚았을 때 이 물고기 

우리가 

$$
P(관측값|확률분포)=P(Data|\theta)
$$

### 사전확률

### 사후확률

### 가능도(Likelyhood)

Data는 하나의 사건(Event) 일 수도 있고 여러 Event의 집할일 수 도 있다.

$$P(확률분포|관측값)=P(\theta|Data)$$ 

- 수식에 있는 '|' 는 어떤 조건(Contition) 을 의미한다.

PDF의 y값에 해당한다.

이는 우도가 특정 데이터(사건) 이 주어졌을 때의 확률분포의 값을 뜻하기 때문이다.

어떤 확률분포에 대해 주어진 데이터가 나타날 가능성이 가능도이다.

- 이러한 가능도는 기본적으로 결합확률 분포로 나타낼 수 있다.

확률분포가 이산적일 경우 특정 데이터(관측치)에 대한 확률을 계산할 수 있기 때문에 가능도와 확률은 개념적으로 차이가 없게 된다.

통계학에서 가능도(likelihood)는  확률분포의 모수가 주어진 데이터(sample)와 일관되는 정도를 나타낸다. 

이러한 가능도는 기본적으로 결합확률 분포로 나타낼 수 있다

확률분포가 연속적일 경우 

### 사후확률의 업데이트

### 합의 법칙

### 곱의 법칙

### Probability vs Likelihood

Probability
:
$P(D | \theta)$

data(Event) 의 범위는 변하지만 분포는 기본적으로 고정됨

기본적으로 구간을 바꿔가면서 확률을 계산한다.

Likelihood
:

$P(\theta| Data)$

The distinction between probability and likelihood is fundamentally important: Probability attaches to possible results; likelihood attaches 
to hypotheses

이산확률분포일 경우 가능도는 결합확률

### 조건부 확률과 머신러닝