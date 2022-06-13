---
title: "[Git]간단한 Git 명령어 및 용법 정리"
date: 2021-07-17 21:52:37
tags:
categories:
  - [Tools]
updated:
---

## Intro

Git은 버전관리와 협업을 위한 툴입니다. 추후 참고할 수 있도록 간단히 내용을 정리하겠습니다.

---

## Git 동작원리

### Git의 영역들

- **Project 영역(working tree)** : 현재 프로젝트에 있는 파일들 전체입니다.
- **Stagind 영역(staging area)** : Project 영역에서 변경된 사항들을 기록하는 index 입니다.
- **Repository** : 깃이 버전 관리를 하기 위해 필요한 데이터들을 저장하는 곳입니다.깃을 초기화해 버전관리를 한 시점부터 현 시점까지의 파일들이 저장되어 있습니다.
  - local  : 사용자의 Local 머신에 저장된 레포지토리입니다.
  - remote : Github, Gitlab 등의 웹 저장소에 레포지토리 입니다.

### Git에서 수행하는 작업들

Git은 기본적으로 Project영역에서 수정작업을 한 뒤 index에 `staging`하고 이를 로컬저장소에 `commit`하고 원격저장소에 `push` 하는 절차를 거칩니다.

- **특정 프로젝트의 업데이트 내용 기록(버전관리)**
  - git add
  - git status
  - git log
  - git commit
- **같은 파일을 여러 작업자가 수정 및 관리(협업)**
  - git branch
  - git checkout
  - git remote add 저장소
  - git fetch
  - git merge
  - git pull
  - git push

![ohno](git-simple.png)
**<그림 1 git 동작원리>**

## git commit
간단한 연습용 프로젝트를 통해 Git을 이해해봅시다.
일단 적당히 디렉토리를 만들고 git을 초기화 합니다.

```bash
mkdir new_project
cd new_project
git init
```
적당한 파이썬 파일 하나를 디렉토리에 추가해 줍니다.
`vim` 이나 `sublimetext` ,`vscode` 등의 편집기를 활용해 파일들을 수정할 수 있습니다.
여기서는 bash shell에서 간단한 명령을 추가했습니다.
```bash
touch this.py
# 파일 편집을 위한 적당한 명령 추가
echo "import this" >> this.py
```
`git status` 를  통해  확인해보면 `commit` 할 파일이 없다고 나옵니다.
이는 파일이 아직 Staging 영역의 index에 올라가지 않아서 그렇습니다.
```bash
git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        this.py

nothing added to commit but untracked files present (use "git add" to track)

```
방금 생성한 파일을 git이 추적하도록 git add를 해줍니다.
만약 폴더 내 여러 파일을 편집한 상황에서 모든 변경사항을 반영하고 싶다면 `git add .`를 해주면 됩니다. 

```bash
git add this.py
```
이제 폴더 내 변경사항이 index에 staging되었으니까 local 저장소에 `commit`을 해줄 수 있습니다.
`commit -m` 을 통해 어떤 부분이 변경되었는지 간단히 메시지를 적어줄 수 있습니다.
```bash
git commit -m "this.py 파일 추가"
```
여기까지가 `working directory` -> `local repository`의 작업흐름입니다.
## git remote
`remote repostory` 는 데이터가 웹 서버에 저장된다는 것을 제외하면 로컬의 그것과 다를게 없습니다. 

서버에 저장소를 만들어 둠으로서 보다 여러 사람들이 저장소에 접근하고 수정할 수 있게끔 해서 소스코드 관리를 보다 편리하게 할 수있습니다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile8.uf.tistory.com%2Fimage%2F27532A36575F3888290EC8)
**<그림2 remote repository>**

`git remote add ` 를 통해 로컬을 외부저장소와 연결할 수 있습니다.
```bash
git remote add origin '외부저장소 링크'
```

`git push`  를 통해 로컬저장소의 내용을 서버의 외부저장소로 전송할 수 있습니다.

```bash
git push -u origin main
```

`git fetch`  를 통해 외부저장소의 변경사항을 로컬로 가져올 수 있습니다. 
이 변경사항을 로컬의 작업내역들과 비교할 수 있고 만약 누군가가 생성한 신규 커밋들이 로컬에서 작업한 부분과 중복되는 부분이 있다면 이를 알 수 있습니다.
```bash
git fetch '외부저장소명' '브랜치명'
```

`git merge`  를 통해 외부저장소의 내용과 로컬의 내용을 동기화합니다.

```bash
git push -u origin main
```

`git pull`  를 통해 `git fetch`와 `merge`를 한번에 시행할 수 있습니다.
`git fetch`를 통해 외부저장소의 변경사항을 확인하고 `git merge`를 통해 로컬과 외부저장소를 병합합니다.

```bash
git pull
```
## git branch

**branch는 git의 커밋과 커밋 사이를 이동할 수 있는 일종의 포인터 입니다.** 

git branch는 git의 버전관리와 협업의 핵심이 되는 컨셉입니다.

여러 작업자가 동시에 작업해야 하는 큰 프로젝트가 있을때 git branch를 사용해서 생산성을 높일 수 있습니다.

![](git-branch.png)

`git branch` 를 통해 현재 branch들을 조회합니다. -a 를 통해 원격과 로컬 branch를 모두 조회할 수 있습니다.

```bash
git branch
```
새 branch를 만듧니다.
```bash
git branch 브랜치명
```
원래 branch를 새로운 branch로 변경합니다.
```bash
git branch -m 원래브랜치 새로운브랜치
```
main에서 새로운 브랜치 new를 만듭니다.
```bash
git branch new main
```
브랜치를 삭제합니다.
```bash
git branch -d 브랜치
```
해당 브랜치로 작업영역을 변경합니다.
```
git checkout 브랜치
```

A 브랜치를 현재 브랜치로 합칩니다.
```
git merge A
```
---

## References

- https://opentutorials.org/module/2676/15202
- https://dzone.com/articles/top-20-git-commands-with-examples
- https://git-scm.com/book/ko/v2/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EB%B8%8C%EB%9E%9C%EC%B9%98%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80

