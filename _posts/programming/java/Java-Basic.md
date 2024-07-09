---
title: "[Java]기본컨셉들"
categories:
  - Programming
  - Java
tags:
  - java_basic
  - thread
date:
updated:
---


# Java 관련

## Java 구동방식

- 1차적으로 컴파일러를 통해 .java 파일을 .class 파일로 변환한다.(바이트 코드)
- 2차적으로 JVM을 통해 .class 파일을 실행한다.(JVM은 OS에 종속적이다.)

## 변수, 자료형, 할당, 리터럴

- 변수 : 데이터를 저장할 수 있는 메모리 공간. 변수를 선언한다는 것은 기본적으로 메모리에 기억 공간을 할당한다는 것이다.
- 자료형 : 변수에 저장되는 데이터의 타입을 결정
- 할당 : 변수에 값을 대입하는 것
- 리터럴 : 변수에 할당되는 값

```java
public class Variable {
    public static void main(String[] args) {
        int a ,b,c;
        a = 1;
        b = 2;
        c = a + b;
        System.out.println(c);
        float f = 3.14f;
    }
}
```

## Data Type

### Primitive Type

### User Defined Type

### 클래스

기본적으로 제공되는 자료형을 Primitive Type이라고 한다.

자료형이 기본적으로 제공되는 것이 아닌 사용자가 직접 만들어서 사용하는 것을 Reference Type이라고 한다.

클래스는 사용자가 직접 만들어서 사용하는 Reference Type이다.

## 배열

> 배열은 동일한 타입의 데이터를 여러개 저장하기 위한 연속적인 메모리 구조이다.

```java
public static void main(String[] args) {
 int[] arr = new int [3];
}
```

## 접근제어자

## 객체지향 프로그래밍

### 상속(Inheritance)

### 다형성(Polymorphism)

> 다형성이란 하나의 변수명, 함수명 등이 상황에 따라 다른 의미로 해석될 수 있는 것을 말한다.
> 자바에서 Overloading과 Overriding이 다형성의 예이다.

- 다형성의 본질은 인터페이스를 구현한 객체 인스턴스를 실행 시점에 유연하게 변경할 수 있다는 점이다.

## 객체지향 설계 원칙

### SRP(Single Responsibility Principle)

### OCP(Open-Closed Principle)

### LSP(Liskov Substitution Principle)

### ISP(Interface Segregation Principle)

### DIP(Dependency Inversion Principle)

## 호출방식

### Call by Value

### Call by Reference

> Call by Reference는 메서드 호출 시에 사용되는 인자의 메모리에 저장되어 있는 값(value)의 주소(Address)를 복사하여 보낸다. 따라서 메서드 내에서 인자의 값을 변경하게 되면, 그 값은 인자로 사용된 변수의 메모리에 저장되어 있기 때문에 변수의 값이 변경된다.

## 메모리

### Stack Memory

> Stack Memory는 메서드가 호출될 때마다 Frame이 추가되고, 메서드가 종료되면 해당 Frame이 제거되는 메모리 영역이다.

### Heap Memory

> Heap Memory는 프로그램이 사용하는 동적 메모리 영역이다.

- 자바에서는 new 연산자를 통해 생성되는 모든 객체는 Heap Memory에 저장된다.
- Heap Memory는 JVM이 시작할 때 생성되고, 모든 스레드가 공유한다.
- Heap Memory는 가비지 컬렉터에 의해 관리된다.

## Thread에 대한 이해

> #Java #concept `Thread` : 프로그램의 가장 작은 실행단위

### Thread

> Thread는 프로그램의 실행 흐름이다.

### Main Thread

### Thread Local

### Thread 의 상태

- New : Thread가 생성되고 아직 start()가 호출되지 않은 상태
- Runnable : 실행 중 또는 실행 가능한 상태
- Blocked : 동기화 블럭에 의해서 일시정지된 상태
- Waiting, Timed Waiting : Thread의 작업이 종료되지는 않았지만 실행가능하지 않은 일시정지 상태

### Thread 구현

### Runnnable

> `Runnable` : #concept
