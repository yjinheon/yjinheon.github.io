---
title: '[SQL]간단한 서브쿼리 용법'
draft: false
date: 2021-08-21T06:52:55.000Z
categories:
  - Data Engineering
tags:
  - sql
---
## **간단한 서브쿼리 용법 정리**

### Subquery

---

**_Concept_**

- **서브쿼리** : 서브쿼리는 하나의 SQL쿼리 안에 포함된 다른 SQL쿼리를 말한다.

---

- **서브쿼리 사용상황**

  - 가장 기본적으로는 알려지지 않은 조건을 사용해서 조회해야할 때
  - DB에 접근하는 속도를 향상시킬 때

- **사용시 주의점**

  - 항상 괄호로 감싸서 사용할 것
  - 서브쿼리의 결과가 2건 이상이라면(다중행) **반드시** 비교연산자와 함께 사용한다,
  - 서브쿼리 내에서는 order by 사용 못함( order by는 쿼리에서 하나만 사용)
  - 서브쿼리는 메인쿼리의 컬럼을 모두 사용할 수 있지만, 메인쿼리는 서브쿼리의 컬럼을 사용할 수 없다.
  - 질의 결과에 서브쿼리 컬럼을 표시해야 한다면 조인 방식으로 변환하거나 함수, 스칼라 서브쿼리 등을 사용해야 한다.

- **종류**

  - 단일 행 서브쿼리 : 특정 행을 반환. 이 행을 조건절도도 사용가능

    - ex) 평균값알아내는 서브쿼리를 통해 평균값 이상의 그룹을 출력

  - 다중행 서브쿼리 : 결과가 2건이상 반환되는 서브쿼리. 반드시 비교연산자와 함께 사용. Where 절에 괄호로 들어간다.
    - IN(서브쿼리) : 서브쿼리의 결과에 존재하는 값과 동일한 조건의미
    - ALL(서브쿼리) : 모든 값을 만족하는 조건
    - ANY(서브쿼리) : 비교연산자에 ">" 를 썼다면 ANY가 어떤 하나라도 맞는지 조건이기 때문에 결과중에 가장 작은값보다 크면 만족한다.
    - EXIST(서브쿼리) : 서브쿼리의 결과를 만족하는 값이 존재하는지 여부 확인. 존재유무만 확인하기에 1건만 찾으면 더 이상검색안함
  - 다중 컬럼 서브쿼리 : 서브쿼리 결과로 **여러 개의 컬럼이 반환**되어 메인쿼리 조건과 동시에 비교되는 것.

  ```sql
  -- 다중컬럼 서브쿼리

  select ord_num, agent_code, ord_date, ord_amount
  from orders
  where(agent_code, ord_amount) IN
  (SELECT agent_code, MIN(ord_amount)
  FROM orders
  GROUP BY agent_code);

  ```

#### Where 절의 Subquery

- 비교연산자 IN 사용

```sql
# 특정 행 반환
SELECT
    employee_id, first_name, last_name
FROM
    employees
WHERE
    department_id IN (SELECT
            department_id
        FROM
            departments
        WHERE
            location_id = "찾는 아이디")
ORDER BY first_name , last_name;

```

- MAX나 MIN 사용

```sql

# where 절에서 서브쿼리로 정의한 조건을 select 절에 쓸 수 있다.

SELECT
    employee_id, first_name, last_name, salary
FROM
    employees
WHERE
    salary = (SELECT
            MAX(salary)
        FROM
            employees)
ORDER BY first_name , last_name;

```

- AVG로 조건걸기

```sql

SELECT
    employee_id, first_name, last_name, salary
FROM
    employees
WHERE
    salary > (SELECT
            AVG(salary)
        FROM
            employees);


```

- 서브쿼리 조건문처럼 사용하기

```sql
SELECT *
  FROM tutorial.sf_crime_incidents_2014_01
 WHERE Date = (SELECT MIN(date)
                 FROM tutorial.sf_crime_incidents_2014_01
              )
```

#### FROM 절의 Subquery(Inline View)

- SQL이 실행될 때만 동적으로 생성되는 Inline view

```sql
SELECT
    MAX(items),
    MIN(items),
    FLOOR(AVG(items))
FROM
    (SELECT
        orderNumber, COUNT(orderNumber) AS items
    FROM
        orderdetails
    GROUP BY orderNumber) AS lineitems;
```

- 파생테이블은 반드시 alias를 가진다,

```sql
select
    substring(address,1,2) as region,
    count(*) as review_count
from review as r left outer join member as m
on r.mem_id = m.id
group by substring(address,1,2)
having region is not null
    and region != '안드'

select avg(review_count),
       max(review_count),
       min(review_count)
from
(select
    substring(address,1,2) as region,
    count(*) as review_count
from review as r left outer join member as m
on r.mem_id = m.id
group by substring(address,1,2)
having region is not null
    and region != '안드') as review_count_summary #서브쿼리로 탄생한 파생테이블은 반드시 alias를 가져야 한다
```

-- Join과 서브쿼리 같이 사용하기

```sql
SELECT *
  FROM tutorial.sf_crime_incidents_2014_01 incidents
  JOIN ( SELECT date
           FROM tutorial.sf_crime_incidents_2014_01
          ORDER BY date
          LIMIT 5
       ) sub
    ON incidents.date = sub.date

```

#### SELECT 절의 Subquery(Scala Subquery)

- SELECT 절 안에 SELECT가 있을 경우 Scala 서브쿼리라 부르며 기본적으로 한 행만 리턴한다.

```sql
SELECT PLAYER, HEIGHT , (SELECT AVG(HEIGHT)
                         FROM PLAYER X
                         WHERE X.TEAM_ID = P.TEAM_ID)
FROM PLAYER_P

```

- 기본적으로 outer join이 적용되어 있다.
- 쿼리 수행 횟수를 최소화하기 위해서 입력값과 출력값을 내부 캐시에 저장한다.
- 대용량 데이터를 처리할 경우 속도가 느려질 수 있다.

```sql

SELECT A.PKID
    , A.TITLE
    , NVL(B.NAME, '탈퇴한 회원'), B.NAME
    , (SELECT COUNT(*) FROM REPLY WHERE P_PKID = B.PKID) AS COUNT1
FROM BOARD B LEFT OUTER JOIN MEMBER M
    ON B.MEM_NO = M.PKID

```

## **References & annotation**

- <https://mode.com/sql-tutorial/sql-sub-queries/>
- <https://www.mysqltutorial.org/mysql-subquery/>

