---
title: "[Spring]기본 컨셉들"
draft: true
date: 2023-07-21T06:52:55.000Z
categories:
  - Backend
tags:
  - spring
  - spring context
created: 2024-06-28T16:02
updated: 2024-06-30T11:10
---

## 참고 블로그

- https://dev-coco.tistory.com/category/%F0%9F%8C%88Programming/Spring

## 기본적인 컨셉들 정리

---

**_Concept_**

- **[Spring]ioc(inversion of control)** : 제어의 역전. 객체의 생성 및 생명주기 관리를 프레임워크가 담당하는 것. : Backend
- **[Spring]dependency injection** : 클래스가 의존성 객체를 외부에서 주입받음으로서 클래스간 결합도를 낮추는 것.객체가 의존하는 다른 객체를 외부에서 선언하고 이를 주입받아 사용하는 것 : Backend
- **[Spring]spring container** : 스프링에서 내부에 존재하는 자바 객체(Bean)의 생명주기를 관리하며 생성된 bean에 추가적인 기능을 제공하는것. 기본적으로 스프링이 관리하는 객체 사이의 의존관계를 결정할 수 있다. : Backend
- **[Spring]bean** : 스프링 컨테이너가 직접 제어권을 가지고 생명주기를 관리하고 의존관계를 부여하는 객체 : Backend
- **[Spring]bean factory** : 스프링 컨테이너의 최상위 인터페이스로 bean을 생성하고 관리하는 기본적인 기능을 제공 : Backend
- **[Spring]application context** : bean factory의 모든 기능을 상속하여 제공하고 프로파일 설정, 메시지 국제화 인터페이스 등 제공

---

### Dependency injection

**클래스가 의존성객체를 외부에서 주입받음으로서 클래스간 결합도를 낮추는 것**

- DI 자체는 단순히 의존성이 있는 객체를 외부에서 주입받는 것이다.
- 객체를 외부에서 주입받음으로 인해 객체간 결합도가 낮아지게 된다.
- 객체간 결합도가 낮다는 것은 하나의 클래스에 대한 의존도가 낮다는 것을 의미한다

**의존관계를 클래스로 추상화하기**

- 의존관계를 인터페이스로 추상화 할 수 있다.
- 의존관계를 인터페이스로 추상화 할 경우 보다 다양한 의존관계를 맺을 수 있고 실제 구현 클래스와의 관계가 느슨해지고 결합도가 낮아진다.
- 클래스 모델이나 코드에는 런타임 시점의 의존관계가 드러나지 않는다.
- 의존성 주입시 구현 클래스가 아닌 인터페이스에 의존하는 것은 SOLID OCP와 DIP에 기반한 전략 패턴이다. - OCP - 컨트롤러 입장에서는 서비스 클래스의 로직에는 관심이 없고 인터페이스의 메소드를 이용해 로직을 구성하기 때문에 내부로직의 변경에 영향받지 않는다(변화에 닫혀있다.) - 서비스 입장에서는 인터페이스만 준수하면 로직 변경이 자유롭다.(확장에는 열려있다.) - DIP - 인터페이스는 컴파일 시점에 어떤 클래스를 담을 지 결정하지 않는다. \* 구현 클래스는 컴파일시점에 결정된다.-> 서비스와 컨트롤러의 결합도가 느슨해진다.
  -> 결과적으로 구현 클래스에 직접 의존하는 것보다 중간에 추상화 계층을 만들어 의존성 주입을 해준는 것이 객체지향적인 전략 패턴에 맞는다.

- 런타임 시점의 의존관계는 컨테이너 팩토리같은 클래스 외부에서 결정된다.
- 이는 설계의 영역이기 때문에 클래스를 만들 때마다 무조건 인터페이스를 만들어주면서 결합도를 낮추고 확장성을 유지할 필요는 없다.
- 하나의 추상화계층에 대해 두 가지 이상의 다른 방식으로 구현을 할 것으로 예상되는 경우는 인터페이스를 사용하는 것이 좋다.

**DI의 장점**

- 의존성이 줄어든다. -> 의존대상의 변화에 영향을 덜 받는다.
- 재사용성이 높아진다.
- 코드 가독성이 높아진다(기능을 분리)

```java
class PastaChef {
    private PastaRecipe pastaRecipe;

    public PastaChef(PastaRecipe pastaRecipe) {
        this.pastaRecipe = pastaRecipe;
    }
}

class BurgerRestaurantOwner {
    private PastaChef pastaChef = new BurgerChef(new pastaRecipe());

    public void changeMenu() {
        pastaChef = new pastaChef(new TomatopastaRecipe());
    }
}
```

### Bean

- 기본적으로 싱글톤으로 빈을 생성한다

**기존 싱글톤 패턴의 단점**

- 클래스 밖에서는 오브젝트를 생성하지 못하도록 생성자를 private으로 만든다.  
   따라서 상속할 수 없으므로 객체지향의 장점인 상속과 이를 이용한 **다형성(polymorphism)을 적용할 수 없다**.
- 생성된 싱글톤 오브젝트를 저장할 수 있는 자신과 같은 타입의 스태틱 필드를 정의한다.  
   그런데 싱글톤은 사용하는 클라이언트가 정해져 있지 않으며, 아무 객체나 자유롭게 접근하고 수정하고 공유할 수 있는 **전역 상태**를 갖는 것은 **객체지향 프로그래밍에서는 권장되지 않는 프로그래밍 모델**이다.
