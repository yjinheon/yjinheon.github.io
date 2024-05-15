---
title: "[Spring]Template method"
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


```java
TraceStatus status = null;

try {
	status = trace.begin("message");
	// 핵심기능 호출
	trace.end(status);
} catch (Exception e) {
	trace.exception(status,e );
	throw e;
}


```

- 기본적으로 변하지 않는 부분과 변하는 부분을 분리
- 추상클래스 활용
- 부모클래스에 변하지 않는 템플릿 코드 생성
- 변하는 부분을 자식클래스로 만들어서 구현
- 기본적으로 변경지점을 하나로 모아서 변경에 쉽게 대처할 수 있는 구조를 고민하는 것이다.
- 핵심은 하위 클래스가 알고리즘의 구조를 

### Template Method

> 작업에서 알고리즘의 골격을 정의하고 일부 단계를 하위 클래스로 연기. 하위 클래스가 알고리즘의 구조를 변경하지 않고도 알고리즘의 특정 단계를 재정의할 수 있음.


문제점

상속을 기본적으로 사용하기 때문에 상속의 단점을 그대로 가져감

- 자식클래스가 부모 클래스의 컴파일 시점에 강하게 결합하는 문제가 있음
- 자식클래스에서 부모클래스의 기능을 사욯하지 않음에도 자식이 부모클래스에 의존함
#### 추상클래스

#### 익명내부클래스

- 추상클래스 객체를 생성하면서 동시에 구현체를 만들기

#### Generic

- 타입 관련 정보를 객체 생성 시점으로 미루는 것
- 리턴타입을 정해두지 않는 것
- generic에서 반환 타입이 필요한 데 반환할 내용이 없을 경우 `Void`  타입 사용 후 null 반환
- generic은 기본타입인 void ,int 등을 선언할 수 없다.