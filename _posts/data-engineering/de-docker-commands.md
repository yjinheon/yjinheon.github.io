---
title: "[Docker]Docker 자주쓰는 명령어"
date:
updated:
tags:
  - [Docker]
categories:
  - [Data Engineering]
---

## 도커 이미지

### docker images

```bash
docker images
```

## 도커 컨테이너

### docker run

: 도커 이미지 실행

```bash
docker run -v [로컬경로]:/[컨테이너경로] -d -p 8080:8080 yjinheon/test:latest
```

### docker ps

```bash
docker ps

# 모든 컨테이너를 보여준다
docker ps -a
```

```bash
# 실행중인 docker containner id 전부 가져오기
docker ps | awk 'NR > 1 {print $1}'

# 맨위의 docker container 하나만 가져오기
docker ps | awk 'NR > 1 {print $1; exit}'
```

### docker rm

```bash
# 컨테이너 ID로 삭제
docker rm [컨테이너 ID]

# 컨테이너 명으로 삭제
docker rm [컨네이너 명]

# 실행중인 컨테이너 강제삭제

docker rm -f [컨테이너명]
```

- id가 none인 도커 이미지 전부 삭제

```bash
docker rmi $(docker images -a|grep "<none>"|awk '$1=="<none>" {print $3}')
```

## 도커 볼륨

### docker volume

```bash
docker create volume [볼륨명]
```

## References

- <https://docs.docker.com/engine/reference/commandline/>
