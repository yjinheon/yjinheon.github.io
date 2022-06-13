---
title: '[pandas]기본자료형을 DataFrame으로 변환하기'
categories:
    - [Preprocessing]
tags:
  - [pandas]
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


<center>Kaggle Customer Score Dataset</center>

#참고

https://cinema4dr12.tistory.com/1016?category=515283

https://www.kdnuggets.com/2021/07/top-python-data-science-interview-questions.html
-->

Python으로 데이터 분석을 하다보면 pandas를 찾게 되는 경우가 많다.
Python 기본 자료형을 pandas에서 제공하는 자료형으로 변환하는 데 익숙해지면 전처리작업을 보다 수월할게 할 수 있다.

 **여기서는 작업을 하면서 자주쓰게 되는 자료형 변환 방법들을 정리하였다**

---

아래 데이터를 사용해서 연습해보자

|   Age |   CustomerID | Genre   |
|------:|-------------:|:--------|
|    19 |            1 | Male    |
|    21 |            2 | Male    |
|    20 |            3 | Female  |
|    23 |            4 | Female  |
|    31 |            5 | Female  |


## Collection to DataFrame



### Dictionary to DataFrame

기본적으로 하나의 row가 하나의 dictionary형태로 list에 들어간다.

```python

data={'Age': {0: 19, 1: 21, 2: 20, 3: 23, 4: 31},
 'CustomerID': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5},
 'Genre': {0: 'Male', 1: 'Male', 2: 'Female', 3: 'Female', 4: 'Female'}}
df = pd.DataFrame(data)

```

### Tuple to DataFrame

Tuple은 분석단계에서보다는 DataBase와 연결해서 CRUD할 일이 있을 경우 자주 사용된다.

```python
data=[(19, 1, 'Male'),
 (21, 2, 'Male'),
 (20, 3, 'Female'),
 (23, 4, 'Female'),
 (31, 5, 'Female')]


df = pd.DataFrame(data, columns=['Age', 'ID', 'Gender'])

```

### List to DataFrame

list의 경우 `list(zip(lst, lst2, lst3))` 로 tuple 형태로 데이터를 변환해준 뒤 DF를 만든다.

```

df = pd.DataFrame(list(zip(lst, lst2, lst3)),
               columns=['Age', 'ID', 'Gender'])
df

```


## DataFrame to Collection
반대로 DataFrame에서 Python 기본 자료형을 받아야와 할 경우도 있다.

이 경우는 pandas library에서 제공하는 함수들을 통해 쉽게 해결할 수 있다.

### Dataframe to Ditonary

```python

df.to_dict()

>>{'Age': {0: 19, 1: 21, 2: 20, 3: 23, 4: 31},
 'CustomerID': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5},
 'Genre': {0: 'Male', 1: 'Male', 2: 'Female', 3: 'Female', 4: 'Female'}}

```

### Dataframe to Tuple

`itertuple()`을 사용할 시 name을 default로 넣으면 컬럼명도 같이 반환된다.

```python
list(df.itertuples(index=False,name=None)) # df to tuple

>>[(19, 1, 'Male'),
 (21, 2, 'Male'),
 (20, 3, 'Female'),
 (23, 4, 'Female'),
 (31, 5, 'Female')]

```

### DataFrame to List

컬럼을 list로 변환

```python
df.columns.values.tolist()
```

값을 list로 변환

```python
df.values.tolist()

>>[[19, 1, 'Male'],
 [21, 2, 'Male'],
 [20, 3, 'Female'],
 [23, 4, 'Female'],
 [31, 5, 'Female']]
```

## References

- https://www.geeksforgeeks.org/create-a-pandas-dataframe-from-lists/
- https://stackoverflow.com/questions/9758450/pandas-convert-dataframe-to-array-of-tuples