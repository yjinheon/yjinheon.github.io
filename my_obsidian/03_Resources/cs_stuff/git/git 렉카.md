
## Git 명령어 렉카

### git stash

> 로컬의 작업중 변경사항을 커밋하지 않고 저장

```bash
git stash -m 'message' # 작업중이던 변경된 파일들 stash 영역에 저장
git stash show [stash number] # stash 영역에 저장된 파일 보기
git stash list # 생성한 stash 리스트 보기
git stash apply [stash number] # 번호에 해당하는 stash 영역에 있는 파일들 불러오기
git stash drop [stash number] # 번호에 해당하는 stash 영역 삭제

```

### git branch

```bash
# 브랜치 삭제
git branch -d [브랜치명] # 로컬 브랜치 삭제
git branch -D [브랜치명] # 강제 삭제(머지여부 상관없이 삭제)
git push origin --delete [브랜치명] # 원격 브랜치 삭제

# 브랜치 전환
git checkout -t origin/[remote] # 원격브랜치를 가져와서 같은 이름으로 브랜치를 로컬에 생성 후 전환
git checkout -b [new_branch] origin/[remote] # 원격브랜치를 새로운 이름으로 생성 후 전환

```

### git fetch

```bash
git fetch # 현재 체크아웃된 리모트 정보를 업데이트
git fetch --prune[-p] # 현재 자신의 로컬에 있는 리모트 브랜치 정보를 최신으로 업데이트

```

### git log
```
git log # 깃 로그 확인
git log -p # 수정된 파일 목록 및 수정내용 전체 확인
git log --name-only # 수정된 파일 목록 확인
git show [commit id] # 특정 커밋 수정된 파일 목록 및 수정내용 확인
git show [commit id] --name-only # 특정 커밋 수정된 파일 목록 확인
git reflog # 깃 모든 커밋 로그 출력 (reset 과 상관없이 로컬에서 커밋한 모든 내역을 확인할 수 있다)

```

### git tags
```bash
git checkout tags/[tag-name] -b [local-branch-name] #특정 태그 버전 로컬 브랜치 생성 후 전환하기

```

### git config


### git cherry pick


#### 깃 초기 설정 : 디렉토리 등록 + 유저 등록(커밋할 때 필요한 정보)

- git init : 현재 디렉터리를 Git이 관리하는 working directory로 설정하고 그 안에. git을 만들어준다.
- git config user.name '이름' : 내가 사용할 이름 추가
- git config user.email '이메일' : 내가 사용할 이메일 추가
    
    - git config --global user.name '이름' : --global을 붙이면 Git 서버 전체의 설정 값을 설정한다.
    - git config (--global) --list : 현재 설정 내용을 확인할 수 있다.
    
- git remote add origin [깃허브 주소] : 리모트 리포지토리 연결(깃허브에 새로운 리포지토리를 만들면 예시 존재)
- git remote -v : 리모트 리포지토리 확인

#### git clone [깃허브 주소] : 깃허브 프로젝트를 그대로 복제할 때 사용

### 깃 작업하기

#### git add : 로컬 디렉토리에서 staging area로 파일을 올리는 명령어(커밋할 파일을 정하는 명령어)

- git add [파일 이름] : 수정 사항이 있는 특정 파일을 staging area에 올린다.
- git add [폴더 이름] : 수정 사항이 있는 특정 폴더를 staging area에 올린다.
- git add . : 수정 사항이 있는 모든 파일을 staging area에 올린다.

#### git reset : 해당하는 커밋으로 이동할 수 있는 명령어

