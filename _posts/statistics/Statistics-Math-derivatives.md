---
title: "[Math]미분 기초개념"
date: 
updated:
categories: 
        - [Statistics]
tags:
mathjax: true

---

> 미분의 정의, Data Science에서 미분이 필요한 이유, 미분 공식들에 대해 알아보자.

## 

## 미분

- 함수의 input인 x에 대해서 나오는 결과값이 변화하는 정도를(0에 근사하는 부분을 탐색) 계산하는 것
- 실제로 계산하는 것은 x의 변화량인 delta_x가 한없이 0에 가까워 질 때의 기울기이다.
- **Data Science에서 미분이 필요한 이유는 기본적으로 모델의 오차함수가 최소화되는 지점(오차함수의 변화율이 0이 되는 지점)을 찾을 때 미분이 활용되기 때문이다.(최적화 문제)**

## 미분 공식

numerical method만큼은 확실히 이해하고 넘어가자.

### numerical  method

실제로 0으로 나눌 수는 없기 때문에 Delta_x를 0에 근사한 값인 1e-5로 나눠준다.이를 numerical method라 한다.

#### 미분 기본공식

$$ f'(x) = {f(x + \Delta x) - f(x) \over \Delta x}, \Delta x \rightarrow 0~ $$

### **power rule**

멱함수의 도함수를 구하는 미분규칙

$ \frac{d} { {dx} }x^n=nx^{n-1} $ 

#### **chain rule**

합성함수에 대한 미분규칙. 바깥함수의 도함수에 안쪽함수를 인자로 넣어주고 안쪽함수의 도함수를 곱해주면 된다.

$$ \frac{dy} {dx} = \frac{dy} {du} \times \frac{du} {dx} $$

좀 더 이해하기 쉽게 나타내면 아래와 같다.

$$F(x) = f(g(x))$$

$$F'(x) \rightarrow f'((g(x)) \cdot g'(x)$$

#### **Exponential**

지수함수에 대한 미분규칙. 지수함수의 경우 도함수도 지수함수이다.

$$ f(x) = e^x \rightarrow f'(x) = e^x $$

#### **Logarithmic**

자연로그에 대한 미분규칙.Logistic Regression이나 Section sigmoid 함수를 미분하는데 도움을 준다.

$$f(x) = lnx \rightarrow f'(x) = { {1} \over {x} } $$

#### **product rule**

두 함수의 곱으로 이루어진 함수에 대한 미분규칙.

$$\frac{d}{ {dx} }\left( {f\left( x \right)g\left( x \right)} \right) = f\left( x \right)\frac{d} { {dx} }g\left( x \right) + \frac{d}{ {dx} }f\left( x \right)g\left( x \right)$$

#### **quotinent rule**

분수형태로 생긴 합성함수에 대한 미분규칙. 시그모이드 함수의 도함수를 구할 때 사용된다.

$$\frac{d}{ {dx} }\left( {\frac{ {f\left( x \right)} } { {g\left( x \right)} } } \right) = \frac{ {\frac{d} { {dx} }f\left( x \right)g\left( x \right) - f\left( x \right)\frac{d}{ {dx} }g\left( x \right)} } { {g^2 \left( x \right)} }$$

### **편미분(Partial Derivtives)**

- 편미분은 다변수 함수의 특정 변수를 제외한 나머지 변수를 상수로 간주하여 미분하는 것이다.
- 최적화 관점에서 보면 파라미터가 2개 이상인 Error 함수에 대해 **우선 1개의 파라미터에 대해서만 미분을 한다**는 것이다.
- 편미분은 ${\partial y} \over {\partial x}$ 와 같이 나타내며 이 경우 x에 대해 편미분한다 하며 x를 제외한 나머지 변수는 상수취급하고 미분한다.
- **선형회귀에서 오차함수의 최소값을 유도할때 사용된다**.
- ex) x에 대해 편미분할 경우

$$ f(x,y) = x^2 + 2xy + y^2$$

$${ {\partial f(x,y)} \over {\partial x} } = { {\partial {(x^2 + 2xy + y^2)} } \over {\partial x}} = 2x + 2y$$

## sympy를 활욯한 미분계산

실무에서 이런식으로 따로 미분을 할 일은 없지만 구현한다는 것에 의의를 두자.

```python
#import sympy
from sympy import *

# Symbol정의하기
x = Symbol('x')

# 함수 정의하기
f = x**4

#도함수 계산하기
derivative_f = f.diff(x)

derivative_f
```

## References

- <https://www.askpython.com/python/examples/derivatives-in-python-sympy#:~:text=Derivatives%20of%20Multivariable%20Functions%20using%20sympy&text=Such%20derivatives%20are%20generally%20referred,all%20other%20variables%20held%20constant>.
- <https://youtu.be/H-ybCx8gt-8>
- <https://ko.wikipedia.org/wiki/%ED%8E%B8%EB%AF%B8%EB%B6%84>
