---
title: "[Fastapi]간단한 서버 구축하기"
draft: true
date: 2023-09-08T06:52:55.000Z
categories:
  - Backend
tags:
  - FastAPI
  - Backend
  - ORM
created: 2024-06-28T16:02
updated: 2024-09-08T14:11
---

ORM(Object-Relational Mapping)의 이해
데이터베이스를 사용하는 애플리케이션을 개발할 때, 우리는 종종 객체 지향 프로그래밍(OOP)과 관계형 데이터베이스 사이의 간극을 마주하게 됩니다. 이 두 패러다임을 효과적으로 연결해주는 기술이 바로 ORM(Object-Relational Mapping)입니다.
ORM이란?
ORM은 객체 지향 프로그래밍 언어와 관계형 데이터베이스 사이의 '통역사' 역할을 합니다. 이 기술을 통해 개발자는 SQL 쿼리를 직접 작성하지 않고도 객체를 통해 데이터베이스와 상호작용할 수 있습니다.
ORM의 주요 특징

객체-테이블 매핑: 클래스를 데이터베이스 테이블과 매핑합니다.
데이터 추상화: 데이터베이스의 세부 사항을 추상화하여 코드의 가독성과 유지보수성을 향상시킵니다.
데이터베이스 독립성: 다양한 데이터베이스 시스템에 대해 일관된 API를 제공합니다.
CRUD 연산 단순화: 생성(Create), 읽기(Read), 갱신(Update), 삭제(Delete) 작업을 객체 지향적 방식으로 수행할 수 있습니다.

ORM의 장점

생산성 향상: SQL 쿼리 대신 프로그래밍 언어로 데이터베이스 작업을 수행할 수 있어 개발 속도가 빨라집니다.
코드 재사용: 데이터베이스 로직을 재사용 가능한 객체로 캡슐화할 수 있습니다.
보안 강화: SQL 인젝션과 같은 보안 위협을 줄일 수 있습니다.

ORM의 단점

성능 오버헤드: 복잡한 쿼리의 경우 직접 작성한 SQL보다 성능이 떨어질 수 있습니다.
학습 곡선: ORM 프레임워크를 익히는 데 시간이 필요할 수 있습니다.

SQLAlchemy: Python의 강력한 ORM
Python 생태계에서 가장 널리 사용되는 ORM 중 하나가 바로 SQLAlchemy입니다. SQLAlchemy는 다음과 같은 특징을 제공합니다:

유연성: 로우 레벨 SQL에서부터 하이 레벨 ORM까지 다양한 추상화 수준을 제공합니다.
강력한 쿼리 빌더: 복잡한 쿼리도 파이썬 코드로 쉽게 작성할 수 있습니다.
다양한 데이터베이스 지원: MySQL, PostgreSQL, SQLite 등 다양한 데이터베이스를 지원합니다.

이제 우리는 SQLAlchemy를 사용하여 어떻게 데이터베이스 작업을 수행하는지 자세히 살펴보겠습니다.

## 컨셉들

---

**_Concept_**

- **ORM** : Object-Relational-Mapping DB 테이블을 객체로 매핑하는 것

---

### tmp

alembic

라우터(Router)
의존성 주입(Dependency Injection)
Pydantic으로 하는 입출력 관리
CRUD 파일 작성
