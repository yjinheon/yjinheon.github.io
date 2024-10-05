---
title: "[Linux]Linux container timezone 설정"
draft: false
date: 2023-07-21T06:52:55.000Z
categories:
  - Data Engineering
tags:
  - linux
---

## 개요

리눅스 ec2 인스턴스에서 생성된 기본 timezone은 UTC이다. 이를 local KST로 변경하자.

## **1. timezone 확인**

```bash
date
```

## **2. timezone 변경**

- 현재 timezone 이 설정된 symbolic link 삭제

```bash
sudo rm /etc/localtime
```

- symbolic link 재생성

```bash
sudo ln -s /usr/share/zoneinfo/Asia/Seoul /etc/localtime
```

- timezone 변경 확인

```bash
date
```
