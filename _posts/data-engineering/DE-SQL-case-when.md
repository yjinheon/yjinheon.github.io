---
title: '[SQL]간단한 CASE WHEN 용법'
categories:
    - Data Engineering
tags:
  - SQL
date: 2021-07-21
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

**간단한 mysql case when 용법 정리**

---

### Case When

- 기본적으로 파생변수(컬럼)를 생성하는데 사용한다.
- 파생변수이기 때문에 Select절 에 들어간다.

#### Case When 용법

용법은 어렵지 않다. 파생변수 Select 절에 들어가는 것만 주의

```sql
SELECT player_name,
       weight,
       CASE WHEN weight > 250 THEN 'over 250'
            WHEN weight > 200 THEN '201-250'
            WHEN weight > 175 THEN '176-200'
            ELSE '175 or under' END AS weight_group
  FROM benn.college_football_players
```

- order by에 사용힐 컬럼 생성

```sql
SELECT CustomerName, City, Country
FROM Customers
ORDER BY
(CASE
    WHEN City IS NULL THEN Country
    ELSE City
END);
```

```sql
SELECT animal_id, name,
case 
    when sex_upon_intake like "Intact%" then "O"
    else "X" 
end as "중성화"
from animal_ins
order by animal_id
```

**References & annotation**
---

- https://www.w3schools.com/sql/sql_case.asp
