---
title: '[pandas]pandas의 특정 열 제외한 모든 컬럼 출력하기'
categories:
  - Preprocessing
tags:
  - pandas
  - Python
date:
updated:
---

<!--

- ML
- Statistics , Math
- Data Engineering
- Programming
- EDA & Visualization
- Data Extraction & Wrangling


## tricks
https://towardsdatascience.com/30-examples-to-master-pandas-f8a2da751fa4

#참고

https://cinema4dr12.tistory.com/1016?category=515283

https://www.kdnuggets.com/2021/07/top-python-data-science-interview-questions.html
-->

**DataFrame의 특정 열 제외하기**

---

## 하나의 컬럼을 DF에서 제거할 결우

기본적으로 두 가지 방법이 있다.

**drop 활용**
```python
df.drop(column_name, axis=1)
```

**.loc 활용**

```python
df.loc[:, df.columns != col]
```
drop이 익숙하다보니 좀 더 많이 사용하게 된다.

## 여러 컬럼을 DF에서 제거할 경우

**indexing 사용**
```python
df[df.columns[~df.columns.isin(['지울','컬럼'])]]
```


**difference 사용**
```python
df[df.columns.difference(['지울', '칼럼'])]

```

difference가 있는걸 모르고 계속 isin을 써왔다.
difference에도 익숙해져야 겠다.


## References

- https://datascience.stackexchange.com/questions/46434/dataframe-columns-difference-use