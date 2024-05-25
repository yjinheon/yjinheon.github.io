---
title: '[Python]Iterator,Generator,yield에 대한 정리'
categories:
    - Programming
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

**Iterator,Generator,yield에 대한 정리**

---

### Iterator

- **Iterators are objects that allow you to traverse through all the elements of a collection and return one element at a time.**
- iterator는 iterable로 생성되는 값을 순서대로 꺼낼 수 있는 객체이다. 
- iter(collections) : returns unmodified iterator
- iter(<function>, to_exclusive) : A sequence of return values until 'to_exclusive'
- next(<iter>,default) :Raises StopIteration or returns 'default' on end.
- <list> = list(<iter>) : Return a list of iterator's remaining elements

```python
temp = ("apple", "banana", "cherry")
myit = iter(temp)

print(next(myit))
print(next(myit))
print(next(myit))

```

```python
In [30]: iv = list(range(0,5))

In [31]: io = iter(iv)

In [32]: while True:
    ...:     try:
    ...:
    ...:         item = next(io)
    ...:         print(item)
    ...:     except StopIteration:
    ...:         break
    ...:
    ...:
0
1
2
3
4
```

#### itertools


```python
from itertools import count, repeat, cycle, chain, islice
```

- `count` :  count(시작, [step]) 의 함수로 시작 숫자부터 step만큼(없으면 1) 씩 무한히 증가하는 generator 반환
- `islice` : islice(iterable객체, [시작], 정지[,step])의 함수로, iterable한 객체를 특정 범위로 슬라이싱하고 iterator로 반환.
- `chain` : chain(**iterable**)은 iterable한 객체들을 인수로 받아 하나의 iterator로 반환

```python
# chain
from itertools import chain
e1 = ['Happiness','Caring','Energy']
e2 = ['Fear','Hurt','Tired']
emotions = chain(e1, e2)

next(emotions) >>> 'Happiness'
next(emotions) >>> 'Caring'
next(emotions) >>> 'Energy'

```

- [itertools](https://www.geeksforgeeks.org/python-itertools/
)
- https://realpython.com/python-itertools/
- https://hamait.tistory.com/803

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

### Generator

- Any function that contains a yield statement returns a generator.
- Generators and iterators are interchangeable.
- **Generators are iterators, a kind of iterable you can only iterate over once. Generators do not store all the values in memory, they generate the values on the fly**

- Lazy-evaluation : 값을 미리 생성하여 메모리에 저장하고 있는게 아니며, 요청이 있을 때마다  함수를 실행하고 값을 공급(yield)해 줌

```python
In [1]: my_gen = (x*x for x in range(3))

In [2]: type(my_gen)
Out[2]: generator

In [3]: for i in my_gen:
   ...:     print(i)
   ...:
0
1
4

```
It is just the same except you used () instead of []. BUT, you cannot perform for i in generator a second time since **generators can only be used once**: they calculate 0, then forget about it and calculate 1, and end calculating 4, one by one


#### yield form

- `yield`는 `return`과 유사하지만 generator를 반환한다.

```python
In [6]: def gen_count(start,step):
   ...:     while True:
   ...:         yield start
   ...:         start += step
   ...:

In [7]: counter = gen_count(10,2)

In [8]: next(counter)
Out[8]: 10

In [9]: next(counter)
Out[9]: 12

In [10]: next(counter)
Out[10]: 14

In [11]: next(counter)
Out[11]: 16
```

- `yield from a`를 통해 `iterable`의 전체 요소들을 반환할 수 있다.

```python
>>> def three_generator():
...     a = [1, 2, 3]
...     yield from a
... 
>>> gen = three_generator()
>>> list(gen)
[1, 2, 3]
```

**References & annotation**
---

- [핵심 stackoverflow ref](https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do)
- Python Comprehensive Cheat Sheet