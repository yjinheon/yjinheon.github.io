---
title: "[Spring]MSA 구축"
draft: true
date: 2023-07-21T06:52:55.000Z
categories:
  - Backend
tags:
  - spring
  - msa
created: 2024-06-28T16:02
updated: 2024-07-15T18:09
---

# 이론

독립적으로 배포 가능한 각각의 기능을 수행하는 서비스로 구성된 프레임워크

- 개별 배포 가능
- 프로그래밍 언어의 제약이 없음
- api 통신을 사용하기 때문에 속도/관리의 어려움

## Gateway

l4 switch (layer 4)

### 용어들

- Route : 기본적으로 방향전환을 의미. 요청서비스의 고유한 값인 id 요청할 uri, Predicate , Filter로 구성됨. 요청된 uri의 조건이 predicate와 일치하는지 확인 후 일치하는 경우 해당 uri 경로로 요청을 매칭시켜줌

- Predicate : API Gateway로 들어온 요청이 주어진 조건을 만족하는지 확인
- Filter : Gateway 기준으로 들어오는 요청및 나가는 응답에 대하여 수정

Global Filer : Gateway 자체필터 -> Logging, 인증, 인가
Local Filter : Subfilter

Reactor : 비동기처리의미

# MSA architecture

## Spring Cloud Gateway

- 요청의 분배

## Spring Cloud Eureka Server

- MS 모니터링 기능과 함께 추가적으로 Spring Cloud Gateway에 목록을 전달하여 Gateway가 로드밸런싱 대상을 설정하도록 작업

## Spring Cloud Eureka Client

- Eureka에 등록되는 Spring Boot서비스

## Spring Config Server

- 변수 값을 제공하는 서버
- 특정 경로로 접근하면 미리 사전에 설정해둔 변수값을 받을 수 있다.
- MSA를 구축하면 각각의 스프링 부트 어플리케이션에 application.yaml 값을 명시하는 것이 아닌 Config 서버로부터 데이터를 받아서 사용한다.

### Config Repository

- 단순하게 데이터를 전달하는 매개체로 실데이터는 Config Server 뒤에 Github 레포지토리와 같은 저장소를 물려서 사용한다.

## Spring Config Client

- Config Server로 부터 변수 데이터를 받기 위한 Client 서버 설정
- 단순 서비스 로직을 수행하는 스프링 부트 어플리케이션을 의미

## Eureka 서버

- Micro Service 활성화 상태 모니터링 (Health Check)
- 현재 가동된는 서버를 확인후 Gateway에 그 목록을 전달하는 역할

## Eureka 클라이언트

- MSA를 구성하는 요소들 중 Eureka서버에서 모니터링 및 관리를 원하는 요소를 Eureka 클라이언트 설정을 진행해서 등록할 수 있다.

```yaml
eureka:
  client:
    register-with-eureka: true # eureka 서버에 등록 여부
    fetch-registry: true # eureka 서버로부터 다른 client 정보를 가져올지 여부
    service-url: defaultZone:http://아이디:비밀번호@아이피:8761/eureka
```

# Config 서버

## Config 저장소

# Spring Cloud Gateway

- public 망에 노출됨
- 기본적으로 퍼플릭 엔드포인트에서 게이트웨이 역할을 수행하기 때문에 서비스를 시작한 수 항상 무중지 상태로 모든 요청을 받아야 한다

기존 스프링부트, Eureka, Config 왁 같은 서비스들은 블로킹 기반으로 모두 톰캣 엔진 사용

- Tomcat Engine : Blocking 기반
- WebFlux, Netty : Non blocking 기반 -> io 중점적인 처리

스프링 클라우드 게이트웨이의 경우 비즈니스 로직 처리보단 단순하게 지나가는 통로 즉, IO 처리를 중점적으로 진행하기 때문에 WebFlux, Netty 사용

## 라우팅 추가하기

> 항상 가동 상태로 유지되어야 하는 게이트웨이 특성상 서버 스크립트를 중지 후 코드를 수정하고 재배포하면 서비스의 실시간성을 보장하지 못한다. 스프링 클라우드 게이트웨이의 경우 가동 중 새로운 비즈니스 로직(경로)이 추가될 경우 해당 주소에 대한 라우팅을 즉시 추가하고 삭제할 수 있는 여러 기능을 제공한다.

기본적으로 중단이 되면 안되기 때문에 아래 두 가지 방식을 사용해 라우팅을 추가하거나 삭제한다

- Actuator
- DB

### Actuator

- 스프링 어플리케이션의 기능을 엔드포인트로 제공한다

## Global Filter

글로벌 필터
스프링 클라우드 게이트웨이에서 글로벌 필터는 모든 라우팅에 대해서 적용되는 필터이다. 따라서 필터만 구현하면 특별한 설정 없이 적용된다.

클라이언트의 요청은 필터 → 마이크로서비스 → 필터 형태로 이동되며 같은 필터라도 마이크로서비스를 접근하기 이전이면 pre, 이후면 post라고 명명한다.

각각의 필터는 Order 값을 가질 수 있으며 pre 필터의 경우 Order 값이 작을수록 빠르게 동작하며, post 필터의 경우 Order 값이 작을수록 늦게 동작한다.
