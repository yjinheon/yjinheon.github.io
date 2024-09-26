---
title: "[Python]functional programming"
draft: true
date: 2021-05-02T06:52:55.000Z
categories:
  - Programming
  - Python
tags:
  - funtional
  - python
created: 2024-06-13T15:50
updated: 2024-09-21T11:36
---

# 함수형 프로그래밍 개념

## 함수

다음 컨셉들을 다룬다.

- 일급 계층 함수
- 고차함수
- 순수함수

---

**_Concept_**

- **functional programming** : 표현식(Expression) 과 평가(Expression)을 사용해 이들을 함수에 캡슐화 하여 특정 상태와 가변 데이터를 피하면서 프로그램을 구축하는 방법론.

- **imperative programming** : 명령형 프로그래밍. 프로그램이 상태가 존재하며 프로그램이 실행되는 순서에 따라서 이전 상태를 바꿔가면서 계산하는 패러다임. : functional
- **declarative programming** : 특정 값에 대한 반환값을 가지는 함수를 연쇄적으로 호출해 최종 결과값을 유도하는 방식
- **first class object** : 함수의 인자로 전달 가능하고, 함수의 리턴값으로 사용가능하며 동적으로 생성가능한 객체를 first class Object라 한다. 파이썬에서 함수는 일급 객체로 취급된다.

---

## Immutable Data

- stateless 개념
- statefull 개념

---

**_Concept_**

- **Tail Call Optimization** : 재귀함수의 최적화를 위해, 함수의 마지막 부분에서 호출되는 함수를 최적화하여 stack overflow를 방지하는 방법론. 기본적으로는 컴파일러에서 재귀를 루프로 변경하는 것.
- **global keyword** : 한영전
- **local keyword** : 한영전

---

### tuple의 list를 처리하는 두 가지 방식

### Strict , Non Strict Evaluation

---

**_Concept_**

- **non-strict** : 한영전
- **strict** : 한영전
- **eager calculation** : 한영전
- **lazy calculation** : 한영전

---

### Recursion

함수형 프로그램은 루프에 의존하지 않으며 루프의 상태를 추적하는 데 따른 부가비용도 없다.

---

**_Concept_**

- **tail recursion function** : recursion call 이 논리적인 실행부분의 마지막 부분에 위치하면서, 이전의 호출을 더 이상 필요로 하지 않는 함수를 말한다.

---

# Function, Iterator , Generator

**함수형 프로그램의 핵심은 순수 함수를 사용해 입력정의역(domain)을 치역(range)의 값으로 바꾸는 것이다.**

- 부수효과가 없는 순수 함수는 변수의 전역적인 상태를 변경하지 않는다. 파이썬의 경우 global을 쓰지 않는다면
- 인자의 결과로 넘길 수 있거나 함수의 결과로 변환할 수 있는 객체인 함수

## 파이썬에서 부족한 순수 함수형 프로그램

- 파이썬은 재귀 깊이을에 제한을 두며 자동으로 TCO를 수행하지 않는다.

### contextmanaer

파이썬 상태관리

### 파일 다루기

- 파일 객체는 항상 with context 안에서 사용
- 파일은 함수에 제공되는 매개변수여야 하며, 열린 파일은 With 문으로 감싸서 상태에 따른 동작을 처리하게끔 해야한다.

핵심 아이디어는 상태가 필요한 특성을 고립시킨 함수적인 설계를 활용해 혼합적으로 접근하는 것이다.

- DB에도 이러한 접근을 적용할 수 있다.

멀티스레드 웹서버의 경우 일반적인 접근방식인 단일DB 연결을 공유하는 것으로부터 성능상의 이득을 얻지 못할 수 있다.

이는 여러 스레드가 하나의 DB연결을 공유할 경우 연결 사용을 위해 대기해야 하는 경우가 생길 수 있기 때문이다. 이러한 대기는 동시성을 저해하고 전체적인 처리속도의 저하로 이어진다.

공유 자원(DB 연결)에 대한 접근을 동기화하기 위해 락(lock)이 필요할 수있다.
이 동기화 과정 자체가 성능 저하로 이어진다.

전체적으로 단일 연결의 재사용으로 인한 이점이 동시성 처리의 제한으로 상쇄될 수 있다.

