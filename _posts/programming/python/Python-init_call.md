---
title: "[Python] init, call method"
categories:
  - Programming
  - Python
date: 
updated: 
tags:
  - init
modified: 2023-12-29T09:45:43+09:00
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

- `__init__` method를 이해한다.
- `__call__` method를 이해한다.

## `__init__` method

init은 생성자(Constructor)라고도 불리며, 객체가 생성될 때 자동으로 호출된다.
기본적으로 객체를 생성할 때, 객체의 속성을 초기화하는 역할을 한다.

```python

class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color


car = Car('BMW', 'red') # __init__ method가 호출된다.
```
## `__call__` method
call은 호출자(Invoker)라고도 불리며, 객체를 함수처럼 호출할 때 자동으로 호출된다.

```

```python

class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __call__(self,size):
        print(f'{self.name} is {self.color} and {size} size')
        

car() # __call__ method가 호출된다.
```
