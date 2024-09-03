---
title: "[IntelliJ]단축키 정리"
categories:
  - Tools
tags:
  - intellij
draft: false
created: 2024-07-21T10:58
updated: 2024-07-21T10:58
---

## 개요

- 자주 쓰는 Intellij 단축키를 생각날때마다 추가한다.
- VScode Keymap 기준으로 추가한다.
- 개인이 커스텀해서 쓰는 단축키라 Intellij 기본 단축키와 다른 단축키가 일부 있다.

## 단축키

### 뷰 관련

- `ctrl+w` : 현재 편집기 닫기

### 편집 관련

- `alt+insert` -> `ctrl+shift+]` : 커서 멈춤이슈로 변경
- `ctrl+e` : window switcher 열기
- `ctrl+enter` : window switcher에서 파일 선택
- `ctrl+shift+r` : 선택한 부분 리팩토링 옵션 표시
- `ctrl+shift+alt+n` : inline 변수 추출
- `ctrl+alt+t` : surround with. if, try catch 등 감쌀 때 사용
- `shift+shift` : 전체 검색
- `ctrl+alt+v` : introduce variable
- `ctrl+space` : 만능 단축키
- `ctrl+shift+ i` : 생성자, getter setter 등 생성
- `alt+insert` : 편집기에서 사용(생성자, getter setter 등 생성)

<!--

## 단축키
## VM 옵션

### 일반설정

-server : JVM이 서버 최적화된 HotSpot 컴파일러를 사용
-Xms4096m : 초기 힙 크기
-Xmx4096m : 최대 힙 크기

### 메모리 관리

-XX:NewRatio=3
-Xss16m : 각 스레드의 스택 크기

### 성능 최적화

-XX:+AlwaysPreTouch : 런타임 중 메모리 할당에 소요되는 시간을 줄여 성능을 향상
-XX:+TieredCompilation : JVM은 자주 사용되는 메서드를 여러 번 컴파일하여 성능 향상, 실행 속도 향상
-XX:ReservedCodeCacheSize=512m : 예약된 코드 캐시 크기
-XX:SoftRefLRUPolicyMSPerMB=50 : SoftReference Least Recently Used(LRU) 정책을 조정
-XX:+UseCodeCacheFlushing : 메모리가 부족할 때 코드 캐시를 지워 특정 시나리오에서 성능을 향상

### 시스템/어플리케이션 속성

-Dsun.io.useCanonCaches=false-ea : 파일 경로에 대한 정규화 캐시 사용을 비활성화하여 특정 환경에서 성능을 향상
-XX:CICompilerCount=4 : 백그라운드 컴파일 스레드 수
-Dsun.io.useCanonPrefixCache=false : 정규화를 위한 접두사 캐시 사용을 비활성화하여 특정 조건에서 성능을 향상
-XX:+HeapDumpOnOutOfMemoryError : OutOfMemoryError가 발생할 때 힙 덤프 파일을 생성하여 메모리 관련 문제 해결에 도움
-XX:-OmitStackTraceInFastThrow : 빠른 throw에서도 예외 메시지에 스택 추적을 포함
-Djdk.attach.allowAttachSelf=true : 디버깅 목적으로 JVM이 자체에 연결
-Dkotlinx.coroutines.debug=off : 프로덕션 환경에서 오버헤드를 줄이기 위해 Kotlin 코루틴에 대한 디버깅을 비활성화
-Djdk.module.illegalAccess.silent=true : 특정 타사 라이브러리에서 발생할 수 있는 불법 모듈 접근에 대한 경고를 표시하지 않음
-Dfile.encoding=UTF-8 : 기본 파일 인코딩
-XX:+UseG1GC : 메모리 사용 패턴이 변동하는 IDE와 같은 애플리케이션에 더 적합한 G1(Garbage-First) 가비지 컬렉터를 사용

-->
