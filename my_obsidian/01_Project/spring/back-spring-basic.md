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


# 디자인 패텬

