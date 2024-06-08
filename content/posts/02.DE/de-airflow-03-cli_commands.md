---
title: "[Airflow]CLI Commands"
draft: false 
date: 
categories:
  - Data Engineering
tags:
  - airflow
created: 2024-06-06T14:03
updated: 2024-06-06T14:49
---

<!--

이미지 넣는법

![](images/02_de/이미지경로.png)

* Upgrade the metadatabase (Latest schemas, values, ...)

```bash
airflow db upgrade
```
-->

## Introduction

자주 쓰는 airflow cli 명령어들 정리
지속 업데이트

## CLI Commands


### mermaid test

{{< mermaid >}}
graph TD
    User --> Webserver
    Webserver <--> Scheduler
    DAGs -->  Scheduler
    airflow <--> Metadata_db[(metadata db)]
    Scheduler --> |Schedules tasks|Executor
    Executor --> |Executes tasks|workers
    DAGs <--> workers
    Metadata_db <--> workers

    subgraph airflow
        direction TB
        Webserver
        Scheduler
        Executor
    end

    subgraph workers
        Worker1
        Worker2
        Worker3
    end
{{< /mermaid >}}

### Testing

- 실질적으로 가장 많이 사용하게되는 명령어
- 작업한 DAGd의 tasks가 잘 동작하는지 확인하기 위해 사용
- 과거시점도 execution_date로 전달 할 수 있기 때문에 backfilling에도 사용됨

```bash
airflow tasks test <dag_id> <task_id> <execution_date>
```

## DB

* 메타데이터 데이터베이스 실행

```bash
airflow db init
```

- 메타데이터 DB 초기화

```bash
airflow db reset
```

