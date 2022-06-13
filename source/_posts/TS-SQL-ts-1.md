---
title: '[SQL]ERROR 3948 (42000): Loading local data is disabled; this must be enabled on both the client and server sides 해결하기'
categories:
  - Troubleshooting
date:
updated:
tags:
	- SQL
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


안쓰던 노트북을 서버로 만들어서 작업중 다음 에러가 발생했다.

ERROR 3948 (42000): Loading local data is disabled; this must be enabled on both the client and server sides  

찾아보니 SQL 서버의 변수값을 변경해 해결할 수 있었다.

아래 명령을 통해 local_infile 상태가 ON 인지 OFF인지 확인 한다.

```SQL
show global variables like 'local_infile';
```

값이 OFF일 경우 아래 명령 실행

```SQL
set global local_infile = true;
```

## References

- https://stackoverflow.com/questions/59993844/error-loading-local-data-is-disabled-this-must-be-enabled-on-both-the-client
