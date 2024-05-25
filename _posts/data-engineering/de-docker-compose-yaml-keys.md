---
title: "[Docker]YAML 파일 작성시 key의 의미"
date: 
tags: 
categories:
  - - Data Engineering
updated:
---

## YAML 파일 작성시 key의 의미

docker-compose.yml 파일을 작성하다 보면 가끔 특수한 key들을 볼 수 있다.
이들을 yaml 파일에서 사용되는 일종의 Operator이며 의미를 알고 있으면 yaml 파일을 해석하거나 docker-compose 파일 작성시 유용하게 활용할 수 있다. 

### `&` 와 `*`

- `&` : `&`는 anchor를 설정해주는 기호이다.
- `*` : `*`는 anchor를 참조하는 기호이다.

- 아래 예제에서 foo는 anchor이고 bar는 anchor를 참조하는 것이다.
- bar 가 foo를 참조하기 때문에 bar의 key1, key2는 foo의 key1, key2와 같은 값을 가지게 된다.

```yaml
foo: &myanchor
  key1: "val1"
  key2: "val2"

bar: *myanchor
```


### `<< `

- `<<`는 merge를 의미한다
- `<<` Operator를 사용해서 anchor로 정의 한 변수를 merge 할 수 있다.
- anchor에서 쓰던 키에 새로운 값을 넣어서 변수를 오버라이딩할 수 있다.
- 아래 예제에서는 bar의 key2를 foo의 key2로 오버라이딩한다.

```yaml
foo: &myanchor
  key1: "val1"
  key2: "val2"

bar:
  << : *myanchor
  key2: "val2-new"
  key3: "val3"

```

## References

- [https://docs.docker.com/compose/compose-file/](https://docs.docker.com/compose/compose-file/)
- https://stackoverflow.com/questions/50072810/whats-the-double-arrow-django-mean-in-a-docker-compose-file
