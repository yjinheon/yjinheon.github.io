---
title: "프론트엔드 기본개념들"
date: 
tags:
  - [React,Concept]
categories:
  - [FrontEnd]
updated:
---

## 개요

- 리액트 관련 개념
- 프론트엔드 개념

## 개념

### Runtime

> Runtime은 기본적으로 프로그램이 자원(램, 변수 등) 을 할당받고 특정한 처리를 하고있는 상태를 의미한다.

- 실행시간 : 런타임은 일반적으로 어플리케이션 실행시간(execution time)과 동일한 의미를 가진다. 
- 어플리케이션 성능평가 : 런타임은 어플리케이션 성능평가를 위한 주요 지표이다. 런타임(실행시간)이 적을 수록 해당 어플리케이션이 보다 효율적이라 볼 수 있다.
- 런타임 최적화 : 메모리 사용을 늘리거나 보다 효율적인 알고리즘을 통해 런타임을 최적화(실행시간 줄임) 할 수 있다.
- 동시성과 병렬성 문제 : 실행할 작업을 여러 쓰레드나 프로세스로 나눠서 할당해 런타임을  최적화 할 수 있다.
- 트레이드 오프 : 런타임 최적화는 보통 더 많은 자원의 소모, 더 복잡한 코드의 작성을 수반하기 때문에 이에 따른 영향을 고려하면서 작업해야 한다.
- Runtime Error : 실행 중인 프로그램에서 발생할 수 있는 에러를 Runtime Error라고 한다.
    - Runtime Error의 종류
        - Null 참조
        - 메모리 부족
        - zero division

### Runtime Environment (RTE)

> 컴파일한 코드를 실행하기 위한 자원(메모리, 프로세서) 을 제공하는 일종의 실행환경.

기본적으로 Runtime이 일어나기 위해 어플리케이션이 OS의 시스템 자원에 접근할 수있도록 해주는 실행환경이다.


### Node Js

> 웹브라우저가 아닌 서버에서 자바스크립트를 실행할 수 있게끔 해주는 런타입 환경

```js
console.log("Hello World")
```

### NPM(Node Package Manager)

> 자바스크립트 라이브러리를 설치하고 버전관리를 위한 프로그램

### WebPack

> 프로젝트에 사용된 파일을 분석하여 브라우저에 호환되는 파일(js,css) 등으로 변환해주는 프로그램

### NVM(Node Version Manager)

> 노드 버전관리를 위한 프로그램

```bash
nvm -v
```

### Eventloop

### DOM

### Virtual Dom

### props

### component

### state

## References

<!--

- https://joontae-kim.github.io/2020/10/26/interview-question-fe/
-->

- https://joshua1988.github.io/web-development/interview/frontend-questions/
