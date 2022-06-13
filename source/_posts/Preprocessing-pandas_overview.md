---
title: "[pandas]Pandas를 활용한 데이터분석 시작하기"
date: 
updated:
categories: 
        - [Preprocessing]
tags:
  - [pandas]
---
## Intro
- **알아야 하는 것**
  - pandas data structure
  - reading data
  - dealing with missing data
  - slicing & indexing
    - loc & iloc
  - map
    - map
    - apply.map
    - apply
  - groupby
  - pandas eda
    - info()
    - head()
    - value_counts()
    - describe
    - dtypes()
---

## pandas 자료구조

### Sereies
> **Series는 일련의 객체를 담을 수 있고 인덱스를 가지고 있는 1차원 배열의 자료구조이다.**  

- 기본적으로 고정길이의 Ordered Dictionary라고 생각하면 편하다.(사전형을 대체하여 쓸수 있다)
- index를 지정하지 않을 경우 기본색인인 정수에서 n-1까지의 숫자가 표시된다.
- Series의 배열과 색인 객체는 value와 index속성을 통해 얻을 수 있다.

```python
# Series 생성
s = pd.Series([1,2,3,4])

In [4]: s
Out[4]: 
0    1
1    2
2    3
3    4
dtype: int64
# Series 객체반환

In [6]: s.values
Out[6]: array([1, 2, 3, 4]) # 1차원 배열형태로 반환됨

In [7]: s.index
Out[7]: RangeIndex(start=0, stop=4, step=1) # range(4) 반환

# Series 생성(index 지정)

s2 = pd.Series([1,2,3,4],index = ['a','b','c','d'])

```
**사전형을 대체하여 Series 사용하기**

```python
# 조건 반환
'b' in s2

'e' in s2

# dictionary로 부터 Series 생성하기
sdic = {"A":10,"B":20,"C":40}
s3 = pd.Series(sdic)

In [9]: s3
Out[9]: 
A    10
B    20
C    40
dtype: int64
```
**Series에서 누락된 데이터 찾기**

```python

pd.isnull(s) # null인 값 찾기

pd.notnull(s) # null 아닌 값 찾기

s.isnull() # 인스턴스 메서드로 null값 찾기

```
**Series의 name속성**
- Series 객체와 index 모두 name 속성을 가질 수 있다
  - DF인덱싱, 슬라이싱에 쓸 수 있다.
- 리스트 객체를 대입하여 Series의 index를 변경할 수 있다.

```python
# name 속성 부여하기
s.name  = 'population'
obj.index.name = 'state'

# index 대입하기
df.index = ['H','J','K','L']

```
### DataFrame

> **R의 데이터 프레임의 pandas버전이다.  
> 로우와 칼럼에 대한 인덱스를 가지고 있다.**
- 단순히 인덱스와 모양이 같은 Series 객체들을 담고있는 Dictionary라고 생각하면 된다.

**DF 생성하기**
- dictionary를 이용해 쉽게 DF를 만들 수 있다.
- 인스탄스 메서드 head()를 이용해 상위 5개 값을 출력할 수 있다.
- dictionary에 없는 값을 넘길 경우 Nan으로 저장된다.
```python
# 생성
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
 'year': [2000, 2001, 2002, 2001, 2002],
 'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

df = DataFrame(data)

df.head() # 상위 5개 출력

Out[13]: 
    state  year  pop
0    Ohio  2000  1.5
1    Ohio  2001  1.7
2    Ohio  2002  3.6
3  Nevada  2001  2.4
4  Nevada  2002  2.9

df2 = pd.DataFrame(data,
                     columns=['year', 'state', 'pop', 'debt'],
                     index=['one', 'two', 'three', 'four', 'five'])


```
**loc속성과 iloc속성 활용 Series, 행열 접근하기**

1. 행번호로 접근하기 (iloc)(index location)
- **: 는 '전체' 를 의미한다. (중요!)**
- 인덱싱 범위에 따라 반환되는 객체의 타입이 달라질 수 있다(DF,Series)
```python
# 행 접근
df2.iloc[0] # 첫번째
df2.iloc[2] # 세번째
df2.iloc[-1] # 마지막 행

# 열 접근
df2.iloc[:,0] # 첫번째 열
df2.iloc[:,2] # 세번째 열
df2.iloc[:,-1] # 마지막 열

```
```python
# indexing with iloc
df2.iloc[0:4] # 첫 4개행
df2.iloc[:,0:2] # 첫 2개 열
df2.iloc[[0,2]:,[0,2]]  # 1,3 행, 1,3 열

```

2. label이나 조건으로 접근하기 (loc)(location)
- 범위지정시 loc는 포함이고 iloc나 기타 python은 포함되지 않음
- iloc의 경우 기본적으로 인덱스 기반 슬라이싱이고 loc는 이름기반 슬라이싱이어서 범위 지정시 주의 필요
```python

# 행접근
df2.loc[:,'year']
# 열접근
df2.loc[:,'year']
# 특정 값 접근
df2.loc['one','year']

# 인덱스가 숫자일 경우

df2.loc[2]

```
3. loc를 활용한 조건문 
- 조건문을 사용해 배열이나 Series, DF를 반환할 수 있다
- values를 사용해 배열을 추출할 수 있다
- **loc가 반환하는 결과는 기본적으로 copy가 아니라 view이기 때문에 값을 대입하거나 수정 할 수 있다**

```python
import pandas as pd
from random import randint
df = pd.DataFrame({'A': [randint(1, 9) for x in range(10)],
                   'B': [randint(1, 9)*10 for x in range(10)],
                   'C': [randint(1, 9)*100 for x in range(10)]})

# 조건문으로 Boolen Series 반환하기

df["B"] > 50

(df["B"] > 50) & (df["C"] == 900)

# loc에 바로 조건문을 넣을 경우

df.loc[(df["B"] > 50) & (df["C"] == 900), "A"] # 행적용 조건문

```
## 데이터 전처리 방법들(index)
### Cleaning
> **noise가 있을 경우 제거, inconsistency 수정**

### Integration
> **데이터 나누기, 합치기(필요에 따라)**

### Transformation
> **데이터형태변환 , 보통 datatype을 맞춰주거나 정규화를 하는 것을 말한다.**
### Redution
> **차원축소, 요인분석등을 사용해 분석 변수들을 줄이는 것**

## References
- https://stackoverflow.com/questions/15315452/selecting-with-complex-criteria-from-pandas-dataframe
- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.repeat.html