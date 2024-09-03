---
created: 2024-04-14T11:06
updated: 2024-08-30T13:35
---

# 240413 mlops 강의

데이터과학자 실무영역

- 모델 아키텍처
- 알고리즘
- 모델 구성요소
- 모델 구체적 구현사항

## ML 기본개념

- 학습 : blackbox
- 모델학습의 결과는 기본적으로 가중치파일의 집합
- 모델추론은 학습된 가중치에 가장 가까운 확률값을 레이어단위로 찾아가는 과정
- 기본적으로 어떤 임계값을 미리 정하고 그걸 넘어야 서빙을 한다
- 모델은 하나의 복합한 함수로 파일로 떨궈진다.
- ML모델은 Input Data의 성능에 영향을 받는다(데이터 의존성). -> 일반적인 모델은 배포이후 성능지표가떨어짐(데이터가 변화하기 때문에)
- 엣지케이스 : 예측하지 못한 사용자 결과

## ML 사이클

### 비즈니스 정의단계 고려사항

- ML도입시 비용대비 비즈니스효용성이 있는가.
  - 성능목표
  - 기술인프라요구사항
  - 비용 제약
  - 투명성: ml 라이프라이클의 모든 디테일을 의사결정관여자가 모두 들여다볼수 있어야한다.
  - 설명 가능성: xai
  - **머신러닝 시스템의 투명성과 설명가능성확보를 위해 KPI를 명확하게 설정할필요가 있다**
- 리스크평가
  - 특정기간 동안 모델을 사용할 수 없는 리스크
  - 특정표본에 대해 잘못된 예측을 반환할 수 있는 리스크 -> 모델은 선형적으로 성능이 떨어지게 되어 있음
  - 시간이 지남에 다라 모델정확도 떨어지는 리스크
  - 5 x 5 리스크 매트릭스 : 발생확률과 영향도 평가

### EDA & Preprocessing

EDA 핵심 체크리스트

- 관련 데이터세트 중 어떤 것을 사용할 수 있는가
- 데이터를 신뢰할 수 있는가
- 이해 관계자들이 이 데이터에 접근할 권한이 있는가
- 여러 데이터 소스를 조합하여 필요한 특성을 만들어낼 수 있는가
- 데이터 수집주기는 요구사항에 맞는가
- 데이터 레이블링이 필요한가
- 모델을 배포한 후 데이터를 어떻게 갱신할 것인가
- 비즈니스 목표와 함께 정의한 KPI를 어떻게 측정할 것인가?
- 이용약관, 목적성 PII 여부, 법적 검토, 소수 집단에 대한 고려 등을 준수했는가?

Feature Selection

데이터 파이프라인 정의

### 여기서부터 인덱싱 다시

### 모델 배포 고려사항

### 모델 컨테이너화

- 컨테이너데이터는 기본적으로 휘발됨. 컴퓨팅 자원을 유연하게 가져가기 위해 컨테이너를 사용하기 때문

### 컨테이너화된 모델 수행

### 스케줄링

- 투명성확보를 위해 airflow 사용

### 모델배포

아티팩트 : 모델의 모든 산출물을 의미

shadow test : AB테스트와 같지만 A에 들어오는 요청을 모두 복제에서 B로 넘김

online : 프로덕션레벨 실제모델

### 모델 피드백 루프

- 기본적으로 모델이 데이터 트렌드에 영향받음
- 모델 성능저하를 조기에 감지하고 최소한의 리소스로 개선

## MLops 필요이유

### 기존 시스템

### 기존 시스템의 문제

## MLops Architecture

### 0수준

- 수동 프로세스
- model registry

### 1수준

- ML 파이프라인자동화
- 형상관리

### 2수준

- CICD 파이프라인자동화
- 형상관리

## Amazon SageMaker

핵심기능

- Experiments & Trials : 실험을 추적, 관리
- Debugger : 훈련지표 및 시스템리소스의 실시간 모니터링
- SageMaker Studio Notebooks : 클라우드기반 ML용 노트북 인스턴스 및 환경 제공
- Processing / Train : 클라우드 컴퓨팅 자원을 활용한 ML 처리 및 추적
- Clarify : ML데이터, 모델의 바이어스 감지 및 모델 예측설명
- Deploy : 배포를 위한 완전관리형 인프라,도구, 워크플로

