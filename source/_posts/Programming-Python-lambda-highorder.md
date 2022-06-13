---
title: '[Python]자주쓰는 High Order 함수 정리(lambda,map,filter,apply..)'
categories:
  - Programming
tags:
   - Python
ate:
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

for loop과 조건문 만으로도 동일한 결과를 낼 수 있지만 **가독성, 속도, 재사용성** 때문애 고차함수를 사용해 프로그래밍을 하는 경우가 많다.
특히 lambda는 데이터 전처리시 자주 사용한다.

---

### High order function


Higher-order Function(고차 함수)

**함수의 매개변수의 인수로 전달이 될수 있고 함수로 결과를 반환할 수 있는 함수를 말한다.**

(First-class Function이 성립되는 3조건 중 2개만 만족한다.)

대표적인 함수로는 map, filter, reduce, lambda 등이 있다.


#### lambda

- `lambda 인자 : 표현식` 형태로 사용한다.
- lambda 함수 자체가 파이썬에서 정의된 함수처럼 기능한다고 생각하면 편하다.
- 간단한 기능의 함수가 컨테이너의 요소로 들어가거나 다른 함수(high order function)의 인자로 함수를 넘길때 주로 사용한다.

```python
# lambda 예시


In [1]: double = lambda x : x+x
   ...: print(double(2))
   ...:
4

```

- 단일 값에 lambda 적용하기


- lambda 자체를 변수에 바인딩하여 사용 가능하다.
  + `PEP8`에 어긋나기 때문에 별로 권장하지 않는다.

```python

In [8]: temp = lambda x,y : x*y

In [9]: temp(2,3)
Out[9]: 6

In [10]: temp(10,50)
Out[10]: 500

```

- lamda로 필터링한 파생변수 만들기

```python
#Conditional Lambda statement
df['Gender'] = df['Status'].map(lambda x: 'Male' if x=='father' or x=='son' else 'Female')
```
#### filter

- `filter(조건함수,iterable`)
- 특정 조건에 따라 필터된 요소들로 `iterator` 객체를 만들어 반환한다.
  + `map`과 마찬가지로 list형태로 만들어 결과를 볼 수 있다.
- 조건에 따라 iterable에서 일부를 뽑을 때 사용한다.

```python
# lamdas in filter

In [2]: even = list(filter(lambda x : x%2 == 0 ,range(10)))
   ...: print(even)
[0, 2, 4, 6, 8]

# lamdas in filter2 
sequences = [10,2,8,7,5,4,3,11,0,1]
filtered_result = filter (lambda x: x > 4, sequences) 
print(list(filtered_result))

```


- 보통은 filter 대신 `list comprehension` 같은 보다 pythonic한 방법을 사용해 iterable에서 일부를 필터링 한다.


```python

# list comprehension을 활용한 filter


In [3]: even = [x for x in range(10) if x %2 == 0]
   ...: print(even)
   ...:
[0, 2, 4, 6, 8]



```

- `dataframe`에서 파생변수를 만들때 쓰기 좋다.

```python

list(filter(lambda x: x>18, df['age']))


```

#### map

- `map(func,list)` 형태로 사욯한다.
- `iterable`의 각 원소에 대해 함수를 적용시킨다.
- map함수 자체는 `map` 타입으로 결과를 리턴하기에 함수가 적용된 결과를 리스트로 받으려면 내장함수 `list()`를 사용해야 한다.

```python

In [2]: map(lambda x: x+x, range(5))
Out[2]: <map at 0x2446499e640>

In [3]: list(map(lambda x: x+x,range(5)))
Out[3]: [0, 2, 4, 6, 8]

```

- **map with lambda**

```python
In [4]: sequences = [10,2,8,7,5,4,3,11,0, 1]
   ...: filtered_result = map (lambda x: x*x, sequences)
   ...: print(list(filtered_result))
   ...:
[100, 4, 64, 49, 25, 16, 9, 121, 0, 1]

```

- `dataframe`의 `series` 객체에 적용해 파생변수를 생성힐때 유용하다.

```python

#Double the age 
df['double_age'] = df['age'].map(lambda x: x*2)

```

#### reduce

- `reduce(func,sequence)` 형태로 사용한다.
- iterable의 요소들을 함수에 누적해서 적용 후 반환한다.
- **`iterable`의 순회가 끝날때까지 재귀적으로 함수를 적용한다고 생각하면 이해가 쉽다.**

```python
In [9]:  def my_add(a, b):
   ...:      result = a + b
   ...:      print(f"{a} + {b} = {result}")
   ...:      return result

In [10]: from functools import reduce

In [11]: numbers = list(range(0,11))

In [12]: reduce(my_add,numbers)
0 + 1 = 1
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15
15 + 6 = 21
21 + 7 = 28
28 + 8 = 36
36 + 9 = 45
45 + 10 = 55
Out[12]: 55
```

- 초기값(함수를 적용하기 시직할 지점)을 추가 인자로 넣어줄 수 있다.

- **reduce에 lambda 적용**
  + 코드 가독성을 해치기 때문에 그다지 권장되지 않는다.

```python
In [13]: numbers = list(range(1,6))

In [14]: reduce(lambda x,y :x*y,numbers)
Out[14]: 120
```


#### apply

- pandas의 dataframe의 행이나 열 단위로 함수를 적용하는 함수이다. `map` 과 유사하지만 df의 메소드로 보다 쉽게 쓸 수 있다.
- `df.apply(func, axis = 0 or 1 )` 형태로 사용한다
  + axis = 0 . 열단위로 함수 적용. default 옵션
  + axis = 1 . 행단위로 함수적용


```python
In [3]: df
Out[3]:
    A   B
0  16  81
1  16  81
2  16  81
3  16  81


# 열단위 함수적용
In [6]: df.apply(np.sum,axis=0)
Out[6]:
A     64
B    324
dtype: int64

# 행단위 함수적용
In [7]: df.apply(np.sum,axis=1)
Out[7]:
0    97
1    97
2    97
3    97
dtype: int64

```

- **lambda with apply 예시**
  + df의 파생변수 생성에 유용하다.

```python

df['age'] = df['Birthyear'].apply(lambda x: 2021-x)

```


#### applymap

- `df.applymap(func)` 형태로 사용항다.
- **df의 모든 요소에 인자로 주어진 함수를 적용한다.**
- na_action='ignore' 옵션을 적용할 경우 null값에 대해서는 함수를 적용하지 않는다.

```python

In [8]: import pandas as pd
   ...:
   ...: df = pd.DataFrame({
   ...:     'Col 1': [30,40,50,60],
   ...:     'Col 2': [23,35,65,45],
   ...:     'Col 3': [85,87,90,89],
   ...:
   ...: },index=["A","B","C","D"])
   ...:
   ...: print("Initial DF:")
   ...: print(df,"\n")
   ...:
   ...: scaled_df=df.applymap(lambda a: a*10)
   ...:
   ...: print("Scaled DF:")
   ...: print(scaled_df,"\n")
Initial DF:
   Col 1  Col 2  Col 3
A     30     23     85
B     40     35     87
C     50     65     90
D     60     45     89

Scaled DF:
   Col 1  Col 2  Col 3
A    300    230    850
B    400    350    870
C    500    650    900
D    600    450    890

```


### References

- [pandas 공식문서](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.applymap.html#pandas.DataFrame.applymap)
- [lambda](https://towardsdatascience.com/lambda-functions-with-practical-examples-in-python-45934f3653a8
)
- [reduce](https://realpython.com/python-reduce-function/)
