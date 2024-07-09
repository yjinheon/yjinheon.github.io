---
title: "[Git]원격저장소 추가하기"
date: 2024-05-16T15:52:55+09:00
draft: false
categories:
  - Data Engineering
tags:
  - Git
created: 2024-05-25T14:52
updated: 2024-06-28T17:49
---

## 개요

git 원격저장소 추가하기 정리
엄청 자주 하는 작업이지만 매번 찾아보면서 작업했기 때문에 이 참에 간단하게 정리한다.


## 절차

- git 저장소 만들기

```bash
git init
```

- 원격저장소 만들기(github)

**README, .gitignore 파일 만들지 말것. 원격저장소랑 로컬 저장소랑 충돌남**

- 로컬 저장소와 원격 저장소 연결

```bash
# 로컬 수정사항 반영 

git add .

# commit

git commit -m "feat: first commit"

#commit 이력으로 remote repository에 업로드

git push -u origin main
```