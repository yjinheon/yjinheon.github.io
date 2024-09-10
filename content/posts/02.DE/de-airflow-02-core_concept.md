---
title: "[Airflow]핵심 컨셉들"
draft: true
date: 2024-03-02T06:52:55.000Z
categories:
  - Data Engineering
tags:
  - airflow
created: "2022-05-06T14:03"
updated: "2024-06-06T14:49"
---

<!--

이미지 넣는법

![](images/02_de/이미지경로.png)

-->

## Introduction

Airflow는 파이썬 기반의 데이터 오케스트레이션 툴로 주로 복잡한 데이터 파이프라인을 관리하는데 사용한다.
Airflow는 기본적으로 ETL Pipeline을 구축하고 관리하는데 사용할 수있으며 세부적으로 아래와 같은 기능들을 제공한다.

- Monitoring : 작업상태 모니터링, 로깅
- Manage Failures : 작업실패 감지, 재시도, 알림기능
- Dependencies : 작업간 의존성 관리
- Backfills : historic data 처리
- Scalability : 분산처리, 병렬처리
- Deployment : On-premise, Cloud, Kubernetes 배포

이 글에서는 Airflow Workflow를 구성하는데 필요한 핵심 개념들을 정리한다.

## Concepts

### Operator

- Operator는 A

### Task

### DAG

- DAG는 각 Task 들이 어떻게 실행되야 하는 지에 대한 일종의 명세이다.
- DAG는 작업 자체보다는 작업 간의 의존성, 작업 재시도방식, 작업 실행주기 , timeout 시 설정 등을 다룬다.

### Local Executer

![[local_executor.png]]

## Reference

What is Apache Airflow?
Apache Airflow is an open-source platform to programmatically author, schedule, and monitor workflows. It is used primarily in data engineering to manage complex data pipelines. With Airflow, you can define your workflows as Directed Acyclic Graphs (DAGs) using Python code, which provides flexibility and ease of use.

Key Concepts in Airflow
DAG (Directed Acyclic Graph)

Definition: A DAG is a collection of tasks organized in a way that specifies their execution order, ensuring there are no cyclic dependencies.
Function: It represents the workflow, defining the relationships and dependencies between tasks.
Example:
python
코드 복사
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

default_args = {
'owner': 'airflow',
'start_date': datetime(2023, 1, 1),
}

with DAG('example_dag', default_args=default_args, schedule_interval='@daily') as dag:
task1 = DummyOperator(task_id='task1')
task2 = DummyOperator(task_id='task2')
task1 >> task2
Task

Definition: A single unit of work within a DAG. Each task represents a specific action or operation.
Attributes: Each task has a unique task_id and is created by instantiating an operator.
Dependencies: Tasks can have dependencies on other tasks, defining the order of execution.
Operator

Definition: An Operator is a template that defines what a task does. It is a fundamental building block in Airflow.
Types:
Action Operators: Perform specific actions (e.g., BashOperator, PythonOperator).
Transfer Operators: Move data between systems (e.g., S3ToRedshiftTransfer).
Sensor Operators: Wait for a certain condition to be met (e.g., S3KeySensor).
DAG Run

Definition: An instance of a DAG execution. Each time a DAG is triggered (manually or by a schedule), a DAG Run is created.
Attributes: Has an execution date and can be in different states (running, success, failed).
Executor

Definition: The component responsible for running the tasks defined in the DAGs.
Types:
SequentialExecutor: Runs tasks sequentially.
LocalExecutor: Runs tasks in parallel on the local machine.
CeleryExecutor: Distributes tasks across multiple worker nodes.
KubernetesExecutor: Runs tasks as individual pods in a Kubernetes cluster.
Queue

Definition: A mechanism to manage and prioritize task execution. Tasks can be assigned to different queues.
Function: Helps in distributing and prioritizing tasks, especially in distributed execution environments.
Web Server

Definition: The user interface for Airflow, allowing users to monitor, trigger, and manage workflows.
Function: Provides a dashboard to visualize DAGs, check task status, view logs, and manage Airflow configurations.
Scheduler

Definition: The component that parses DAGs, determines task dependencies, and schedules task execution.
Function: Monitors the DAGs and triggers tasks based on their schedule and dependencies.
Metadata Database

Definition: Stores metadata about DAGs, tasks, and their states.
Function: Keeps track of task execution status, history, and scheduling information. Typically uses a relational database like PostgreSQL or MySQL.
Key Takeaways about Airflow Concepts
Flexibility and Extensibility: Airflow allows you to define workflows as code using Python, making it highly flexible and extensible.
Task Dependencies: Tasks within a DAG can have dependencies, ensuring they run in the correct order.
Scheduling: Airflow’s scheduler can trigger DAGs based on time intervals or external events.
Monitoring: The web server provides comprehensive monitoring capabilities, allowing users to track the progress and status of workflows.
Distributed Execution: Executors like CeleryExecutor and KubernetesExecutor enable distributed task execution, allowing for scalability and fault tolerance.
Metadata Storage: The metadata database keeps detailed records of task executions, which is essential for auditing, debugging, and optimization.
Queue Management: Using queues, Airflow can manage task priorities and distribution effectively, especially in complex workflows.
