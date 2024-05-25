---
title: "Anaconda 시작시 기본설정"
date: 2021-07-08 17:09:02
tags:
categories:
  - [Infra,Config]
updated:
---

## Intro

Anaconda를 자주 설치하고 지우기 때문에 Anaconda를 설치하면 하는 루틴들을 정리해두려고 합니다.

## 주피터 시작경로 설정

1. powershell에서 해당 명령어 실행
   
   ```powershell
   jupyter notebook --generate-config
   ```

2. 'C:\Users\유저명\.jupyter\jupyter_notebook_config.py' 경로로 이동

3. #c.NotebookApp.notebook_dir= ''  를 주석처리하고 원하는 경로 입력 

4. 시작메뉴 주피터 속성 에서  **%USERPROFILE%/** 과 **%HOMEPATH%** 삭제

## Jupyterlab 바로가기 설청

1. conda 설치경로\Script에 들어가서 activate.bat 파일을 연다.
2. activate.bat 파일을 다른 이름으로 저장한다(activate_jupyter).
3. 다른이름으로 저장한 파일의 맨 아래에 다음 두 줄을 추가한다.
   
   ```bat
    cd <작업경로>
    jupyter lab
   ```
4. 새로만든 파일의 바로가기를 만든다.
5. 바로가기 아이콘을 jupyter lab 아이콘으로 변경한다.
6. 시작메뉴에 바로가기를 추가한다.

## Jupyterlab theme 설치

## 가상환경 생성 및 Jupyter 등록

가상환경 자체는 단순히 자신이 필요한 python환경을 구축하기 위해 폴더 안에 필요한 패키지만을 모아 놓은 것이다. 보통 프로젝트 단위로 작업을 할때 패키지 의존성(dependancy)으로 인한 오류들을 줄이기 위해 사용한다. `vertualenv`로도 가상환경을 설치할 수 있지만 `conda`를 사용한다면 conda명령어를 통해 쉽게 가상환경을 설치하고 삭제할 수 있다.
![png](conda_venv.png)

### conda 가상환경 명령어

1. 가상환경 만들기 
   
   ```bash
   conda create –n 가상환경이름 python=버전 
   ```
2. 가상환경 활성화  
   
   ```bash
   conda activate 가상환경이름
   ```
3. 가상환경 비활성화  
   
   ```bash
   conda activate 가상환경이름
   ```
4. 가상환경에 패키지 설치 
   
   ```bash
   conda install 패키지이름 
   ```
5. 가상환경 정보 확인 
   
   ```bash
   conda info --enves 
   ```
6. 가상환경 복사
   
   ```bash
   conda create –n 복사된 가상환경 --clone 복사될 가상환경 
   ```
7. 가상환경 설치패키지 확인
   
   ```bash
   # 가상환경 활성화 시킨 후 시행
   conda list
   ```
8. 가상환경 삭제
   
   ```bash
   conda env remove -n 가상환경이름 
   ```

### 주피터 커널 등록

1. ipykernel 설치
   
   ```bash
   pip install ipykernel
   ```
2. 가상환경 주피터 등록
   
   ```bash
   python -m ipykernel install --user --name 가상환경 이름 --display-name 커널 이름
   ```
3. 가상환경 주피터 커널 삭제
   
   ```bash
   jupyter kernelspec uninstall 가상환경이름
   ```

## References

- https://ooyoung.tistory.com/7
- https://django-easy-tutorial.blogspot.com/2015/08/python-virtual-environment-setup-in-ubuntu.html
