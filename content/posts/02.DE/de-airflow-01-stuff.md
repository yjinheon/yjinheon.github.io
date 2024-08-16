---
title: "[Airflow]Stuff"
draft: true
date: 2024-03-02T06:52:55.000Z
categories:
  - Data Engineering
tags:
  - airflow
created: 2024-06-08T18:29
updated: 2024-07-09T11:00
---

<!--

이미지 넣는법

![](images/02_de/이미지경로.png)

-->

# Executer

## Executer concept

Executor는 task를 실행하는 방법을 결정한다. Airflow는 다음과 같은 세가지의 executer를 제공한다.

### Sequential Executer

SequentialExecuter는 task를 순차적으로 실행한다. 이 executer는 개발과 테스트 목적으로 사용된다. 이 executer는 실제로 사용하기에는 매우 느리다.

### Local Executer

![[local_executor.png]]

# Core Concepts

# Scheduling

execution_date
