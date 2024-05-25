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
- 로컬에서 저장소 업데이트를 자동화 하려면 passphrase를 따로 입력받지 않고 스크립트에서 자동으로 배포할 수 있게끔 설정을 잡아줄 필요가 있음

## 해결1

```bash

eval "$(ssh-agent -s)"
# ssh agent의 pid 확인
ssh-add

```

첫번째 방법은 세션 단위에서 passphrase를 매번 입력하지 않도록 설정하는 방식이다. 이 방식은 현재 세션에서만 유효하다. 즉, 세션을 종료하면 다시 passphrase를 입력해야 한다.

## 해결2

ssh key를 사용할 때마다 passphrase를 입력하지 않도록 설정

bashrc에 아래 내용을 추가

```bash
env=~/.ssh/agent.env

agent_load_env () { test -f "$env" && . "$env" >| /dev/null ; }

agent_start () {
    (umask 077; ssh-agent >| "$env")
    . "$env" >| /dev/null ; }

agent_load_env

# agent_run_state: 0=agent running w/ key; 1=agent w/o key; 2=agent not running
agent_run_state=$(ssh-add -l >| /dev/null 2>&1; echo $?)

if [ ! "$SSH_AUTH_SOCK" ] || [ $agent_run_state = 2 ]; then
    agent_start
    ssh-add
elif [ "$SSH_AUTH_SOCK" ] && [ $agent_run_state = 1 ]; then
    ssh-add
fi

unset env
```

로그인 시 자동으로 ssh-agent를 실행하고 ssh-add를 실행하여 passphrase를 입력하지 않도록 설정한다.

두번째 방법을 통해 crontab을 이용하여 자동으로 git 저장소를 업데이트하는 환경을 구축하였다.

## Reference

- <https://www.asterhu.com/post/2023-12-21-use-ssh-github-push-crontab/>
- <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/working-with-ssh-key-passphrases?platform=windows>
