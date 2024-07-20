---
title: "[Python]poetry 가상환경"
draft: false
date: 2022-04-02T06:52:55.000Z
categories:
  - Programming
  - Python
tags:
  - python
  - poetry
created: 2024-06-13T15:50
updated: 2024-07-18T13:54
---


<!--

<center>Kaggle Customer Score Dataset</center>

https://velog.io/@whattsup_kim/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%99%98%EA%B2%BD-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0-2-Poetry

--->


### poetry 초기 설정하기

프로젝트 폴더 내부에 가상환경 만들기

```bash
poetry config virtualenvs.in-project true
poetry config virtualenvs.path "./.venv"

# 인터프리터가 나오지 않을 경우 아래 명령어로 인터프리터 위치를 탐색
which python
```




