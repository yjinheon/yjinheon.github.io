---
title: "[linux]데이터 관련 프로젝트시 자주 사용하는 commandline 명령어 모음"
categories:
  - - Data Engineering
    - Linux
date: 2021-10-08 17:09:02
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

## 데이터 관련 프로젝트시 자주 사용하는 commandline 명령어 모음

### 도움말

- man

### 파일관리

- pwd
- cd
- ls
- mkdir
- rmdir
- cp
- mv
- rm
- ln
- chmod

### 파일처리

- cat
- echo
- head
- tail
- more/less
- grep
- sed\*
- awk\*
- find\*
- which
- sort
- uniq
- cut
- tr
- zip
- unzip
- gunzip
- tar

### 프로세스 관리

- top
- ps
- kill
- fg
- bg

### 네트워크

- ssh
- scp
- ping
- traceroute
- curl
- finger
- who

### 편집기

- vi
- vim
- nvim
- nano

### 파이프와 리디렉션

### 셀 환경변

- export
- $path
- $ps1

### 권한관리

#### 파일권한체크

```bash
stat -Lc '%a %A'
```

- `stat` 메타데이터 정보 확인
- `-L` symlink 파일 참조
- `-c` output 설정
- `%a` 8진법 권한
- `%A` Human readable한 권한

### Unsorted

- cal
- history

**References & annotation**

---

- 따라하며 배우는 데이터과학 (책)

