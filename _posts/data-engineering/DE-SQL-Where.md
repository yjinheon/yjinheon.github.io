---
title: "[SQL]WHERE절의 이해"
categories:
  - Data Engineering
tags:
  - SQL
date: 2021-08-02 00:00:00
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

## Where 절

조건생성을 위해 Where절을 사용한다.

#### BETWEEN

- 특정 칼럼의 값이 시작점, 끝점인 데이터만 출력

```sql
select *
from ordersdetails
where priceeach between 30 and 50;
```

#### IN

- or 연산자

```sql
select customernumber
from customers
where country in ('USA','CANADA')

```

#### IS NULL

- null 데이터 출력

```sql
SELECT * FROM copang_main.member where ADDRESS is NULL;

SELECT * FROM copang_main.member where address is NOT NULL;

SELECT * FROM copang_main.member where
address is NULL
OR height IS NULL
OR weight IS NULL; # 세 컬럼중 하나라도 null이 있는 로우만 조회


SELECT # coalesce
    coalesce(height,'####'), # null이 아닌 값은 그대로 반환, null일 경우 입력한 값 반환
    coalesce(weight,'----'),
    coalesce(address,'@@@@')
FROM copang_main.`member`;

```

**NULL 변환함수**

1. coalesce : 첫번째로 null이 아닌 값을 반환

2. ifnull : 첫번째 인자가 null인 경우 두번째 인자, 아닐 경우 해당 값 표현

3. if(a1,a2,a3) : ifelse 처럼 사용가능

#### LIKE

- 문자열 매칭하기

```sql
SELECT * FROM main.`member` WHERE address like '서울%'; # address가 서울로 시작하는 row 조회
SELECT * FROM main.`member` WHERE address like '%고양시%'; # 고양시라는 단어 앞뒤로 임의의 길이를 가진 문자열 조건
```

#### 이스케이핑 문제

- 어떤 문자가 그것에 부여된 특정한 의미,기능으로 해석되는 것이 아니라 단순한 문자 하나로 해석되게끔 하는 것을 `이스케이핑`이라 한다.
- ' 이스케이핑 -> select \* from copang_main.test where sentence like '%\'%'
- \_ 이스케이핑 -> select \* from copang_main.test where sentence like '%\_%'
- " 이스케이핑 -> select \* from copang_main.test where sentence like '%\"\"%'
- 대문자 제외 소문자 찾기 select \* from copang_main.test where sentence like binary '%g%'

#### ANY

- **ANY는 나올 수 있는 모든 조건에 OR 연산을 수행한것과 동일한 결과 반환**
- 수량이 10개인 제품 전부 반환

```sql
SELECT ProductName
FROM Products
WHERE ProductID = ANY
  (SELECT ProductID
  FROM OrderDetails
  WHERE Quantity = 10);
```

- 수량이 1000개 초과인 제품 전부 반환

```sql
SELECT ProductName
FROM Products
WHERE ProductID = ANY
  (SELECT ProductID
  FROM OrderDetails
  WHERE Quantity > 1000);
```

#### ALL

- 조건을 모두 만족하는 행을 반환

```sql
SELECT ProductName
FROM Products
WHERE ProductID = ALL
  (SELECT ProductID
  FROM OrderDetails
  WHERE Quantity = 10);
```

#### EXISTS

- EXISTS는 행의 존재 여부를 확인하여 True/False 값을 반환

```sql
SELECT SupplierName
FROM Suppliers
WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.supplierID AND Price = 22);
```

## References

- SQL로 맛보는 데이터 전처리분석

