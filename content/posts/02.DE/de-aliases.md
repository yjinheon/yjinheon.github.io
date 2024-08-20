---
title: "[Config]Aliases"
draft: false
date: 2024-03-02T06:52:55.000Z
categories:
  - Data Engineering
tags:
  - aliases
  - config
---

터미널 작업시 걸어두는 alias 정리. 없으면 상당히 불편해진다.

```bash
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias grep='grep --color=auto'
alias l.='ls -d .*'
alias ll='ls -l'
alias pg_ctl='pg_ctl -D /data/postgres/data' # db 경로에 따라 수정
alias which='alias | /usr/bin/which --tty-only --read-alias --show-dot --show-tilde'
```
