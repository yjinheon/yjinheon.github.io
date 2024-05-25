---
title: '[Pyspark]하둡의 컨셉 이해하기'
categories:
  - Data Engineering
date: 2021-12-29
updated:  
tags: 
    - Pyspark
    - Hadoop
---
> Pyspark를 본격적으로 쓰기 전에 하둡의 컨셉을 간단히 정리하자.

## 하둡

: 하둡은 Data Locality에 바탕을 둔 분산컴퓨팅을 위한 소프트웨어 플랫폼 및 프레임워크이다. 기본적인 컨셉은 분산처리(큰 문제를 작은 문제의 집합으로 나누고 정리하는 것)이다.

하둡은 HDFS (Hadoop Distributed File System) 와 YARN(Yet Another Resource Navigator)로 구성된다.

- 하둡은 데이터가 비공유 접근을 허용하는 클러스터의 노드에서 지역적으로 처리될 수 있게 한다
- 각 노드는 다른 노드들과 통신할 필요 없이 전체 데이터의 훨씬 작은 부분을 독립적으로 처리할 수 있다.
- 기본적으로 분산시스템이기에 네트워크 연결을 통해 여러 연산자원(노드들)의 사용을 조정한다.
- 선형적 확장성을 가진다. 이는 노드의 수 , 스토리지의 양 , 잡 루틴이 선형적 관계로 엮여있다는 것을 의미한다. (만약 노드의 수를 늘린다면 그만큼 처리시간이 줄어들 것이라고 예측할 수 있다.)

**데이터가 기본적으로 분산되어있고 확장가능하며(노드의 수를 늘리는 방식으로) 오류에 대처할 수 있다.**

이는 분산파일시스템의 구현을 통해 가능해진다.

### Schima-on-Write

: 데이터를 저장할때 스키마를 우선 정의하는 것

주로 RBDMS에 자주 쓰인다. 데이터에 대해 익숙하고 자주 쓴다고 가정할 경우 Schima-on-Write 방식이 보다 적합할 수 있다.

### Schima-On-Read

: 분석을 위해 파일 시스템에서 데이터를 읽을 때 스키마가 정의되는 것.

반구조화를 포함한 광범위한 데이터를 저장하고 처리할 수 있다.이는 데이터를 원본 그대로 저장할 수있다는 것을 의미하며 빅데이터 처리 측면에서 강점을 가진다는 것을 의미한다.

<img src="https://www.oreilly.com/content/wp-content/uploads/sites/2/2019/06/hwyn_0105-2d2be3e87d610d5bece7f647d47d5fcc.png" alt="drawing" width="500"/>

### Data Locality

: 데이터가 있는 곳으로 이동해서 계산하는 것. 데이터의 이동이 아닌 계산의 이동.

**데이터 지역성은 계산하기 위해 데이터를 이동하는 것이 아니라 데이터를 그대로 두고 계산을 이동시키는 것이다.**
빅 데이터를 계산하기 위해 데이터를 이동(move)를 최대한 줄여
시스템 쓰루풋(throughput)과 혼잡도를 늦추게 하는 것이다. 
따라서 통신 대역폭이 당연히 줄어들고 성능은 늘어난다.

기본적으로 대용량데이터를 다룰경우 데이터를 옮기는 것보다 프로그램 자체를 이동시키는 것이 효율적이라는 아이디어에 기반한 개념이다.

## 비공유 아키텍처

: Shared Nothing Architecture

분산 컴퓨팅에 사용되는 아키텍처로 RAM, Disk 등의 자원을 공유하지 않는 독립적인 노드들로 이루어진다.

각각의 노드는 독립적인 처리장치와 프로세스, 디스크를 가지고 있다.

<img src="https://phoenixnap.com/kb/wp-content/uploads/2021/09/shared-nothing-architecture-diagram.png" alt="drawing" width="800"/>

### Node

### Cluster

### Mater/Slave

## References

- https://en.wikipedia.org/wiki/Shared-nothing_architecture
- https://phoenixnap.com/kb/shared-nothing-architecture