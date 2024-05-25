---
title: "[linux]기본 에디터 neovim으로 변경하기"
categories:
  - - Data Engineering
    - Linux
date: 2021-11-08 17:09:02
updated:
tags:
  - commandline
  - Linux
modified: 2023-12-30T13:35:45+09:00
---

<!--
<center>Kaggle Customer Score Dataset</center>

- Machine Learning
- Statistics , Math
- Data Engineering
- Programming
- EDA & Visualization
- Preprocessing


#신경망이란 무엇인가?

https://www.youtube.com/watch?v=aircAruvnKk


#참고

https://cinema4dr12.tistory.com/1016?category=515283

https://www.kdnuggets.com/2021/07/top-python-data-science-interview-questions.html
-->

## 유저 편집기 변경

> nano -> nvim

현재 편집기 확인

```bash

# check current editor
echo $EDITOR
```

현재 쉘의 편집기를 리눅스 환경변수로 등록

```bash
nvim ~/.bashrc


export VISUAL="nvim"
export EDITOR=$VISUAL

source ~/.bashrc
```

## 글로벌 설정

```bash

sudo nvim /etc/profile

```
