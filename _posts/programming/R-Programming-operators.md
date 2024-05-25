---
title: "[R]특별한 R 연산자들(Binary Oerators)"
date: 2021-03-02 14:11:05
updated:
categories: 
        - [Programming,R]
tags:
  - [R]


---

## Intro

R로 분석을 하다보면 자연스럽게 손에 익게 되는 몇가지 연산자들이 있습니다. 이 포스팅에서는 R에서 사용되는 특별한 연산자들과 특정 연산자를 단축키로 Rstudio에 추가하는 법을 다룹니다.

## 연산자들

### %in% (matching 연산자)

**특정 vector 내에 원하는 요소가 있는지 확인하고 이를 반환할 때 사용합니다.** x%in%y 일 경우 x 기준으로 y와 매칭되는 값에 대한 논리값을 반환합니다.

```r
a <- seq(1, 5)
b <- seq(3, 12)


> b %in% a  
 [1]  TRUE  TRUE  TRUE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
> a %in% b
[1] FALSE FALSE  TRUE  TRUE  TRUE
```

### %>% (pipe)

tidyverse에 포함되어 있어 아마도 가장 유명할 연산자인 pipe operator입니다.

자주 쓰이기 때문에 Rstudio에 ctrl+shift+m으로 단축키가 지정되어 있습니다.

**기능은 함수들을 연결해 직관적으로 전달하는 것입니다.** f(g(x)) 와 같은 합성함수를 R 코드 상에서 직관적으로 구현한 것이라고 이해하면 될 것 같습니다.

이 연산자는 특히 데이터 분석에 유용한데 파이프 연산자를 사용하면 코드 가독성을 저해하는 분석 과정상에서의 중간 객체를 만들 필요가 없어지기 때문입니다.

```r
iris %>% # df에 연속적으로 함수를 전달함
  subset(Sepal.Length > 3) %>%
  aggregate(. ~ Species, ., mean)
```

### %<-% (unpacking)

생각보다 자주 사용하게 되는 unpacking 연산자 입니다. **기능은 list나 vector를 분해해서 이름을 할당하는 것입니다.** list object인 선형회귀 모형의 특정 요소들을 불러와 이름을 할당해 독립적인 객체로 만들 수 있습니다.

```r
library(zeallot)

m<- lm(hp ~ gear, data = mtcars)
c(mcall,...,mdf,mstat) %<-% summary(m)

mcall # 모델식
lm(formula = hp ~ gear, data = mtcars)

> mdf # 자유도
     value      numdf      dendf 
 0.4816578  1.0000000 30.0000000 
> mstat # 통계량
            (Intercept)        gear
(Intercept)   0.8370370 -0.21851852
gear         -0.2185185  0.05925926
```

### %x% (행렬곱-벡터의 내적)

**%x%는 벡터의 내적을 반환합니다.**

```r
c <- matrix(1:4,nrow = 2)

> c %*% c
     [,1] [,2]
[1,]    7   15
[2,]   10   22
```

### %o% (행렬곱-벡터의 외적)

**%o%는 벡터의 외적을 반환합니다.**

```r
> d <- 1:3
> d %o% d
     [,1] [,2] [,3]
[1,]    1    2    3
[2,]    2    4    6
[3,]    3    6    9
```

### %$% (값 할당하기)

**magrittr** 패키지의 %$% 연산자는 데이터 프레임이 중심이 되는 분석을 할때 사용하는 단순하지만 유용한 연산자입니다. **기능은 데이터 프레임에서 단순히 특정 변수를 추출하는 것입니다.**

```r
library(magrittr)

mtcars %$%
  cor(disp, mpg)
```

---

## 특정 단축키를 addin으로 Rstudio에 추가하기

특별한 연산자들은 유용하지만 %>%와 같이 Rstudio에서 미리 단축키로 지정해놓지 않은 연산자들을 매번 타이핑해서 사용하는 것은 귀찮은 일입니다.  
따라서 자주 사용하는 연산자의 경우 Rstudio addin을 사용해 %in% 처럼 단축키를 만들어 주는 것을 고려해볼 수 있습니다.

```r
 # 사용자 정의 단축키를 추가하는 Rstudio addin 설치

devtools::install_github("rstudio/addinexamples", type = "source")
```

**References & annotation**

- https://www.datamentor.io/r-programming/infix-operator/
- https://github.com/r-lib/zeallot
- https://rfriend.tistory.com/35
- https://stackoverflow.com/questions/25179457/r-what-are-operators-like-in-called-and-how-can-i-learn-about-them # Binary operator에 대한 자세한 설명이 나와있습니다.