- Model Monitor : 모델의 성능 가시성 확보 도구
- Distributed Training : 분산훈련을 위한 전용 라이브러리
- Feature Store : 기계 학습 특성 관리를 위한 완전 관리형 서비스
- Pipelines : 기계학습을 위한 특수 목적용 CI/CD 서비스
- ML Governance : 목적별 거버넌스 도구 제공. 엑세스 제어 및 ML 프로젝트 투명성 향상

# 2nd Day 실습

## 04 추론데이터 서빙을 위한 API구축

DynamoDB

데이터 처리 및 저장의 역사

- CPU의 단위비용은 시간의 흐름에 따라 올라가지만 스토리지 비용은 낮아지고 있다.

관계형모델

- 정규화를 통한 중복 제거 -> CPU비용이 높아지고 스토리지 비용이 낮아짐(저장효율이 올라감)
- 기본적으로 수직적 확장(Scale UP) -> 컴퓨팅 파워의 크기를 늘리는 방식

NoSQL

- 중복허용
- 비정규화, 계층적
- 연산최적화->실시간, 빠른 응답
- 수평적 확장 -> 컴퓨터를 늘리는 방식

## Amazon DynamoDB

- node 수준이아닌 partition level에서 확장됨
-
- partition key : `=` 쿼리 패턴만 지원. 응답속도를 일정하게 가져감
- sort key : 2차 필터 지원. optional. 여러개의 필터를 가질 수 있음
- 하나의 row는 item

테이블 설계

- partition key는 primary key의 성격을 가짐
- 인덱싱되어 저장됨(Key-Value)

테이블 설계원칙

- 어플리케이션이 충족해야하는 특정쿼리 패턴을 알고 있는 경우에 DynamoDB사용
- 단일테이블이나 다형성 테이블설계
- 서비스 수준에 다형성 권장

GSI(Gloval Se)

```bash

python main_with_sagemaker.py
\ --namesapce dev
\ --base_date 2024-04-13
\ --task postprocess
\ --dataset_name prepared_watch_log
\ --instance_type ml.m5.large
\ --serve_ddb_table_name mlops-recommend-ddb-yjinheon-dev
\ --serve_recommend_type like
\ --serve_contents_type movie
\ --serve_data_version 1
\ --serve data_ttl 259200
\

```

```bash
command = f"""
python main_with_sagemaker.py \
  --namespace {namespace} \
  --base_date {today} \
  --task postprocess \
  --dataset_name prepared_watch_log \
  --instance_type ml.m5.large \
  --serve_ddb_table_name mlops-recommend-ddb-<유저명>-dev \
  --serve_recommend_type like \
  --serve_contents_type movie \
  --serve_data_version 1 \
  --serve_data_ttl 259200 \
  --serve_contents_limit 5 \
  --model_name {model_name}
"""
p = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print(p.stdout.decode("utf-8"))
```

dev환경에서 항상 같은 결과를 반환해야하기 때문에 seed고정

## Lambda

- soft limit : 리전동시성제약 (늘릴 수 있음)
- hard limit : 리전동시성제약 (늘리기 불가능)
- lambda의 동시성은 동시에 떠있는 함수의 수
- lambda의 동시성 확장. burst limit
- Reserved Concurrency : 여러 조직에서 공유하는 동시성을 어느정도 예약해서 가져가는것
- Provisioned Concurrency 동시성으로 cold start 문제를 어느정도 해결할 수 있다.
- Autoscaling with Provisioned Concurrency
- arn : lambda의 주소
- lambda는 가중치 기반 (round robin)

## Amazon API Gateway

## Airflow

- Airflow Worker

### Airflow Task

Operator : Operator
Sensor : 특정 이벤트가 발생하기를 기다리는 Operator의 특수하위 클래스
TaskFlow-decorated : @task로 정의된 파이썬 함수

순서정의

- `>>` ,`[]` : 대괄호는 병렬실행을 의미

X-Com

- Xcom은 직렬화 가능한 소규모 데이터 교환을 위해 설계됨
- 대용량 데이터를 교환하는데는 적합하지 않음

# 개념체크

- Feature Store
- model reposidoty
- ml metastore:w
- multiprimary 구성
- replica 개념
- DB connection은 맺을 때마난 컴퓨팅리소스 낭비가 심하기 때문에 전역변수로 선언해서 사용한다.
- 워크플로우에 대한 병렬적 학습

- soft limit : 리전동시성제약 (늘릴 수 있음)
- hard limit : 리전동시성제약 (늘리기 불가능)
- lambda의 동시성은 동시에 떠있는 함수
- lamda의 진입점은 main이 아니라 lambda function의 lambda handleer함수