따라서 멀티스레드 환경에서는 단일DB연결을 공유하는 것보다 각 스레드가 독립적인 연결을 사용하는 DB연결객체를 어플리케이션의 인자로 전달하는 방식이 보다 나은 전략일 수 있다.

**여러개의 DB 연결을 관리하는 Connection Pool을 만들어서 필요에 따라 스레드에 할당하는 방식과 조합해서 쓸 수 있다.**

## Generator

### Generator를 사용할때 발생가능 한 문제점

- Generator는 컬렉션의 크기를 알아야 할 필요가 있는 len() 메소드를 가질 수 없다.
- Generator는 기본적으로 오직 한 번만 사용할 수 있다. 이는 Generator에 특정한 상태가 있다는 것이다.

`itertools.tree()` 메서드를 사용해 한번밖에 사용하지 못하는 한계를 넘어설 수 있다.

```python

import itertools
def limits(iterable):
  max_tee , min_tee = itertools.tee(iterable,2)

  return max(max_tee), min(min_tee)

```

### yield 를 통해 재귀의 결과 반환

사용하면 안되는 식

```python

return recursive_iter(args) # iterator를 반환한다.

```

만들어진 값을 반환하고자 할 경우 아래 방식을 사용한다.

```python

for res in recursive_iter(args):
  yield res

```

```python

yield from recursive_iter(args) # yield from은 iterable의 전체 요소를 반환한다.

```

### 문자열 다루기

## adfkajfa

### list , dict , set 사용하기

List , dict, set, tuple은 일종의 실체화한(materialized) iterable로 볼 수 있다.

iterable을 실체화 한다는 것은 generator가 생성하는 값들을 리스트와 같은 자료구조로 변환하여 그 값을 메모리에 저장하는 것을 의미한다. 이는 generator가 일반적으로 하는 것처럼 값을 lazy calculation이 아닌 한번에 모든 값을 메모리에 로드하여 사용하게끔 하는 것이다.

### statefull dictionary 사용하기

두 가지 방식

- 매핑을 누적시키는 상태가 존재하는 딕셔너리
- 고정시킨 (frozen) dictionary

### stateful set 다루기

#### bisect 모듈을 활용한 매핑 만들기

bisect는 이진 탐색 알고리즘을 구현한 모듈로, bisect.bisect() 함수는 정렬된 리스트에 값을 삽입할 때 정렬을 유지할 수 있는 인덱스를 반환한다.

bisect 모듈을 사용한다는 것은 정렬된 객체를 만들고 추후에 그 객체를 검색에 활용한다는 것이다.

bisect 예제

```python


```

Stateful set 예제

```python


```

## 핵심 사항들

- 메모리 사용을 줄이고 성능을 향상시키기 위해 가능한 제너레이터 식과 함수를 선호한다.
- 함수형 프로그래밍의 일반적인 컨셉은 statefull 한 변수 사용을 제한하는 것이지만 python의 collection 객체들은 상태가 있으며, 알고리즘들 중 상당수는 반드시 사용해야 한다.

## 옮길 것들

**Iterator, Generator, yield에 대한 정리**

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

- `count` : count(시작, [step]) 의 함수로 시작 숫자부터 step만큼(없으면 1) 씩 무한히 증가하는 generator 반환
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

- [itertools](https://www.geeksforgeeks.org/python-itertools/)
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

- Lazy-evaluation : 값을 미리 생성하여 메모리에 저장하고 있는게 아니며, 요청이 있을 때마다 함수를 실행하고 값을 공급(yield)해 줌

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

## **References & annotation**

- [핵심 stackoverflow ref](https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do)
-

# Collection

다음 함수를 컬렉션과 함께 작업하는 방법을 살펴본다.

- any와 all
- len() , sum() 과 관련한 고차 통계처리

- zip()
- reversed
- enumerate

## 내장 Collection 함수 구분하기

### Scala

### Collection

#### Reduction

#### MAP

# Higher Order Functions

# Recursion

# Reduction

# Complex Stateless Objects

# Itertools

itertools youtube 확인

# Itertools for Combinatorics

# Functools

# Toolz

# Decorator Design

# PyMonad

# Multiprocessing

# Web Functional

# Optimization
