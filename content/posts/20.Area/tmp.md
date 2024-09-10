---
id: tmp
aliases: []
tags: []
created: 2024-06-28T16:02
date: 2023-07-21T06:52:55.000Z
draft: true
title: 임시
updated: 2024-09-10T08:51
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

# 이미지 렉카

![network-tools.png](assets/imgs/network-tools.png)
