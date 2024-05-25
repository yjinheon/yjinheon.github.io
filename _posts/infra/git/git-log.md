---
title: "[Git]commit, push 제외 자주쓰는 git 명령어들"
date: 2021-08-02 00:00:00
tags: 
  - Git
categories:
  - [Infra,git]
updated:
---

<!--

merge 렉카 : https://kotlinworld.com/277

merge flow :
master 에서 출발
나의 작업용 브랜치를 만들기 위해 master 에서 feature 브랜치를 생성
feature 브랜치에서 add commit 등의 작업
내가 지금까지 push했던것은 local에 있던 코드를 remote의 브랜치로 전달한것
PR 메시지 작성
remote feature 에서 remote master로 merge
local master에서 최신의 remote master 내용을 반영하기 위해 git pull origin master
local feature 에서 최신이 된 local master 내용을 반영하기 위해 git merge master
충돌 발생 (local feature 에서)
충돌 해결 후 add ,commit => 새 변경 사항
remote feature에 새 변경 사항을 push
충돌 해결 (remote feture 에서)

-->

#### Branch 생성

```bash
git branch
```

#### 생성한 Branch로 이동

```bash
git switch example
```

- branch를 만들면서 현재 branch 변경

```bash
git switch -c example2  # c 는 아마 create를 의미
```

#### branch 삭제

```bash
git branch -d example
```

- merge가 정상적으로 안되는 branch를 강제 삭제할 겨우

```bash
git branch -D example
```

- 원격 브랜치를 삭제할 경우

```
git push origin --delete example
```

#### 파일옮기기, 이름 바꾸기

단순히 unix mv 명령어를 사용해도 된다.

```bash
git mv  old_file new file 
```

#### 커밋내역 확인하기

log를 통해 이전 커밋 내역을 확인한다.

```bash
git log
```

#### 커밋내역 삭제하기

```bash
git reset HEAD~n  최근 내역 n개 삭제
git log  # 삭제된 커밋 확인
```

#### 변경사항 복원하기

restore  :  변경 내역이 있는 파일을 복원할 수 있다.

```bash
git restore a_file 
```

- stage 된 파일 복원

```bash
git restore --staged a_file
```

#### branch 합치기(merge)

- 여기서는 현재 branch의 commit을 대상이 되는 branch의 commit까지 옮기는 작업인 `Fast Forward Merge` 만 다룬다.
- `Fast Forward Merge`는 중간에 다른 커밋이 추가되면 충돌 오류가 발생한다.

```bash
git switch example
git merge example2
```

## References

- [브랜치와 Merge의 기초](https://git-scm.com/book/ko/v2/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EB%B8%8C%EB%9E%9C%EC%B9%98%EC%99%80-Merge-%EC%9D%98-%EA%B8%B0%EC%B4%88)
- https://git-scm.com/book/ko/v2
- https://goddaehee.tistory.com/274
