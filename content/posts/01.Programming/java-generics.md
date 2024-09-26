---
title: "[Java]Generics 개념"
draft: true
date: 2024-06-02T06:52:55.000Z
categories:
  - Programming
  - Java
tags:
  - Java
  - Generic
created: 2024-09-16T23:00
updated: 2024-09-17T13:21
---

# Generic

## 다형성

- 기본적으로 객체간에 상하관계가 존재
- 다운캐스팅 , 업캐스팅 가능

## Generic

- **기본적으로 데이터 타입의 결정을 미래 시점으로 미루는 것.**

- 생성시점에 원하는 타입 지정 : 다이아몬드 기호 안에 타입 매개변수 지정
- 타입 매개변수 : Generic 클래스나 메소드에서 타입으로 활용. 보통 T 표시
- 객체 생성시점에 모든 참조형 타입을 지정할 수 있다.
- 타입 추론 : 제네릭 타입 객체 생성시 new 에서 타입을 생략할 수 있다.
- 메소드와 제네릭 : 메소드는 매개변수에 인자를 전달해서 사용할 값을 결정. **제네릭은 타입 매개변수에 타입 인자를 전달해 타입을 결정.**

---

**_Concept_**

- **Generic** : 데이터 타입이 나중에 결정되는 것을 의미. 클래스에서 사용할 객체의 데이터 타입을 컴파일 시점에 결정하는 것. 컴파일 시 타입 체크를 하기 때문에 런타임 에러를 방지할 수 있으며(타입안정성) 실행 시점에 다른 타입을 받아서 처리할 수있기 때문에 생산성이 늘어난다.(재사용성)
- **Type Parameter** : Generics에서 데이터 테입을 전달하는 변수. Generic class를 사용할 때 실제 타입으로 대체된다.

---

### Generic Method

- Generic Method 타입추론 : 자바 컴파일러가 input type과 output type의 정보를 알고있기 때문에 타입을 메소드 실행시 명시할 필요가 없다.
- Generic Type 과 Generic Method 우선순위. 제네릭 메서드가 보다 더 우선함
- Generic Type보다 Generic Method가 우선함

---

**_Concept_**

- **Generic Method** : 데이터 타입이 나중에 결정되는 것을 의미. 클래스에서 사용할 객체의 데이터 타입을 컴파일 시점에 결정하는 것. 컴파일 시 타입 체크를 하기 때문에 런타임 에러를 방지할 수 있으며(타입안정성) 실행 시점에 다른 타입을 받아서 처리할 수있기 때문에 생산성이 늘어난다.(재사용성)

---

### 타입 매개변수 제한

### Generic Method

### Variance

---

**_Concept_**

- **Concept1** : definition
- **Concept** : definition2
- **Concept1** : definition
- **Concept1** : definition
- **Concept1** : definition

---

### Wildcard

와일드 카드는

- 비제한 와일드카드
- ? == <? extends Object>

- 단순히 일반 메소드에 제네릭 타입을 받을 수 있는 매개변수가 하나 있는 거
- 상한 와일드 카드
- 하한 와일드 카드
- 기본적으로 이미 만들어진 (타입이 결정된) 제네릭 타입을 전달 받아서 활용할 때 사용

---

**_Concept_**

- **Concept1** : definition
- **상한 와일드카드** : definition2

---

### Type Erasure

[[java-mid2-index]]
