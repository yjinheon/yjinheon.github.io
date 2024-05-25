<!-- MarkdownTOC -->

- [File Processing(Reading, Writing File)](#file-processingreading-writing-file)
  - [File and Dictionary Access](#file-and-dictionary-access)
  - [File Reading](#file-reading)
    - [json](#json)
  - [numpy](#numpy)
    - [numpy basics](#numpy-basics)
      - [boolen indexing](#boolen-indexing)
      - [fancy indexing](#fancy-indexing)
    - [numpy 배열 변형하기(array transformation)](#numpy-배열-변형하기array-transformation)
      - [Transpose](#transpose)
      - [Changing Array Shape](#changing-array-shape)
      - [np.reshape](#npreshape)
      - [Adding/Removing Elements](#addingremoving-elements)
      - [Combine array](#combine-array)
    - [Split array](#split-array)
    - [numpy method](#numpy-method)
      - [np.where](#npwhere)
      - [np.select](#npselect)
      - [np.log](#nplog)
      - [np.sort(배열 정렬하기)](#npsort배열-정렬하기)
      - [np.pad](#nppad)
      - [np.argwhere](#npargwhere)
    - [numpy broadcasting](#numpy-broadcasting)
      - [numpy 통계](#numpy-통계)
      - [numpy boolen](#numpy-boolen)
      - [numpy 선형대수](#numpy-선형대수)
      - [numpy 집합 함수들](#numpy-집합-함수들)
      - [numpy sampling](#numpy-sampling)
  - [pandas](#pandas)
    - [Creating Pandas Object](#creating-pandas-object)
      - [Series](#series)
      - [DataFrame](#dataframe)
        - [DF methods](#df-methods)
        - [DF 생성하기](#df-생성하기)
    - [Viewing Data](#viewing-data)
      - [type casting](#type-casting)
    - [Sampling Data](#sampling-data)
    - [Data Selection](#data-selection)
    - [Reshaping](#reshaping)
    - [Operations](#operations)
      - [apply](#apply)
      - [applymap](#applymap)
      - [agg](#agg)
      - [aggregate](#aggregate)
    - [Maipulation](#maipulation)
      - [Renaming Colunm](#renaming-colunm)
      - [Removing Column](#removing-column)
    - [Grouping Data](#grouping-data)
  - [응용 하기](#응용-하기)
    - [Merging,Joining and Concatenating](#mergingjoining-and-concatenating)
    - [Exporting data](#exporting-data)
    - [옮길 것들](#옮길-것들)
    - [Textdata](#textdata)
      - [regex](#regex)
      - [replace](#replace)
      - [match](#match)
    - [Date and Time](#date-and-time)
    - [Miscellaneous](#miscellaneous)
      - [vlookup](#vlookup)
  - [결측값 처리(Missing value)](#결측값-처리missing-value)
    - [결측치 관련 함수](#결측치-관련-함수)
    - [결측치 처리](#결측치-처리)
- [결측치 개수 파악](#결측치-개수-파악)
- [결측치 비율 파악](#결측치-비율-파악)
    - [imputer](#imputer)
  - [Read/Write File](#readwrite-file)
- [EDA](#eda)
  - [dlookr](#dlookr)
  - [pingouin](#pingouin)
  - [데이터를 받았을 때 해야하는 것](#데이터를-받았을-때-해야하는-것)
    - [DF 확인](#df-확인)
  - [Descriptive Stataistics](#descriptive-stataistics)
    - [IQR](#iqr)
    - [단일변수 분석](#단일변수-분석)
    - [상관관계 분석](#상관관계-분석)
  - [Type Checking \& Casting (데이터 타입변환)](#type-checking--casting-데이터-타입변환)
    - [Type Checeking](#type-checeking)
  - [Reshaping(데이터 재구조화)](#reshaping데이터-재구조화)
  - [데이터 클리닝(missign)](#데이터-클리닝missign)
  - [텍스트 데이터 전처리](#텍스트-데이터-전처리)
  - [시계열 데이터 전처리](#시계열-데이터-전처리)
  - [연관성 검정](#연관성-검정)
    - [numerical data : 상관분석, 다중공선성 겸정](#numerical-data--상관분석-다중공선성-겸정)
    - [categorical data : 독립성 검정](#categorical-data--독립성-검정)

<!-- /MarkdownTOC -->

# File Processing(Reading, Writing File)

- python doc  libraries

## File and Dictionary Access

- []()

## File Reading

### json

```python
def load_train_json(path):
    f = pd.read_json(path ,typ = 'frame', encoding="utf-8")
    df = pd.DataFrame(f)
    df = df.sort_values(by=['like_cnt'],ascending=False)
    df = df[df['like_cnt']>10]
    print('load_train_json')
    return df


def load_val_json(path):
    f = pd.read_json(path ,typ = 'frame', encoding="utf-8")
    df = pd.DataFrame(f)
    df = df.sort_values(by=['like_cnt'],ascending=False)
    print('load_test_json')
    return df

def load_meta_json(path):
    f = pd.read_json(path ,typ = 'frame', encoding="utf-8")
    df = pd.DataFrame(f)
    print('load_meta_json')
    return df
```

## numpy

**numpy 기능들**

- 벡터 배열상에서 데이터 가공, 정제, 부분집합 필터링, 변형 및 기타연산
- 정렬, unique 탐색, 집합연산같은 일반적인 배열처리 알고리즘

numpy의 중요한 특징은 **파이썬 반복문을 사용하지 않고** 대용량 배열에 대한 복잡한 연산이 가능하다는 것.

### numpy basics

- 배열 생성

```python
In [5]: import numpy as np
   ...: arr = np.arange(0,10) # 0에서 9까지 의 
   ...:
   ...: arr.reshape(2,5) # 배열 형태 변환
Out[5]:
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])

In [6]: import numpy as np
   ...: arr = np.arange(0,10)
   ...:
   ...: arr=arr.reshape(2,5)
```

- 배열 형태 확인(ndim,shape,len)

```python
In [7]: arr.ndim # 차원 수
Out[7]: 2

In [8]: arr.shape # 모양
Out[8]: (2, 5)

In [9]: len(arr)
Out[9]: 10
```

- 배열 데이터 타입 확인(dtype)

```python
In [15]: arr_2 = np.random.rand(5)

In [16]: arr_2
Out[16]: array([0.55155657, 0.32745746, 0.92681611, 0.04614794, 0.17832697])

In [17]: arr_2.dtype
Out[17]: dtype('float64')

In [18]: arr_3 = np.array([5,6,7],dtype = np.float64)

In [19]: arr_3.dtype
Out[19]: dtype('float64')
```

- 배열 데이터 타입 변환(astype)

```python
In [24]: arr_2=arr_2.astype(np.int64)

In [25]: arr_2.dtype
Out[25]: dtype('int64')

In [26]: arr_3=arr_3.astype(np.int64)

In [27]: arr_3.dtype
Out[27]: dtype('int64')
```

**배열 생성함수들**

- `array` : 입력데이터를 다차원 배열로 변환.
- `arange` : `range`와 동일하지만 다차원 배열을 반환.
- `np.empty(a)` ,`np.empty_like(M)` : 0 이나 1로 값을 초기화하지 않은 배열을 반환.
- `np.ones(a)` : a 크기의 1으로 채워진 배열을 반환 
- `np.ones_like(M)` M 배열의 사이즈와 같은 1으로 채워진 배열을 반환
- `np.zeros(a)` : a 크기의 0으로 채워진 배열을 반환 
- `np.zeros_like(M)` M 배열의 사이즈와 같은 0으로 채워진 배열을 반환
- **`np.full` :인자로 값과 형태를 받고. 인자로 받은 형태에 값을 채운다. (자주 쓴다.)**
  
```python
  # np full 용법
```

```
- `np.full_like` : 인자로 값과 형태를 받고. 인자로 받은 형태에 값을 채운다.
- `eye` , `identity`: N * N 크기의 단위행렬생성
- `np.random.rand(n)` : n 크기 난수 배열 생성

### numpy indexing

- 기본 파이썬 list indexing과 유사하지만 차원이 복잡해지면 어려워진다.

#### 기초 슬라이싱과 인덱싱

- 기본적으로 list의 그것과 다를 건 없다.
- `i:j:k` 형태로 인덱싱한다.
    + i는 starting index 
    + j는 stopping index(j-1 까지 슬라이싱된다.)
    + k는 step

```python

In [1]: import numpy as np

In [2]: x = np.array(range(10))

In [3]: x[1:7:2]
Out[3]: array([1, 3, 5])

In [4]: x[-2:10]
Out[4]: array([8, 9])

In [5]: x[-3:3:-1]
Out[5]: array([7, 6, 5, 4])

In [6]: x[5:]
Out[6]: array([5, 6, 7, 8, 9])
```

- 인덱스 리스트를 통해 쉽게 배열의 값에 접근할 수 있다.

```python
In [50]: arr_2d = np.arange(1,10).reshape(3,3)

In [51]: arr_2d
Out[51]:
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])

In [52]: arr_2d[0][2]
Out[52]: 3

# 보통 두 번째 방법을 많이 사용한다.

In [53]: arr_2d[0,2]
Out[53]: 3
```

- 다차원 슬라이싱하기

```python
In [54]: arr_2d[:2,1:]
Out[54]:
array([[2, 3],
       [5, 6]])
```

- 좀 복잡한 형태의 다차원 슬라이싱

![](https://media.geeksforgeeks.org/wp-content/uploads/Numpy1.jpg)

```python
# 다차원 배열 인덱싱 예시
 [[0  1  2  3  4  5] 
  [6 7 8 9 10 11]
  [12 13 14 15 16 17]
  [18 19 20 21 22 23]
  [24 25 26 27 28 29]
  [30 31 32 33 34 35]]

a[0, 3:5]  =  [3 4]

a[4:, 4:] = [[28 29],
             [34 35]]

a[:, 2] =  [2 8 14 20 26 32]

a[2:;2, ::2] = [[12 14 16],
                [24 26 28]]
```

- `:` 연산자를 통해  `:` 가 위치하는 축의 모든 값에 접근할 수 있다.
- 배열 자체에 `[:]` 를 사용할 경우 배열의 모든 값이 할당된다.
  + **기본적으로 데이터가 복사되지 않는다.**
  + 데이터를 복사해야 할 경우 `copy` 함수를 따로 사용한다.

```python
In [44]: arr
Out[44]:
array([[0.23061655, 0.86734388, 0.27967631],
       [0.63734555, 0.47048728, 0.04833744],
       [0.99362969, 0.87636748, 0.59988875]])

In [45]: arr[:,1]
Out[45]: array([0.86734388, 0.47048728, 0.87636748])

In [46]: arr[:,1]
Out[46]: array([0.86734388, 0.47048728, 0.87636748])

In [47]: arr[:]
Out[47]:
array([[0.23061655, 0.86734388, 0.27967631],
       [0.63734555, 0.47048728, 0.04833744],
       [0.99362969, 0.87636748, 0.59988875]])
```

- **배열의 일부(subset)는 원본배열의 View 이기 때문에 파이썬 `list` 와 달리 배열의 일부에 대한 변경은 그대로 원본배열에 반영된다.**

```python
In [28]: arr_new = np.arange(10)

In [29]: arr_new[4:7] = 10

In [30]: arr_new
Out[30]: array([ 0,  1,  2,  3, 10, 10, 10,  7,  8,  9])
```

#### boolen indexing

- 실질적으로 가장 자주쓰는 인덱싱이다.

```python
In [62]: temp=np.random.rand(3,3)

In [63]: temp[temp>0.5]
Out[63]:
array([0.77402793, 0.59064775, 0.67170741, 0.51967736, 0.75161734,
       0.98559447])
```

#### fancy indexing

- 인덱싱과 슬라이싱의 차이는 입력된 범위의 값을 가져오느냐 연속된 값들을 가져오느냐의 차이밖에 없다.

```python
In [56]: array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    ...:
    ...: 
    ...: array[[0, 2], :3]
Out[56]:
array([[1, 2, 3],
       [7, 8, 9]])
```

### numpy 배열 변형하기(array transformation)

#### Transpose

```python
 i = np.transpose(b) Permute array dimensions
 i.T Permute array dimensions
```

#### Changing Array Shape

```python
b.ravel() [[Flatten]] the array
g.reshape(3,-2) [[Reshape]], but don’t change data
b.flatten() # rabel() 과 같지만 배열의 copy를 생성
```

#### np.reshape

- n차원 배열 flatten관련해서 특히 중요하다.

- reshape()의 '-1'이 의미는, 변경된 배열의 '-1' 위치의 차원은 "원래 배열의 길이와 남은 차원으로 부터 추정"이 된다는 것이다.

- -1외의 나머지 차원에 의해서 -1에 해당하는 차원이 결정된다고 생각하면 편하다.

- `np.reshape(-1)` 인 경우 단순히 1차원 배열을 반환한다.

- 행자리에 -1이 있을 경우(-1,)
  
  ```python
  In [1]: import numpy as np
  ```

In [2]: arr = np.arange(1,13)

In [3]: arr
Out[3]: array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])

In [4]: arr.reshape(-1,2)
Out[4]:
array([[ 1,  2],
       [ 3,  4],
       [ 5,  6],
       [ 7,  8],
       [ 9, 10],
       [11, 12]])

In [5]: arr.reshape(-1,3)
Out[5]:
array([[ 1,  2,  3],
       [ 4,  5,  6],
       [ 7,  8,  9],
       [10, 11, 12]])

```
- 열자리에 -1이 있을 경우

```python

In [1]: import numpy as np

In [2]: arr = np.arange(1,13)

In [3]: arr.reshape(2,-1)
Out[3]:
array([[ 1,  2,  3,  4,  5,  6],
       [ 7,  8,  9, 10, 11, 12]])

In [4]: arr.reshape(3,-1)
Out[4]:
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
```

#### Adding/Removing Elements

```python
 h.resize((2,6)) Return a new array with shape (2,6)
 np.append(h,g) Append items to an array
 np.insert(a, 1, 5) Insert items in an array
 np.delete(a,[1]) Delete items from an array
```

#### Combine array

```python
In [11]: arr_1 = np.arange(1,5)

In [12]: arr_2 = np.arange(6,10)

In [13]: np.concatenate((arr_1,arr_2),axis=0)
Out[13]: array([1, 2, 3, 4, 6, 7, 8, 9])

In [14]: np.vstack((arr_1,arr_2))
Out[14]:
array([[1, 2, 3, 4],
       [6, 7, 8, 9]])

In [15]: np.r_[arr_1,arr_2]
Out[15]: array([1, 2, 3, 4, 6, 7, 8, 9])

In [16]: np.hstack((arr_1,arr_2))
Out[16]: array([1, 2, 3, 4, 6, 7, 8, 9])

In [17]: np.c_[arr_1,arr_2]
Out[17]:
array([[1, 6],
       [2, 7],
       [3, 8],
       [4, 9]])
```

### Split array

```python
In [19]: np.hsplit(arr_1,2)
Out[19]: [array([1, 2]), array([3, 4])]


In [24]: arr_3 = np.arange(1,10).reshape(3,3)

# 행 단위 split

In [25]: np.vsplit(arr_3,3)
Out[25]: [array([[1, 2, 3]]), array([[4, 5, 6]]), array([[7, 8, 9]])]
```

### numpy method

- 위의 3개가 중요하고 그 아래는 그다지 쓸 일이 없다.

#### np.where

- `np.where(조건,if true 값,else 값)` 방식으로 사용한다.
- 기본적으로 조건에 기반해 새로운 배열을 생성한다.
- **logical statement를 vectorize한다.**

```python
Out[63]: df
   A   B   C     D
0  9  14  10  0.24
1  8   2  17  0.56
2  3  18  16  0.12
3  3   4  16  0.88
4  9   8  16  0.61
5  7   3  17  0.44



In [64]: df["E"] = np.where((df["B"] > 10) & (df["C"] > 10), 1, 0)
    ...: df
Out[64]:
   A   B   C     D  E
0  9  14  10  0.24  0
1  8   2  17  0.56  0
2  3  18  16  0.12  1
3  3   4  16  0.88  0
4  9   8  16  0.61  0
5  7   3  17  0.44  0
```

#### np.select

- `np.where`의 multiple condition 버전이다.
- 2개 이상의 조건을 한번에 처리해야 할경우 pandas를 사용하는 것 보다 `np.select`를 활용해 한번에 처리하는 것이 낫다.

![](https://i.imgur.com/Z3XHteT.png)

```python
# np select 예시
In [65]: conditions = [
    ...:   (df["B"] >= 10) & (df["A"] == 0),
    ...:   (df["B"] >= 10) & (df["A"] == 8)
    ...: ]
    ...: values = [1, 2]
    ...: df["F"] = np.select(conditions, values, default=0)
    ...: df
    ...:
Out[65]:
   A   B   C     D  E  F
0  9  14  10  0.24  0  0
1  8   2  17  0.56  0  0
2  3  18  16  0.12  1  0
3  3   4  16  0.88  0  0
4  9   8  16  0.61  0  0
5  7   3  17  0.44  0  0
```

#### np.log

- 자연로그를 리턴한다.
  - np.log(np.e) 는 1을 리턴한다.
- 데이터 정규화시 사용.

```python
np.log([1, np.e, np.e**2, 0])
array([  0.,   1.,   2., -Inf])
```

#### np.sort(배열 정렬하기)

- `np.sort(M)` 로 배열을 정렬한다.
  + M.sort() 는 배열 자체를 정렬한 결과를 리턴하지만 `np.sort(M)`은 배열의 복사본을 정렬해 리턴한다,

```python
In [39]: arr_1d = np.random.randint(0, 10, 10)
    ...:
    ...: arr_2d = np.random.randint(0, 10, (3, 4))
    ...:
    ...: print(arr_1d)
    ...: print(arr_2d)
[2 0 1 8 5 2 8 0 3 9]
[[8 4 3 1]
 [0 4 6 7]
 [2 1 0 5]]

In [40]: print(np.sort(arr_1d))
[0 0 1 2 2 3 5 8 8 9]
```

- `np.sort(M)[::-1]` : 역순 정렬  

```python
In [41]: print(np.sort(arr_1d)[::-1])
[9 8 8 5 3 2 2 1 0 0]
```

- 행과 열 기준으로 정렬이 가능하다.
  + `np.sort(x, axis=1)` : 열 기준
  + `np.sort(x, axis=0)` : 행 기준

```python
In [42]: print(np.sort(arr_2d, axis=0))
    ...: print(np.sort(arr_2d, axis=1))
[[0 1 0 1]
 [2 4 3 5]
 [8 4 6 7]]
[[1 3 4 8]
 [0 4 6 7]
 [0 1 2 5]]
```

#### np.pad

- 배열을 일정한 고정길이로 만들기 위해 특정한 값으로 채우는 함수.

```python
Z = np.ones((5,5))
Z.pad(pad_width=1, 
      mode='constant', # 특정한 값을 지정해서 패딩할 경우
      constant_values=0) # 값 지정

Z      
[[0. 0. 0. 0. 0. 0. 0.]
 [0. 1. 1. 1. 1. 1. 0.]
 [0. 1. 1. 1. 1. 1. 0.]
 [0. 1. 1. 1. 1. 1. 0.]
 [0. 1. 1. 1. 1. 1. 0.]
 [0. 1. 1. 1. 1. 1. 0.]
 [0. 0. 0. 0. 0. 0. 0.]]
```

- 2차원 배열 패딩

```python
In [16]: m = np.arange(1,9).reshape(2,4)

In [17]: m
Out[17]:
array([[1, 2, 3, 4],
       [5, 6, 7, 8]])


## 행과 열 모두 2개씩 0으로 패딩 
In [20]: np.pad(m,((2,2),(2,2)),'constant',constant_values =0)
Out[20]:
array([[0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 2, 3, 4, 0, 0],
       [0, 0, 5, 6, 7, 8, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0]])


In [21]: np.pad(m,((1,2),(2,3)),'constant',constant_values =0)
Out[21]:
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 2, 3, 4, 0, 0, 0],
       [0, 0, 5, 6, 7, 8, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]])
```

#### np.argwhere

- `np.argwhere(condition)`은 배열에서 조건에 해당하는 값의 인덱스를 리턴한다.

```python
x = np.arange(6).reshape(2,3)
>>>x
array([[0, 1, 2],
       [3, 4, 5]])
>>>np.argwhere(x>1)
array([[0, 2],
       [1, 0],
       [1, 1],
       [1, 2]])
```

### numpy broadcasting

- numpy의 연산은 기본적으로 같은 크기의 배열간의 연산을 전제한다.

- 하지만 특정 조건을 만족했을 때 numpy는 자동적으로 크기가 다른 배열간의 연산을 수행하기도 하는데 이를 `broadcasting`이라 한다.

- `broadcasting` 연산이 성립되기 위한 다음의 3가지 규칙이 존재한다.
  
  + **규칙 1: 두 배열의 차원 수가 다를 경우, 크기가 작은 배열의 모양은 맨 앞(왼쪽)에 패딩됨**
  + **규칙 2: 두 배열의 모양이 임의의 차원에서 일치하지 않으면 해당 차원에서 모양이 1인 배열은 다른 모양과 일치하도록 확장됨**
  + **규칙 3: 어떤 차원에서든 크기가 일치하지 않고 둘 다 1과 같지 않으면 오류가 발생.**

- **단순히 한쪽의 크기를 맞춰서 연산이 가능하게끔 만드는 것이라고 생각하면 이해하기 쉽다.**

![](https://jakevdp.github.io/PythonDataScienceHandbook/figures/02.05-broadcasting.png)

- `a` 의 차원이 더 작기 때문에 규칙 1,2 에 따라 연산시 `a` 가 padding 되고 확장됨.

```python
In [5]: M = np.ones((2, 3))
   ...: a = np.arange(3)

In [6]: print(M.shape)
(2, 3)

In [7]: print(a.shape)
(3,)

In [8]: M + a
Out[8]:
array([[1., 2., 3.],
       [1., 2., 3.]])

In [9]: a.shape
Out[9]: (3,)
```

**ref**

- [Numpy 공식문서](https://numpy.org/doc/stable/index.html)
- [numpy array transfrormation](https://www.datacamp.com/community/blog/python-numpy-cheat-sheet)
- [numpy indexing](https://www.geeksforgeeks.org/numpy-indexing/)
- [numpy broadcasting](https://jakevdp.github.io/PythonDataScienceHandbook/02.05-computation-on-arrays-broadcasting.html)
- [numpy padding](https://sparrow.dev/numpy-pad/)
- [numpy select](https://towardsdatascience.com/3-numpy-functions-to-facilitate-data-analysis-with-pandas-b1ad342a569)

#### numpy 통계

**no blog**

- a.sum() : Array-wise sum

- a.min() : Array-wise minimum value

- b.max(axis=0) :Maximum value of an array row

- b.cumsum(axis=1): Cumulative sum of the elements

- a.mean() : Mean

- b.median() : Median

- a.corrcoef() :Correlation coefficient

- np.std(b) : standarddeviation

- np.histogram : 객체를 구간수로 구분하여 각 구간수에 속하는 빈도수 리턴. `np.histogram([1, 2, 1], bins=[0, 1, 2, 3])`

- np.bincount : 0부터 가장 큰 값까지 각각의 발생 빈도수를 체크

#### numpy boolen

- no blog

#### numpy 선형대수

#### numpy 집합 함수들

- `np.unique` 함수 말고 다른 함수는 거의 쓸일이 없다.
- `np.unique(array)` : 고윳값
- `np.union1d(array,array)`: 합집합
- `np.intersect1d(array,array,assume_unique)` : 교집합
- `np.setdiff1d(arr1, arr2, assume_unique=True)` : 차집합
- `np.setxor1d(arr1, arr2, assume_unique=True)` : 대칭차집합(교집합의 여집합)

#### numpy sampling

- `np.random.seed` : 초기값설정. 재현성 확보
- `np.random.randint : 균일 분포의 정수 난수 1개
- `np.random.rand` : 0부터 1사이의 균일 분포에서 random 다차원 배열 반환
- `np.random.randn` : 가우시안 표준 정규 분포에서 random 다차원 배열 반환
- `np.random.shuffle`: 기존 배열의 순서 섞기
- `np.random.permutaion` : 기존 배열은 냅두고, 순서를 랜덤하게 섞은 배열 객체를 새로 생성
- `np.random.choice` : 1차원 배열로부터 랜덤 복원/비복원 추출(replace)
- `np.bincount` : 0 부터 객체x의 최대값인 9까지 각 원소의 빈도수를 계산
- `binomial`
- `normal`
- `beta`
- `chisqare`
- `gamma`

## pandas

- sample df는 무조건 penguins에서 랜덤 샘플링 30개

```python
import pandas as pd
import seaborn as sns

penguins = sns.load_dataset("penguins")
df = penguins.sample(30)

print(df)
```

### Creating Pandas Object

#### Series

#### DataFrame

##### DF methods

- `df.values` : df의 값을 배열형태로 리턴한다.

```python
   species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
221  Gentoo     Biscoe            50.0           16.3              230.0       5700.0    Male
145  Adelie      Dream            39.0           18.7              185.0       3650.0    Male
128  Adelie  Torgersen            39.0           17.1              191.0       3050.0  Female
292  Gentoo     Biscoe            48.2           15.6              221.0       5100.0    Male
89   Adelie      Dream            38.9           18.8              190.0       3600.0  Female
295  Gentoo     Biscoe            48.6           16.0              230.0       5800.0    Male
119  Adelie  Torgersen            41.1           18.6              189.0       3325.0    Male
88   Adelie      Dream            38.3           19.2              189.0       3950.0    Male
338  Gentoo     Biscoe            47.2           13.7              214.0       4925.0  Female
136  Adelie      Dream            35.6           17.5              191.0       3175.0  Female

In [22]: df.values
Out[22]:
array([['Gentoo', 'Biscoe', 50.0, 16.3, 230.0, 5700.0, 'Male'],
       ['Adelie', 'Dream', 39.0, 18.7, 185.0, 3650.0, 'Male'],
       ['Adelie', 'Torgersen', 39.0, 17.1, 191.0, 3050.0, 'Female'],
       ['Gentoo', 'Biscoe', 48.2, 15.6, 221.0, 5100.0, 'Male'],
       ['Adelie', 'Dream', 38.9, 18.8, 190.0, 3600.0, 'Female'],
       ['Gentoo', 'Biscoe', 48.6, 16.0, 230.0, 5800.0, 'Male'],
       ['Adelie', 'Torgersen', 41.1, 18.6, 189.0, 3325.0, 'Male'],
       ['Adelie', 'Dream', 38.3, 19.2, 189.0, 3950.0, 'Male'],
       ['Gentoo', 'Biscoe', 47.2, 13.7, 214.0, 4925.0, 'Female'],
       ['Adelie', 'Dream', 35.6, 17.5, 191.0, 3175.0, 'Female']],
      dtype=object)
```

- df.columns : 컬럼 라벨을 반환한다.
  + 대개의 경우 list로 변환해서 사용한다.

```python
In [26]: df.columns
Out[26]:
Index(['species', 'island', 'bill_length_mm', 'bill_depth_mm',
       'flipper_length_mm', 'body_mass_g', 'sex'],
      dtype='object')

In [27]: df.columns.tolist()
Out[27]:
['species',
 'island',
 'bill_length_mm',
 'bill_depth_mm',
 'flipper_length_mm',
 'body_mass_g',
 'sex']
```

##### DF 생성하기

| Age | CustomerID | Genre  |
| ---:| ----------:|:------ |
| 19  | 1          | Male   |
| 21  | 2          | Male   |
| 20  | 3          | Female |
| 23  | 4          | Female |
| 31  | 5          | Female |

**Collection to DataFrame**

- Dictionary to DataFrame

기본적으로 하나의 row가 하나의 dictionary형태로 list에 들어간다.

```python
data={'Age': {0: 19, 1: 21, 2: 20, 3: 23, 4: 31},
 'CustomerID': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5},
 'Genre': {0: 'Male', 1: 'Male', 2: 'Female', 3: 'Female', 4: 'Female'}}
df = pd.DataFrame(data)
```

- Tuple to DataFrame

Tuple은 분석단계에서보다는 DataBase와 연결해서 CRUD할 일이 있을 경우 자주 사용된다.

```python
data=[(19, 1, 'Male'),
 (21, 2, 'Male'),
 (20, 3, 'Female'),
 (23, 4, 'Female'),
 (31, 5, 'Female')]


df = pd.DataFrame(data, columns=['Age', 'ID', 'Gender'])
```

- List to DataFrame

list의 경우 `list(zip(lst, lst2, lst3))` 로 tuple 형태로 데이터를 변환해준 뒤 DF를 만든다.

```python
df = pd.DataFrame(list(zip(lst, lst2, lst3)),
               columns=['Age', 'ID', 'Gender'])
df
```

**DataFrame to Collection**

반대로 DataFrame에서 Python 기본 자료형을 받아야와 할 경우도 있다.

이 경우는 pandas library에서 제공하는 함수들을 통해 쉽게 해결할 수 있다.

- Dataframe to Ditonary

```python
df.to_dict()

>>{'Age': {0: 19, 1: 21, 2: 20, 3: 23, 4: 31},
 'CustomerID': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5},
 'Genre': {0: 'Male', 1: 'Male', 2: 'Female', 3: 'Female', 4: 'Female'}}
```

- Dataframe to Tuple

`itertuple()`을 사용할 시 name을 default로 넣으면 컬럼명도 같이 반환된다.

```python
list(df.itertuples(index=False,name=None)) # df to tuple

>>[(19, 1, 'Male'),
 (21, 2, 'Male'),
 (20, 3, 'Female'),
 (23, 4, 'Female'),
 (31, 5, 'Female')]
```

- DataFrame to List

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

### Viewing Data

- info
- describe
- shape
- pydatalook
- 결측치 이상치 확인
- 히스토그램
- pandas profiliing : 반드시 최신버전으로 업데이트 할 것
- type 확인

#### type casting

https://stackoverflow.com/questions/40095712/when-to-applypd-to-numeric-and-when-to-astypenp-float64-in-python

- [Type Casting 무지성 카피할 것](https://stackoverflow.com/questions/15891038/change-column-type-in-pandas)

### Sampling Data

### Data Selection

- `filter`를 통해 sql 처럼 열 선택

```python
# select columns containing 'a'

In [3]: df.filter(like='a',axis=1).head()
   ...:
   ...:
Out[3]:
     island  body_mass_g
167   Dream       4050.0
207   Dream       3450.0
295  Biscoe       5800.0
139   Dream       4250.0
106  Biscoe       3750.0
```

- 정규식를 활용한 열 필터링

```python
# select columns using regex
df.filter(regex='b$',axis=1)
```

- `axis=0` 인 경우 index를 기준으로 필터링하기 때문에 index가 문자열인 경우를 제외하면 굳이 쓸 일이 없다.

```python
In [8]: df
Out[8]:
       Name  Age
0    Harris   20
1    Taylor   27
2      Lucy   29
3  Nicholas   20

In [9]: df.filter(regex='1',axis=0)
Out[9]:
     Name  Age
1  Taylor   27
```

### Reshaping

- 테이블 형태 자체를 바꾸기

### Operations

- 파생변수 만들기
- 하나의 테이블에서 다른 파생테이블을 만들기 ex) 요약통계량 테이블

#### apply

#### applymap

#### agg

#### aggregate

### Maipulation

#### Renaming Colunm

- 특정 칼럼을 대체하기

```python
df = df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'})
# Or rename the existing DataFrame (rather than creating a copy) 
df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'}, inplace=True)
```

#### Removing Column

**DataFrame의 특정 열 제외하기**

- **하나의 컬럼을 DF에서 제거할 결우**

기본적으로 두 가지 방법이 있다.

**drop 활용**

```python
df.drop(column_name, axis=1)
```

**.loc 활용**

```python
col = ['사용할','컬럼']

df.loc[:, df.columns != col]
```

drop이 익숙하다보니 좀 더 많이 사용하게 된다.

- **여러 컬럼을 DF에서 제거할 경우**

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

**ref**

- https://datascience.stackexchange.com/questions/46434/dataframe-columns-difference-use

### Grouping Data

**기본적인 용법들**

- 데이터 불러오기

```python
# 데이터 불러오기
In [1]: import pandas as pd
   ...: drinks = pd.read_csv('http://bit.ly/drinksbycountry')
   ...: drinks.head()
Out[1]:
       country  beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol continent
0  Afghanistan              0                0              0                           0.0      Asia
1      Albania             89              132             54                           4.9    Europe
2      Algeria             25                0             14                           0.7    Africa
3      Andorra            245              138            312                          12.4    Europe
4       Angola            217               57             45                           5.9    Africa
```

- 대륙별 beer_servings 평균

```python
drinks.groupby('continent').beer_servings.mean()

Out[2]:
continent
Africa            61.471698
Asia              37.045455
Europe           193.777778
North America    145.434783
Oceania           89.687500
South America    175.083333
Name: beer_servings, dtype: float64
```

- `.agg()`와 같은 집계함수를 사용해 한 변수의 여러 요약통계량을 구하는 것이 가능하다.

```python
drinks[drinks.continent=='Asia'].beer_servings.agg(['count','mean','max','min'])

Out[3]:
count     44.000000
mean      37.045455
max      247.000000
min        0.000000
Name: beer_servings, dtype: float64
```

- `groupby`를 통해 대륙별 요약통계량 구하기

```python
drinks.groupby('continent').beer_servings.agg(['count','mean','max','min'])

               count        mean  max  min
continent
Africa            53   61.471698  376    0
Asia              44   37.045455  247    0
Europe            45  193.777778  361    0
North America     23  145.434783  285    1
Oceania           16   89.687500  306    0
South America     12  175.083333  333   93
```

- 분석할 칼럼을 지정해주지 않으면 모든 numeric의 평균을 그룹별로 반환한다.

```python
drinks.groupby('continent').mean()

               beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol
continent
Africa             61.471698        16.339623      16.264151                      3.007547
Asia               37.045455        60.840909       9.068182                      2.170455
Europe            193.777778       132.555556     142.222222                      8.617778
North America     145.434783       165.739130      24.521739                      5.995652
Oceania            89.687500        58.437500      35.625000                      3.381250
South America     175.083333       114.750000      62.416667                      6.308333
```

- group by 시각화

```python
# m
%matplotlib inline
drinks.groupby('continent').mean().plot(kind='bar')
```

![](https://i.imgur.com/KvoD6CS.png)    

- 데이터를 long form으로 바꾸고 `seaborn`을 활용해 구현할수도 있다.

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

drinks_melt = pd.melt(drinks, id_vars=['country', 'continent'], var_name='beberage_type', value_name='servings')
plt.figure(figsize=(8,4)) # avoid overlapping
sns.barplot(x='continent', y='servings', hue='beberage_type', data=drinks_melt, estimator=np.mean)
plt.show()
```

## 응용 하기

- Groupby에서 특정 그룹에 접근하기
- Groupby에서 특정 그룹에 접근 후 필터링 하기 (filter 사용)
- pd.cut 을 사용한 파생변수 만들기

- `get_group`으로 아시아 그룹만 접근

```python
drinks.groupby('continent').get_group('Asia').head()

Out[9]:
        country  beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol continent
0   Afghanistan              0                0              0                           0.0      Asia
12      Bahrain             42               63              7                           2.0      Asia
13   Bangladesh              0                0              0                           0.0      Asia
19       Bhutan             23                0              0                           0.4      Asia
24       Brunei             31                2              1                           0.6      Asia
```

- 여러 그룹의 통계량을 조건걸어서 구할 경우

```python
In [10]: drinks.groupby(['wine_servings', 'continent']).get_group((0, 'Asia')).total_litres_of_pure_al
    ...: cohol.sum()
    ...:
Out[10]: 6.2
```

```python
# pd.cut을 활용한 연속형 변수의 구간화 변수생성
drinks['Range'] = drinks.groupby('country').beer_servings.apply(pd.cut, bins=2)
drinks.head()
```

TF를 반환하는 lamba 함수를 작성할 경우 any()나 all()을 써서 값을 반환해줄 필요가 있다.

```python
## filter를 사용한 조건식. 위의 결과와 같은 값을 리턴한다.
drinks.groupby(['wine_servings','continent']).filter(lambda x : ((x.wine_servings == 0) & (x.continent=='Asia') ).any()).total_litres_of_pure_alcohol.sum()
```

**ref**

* https://www.youtube.com/watch?v=qy0fDqoMJx8
* https://pandas.pydata.org/docs/reference/groupby.html

### Merging,Joining and Concatenating

- 여러 테이블 합치기

### Exporting data

- https://stackoverflow.com/questions/36977223/how-should-i-read-a-csv-file-without-the-unnamed-row-with-pandas

두 가지 모두 알아야 함

```python
df.to_csv('file.csv', index=False)
df = pd.read_csv('file.csv', index_col=0)
```

### 옮길 것들

**DF handling**

- index
- values
- columns
- dtypes
- info
- select_dtypes
- loc
- iloc
- insert
- head
- tail
- apply
- applymap
- aggregate
- drop
- rename
- replace
- nsmallest
- nlargest
- sort_values
- sort_index
- value_counts
- describe

### Textdata

#### regex

#### replace

#### match

### Date and Time

### Miscellaneous

#### vlookup

* any()와 all() 관련 함수
* filter
* assign
* pd.cut과 np.digitize를 활용한 연속형 변수의 구간화
* pandas query as dplyr filter

## 결측값 처리(Missing value)

### 결측치 관련 함수

**Missing data**

- isna
- isnull
- notna
- notnull
- dropna
- fillna

### 결측치 처리

- 결측치 파악
  
  ```python
  
  ```

# 결측치 개수 파악

df.isnull().sum().to_frame('count_nan')

# 결측치 비율 파악

pd.DataFrame(data=df.isnull().sum()/len(df),columns=['nan_ratio'])

```
- 결측치 제거

어지간히 데이터가 없는게 아닌 이상 결측데이터는 그냥 날리는 것이 속편하다.
```

```
- 결측치 채우기(filna)

```python

df["A"] = df["A"].fillna(0) # 0으로 채워넣기
df["WeeklyExercise"] = df["WeeklyExercise"].fillna(method="ffill") # NaN값이 나오기 전 값으로 뒤의 NaN값 채워넣기 (Forward Fill)
df["Salary"] = df["Salary"].fillna(df["Salary"].median()) # 중간값으로 채워넣기
df.tail()
```

- interpolate를 활용한 결측치 채우기

### imputer

파이프라인 내부의 연산으로 사용

```
imputer_numeric = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
])
```

- 단독을 사용학ㄹ 경우

```python
from sklearn.impute import SimpleImputer

## default, imputing 'mean' value
imputer = SimpleImputer() 
X_train_imputed = imputer.fit_transform(X_train)
X_val_imputed = imputer.transform(X_val)
```

무지성 추가

https://stackoverflow.com/questions/50529022/pandas-melt-unmelt-preserve-index
https://wikidocs.net/46755
https://kongdols-room.tistory.com/170
https://www.tutorialspoint.com/r/r_data_reshaping.html
https://koreadatascientist.tistory.com/12
https://j-ungry.tistory.com/118
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=yu_seon_kim&logNo=221556994880
https://blog.naver.com/PostView.naver?blogId=kurtnim&logNo=222271823879
https://stackoverflow.com/questions/36267745/how-is-a-pandas-crosstab-different-from-a-pandas-pivot-table
https://3months.tistory.com/194
https://rfriend.tistory.com/280
https://dojang.io/mod/page/view.php?id=2360

## Read/Write File

# EDA

- info
- describe
- shape
- pydatalook
- 결측치 이상치 확인
- 히스토그램
- pandas profiliing
- type 확인
- breeze eda
- 시각화를 통한 데이터 구조 파악
- seaborn 기초 시각화

## dlookr

몇가지 함수만 파이썬 버전으로 가져와서 사용

## pingouin

- pinguin을 활용한 정규성 검정

https://pingouin-stats.org/

## 데이터를 받았을 때 해야하는 것

- [EDA가이드라인](https://medium.com/bondata/%EC%B4%88%EC%8B%AC%EC%9E%90%EB%A5%BC-%EC%9C%84%ED%95%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%8B%9C%EA%B0%81%ED%99%94-eda-%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8-%EC%8B%A4%EC%8A%B5-62d11f93e17e)

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
# 커널을 구성하다보면 에러는 아니지만, 빨간색 네모 박스 warning이 뜨는 경우를 제거 
import warnings
warnings.filterwarnings('ignore')


# notebook을 실행한 브라우저에서 바로 그림을 볼 수 있게 해주는 라인
%matplotlib inline
# os 패키지를 통해 현재 디렉토리 위치를 변경하고, read_csv를 더 편리하게 함
import os
os.getcwd() # 현재 디렉토리 파악
os.chdir(r"______") # 불러오고 싶은 파일이 위치한 주소를 ___에 입력




# intera



# cheat
```

- 한글폰트 시각화 관련

```python
# 다른 노트북 작성할 때도 이 셀만 떼서 사용 가능하다.
import matplotlib.pyplot as plt 
import platform                

# 웬만하면 해주는 것이 좋다.
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus']= False

if platform.system() == 'Darwin': # 맥os 사용자의 경우에
    plt.style.use('seaborn-darkgrid') 
    rc('font', family = 'AppleGothic')

elif platform.system() == 'Windows':# 윈도우 사용자의 경우에
    path = 'c:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=path).get_name()
    plt.style.use('seaborn-darkgrid') # https://python-graph-gallery.com/199-matplotlib-style-sheets/
    rc('font', family=font_name)
```

- colab 한글폰트 시각화 관련

```shell
# 이후 런타임 재시작
!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf
```

이후 폰트를 나눔폰트로 바꾼다.

```python
import matplotlib.pyplot as plt

plt.rc('font', family='NanumBarunGothic') 
```

### DF 확인

- df.head()

- df.shape

- df.describe()

- df.dtypes()

- object type select
  
  ```python
  
  ```

cat_cols = df.select_dtypes('object').columns 

```
- not object type select

```python

cat_cols = df.select_dtypes('object').columns 
```

**데이터가 만약 wide로 되어 있다면 반드시 Long 형태로 바꾼다.**
시각화에 유용. 어차피 해야한다.

추가적으로 쓸 수 있는 util

## Descriptive Stataistics

### IQR

IQR 구현

```python
import numpy as np

[[define]] array of data
data = np.array([14, 19, 20, 22, 24, 26, 27, 30, 30, 31, 36, 38, 44, 47])

[[calculate]] interquartile range 
q3, q1 = np.percentile(data, [75 ,25])
iqr = q3 - q1

[[display]] interquartile range 
iqr

12.25
```

```python
import numpy as np
import pandas as pd

[[create]] data frame
df = pd.DataFrame({'rating': [90, 85, 82, 88, 94, 90, 76, 75, 87, 86],
                   'points': [25, 20, 14, 16, 27, 20, 12, 15, 14, 19],
                   'assists': [5, 7, 7, 8, 5, 7, 6, 9, 9, 5],
                   'rebounds': [11, 8, 10, 6, 6, 9, 6, 10, 10, 7]})

[[define]] function to calculate interquartile range
def find_iqr(x):
  return np.subtract(*np.percentile(x, [75, 25]))
```

### 단일변수 분석

- 주요 feature나 target에 대해 분포 파악
- 단순히 시행을 하는데서 그치지 않고 해석 보태기
- 통계량 파악

### 상관관계 분석

## Type Checking & Casting (데이터 타입변환)

### Type Checeking

https://stackoverflow.com/questions/15891038/change-column-type-in-pandas

## Reshaping(데이터 재구조화)

- pivot : unmelt. long to wide
- melt : wide to long
- pivot_table
- crosstab
- stack

- 멀티 인덱싱 변환하기(Single 인덱스로 바꾸기)
- 컬럼에 있을 경우 hirerachical-index라고 한다.

```python
df.columns = df.columns.get_level_values(0) # 첫번째 컬럼으로 사용

df.columns = [' '.join(col).strip() for col in df.columns.values] # flattening and renaming

dat.columns = ["_".join(a) for a in dat.columns.to_flat_index()] # flattening and renaming 최신버전

# https://stackoverflow.com/questions/14507794/pandas-how-to-flatten-a-hierarchical-index-in-columns
# https://stackoverflow.com/questions/26323926/pandas-groupby-agg-how-to-return-results-without-the-multi-index
```

- 멀티인덱싱 사용(쓸일 거의 없음)
- dictionary to dataframe
- list to dataframe
- https://stackoverflow.com/questions/18837262/convert-python-dict-into-a-dataframe

## 데이터 클리닝(missign)

- 결측치 확인
- 결측치 삭제
- 결측치 대체

## 텍스트 데이터 전처리

## 시계열 데이터 전처리

## 연관성 검정

### numerical data : 상관분석, 다중공선성 겸정

### categorical data : 독립성 검정

