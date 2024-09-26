---
id: tmp
aliases: []
tags: []
created: 2024-06-28T16:02
date: 2023-07-21T06:52:55.000Z
draft: true
title: 임시
updated: 2024-09-17T13:22
---

### Map loop 방법

### Java Map과 HashMap 차이

### Java List와 ArrayList , LinkedList 차이

### ETL tool 로서의 Apache Beam 알아보기

<https://esevan.tistory.com/19>

### isEmpty() 와 isBlank() 차이

- isEmpty() : 문자열의 길이가 0인지 확인.
- isBlank() : 문자열이 null이거나 공백만 있는지 확인. white space만 있는 경우도 true를 반환한다.

### stream api

peak() : 중간 연산자로 stream의 요소를 확인할 수 있다.

### ConcurrentHashMap

### Abstract Class vs Interface

#### 추상클래스의 활용

- 공통 멤버의 통합으로 중복 제거

### Audit Log Handling

- BlockingQueue;
- ExecutorService;
- Executors;
- LinkedBlockingQueue;
- Handler;
- LogRecord;

### private 생성자 사용이유

클래스의 인스턴스화를 막고 정적 메소드 만을 사용하도록 강제

### 모니터링 테이블 예시

```sql
CREATE TABLE task_exec_log (
    transaction_id varchar(40),
    task_order_id varchar(40),
    vehicle_type varchar(20),
    page int,
    vehicle_id varchar(20)
    stml text , -- retry purpose
    exec_time int(4),
    success boolean
);
```

### Collections Syncronized List

### 로깅을 위한 메시징 큐 어플리케이션

https://velog.io/@leehyeonmin34/weather-reminder-message-q-as-code

### 반드시 읽을 것

https://github.com/trimstray/the-book-of-secret-knowledge?tab=readme-ov-file#black_small_square-text-editors

![network-tools.png](assets/imgs/network-tools.png)

### Object Mapper

ObjectMapper는 Jackson 라이브러리의 ObjectMapper 클래스를 말한다. ObjectMapper는 JSON 데이터를 Java 객체로 변환하거나, Java 객체를 JSON 데이터로 변환하는 역할을 한다.

### VO에 대한 이해

각각의 annotation에 대한 이해

```java
@Data
@NoArgsConstructor
@RequiredArgsConstructor
@ToString // ?
public class TaskLogVo {
private BigDecimal taskLogId;
@NonNull private String transactionId;
@NonNull private String taskType;
private String taskId;
@NonNull private String taskName;
private String taskDescription;
private String vehicleId;
private String parentId;
private String direction;
private long executedTime;
private int expenseTime;
private String inputParam;
private String outputSchema;
private String executionError;
}
```

### Jackson 확장구조

- https://d2.naver.com/helloworld/0473330
- https://tomining.tistory.com/191

### Transactional의 이해

transactional은 메소드에 적용되는 어노테이션으로, 메소드가 실행되는 동안 트랜잭션을 시작하고, 메소드가 정상적으로 종료되면 트랜잭션을 커밋하고, 예외가 발생하면 롤백한다.

### 직렬화 역직렬화 개념

### class getName() vs getSimpleName()

### obsidian tasks export

quick add plugin

## 240916

- [ ] Generic Method

- [ ] 와일드 카드

- [ ] 타입 매개변수 상한

### 다형성

- 기본적으로 객체간에 상하관계가 존재
- 다운캐스팅 , 업캐스팅 가능

### 타입 매개변수 제한

### Generic Method

- Generic Method 타입추론 : 자바 컴파일러가 input type과 output type의 정보를 알고있기 때문에 타입을 메소드 실행시 명시할 필요가 없다.
- Generic Type 과 Generic Method 우선순위. 제네릭 메서드가 보다 더 우선함

- Generic Type보다 Generic Method가 우선함

### 와일드카드

- 비제한 와일드카드
- ? == <? extends Object>

- 단순히 일반 메소드에 제네릭 타입을 받을 수 있는 매개변수가 하나 있는 거

- 상한 와일드 카드
- 하한 와일드 카드
- 기본적으로 이미 만들어진 (타입이 결정된) 제네릭 타입을 전달 받아서 활용할 때 사용

### 타입 이레이저

자바의 제네릭 타입은 컴파일 시점에만 존재하고 런타임에는 제네릭 정보가 지워지는 데 이를 타입 이레이져라 한다.

## 240919

- [x] Logging pacakaging

### static method referenced non static method meaning

### 캡슐화

다음의 두가지 요소를 만족해야 한다.

- 데이터와 메서드 결합
- 데이터나 메서드를 은닉

### this 키워드

this는 기본적으로 객체 위치 주소값을 가리키는 포인터이다.

## 240925

### 기술스택들

⚡ 주문 플로우 차트 ⚡
Redis 기반의 재고 관리

효율적인 재고 관리를 위해 Redis를 활용한 캐싱 전략 도입
Redisson의 분산 락을 사용하여 1000건 이상의 대량의 동시 재고 감소 요청에도 데이터 일관성 유지
일정 주기로 DB와 동기화 작업을 수행하는 자동화 스케줄링
Flash Sale 이벤트 도입 : 일부 비동기 방식으로 전환 및 성능 최적화

재고 확인 및 감소 : 동기 방식과 분산 락 사용 → 데이터 불일치 문제 방지
결제 및 배송 처리 : 비동기적으로 전환하여 주문 속도 개선
평균 응답 속도가 50% 개선되었고, TPS는 300 → 350으로 약 17% 증가하여 대규모 트래픽에도 안정적인 주문 처리가 가능해짐
Kafka 기반 비동기 메시징 시스템 도입 → 이메일 전송 처리 성능 개선

사용자가 이메일 전송을 요청하면, Kafka 토픽에 이벤트를 발행하고 즉시 응답을 반환하는 구조로 변경
실제 이메일 전송 작업은 Kafka의 consumer가 해당 토픽을 구독하고, 백그라운드에서 비동기적으로 처리함
응답 시간 : 1건당 3980ms → 100건당 12ms로 개선, TPS : 0.26 → 95.69로 대폭 향상됨
API Gateway와 JWT 기반의 인증/인가 시스템

API Gateway를 통해 클라이언트 요청을 라우팅하고, 토큰 인증 필터를 적용하여 보안 강화
Access/Refresh Token 기반으로 인증 관리 및 Redis에 저장된 블랙리스트를 기반으로 로그아웃된 사용자의 접근 차단
Resilience4j의 CircuitBreaker 패턴을 도입하여 서비스 간 장애 전파 방지 및 안정적인 사용자 경험 제공

회원 정보 조회 시, Order Service와 연동하여 해당 회원의 주문 내역을 함께 조회하는 기능 구현
10번의 호출 중 절반 이상 실패 시 CircuitBreaker가 open 상태로 전환 → 에러 응답 대신 빈 주문 내역을 반환

#### 뭔가 적을 필요가 있을 경우 사용

# 이미지 렉카

![network-tools.png](assets/imgs/network-tools.png)
