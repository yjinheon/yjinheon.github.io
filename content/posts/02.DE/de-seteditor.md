---
title: "[Linux]기본 에디터 neovim으로 변경하기"
draft: false
date: 2021-05-02T15:52:55+09:00
categories: ["Data Engineering"]
tags: ["Neovim"]
---

## 유저 편집기 변경

> nano -> nvim

현재 편집기 확인

```bash

# 현제 편집기 확인
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