- 최신 버전으로도, 과거 버전으로도 갈 수 있다.(git reflog를 통해 확인 가능)
- 최종 수정본을 과거 수정본으로 가지고 온 후 commit을 하면 reset과 최신 버전 사이의 commit history가 사라진다.
- 즉, 커밋되지 않은 변경사항을 버리거나 커밋 자체를 없앨 수 있다.
- git reset [옵션] [커밋 아이디] : 옵션에 따라 작업 영역이 달라진다. (working directory / staging area / repository)
    
    - [옵션] 
        
        - soft : repository만 변경됨(HEAD가 [커밋 아이디]를 가리킴
        - mixed(default값) : soft + staging area가 변경됨
        - hard : mixed + working directory가 변경됨(모두 바뀌기 때문에 조심히 사용해야 함)
        
    - [커밋 아이디] : 커밋 아이디는 전체를 작성할 필요 없이 보통은 앞자리 4개만 작성함
        
        - HEAD^ : HEAD^는 바로 이전 커밋이란 뜻으로 [커밋 아이디] 자리에 사용 가능함
        - HEAD~x : , x단계 전에 있던 커밋이라는 뜻
        
    
- git reset [파일명] : 해당 파일 staging 취소

#### git status : commit을 하기 전 staging area를 확인하는 명령어(문제 발생 시 현 상태 확인용으로 사용)

1. Changes to be committed : 커밋에 반영될 변경사항
2. Changes not staged for commit : 커밋에 반영되지 않는 변경사항

#### git push : 로컬 리포지토리 버전을 리모트 리포지토리에 올리는 명령어(push를 하기 전 pull을 해야 함)

- git push [옵션] [리모트명] [로컬명] : 현재 로컬에 있는 브랜치 내용을 [리모트]라는 리모트 리포지토리로 보내는 것
    
    - [옵션]
        
        - -u : --set -upstream이라는 옵션의 약자로 파일들을 tracking 하기 위해서 사용한다.
        - -f : 로컬 리포지토리의 내용으로 리모트 리포지토리의 내용을 덮어쓰는 명령어(개인 프로젝트용)
        
    - git push -u origin master로 로컬 리포지토리 내용을 처음으로 리모트 리포지토리에 올릴 때 사용
    - git push [리모트] [로컬]:[브랜치]: -u 옵션을 사용하지 않았을 때 대처 방법(가능하면 -u 사용)
    

#### git pull : 로컬 리포지토리를 리모트 리포지토리와 동일하게 만드는 명령어

1. git pull은 git fetch + git merge를 동시에 하는 명령어라고 생각하면 편하다.
2. git pull은 리모트 리포지토리의 브랜치를 검토할 필요 없이 바로 합칠 때 사용
3. git fetch는 리모트 리포지토리의 브랜치의 내용을 살펴본 후 merge 할 때 사용(git pull을 바로 하기 의심스러울 때)
4. git fetch를 한 후 git diff로 비교, 확인 작업을 진행한다.

#### git fetch : 로컬 리포지토리에서 현재 HEAD가 가리키는 브랜치의 upstream 브랜치로부터 최신 커밋들을 가져오는 명령어(리모트 브랜치만 가져오는 명령어)

#### git diff [A] [B] : A, B 간 비교

- git diff [커밋 A 아이디] [커밋 B 아이디] : 두 커밋 간 비교
- git diff [로컬] [리모트] : 브랜치 간 비교
- 빨간색 글자 : 이전 커밋의 모습 / 초록색 글자 : 이후 커밋의 모습 

#### git merge [병합할 브랜치명]: 현재 브랜치에 다른 브랜치를 가져오는 명령어

- git merge --abort : merge 하다가 conflict가 발생했을 때, merge 작업을 중단하고 이전 상태로 돌아가는 명령어

#### git rebase [브랜치명] : 커밋을 재배치한다. 즉, 베이스 커밋을 바꾸는 명령어

- git rebase --continue : Conflict 발생해서 제대로 진행되지 못한 리베이스 계속 진행을 지시하는 명령어

#### git merge vs git rebase

1. merge는 두 브랜치를 합쳤다는 정보를 커밋 히스토리에 남기기 위해
2. rebase는 커밋 히스토리를 깔끔하게 만들기 위해

#### git log : 커밋 히스토리를 출력하는 명령어

- [커밋 아이디] / 작성자 / 날짜 / 커밋 메시지 등의 정보를 알려준다.
- git log --pretty=oneline : --pretty 옵션을 사용하면 다양한 방식으로 출력 가능(1줄로 보여주는 명령어)
- git log --all --graph : 모든 브랜치의 커밋 히스토리를, 커밋 간의 관계가 잘 드러나도록 그래프 형식으로 출력
- git reflog : HEAD가 그동안 가리켜왔던 커밋 기록 출력

#### git commit : Git에서 핵심적인 개념, staging area의 현 상태를 하나의 버전으로 남기는 작업 혹은 결과

1. 커밋에 전달되는 정보 : 사용자 아이디, 날짜 + 시간, 커밋 메시지
2. 주의사항 : 커밋된 코드는 항상 정상적으로 실행되어야 한다. 언제든지 해당 시점으로 돌아갈 수 있기 때문이다.
3. Vi 에디터 사용 방식을 알면 편하다. / i는 입력 상태로 변경 / :wq는 저장
4. commit을 한다고 해도 staging area에는 변화가 없다.

- git commit : 커밋 메시지를 작성할 수 있는 창이 뜬다. 긴 커밋 메시지를 쉽게 남길 수 있다.
- git commit -m "[커밋 메시지]" : 원하는 메시지 남기기
- git commit --amend : 가장 최근의 커밋을 수정하는 명령어

#### git branch ( [옵션] ) ( [브랜치명] ) : branch 관련 명령어

- git branch : 모든 브랜치를 검색
- git branch [브랜치명] : 브랜치 생성
- git branch -d [브랜치명] : 해당 브랜치 삭제

#### git checkout ( [옵션] ) [브랜치명, 커밋 아이디, 파일명]

- git checkout [브랜치명] : 해당 브랜치로 이동
- git checkout -b [브랜치명] : 해당 브랜치를 생성 후 이동
- git checkout [커밋 아이디] : 해당 커밋으로 이동(특정 커밋에서 새로운 브랜치를 만들고 싶을 때 사용)
- git checkout [파일명] : working directory에서 수정한 내용 취소하기(복구 불가)

#### git blame [파일명] : 어떤 파일의 작성자와 작업 내용을 확인하는 명령어

#### git show [커밋 아이디] : [커밋 아이디]를 통해서 해당 커밋 정보를 확인하는 명령어

#### git revert : 특정 커밋에서 이루어진 작업을 되돌리는 커밋을 새로 생성하는 명령어

- git revert [커밋 아이디] : 해당 [커밋 아이디] 지점으로 되돌리기
- git revert [커밋 아이디1..커밋아이디2] : [커밋 아이디 1] 다음부터 [커밋 아이디 2] 지점까지 되돌리기

#### git stash : 임시 저장 명령어

1. 최근 커밋 이후로 working directory에서 작업한 모든 내용을 깃이 따로 보관한다.
2. 해당 working directory는 최근 커밋 상태로 돌아간다.
3. 잘못된 브랜치에서 작업했을 때 사용
4. 해당 작업이 끝나지 않았지만 다른 작업을 해야 하는 상황에 사용

- git stash list : stash 확인(1개도 없다면 아무것도 나오지 않음)
- git stash apply stash@{번호} : stash 적용하기
- git stash drop stash@{번호} : 해당 stash 삭제 
- git stash pop stash@{번호} : 해당 stash를 삭제한 후 적용하기(더 이상 사용하지 않겠다는 의미)

#### git cherry-pick [커밋 아이디] : 자신이 원하는 작업이 들어있는 커밋들만 가져와서 추가하는 명령어

#### git tag [태그명] [커밋 아이디] : 커밋들에 의미를 부여할 수 있는 명령어

- git tab -d [태그명] : 태그 삭제

#### git config alias.[별명] [명령어] : 길이가 긴 명령어를 원하는 이름으로 사용할 수 있게 해주는 명령어

출처: [https://sweets1327.tistory.com/31](https://sweets1327.tistory.com/31) [개발자의 공부 기록:티스토리]
