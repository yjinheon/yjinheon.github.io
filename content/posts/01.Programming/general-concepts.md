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
updated: 2024-08-29T10:17
---

## 개요

알면 좋은 개념들을 정리한다.

## Java

---

**_Concept_**

- **클래스 로더** : JRE의 일부로 자바 클래스와 인터페이스를 동적으로 로드하는 하위 시스템. 자바 바이트 코드를 읽어서 JVM의 실행엔진이 사용할 수 있도록 JVM메모리의 메서드 영역에 적재하는 역할을 한다. 클래스 로딩은 기본적으로 클래스파일을 읽어서 바이너리 코드로 만들고 이를 메모리에 메서드 영역에 저장하는 과정이다. : Java
- **스택 메모리** : Stack Memory. 함수호출과 지역변수에 사용되는 메모리 영역. 함수 호출 시 할당되며 함수 호출이 끝나면 해제됨. : Java
- **가비지 컬렉터** : Garbage Collector. 더 이상 사용되지 않는 메모리를 해제하는 역할을 하는 매커니즘. : Java
- **힙 메모리** : Heap Memory. 객체를 저장하는 메모리 영역. 런타임에 동적할당됨 JAVA에서는 GC가 관리. : Java
- **원시 타입** : Primitive Type . int, long, float, double, boolean, char 등의 기본 데이터 타입. Stack Memory에 저장됨 : JAVA
- **참조 타입** : Referenced Type. 객체의 주소값을 저장하는 데이터 타입. null 값을 가질 수 있음. Heap에 저장됨 : Java
- **박싱과 언박싱** : Boxing & Unboxing. 원시타입과 해당 래퍼 클래스간의 변환을 의미한다. 원시타입을 래퍼 클래스로 변환할 경우 박싱, 래퍼클래스를 원시타입으로 변환할 경우 언박싱이라고 한다. : Java

---

## 메모리

### Stack Memory

> Stack Memory는 메서드가 호출될 때마다 Frame이 추가되고, 메서드가 종료되면 해당 Frame이 제거되는 메모리 영역이다.

### Heap Memory

> Heap Memory는 프로그램이 사용하는 동적 메모리 영역이다.

- 자바에서는 new 연산자를 통해 생성되는 모든 객체는 Heap Memory에 저장된다.
- Heap Memory는 JVM이 시작할 때 생성되고, 모든 스레드가 공유한다.
- Heap Memory는 가비지 컬렉터에 의해 관리된다.

# Web

## Unsorted

---

**_Concept_**

- **CORS** : Cross Origin Resource Sharing. 추가 HTTP 헤더를 사용하여, 한 출처에서 실행 중인 웹 애플리케이션이 다른 출처의 선택한 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 메카니즘. | WEB

---
