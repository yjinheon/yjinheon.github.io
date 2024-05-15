---
created: 2024-01-14T09:24
updated: 2024-02-04T17:02
---
## docker 명령어 정리


- docker 명령어를 정리합니다.
- docker 관련해서 자주 쓰거나 공유가 필요하다 싶은 내용이 있으면 이 문서에 업데이트 부탁드립니다.
- docker 개념은 아래 링크 참고 바랍니다.


*레퍼런스*

- https://cultivo-hy.github.io/docker/image/usage/2019/03/14/Docker%EC%A0%95%EB%A6%AC/
- https://www.44bits.io/ko/post/easy-deploy-with-docker#%EB%8F%84%EC%BB%A4docker-%EC%84%A4%EC%B9%98%ED%95%98%EA%B3%A0-%EA%B8%B0%EB%B3%B8%EC%A0%81%EC%9D%B8-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0


### docker run - 네트워크 연결

```bash
docker run -d -p 8080:8080 --network <네트워크명> --name <컨테이너명> 
```

- **-d** : 백그라운드에서 컨테이너가 실행옵션
- **-p 8080:8080** : 호스트와 컨테이너 포트 연결 <호스트:컨테이너>
- **--network** : container 이름 지정
- **--name** : 컨테이너의 이름을 지정

### docker network- 네트워크 확인

```bash
docker network ls
```

### docker stats

docker container의 자원사용량을 모니터링하기 위한 명령어

```bash
docker stats
```

### docker inspect

```bash

# check swap memory allocation

docker inspect [container-name] | grep MemorySwap

# confirm soft memory limit

docker inspect [container-name] | grep MemoryReservation01
```

### docker compose

- 실행 : docker-compose build && docker-compose up -d
- 이미지까지 삭제 후 down : docker-compose down –rmi all
- 실행 후 로그 확인 : docker-compose logs -f

### docker rm

컨테이너 삭제를 위해 rm 명령어 사용

#### 로컬 시스템의 모든 컨테이너 삭제

```bash

docker rm -f $(docker ps -aq)

```

#### 로컬시스템의 모든 도커 이미지 삭제

- 위험함

```bash
docker rmi $(docker images -q)
```

#### 사용하지 않는 이미지 삭제

```bash
docker image prune
```

```bash
docker system prune
systemctl restart docker service
```
