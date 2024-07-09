---
title: "[Java]Memory"
draft: true
date: 2021-05-02T06:52:55.000Z
categories:
  - Programming
  - Java
tags:
  - stack
  - heap
  - memory
created: 2024-06-13T15:50
updated: 2024-06-29T22:48
---

## 개요

업무상 알아야되는 지식들 정리


---
**_Concept_**

-  **클래스 로더** : 자바 바이트 코드를 읽어서 JVM의 실행엔진이 사용할 수 있도록 JVM메모리의 메서드 영역에 적재하는 역할을 한다. 클래스 로딩은 기본적으로 클래스파일을 읽어서 바이너리 코드로 만들고 이를 메모리에 메서드 영역에 저장하는 과정이다.
-  **스택 메모리** : 
-  **힙 메모리** : 
---


## 메모리

### Stack Memory

> Stack Memory는 메서드가 호출될 때마다 Frame이 추가되고, 메서드가 종료되면 해당 Frame이 제거되는 메모리 영역이다.

### Heap Memory

> Heap Memory는 프로그램이 사용하는 동적 메모리 영역이다. 

- 자바에서는 new 연산자를 통해 생성되는 모든 객체는 Heap Memory에 저장된다.
- Heap Memory는 JVM이 시작할 때 생성되고, 모든 스레드가 공유한다.
- Heap Memory는 가비지 컬렉터에 의해 관리된다.
