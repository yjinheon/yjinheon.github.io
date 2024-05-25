---
title: "[Git]기본적인 컨셉들"
date: 2021-07-17 21:52:37
tags:
  - git
categories:
  - - Infra
    - git
updated:
---

## git 시작하기


### git init

> 로컬에 저장소를 생성합니다.

```bash
git init <생성할레포>
```

### git clone

> 원격 저장소를 로컬에 복제 합니다.

```bash
git clone <클론할 레포>
```

### git add

> git repository에 파일이나 파일에 대한 변경사항을 추가합니다. git을 add 한다는
> 것은 새로운 파일이나 수정사항을 커밋하기 위해 staging area에 변경사항을
> 추가하는 것을 의미합니다.

#### git add 예제

- 테스트파일을 스테이징에 추가

```bash
touch test.md
git add test.md
```

-  수정사항이 있는 모든 파일을 staging area에 추가
```bash
git add .
```




## 컨셉

### git의 4가지 영역

### staging area

git 의 핵심은 사용자가 관리하고 싶은 파일들만 변경사항을 관리할 수 있다는
것이다. 이를 위해 필요한 것이 staging area(index) 이다.

staging area는 코드를 커밋 하기 전에 사용하는 일종의 중간영역이다.

git add 명령을 사용해 개별 파일이나 디렉토리를 추가하거나 전체 또는 특정
디렉토리의 모든 변경사항을 추가하는 옵션을 사용할 수 있다.

### git commit

> 변경사항을 git 저장소에 추가합니다. commit은 git에서 변경사항을 관리하는 가장
> 기본이 되는 단위입니다.

```bash
git commit -m"커밋메시지"
```

### git push

> commit 한 내용을 원격 저장소에 반영합니다.

### git pull

> 원격 저장소의 변경사항을 local 저장소에 반영한다. 기본적으로 git fetch와 git merge의 통합이다.

## git status

> 현재 저장소 상태를 확인합니다. 상태를 확인한다는 것은 저장소의 head, staging
> area를 확인한다는 것이다.

```bash
git status
```

### working tree

git에서 working tree는 현재 작업하고 있는 디렉토리를 뜻합니다.

```bash
 git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

### head 개념

git에서 heads는 현재 작업하고 있는 branch를 뜻합니다.


```bash
commit 273457e05c9a41180eafebd8009592312758b796 (HEAD -> main, origin/main, origin/HEAD)
Author: jinheonyoon <yjinheon@gmail.com>
Date:   Mon Mar 28 16:49:38 2022 +0900
```

## git branch

> git branch는 기능개발이나 이슈처리를 독립적으로 수행하기 위한 repository를
> 생성하고 관리하기 위한 명령어입니다.

### branch 사용 이유

> 기본적으로 여러작업을 독립적으로 동시에 진행하기 위해 사용합니다. 예를 들어
> feature를 추가하는 branch와 버그를 수정하는 branch를 따로 파고 나중에 merge
> 하는 방식으로 작업을 효율화하고 충돌을 방지할 수 있습니다.

### branch 생성

```bash
git branch <브랜치 명>
```

### branch 삭제

```bash
git branch -d <브랜치 명>
```

### branch 이름 변경

```bash
git branch -m <브랜치 명> <새 브랜치 명>
```

### branch 목록 조회

```bash
git branch -l(로컬 브랜치 목록 조회)
git branch -r  (원격 브랜치 목록 조회)
git branch -a  (모든 브랜치 목록 조회)
```

### branch 이동

```bash
git checkout <이동 브랜치>
```

### 특정 branch 생성 후 해당 branch로 이동

```bash
git checkout -b {New Branch Name}
```

### 모든 변경사항 취소

```bash
git checkout.
```

### 현재 branch 확인

## git merge

> git merge는 기본적으로 다른 branch를 현재 checkout된 브랜치와 병합하는 명령어
> 이다.

```bash
git checkout master # 마스터 브랜치로 이동

git merge test
```


## git remote

> 현재 프로젝트에 등록된 리모트 저장소를 확인하기 위해 git remote 명령어를 사용한다.


---
**NOTE**
refusing to merge unrelated histories 에러

git remote 저장소를 추가 한뒤 local에 있는 repository로 반영하려면  먼저 pull을 해서 프로젝트를 병합시켜줘야 한다.

단순히 git pull origin 브랜치 명을 사용하면 `refusing to merge unrelated histories` 에러가 발생하면서 병합이 되지 않는다.

이 때 서로 다른 두 레포지토리의 기록의 저장을 허용하는  `--allow-unrelated-histories` 옵션을 줘서 해결할 수 있다.

```bash
git pull origin 브런치명 --allow-unrelated-histories
```

---

### 로컬 저장소와 리모트 저장소 연결



### 리모트 저장소 추가


```bash

git remote add 

```


### 리모트 저장소 확인

```bash
git remote -v

```

### 리모트 저장소 버전 확인

```bash


```



## git merge

### Merge 명령옵션

#### --squash

%% 이 옵션은 대상 브랜치의 모든 커밋을 하나의 커밋으로 합쳐서 merge 하는
방식이다.

즉, 대상 브랜치에서 작업했던 히스토리를 하나의 메시지로 압축시키는 것이죠.

이 옵션은 테스트 브랜치에서 원래 브랜치에 병합할 때 유용한 방식입니다.

즉, 애초에 하나인 브랜치가 임시로 빠져나와서 다시 통합할 때 사용하는 것이
좋습니다.

예를 들어, master 브랜치가 있고, 이를 그대로 복사한 child 브랜치가 있다고
가정하겠습니다.

그리고 child 브랜치에서 커밋을 5번을 했다고 했을 때, 당연히 master branch보다
커밋 수가 앞서 있겠죠?

이 때 master 브랜치에서 --squash 옵션을 이용해서 child 브랜치를 병합하면, child
브랜치의 5번의 커밋 내역은 무시되고 파일 수정 이력만 받게 됩니다.

따라서 깔끔한 히스토리와 함께 merge를 할 수 있게 됩니다. %%

```bash
git merge --suash child # child의 commit을 한꺼번에 병합할 경우 사용
```

### Fast forword

> merge할 브랜치 의 commit이 현재 branch (masger 브랜치) 의 commit 보다 앞서가
> 있는 경우 기준 브랜치의 커밋을 대상 브랜치 커밋으로 이동시키는 merge 방식을
> fast forward라고 합니다.

- 기본적으로는 master branch의 head를 test branch의 head로 이동하는 것입니다.

## git log

> 프로젝트 히스토리를 시간 역순으로 보여줍니다.

```bash
git log --stat
```

최신커밋 확인하기

```bash
git log -n 1
```

https://lucas-owner.tistory.com/35

## git revert

## git config


## References

- https://www.lainyzine.com/ko/article/summary-of-how-to-use-git-for-source-code-management/


