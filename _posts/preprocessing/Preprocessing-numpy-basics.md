---
title: '[Python]numpy 연산과 활용법'
categories:
  - - Preprocessing
tags:
  - numpy
date:
updated:
---

<!--

<center>Kaggle Customer Score Dataset</center>

- Machine Learning
- Statistics , Math
- Data Engineering
- Programming
- EDA & Visualization
- Preprocessing


#신경망이란 무엇인가?

https://www.youtube.com/watch?v=aircAruvnKk


#참고

https://cinema4dr12.tistory.com/1016?category=515283

https://www.kdnuggets.com/2021/07/top-python-data-science-interview-questions.html
-->

## numpy

**numpy 기능들**

- 벡터 배열상에서 데이터 가공, 정제, 부분집합 필터링, 변형 및 기타연산
- 정렬, unique 탐색, 집합연산같은 일반적인 배열처리 알고리즘


numpy의 중요한 특징은 **파이썬 반복문을 사용하지 않고** 대용량 배열에 대한 복잡한 연산이 가능하다는 것이다.

기본적으로 C랑 포트란 기반으로 짜여졌기 때문에 같은 연산이라면 pandas랑 비교도 안되게 빠르게 수행할 수 있다.

---

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
- **`np.full` :인자로 값과 형태를 받고. 인자로 받은 형태에 값을 채운다.(자주쓴다.)**
```python
# np full 용법

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

- **배열의 일부는 원본배열의 View 이기 때문에 파이썬 `list` 와 달리 배열의 일부에 대한 변경은 그대로 원본배열에 반영된다.**

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
b.ravel() #Flatten the array
g.reshape(3,-2) #Reshape, but don’t change data
b.flatten() # rabel() 과 같지만 배열의 copy를 생


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

-  `np.sort(M)[::-1]` : 역순 정렬  

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




### numpy broadcasting


- numpy의 연산은 기본적으로 같은 크기의 배열간의 연산을 전제한다.
- 하지만 특정 조건을 만족했을 때 numpy는 자동적으로 크기가 다른 배열간의 연산을 수행하기도 하는데 이를 `broadcasting`이라 한다.
- `broadcasting` 연산이 성립되기 위한 다음의 3가지 규칙이 존재한다.
    + **규칙 1: 두 배열의 차원 수가 다를 경우, 크기가 작은 배열의 모양은 맨 앞(왼쪽)에 패딩됨**
    + **규칙 2: 두 배열의 모양이 임의의 차원에서 일치하지 않으면 해당 차원에서 모양이 1인 배열은 다른 모양과 일치하도록 확장됨**
    + **규칙 3: 어떤 차원에서든 크기가 일치하지 않고 둘 다 1과 같지 않으면 오류가 발생.**

- **단순히 한쪽의 크기를 맞춰서 연산이 가능하게끔 만드는 것이라고 생각하면 이해하기 쉽다.**

![](https://jakevdp.github.io/PythonDataScienceHandbook/figures/02.05-broadcasting.png)

- `a` 의 차원이 더 작기 때문에 규식 1,2 에 따라 연산시 `a` 가 padding 되고 확장됨.

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

**References**

- [Numpy 공식문서](https://numpy.org/doc/stable/index.html)
- [numpy array transfrormation](https://www.datacamp.com/community/blog/python-numpy-cheat-sheet)
- [numpy indexing](https://www.geeksforgeeks.org/numpy-indexing/)
- [numpy broadcasting](https://jakevdp.github.io/PythonDataScienceHandbook/02.05-computation-on-arrays-broadcasting.html)
- [numpy padding](https://sparrow.dev/numpy-pad/)
- [numpy select](https://towardsdatascience.com/3-numpy-functions-to-facilitate-data-analysis-with-pandas-b1ad342a569)
