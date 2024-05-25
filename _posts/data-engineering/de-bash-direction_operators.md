---
title: "[Bash]Direction Operators"
date: 
tags:
  - [Bash]
categories:
  - [Data Engineering]
updated:
---


## Direction Operators

리눅스에서 데이터의 입출력방향을 다루는 연산자는 Direction Operators이다.

Direction Operators에는 `>`와 `>>`가 있다.

`>`와 `>>` 의 차이점은 Linux에서의 데이터의 출력방향이다.

`>` : 기존 파일을 덮어쓰거나 지정한 이름의 파일이 디렉토리에 없는 경우 파일을
생성한다 `>>` : 기존 파일에 추가하거나 지정한 이름의 파일이 디렉토리에 없는 경우
파일을 생성한다.

정리하면 다음과 같다.

- 파일을 수정하고 기존 데이터를 덮어쓰려면 `>` 사용.
- 파일에 무언가를 추가하려면 `>>` 연산자를 사용.

## 예제

1. `>` 연산자 사용


```bash

# a.txt 파일에 "Hello World"를 출력한다.

echo "Hello World" > a.txt

```

2. `>>` 연산자 사용

```bash

a.txt 파일에 "Goodbye World"를 추가한다.

echo "Goodbye World" >> a.txt

```

```bash
cat a.txt

Hello World
Goodbye World

```

## References

- [https://www.tutorialspoint.com/unix/unix-io-redirections.htm](https://www.tutorialspoint.com/unix/unix-io-redirections.htm)
