---
title: '[Python]for-loop관련 함수들'
categories:
  - - Programming
tags:
    - Python
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

- 대부분의 문제는 반복문과 제어문을 잘 쓰면 어떻게든 해결이 된다.
- for loop에 자주쓰이는 유용한 내장함수로 zip과 enumerate가 있다.
- itertools를 활욯해 반복문의 코드 가독성을 높일 수 있다.

---

## for-loop

#### zip

- 같은 크기의 여러 `iterable`를 한 쌍으로 묶은 뒤 tuple의 형태로 접근할 수 있는 `iterator`를 반환한다.
- 2개 이상의 인자를 넘겨서 병렬처리가 가능하다(가변인자를 받는다.)

```python

num = [1, 2, 3]
name = ["A", "B", "C"]
for i in zip(num, name):
   print(i)

(1, 'A')
(2, 'B')
(3, 'C')

```

- zip으로 쉽게 dictionary를 만들 수 있다.

```python

food = ['beef', 'chicken']
count = [5, 10]

stock = dict(zip(food, count))

# dictionary comprehension을 사욯할 경우


stock2 = {k:v*2 for k, v in zip(food, count)} # stock이 2배 늘어남

print(stock)
print(stock2)

```

- `*` 연산자를 사용해 unzip이 가능하다
- `*` 은 iterable의 각 요소를 분리하는 역할을 한다.
  + * (a, b, c, d) 는 a,b,c,d 각각을 분리한 것과 같다.
- zip(* zipped) 는 배열의 각 요소들을 분리한 다음 페어로 다시 묶은 것이다.

```python
a = [(1, 2, 3), (4, 5, 6)]


b,c,d=zip(*a) # 배열을 페어링

In [12]: b
Out[12]: (1, 4)

In [13]: c
Out[13]: (2, 5)

In [14]: d
Out[14]: (3, 6)


```


#### enumerate

- **Get the element and index from a list**
- `iterable`에 사용한다. `iterable`의 인덱스와 원소를 튜플형태로 반환한다.
- `zip`과 다른 것은 배열을 묶는게 아니라 배열의 인덱스를 원소와 함께 묶은 `iterator`를 반환한다는 것.

```python
lst = ['a','b','c','d']
for i in enumerate(lst):
    print(i)

(0,'a')
(1,'b')
(2,'c')
(3,'d')
```

**zip()과 enumerate() 활용**

- 인덱스와 배열을 묶은 값을 모두 반환해야 할경우 zip과 enumerate를 같이 사용한다.

```python
names = ['Alice', 'Bob', 'Chris']
ages = [18, 20, 24]

for i, (name, age) in enumerate(zip(names, ages)):
    print(i, name, age)
# 0 Alice 18
# 1 Bob 20
# 2 Chris 14

```

### itertools를 활용한 반복문 응용

**itertools.product를 활용한 이중 반복문 변형**

```python
# 기존 반복문
for i in i_ex:
    for j in j_ex:
        print(i,j)

# itertools활용
import itertools
for i, j in itertools.product(i_ex, j_ex):
    print(i, j)


```

**References & annotation**


- [unzipping 연산자](https://stackoverflow.com/questions/5917522/unzipping-and-the-operator)
- [itertools](https://www.geeksforgeeks.org/python-itertools/
)
