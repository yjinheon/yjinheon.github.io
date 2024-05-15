---
title: "[Spring]Strategy_Pattern"
categories:
  - - backend
    - Spring
tags:
  - design-pattern
  - Spring
date: 
updated: 
status:
  - in_progress
---


### Strategy Pattern

> 변하지 않는 부분을 Context로 만들어 두고 변하지 않는 부분을 `Strategy` 라는 인터페이스를 만들어 해당 인터페이스로 구현하는 방식으로 변경에 쉽게 대처할 수 있는 구조를 만든 것.
> 기본적으로 상속이 아닌 Strategy  에 위임하는 방식으로 문제를 해결


- 디자인 패턴은 기본적으로 의도가 중요하다.


- Context : 일종의 템플릿
- Strategy : 구현할 로직


- 실행시점에 유연하게 Code Snippet을 전달함