---
title: "[Spring]jpa"
draft: true
date: 2023-07-21T06:52:55.000Z
categories:
  - Backend
tags:
  - jpa
created: 2024-06-28T16:02
updated: 2024-06-28T18:07
---

## 실전스프링부트 jpa

김영한 실전 스프링부트와 jpa takeaway

- entity manager를 통한 모든 데이터 변경은 항상 transactional 안에서 이루어져야 한다.
- Test 환경에서의 Transactional 은 테스트가 끝난다음에 기본적으로 Rollback을 한다.
	- Rollback annotation을 false로 할 경우 테스트에서도 Transaction이 반영됨

```java
@Test
@Transactional
@Rollback(false)

```
- 영속성 컨텍스트에서 id(식별자) 가 같으면 같은 엔티티로 인식한다.


- 쿼리 파라미터 로그 남기기
- build.gradle에 해당 library적용

```yaml
implementation 'com.github.gavlyukovskiy:p6spy-spring-boot-starter:1.8.1'
```

## jpa에서 표현할 수 있는 관계

jpa에서 가장 중요한 것은 객체와 관계형 DB 테이블이 어떻게 매핑되는지를 이해하는 것이다.

jpa의 목적 자체가 객체지향 프로그래밍과 관계형 DB 테이블 사이의 패러다임 불일치를 해결하는 것이기 때문이다.


### 컨셉

- 방향 : 양방향, 단방향(객체참조)

### 연관관계의 주인

- 연관관계의 주인은 연관관계를 갖는 두 오브젝츠 사이에서  조회, 저장, 수정, 삭제를 할 수
- 외래키가 있는 오브젝트를 연관관계의 주인으로 정한다.

### 연관관계 매핑 분석
- 다대다 관계 : 쓰면안됨. 일대다 다대일 관계로 풀 것
- 양방향 연관관계 : 쓰면안됨

#### 회원과 주문

회원이 주문을 한다라기 보다 주문을 생성할때 회원이 필요하다고 인식하는게 나음

- 일대다, 다대일의 양방향 연관관계
- **외래키가 있는 주문을 연관관계의 주인으로 설정**