- 스태틱 팩토리 메서드인 getInstance()를 만들고 이 메서드가 최초로 호출되는 시점에서 한번만 오브젝트가 만들어지게 한다. 그런데 **서버환경에서는 싱글톤이 하나만 만들어지는 것을 보장하지 못한다**.  
   서버에서 클래스 로더를 어떻게 구성하고 있느냐에 따라서 싱글톤 클래스임에도 하나 이상의 오브젝트가 만들어질 수 있기 때문이다. 여러 개의 JVM에 분산돼서 설치가 되는 경우에도 각각 독립적으로 오브젝트가 생기기 때문에 싱글톤으로서의 가치가 떨어진다.
- 그리고 싱글톤은 **테스트하기도 힘들다**. 만들어지는 방식이 제한적이라서 테스트에서 사용될 때 모의(Mock) 객체 등으로 대체하기가 힘들다. 초기화 과정에서 생성자 등을 통해 사용할 오브젝트를 다이나믹하게 주입하기도 힘들기 때문에 필요한 오브젝트는 직접 오브젝트를 만들어 사용할 수밖에 없다.

**기존 싱글톤 패턴의 단점을 보완하는 싱글톤 레지스트리(Singleton Registry)**

기존 싱글톤 패턴의 단점때문에 스프링에서는 직접 싱글톤 형태의 오브젝트를 만들고 관리하는 기능을 제공한다.

이를 **싱글톤 레지스트리(Singleton Registry)**라고 한다.

이는 스태틱 메서드와 private 생성자를 사용해야 하는 비정상적인 클래스가 아니라 평범한 자바 클래스를 싱글톤으로 활용하게 해준다. 이 덕분에 public 생성자를 구현할 수 있어서 생성자 파라미터로 의존관계 주입이 가능하고, 테스트 시 모의 객체도 생성이 가능하다.

가장 중요한 점은 싱글톤 패턴과 달리 스프링이 지지하는 객체지향적인 설계 방식과 원칙, 디자인 패턴(싱글톤 패턴 제외) 등을 적용하는 데 아무런 제약이 없다는 점이다.

**bean을 생성라고 로딩하는방식**

- lazy loading : 메서드나 클래스가 빈 로딩 요청을 받는 시점에 인스턴스 생성 및 로딩
- pre loading: 모든 빈과 설정파일들 이 ApplicationContext에 의해 로드 요청이 될 때 인스턴스화되고 로드됨다.

### 컨테이너

#### 컨테이너 기능

#### 컨테이너 생성과정

#### 컨테이너

- 구현 클래스에 있는 의존성을 제거하고 인터페이

### 스프링 컨테이너와 스프링 빈

### 싱글톤 컨테이너

- 싱글톤 레지스트리

### 컴포넌트 스캔

## 의존관계 자동 주입

## 빈 생명주기 콜백

## 빈 스코프

### Application Context

- Bean 생명주기 관리
- @Configuration이 붙은 클래스들을 설정정보로 등록
- ApplicationContext는 BeanFactory의 기능들을 상속받는다.
- ApplicationContext는 빈 관리 기능 + 편리한 부가 기능을 제공한다.
- BeanFactory를 직접 사용할 일은 거의 없다. 부가 기능이 포함된 ApplicationContext를 대신 사용한다.
- BeanFactory나 ApplicationContext를 스프링 컨테이너라고 부른다.

### 추상화

**구현 분리를 위한 인터페이스 사용**

- 의존관계에 있는 객체는 인터페이스에 의존한다. 인터페이스의 구현을 변경하더라도 이 책임을 사용하는 객체를 변경할 필요는 없다.

---

**_Concept_**

- **Interface** : 자바에서 Interface는 특정 책임을 선언하는 추상 자료형이다. 인터페이스를 구현하는 클래스는 이 책임을 정의해야 한다. : JAVA
- **[Spring]Service** : 보통 어플리케이션 개발에서 사용사례를 구현하는 객체를 서비스라 한다. : Backend | Web
- **[Spring]Repository** : 데이터베이스와 직접 작업하는 객체를 DAO또는 리포지토리라 한다. : Backend
- **[Spring]Proxy** : 이메일 전송 등 앱 외부와 통신을 담당하는 객체를 프록시라 한다. : Backend
- **[Spring]POJO** : 의존성이 없는 단순 객체로 속성과 메서드로만 구성됨 : Java | Backend | Web

---

## Entity, DTO , VO

### **Entity, DTO 클래스를 분리하는 이유**

Entity와 DTO를 분리해서 관리해야 하는 이유는 DB 와 View 사이의 역할을 철저히 분리하기 위해서 입니다.

Entity 클래스는 실제 테이블과 매핑되어 만일 변경되게 된다면 다른 클래스에 영향을 끼치고,  
DTO 클래스는 View와 통신하며 자주 변경되므로 분리 해주어야 합니다. (Entity 클래스 보호)

DTO는 Domain Model의 순수성을 지키기 위해 DTO는 Domain Model 객체를 그대로 두고 복사하여  
다양한 Presentation Logic을 추가한 정도로 사용하며,

- DTO copy(Domain Model) + Persentation Logic

Domain Model 객체는 Persistence 만을 위해 사용한다.