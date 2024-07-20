---
title: "[FastAPI]Pydantic  데이터 업데이트"
categories:
  - - backend
    - FastAPI
tags:
  - FastAPi
date: 
updated: 2024-07-20T21:10
description: pydantic 데이터모델링 개념
created: 2024-06-07T07:02
---

## Pydantic

pydantic은 FastApi에서 사용하는 데이터 모델링 라이브러리로 기본 python에서 제공하는 `dataclass`보다 데이터 검증 측면에서 나은 모습을  보인다.

1. Data Parsing : 데이터 타입 추론 및 형변환 
2. Data Validation: 데이터 유효성 검사

## Pydantic 데이터 모델 업데이트

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str = None

```
id 와 name 필드를 가지는 user를 생성한다

```python
user = User(id=1, name='Jack')
```
데이터를 직렬화 하여 출력하면 아래와 같이 나온다.

```python
import json

json.dumps(user.dict())
# Output: '{"id": 1, "name": "Jack", "email": null}'
```

user를 생성시 email field에 값을 넣지 않았기에 null이 출력된다.

```python
class User(BaseModel):
    id: int
    name: str
    email: str = None
    
    class Config:
        # use exclude_unset=True
        exclude_unset = True
        
json.dumps(user.dict())
# Output: '{"id": 1, "name": "John"}' 
# email field가 출력되지 않는다.

```
Config class에 `exclude_unset` 옵션을 추가해 정의되지 않은 옵션은 객체 생성시 필드 자체를 만들지 않게끔 할 수있다.

- pydantic model에서 `exclude_unset` 옵션을 통해 명시적으로 값을 지정하지 않은 필드를 객체 생성시 제외시킬 수 있다.
- `exclude_unset=True`는 기본적으로 partial update를 위해 사용.
- request에서 받은 요청 중 item의 초기값을 제외한 입력값만 추려서 dict를 구성해줌


## References

- https://fastapi.tiangolo.com/tutorial/body-updates/#__tabbed_1_2
