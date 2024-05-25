---
title: '[SQL]Postgresql 자주 사용하는 명령어'
categories:
  - [Data Engineering]
tags:
  - SQL
  - Postgresql
date: 
updated:
---

<!--

<center>중앙정렬 예제</center>

-->

## 터미널 접속

```bash
pqsl -u 

```


## 터미널 접속 후 사용

- \l  :   데이터베이스 리스트 조회
- \c - 데이터베이스 연결 ex) \c mydb
- \dn :  스키마 조회
- \dt - public 스키마의 테이블 조회
- \dt schema1.*  :  특정 스카마의 테이블 조회.

- dt 명령어에서 스키마 검색 범위 확장하기

```bash
SET search_path TO my_schema, public;
\d
```
