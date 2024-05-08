---
title: "[Docker]Docker 기본개념"
date: 2021-07-07
tags:
  - [Docker]
categories:
  - [Data Engineering]
updated:
---

## Docker개념

- 도커 이미지는 다른 이미지 위에 쌓는게 가능하다.
- VM은 독립적으로 운영되고 독립적인 자원을 사용하기 때문에 그 경우에 효율적일 수 있다.
- 도커의 Layer는 설계도이다.
- 이미지는 기본적으로 아직 실행되지 않은 컨테이너이다.

Docker Container는 가상환경과 다르다.

가상환경은 python version만 폴더안에 있는걸 쓰는 것이고 Docker Container는 아예 독립된 환경이다.

## Doker 명령어들

도커 빌드하기

```bash
$ cd /path/to/Dockerfile
$ sudo docker build .
```

현재 실행되고 있는 도커 프로세스 확인

```
$ sudo docker ps
```

전체 도커 프로세스 확인

```
$ sudo docker ps -a
```

도커 이미지 확인

```
$ sudo docker run -d <image_name>
```

Run an image in interactive mode with the command `/bin/bash`

```
$ sudo docker run -i -t <image_name> /bin/bash
```

Run an image in interactive mode with the command `/bin/bash` and link the ports.

```
$ sudo docker run -i -t --link <docker_container_name>:<docker_container_alias> <image_name> /bin/bash
```

Run an image with an ENTRYPOINT command in interactive mode with the command `/bin/bash`

```
$ sudo docker run --entrypoint /bin/bash -i -t <image_name>
```

Run an image in interactive mode with the command `/bin/bash` mounting the host director `/var/app/current` to the container directory `/usr/src/app`

```
$ sudo docker run -i -t -v /var/app/current:/usr/src/app/ <image_name> /bin/bash
```

Run an image in interactive mode with the command `/bin/bash` setting the environments variables `FOO` and `BAR`

```
$ sudo docker run -i -t -e FOO=foo -e BAR=bar <image_name> /bin/bash
```

## References

- https://gist.github.com/dwilkie/f8d6526edc5f1a8aca385df5113567e4
