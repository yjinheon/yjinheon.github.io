---
title: '[Python] asterisk를 활용한 unpacking'
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
- Data Extraction & Wrangling

ience-interview-questions.html
-->

**asterisk를 활용한 Unpacking을 간단히 정리**

Python에서 `*`(asterisk)를 쓰는 방법은 크게 3가지이다.

- **function call 할때 인자를 unpacking 하기** 
  
  - `*` 연산자는 리스트 또는 튜플과 같은 iterable을 unpack한다
  - `**` 연산자는 dictionary를 펑션에 필요한 인수로 unpack한다.

- **Variadic Parameters(가변인자) 사용하기**
  
  - positional arguments 나 keyword arguments(dictionary 형태)를 여러개 받고 싶을 때 사용한다

- **곱셈, 거듭제곱의 연산자로 사용**

여기서는 일단 iterable에 unpacking을 적용하는 것 중심으로 작성한다.

---

## unpacking parameters

- 5개의 positional argument를 받는 함수가 있을 때 unpacking을 활용해 보다 간소화해서 실행할 수 있다.

```python
def num_sum(num1,num2,num3,num4,num5):
    return num1 + num2 + num3 + num4 + num5

num_list = list(range(1,6))

num_sum(*num_list) # 1+2+3+4+5
```

## iterable의 데이터를 unpacking하기

- list unpacking
  
  ```python
  test = [1, 2, 3, 4]
  print(*test) # 1 2 3 4
  ```

- tuple unpacking

```python
test = (5, 6, 7, 8)
print(*test) # 5 6 7 8
```

- unpacking 을 활용해 iterable을 여러 부분으로 나눌 수 있다.

```python
n = [2, 3, 4, 5, 6 ,7]

# unpacking의 좌변은 iterable의 형태를 가져야 한다,

*a, = num
# a = [2, 3, 4, 5, 6 ,7]

*a, b = num
# a = [2, 3, 4, 5, 6]
# b = 7

a, *b, = num
# a = 2
# b = [3, 4, 5, 6, 7]

a, *b, c = num
# a = 2
# b = [3, 4, 5, 6]
# c = 7
```

- dictionary unpacking 예시

```python
dct = {'a':3, 'b':3,'c':5,'d':3}

lst = ['c', 'd', 'a', 'b', 'd']

res = [*map(dct.get,lst)] # unpacking

res2 = map(dct.get,lst)


print(res)

# 각 인자를 unpacking해서 출력
for i in res2:
      print(i) # 3, 3, 5 ,3 
```

## multiple list를 합치기

```pyhton
num_list = [1,2,3,4,5]
num_list2 = [6,7,8,9,10]

new_list = [*num_list, *num_list_2]
# [1,2,3,4,5,6,7,8,9,10]
```

## References

- https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/
- https://mingrammer.com/understanding-the-asterisk-of-python/
- https://towardsdatascience.com/unpacking-operators-in-python-306ae44cd480