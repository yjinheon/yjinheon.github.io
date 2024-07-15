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
updated: 2024-06-30T11:10
---

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

아머ㅏㅓㅏㅓ
## Eureka 서버

- Micro Service 활성화 상태 모니터링 (Health Check)
- 현재 가동된는 서버를 확인후 Gateway에 그 목록을 전달하는 역할

## Eureka 클라이언트

- MSA를 구성하는 요소들 중 Eureka서버에서 모니터링 및 관리를 원하는 요소를 Eureka 클라이언트 설정을 진행해서 등록할 수 있다.

# Config 서버

## Config 저장소

