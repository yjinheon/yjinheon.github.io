---
title: '[R]make: gfortran: No such file or directory 해결하기'
categories:
   - Troubleshooting
date:
updated:

tags:
- R
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

시계열 분석을 할 일이 있어서 Rstudio server에다가 `forecast` package를 설치하려 하는데 dependancy package를 설치하는 도중

아래와 같은 오류가 떴다.

`make: gfortran: No such file or directory`

그리고 라이브러리 설치가 안된다..

찾아보니까 package가 소스 형태라 컴파일러가 필요한데 그 중 포트란 컴파일러가 서버에 설치되지 않아서 생긴 문제였다.

터미널에다 아래 명령어를 쳐서 해결하였다.

```bash
sudo pacman -S gcc-fortran
```


우분투 사용자의 경우 아래와 같이 컴파일러를 설치해주면 된다.

```bash
sudo apt-get install gfortran
```

윈도우 사용자의 경우 [링크](https://fortran-lang.org/learn/os_setup/install_gfortran) 에서 설치법을 확인할 수 있다.

**References & annotation**
---
- https://www.r-bloggers.com/2021/03/gfortran-support-for-r-on-macos-2/
- https://fortran-lang.org/learn/os_setup/install_gfortran