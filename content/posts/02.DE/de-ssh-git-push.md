---
title: "[Git]ssh passphrase없이 commit하기"
date: 2024-05-15T15:52:55+09:00
draft: false
categories:
  - Data Engineering
tags:
  - Git
created: 2024-05-25T14:52
updated: 2024-05-25T19:26
---

## 문제상황

- SSH를 통해 git 저장소를 원격 저장소와 로컬에서 자동으로 동기화 하려함
- cron으로 12시간 마다 저장소를 업데이트 하려 했는데 git push 할때 마다 ssh passphrase를 입력해야함
- 로컬에서 저장소 업데이트를 자동화 하려면 passphrase를 따로 입력받지 않고 스크립트에서 자동으로 배포할 수 있게끔 설정을  잡아줄 필요가 있음



## 해결1

```bash

eval "$(ssh-agent -s)"
# ssh agent의 pid 확인
ssh-add

```


## 해결2

```bash

eval "$(ssh-agent -s)"
# ssh agent의 pid 확인
ssh-add

```


## Reference

- <https://www.asterhu.com/post/2023-12-21-use-ssh-github-push-crontab/>

