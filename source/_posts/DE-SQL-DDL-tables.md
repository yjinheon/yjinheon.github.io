---
title: '[DDL]Table 구조 다루기'
categories:
  - Data Engineering
date:
updated:
tags: 
  - SQL
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

## Data Definition

- `ALTER`는 DB구조를 변경하는데 쓴다.
- `TRUNCATE`는 데이터를 삭제하는데 쓴다.
- `DROP`은 테이블 자체를 삭제한다.

### 테이블 데이터 다루기


- 테이블 생성

```sql
CREATE TABLE t ( id INT PRIMARY KEY,
                 name VARCHAR NOT NULL, 
                 price INT DEFAULT 0);

```

- 테이블 삭제

```sql
DROP TABLE t;

```

- 새 컬럼 추가

```sql
ALTER TABLE t ADD COLUMN;

```

- 새 제약조건 추가

```sql
ALTER TABLE t ADD CONSTRAINT;

```

- 제약조건 삭제

```sql
ALTER TABLE t DROP CONSTRAINT;

```

- 테이블명 변경

```sql
ALTER TABLE t RENAME to t2;

```

- 컬럼명 변경

```sql

ALTER table t1 RENAME c1 to c2;

```

- 테이블 데이터 삭제

테이블 구조는 남기고 데이터를 전부 날린다.

```sql

TRUNCATE TABLE t;

```

**References & annotation**
---

- [mysql tutorial](https://www.mysqltutorial.org/mysql-join/)
