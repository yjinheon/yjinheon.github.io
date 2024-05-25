---
title: '[Git]Private repository import 하기'
categories:
  - [Infra,git]
tags:
  - Git
date:
updated:
---

<!--

<center>Kaggle Customer Score Dataset</center>

- Machine Learning
- Statistics , Math
- Data Engineering
- Programmingdf
- EDA & Visualization
- Data Extraction & Wrangling

#신경망이란 무엇인가?

https://www.youtube.com/watch?v=aircAruvnKk


#참고

https://cinema4dr12.tistory.com/1016?category=515283

https://www.kdnuggets.com/2021/07/top-python-data-science-interview-questions.html
-->

**보안이나 기타 이유로 private repository에서 관리하는 패키지를 써야할 경우가 있다.**

**나중에도 자주 쓸거 같으니까 개인용 패키지를 pandas나 sklearn처럼 설치하고 사용하는 법을 정리해두자.**

---

## 작업용 repository 만들기

적당한 이름의 private repository를 만들고 패키지를 넣을 디렉터리를 만들어준다. 

```bash
mkdir some_package
```

## `__init__.py` 만들기

`__init__.py` 파일을 디렉터리에 넣으면 pip에서 해당 디렉토리를 패키지로 인식한다.

```python
# example 패키지(디렉토리)의 broadcast 파일에서  전부 가져오기

from example.broadcast import *
```

## 패키지에 함수 넣기

패키지 디렉토리에 포함될 함수를 넣어준다.

여기서는 numpy의 broadcast를 구현하는 함수를 넣어주었다.

```python
# broadcast.py
import numpy as np
m1 = np.array([[1,2],[3,4]])
m2 = np.array([10,20])

print(m1 * m2)

```

## `setup.py` 만들기

setup.py에는 패키지의 메타데이터를 넣어준다.

```python

"""
Python package setup info
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='레포이름',
    version='0.0.1',
    author='jinheonyoon',
    author_email='yjinheon@gmail.com',
    description='Package 설치 확인',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/yjinheon/레포이름.git',
    project_urls = {
        "Bug Tracker": "https://github.com/yjinheon/레포이름/issues"
    },
    license='jinheonyoon',
    zip_safe = False,
    packages = ['설치한 패키지 명'],
    install_requires = [
        'numpy==1.20.1',
        'pandas==1.3'
        ]
)


```


## token 생성하기

Github 계정의 `Setting`의 `developer settings`에서 token을 생성할 수 있다.
 
[여기](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) 참조



## 설치하기

생성한 토큰을 로컬에 변수로 넣어준다.

```
export token=생성한 토큰
```

$token으로 토큰을 불러와서 일반 package처럼 private repository의 package를 설치할 수 있다.

설치할 때는 `powershell`이나 `git`을 관리자 모드로 열어야한다.

```bash
pip install git+https://{$token}@github.com/yjinheon/toolbox
```


## 사용하기 & 결론

repository로 설치를 하고 불러올 때는 package명으로 불러와줘야 한다.

```python
import seaborn as sns
from eda import glimpse # 최근에 넣어둔 eda용 헬퍼함수

df = sns.load_dataset('penguins')


glimpse(df)
Shape:  (344, 7)
species           object   0 (0%) NAs : Adelie, Adelie, Adelie, Adelie, Adelie, Adelie, Adelie, Adelie, Adelie
island            object   0 (0%) NAs : Torgersen, Torgersen, Torgersen, Torgersen, Torgersen, Torgersen, Torg
bill_length_mm    float64  2 (1%) NAs : 39.1, 39.5, 40.3, nan, 36.7, 39.3, 38.9, 39.2, 34.1, 42.0
bill_depth_mm     float64  2 (1%) NAs : 18.7, 17.4, 18.0, nan, 19.3, 20.6, 17.8, 19.6, 18.1, 20.2
flipper_length_mm float64  2 (1%) NAs : 181.0, 186.0, 195.0, nan, 193.0, 190.0, 181.0, 195.0, 193.0, 190.0
body_mass_g       float64  2 (1%) NAs : 3750.0, 3800.0, 3250.0, nan, 3450.0, 3650.0, 3625.0, 4675.0, 3475.0, 4
sex               object  11 (3%) NAs : Male, Female, Female, nan, Female, Male, Female, Male, nan, nan

```

아직 패키지만 만든 상태라서 편한지 어떤지는 모르겠다. 몇주 써보고 좀 익숙해져야 할 것 같다.


## References

- [Personal access token 만들기](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [private-python-package](https://docs.readthedocs.io/en/stable/guides/private-python-packages.html)
- [custom-package](https://towardsdatascience.com/create-your-custom-python-package-that-you-can-pip-install-from-your-git-repository-f90465867893)