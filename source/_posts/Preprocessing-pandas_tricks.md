---
title: "[pandas]pandas 함수와 기초용법들"
date: 
updated:
categories: 
        - [Preprocessing]
tags:
  - [pandas]
---

## **pandas tricks**
> pandas관련 자주 사용할만한 코드 정리

### pandas version확인
```python
pd.__version__ # pandas version확인
```
```python
pd.show_versions() #의존성 패키지 확인
```

### DF 생성하기
> 여러 방법이 있지만 보통 dictionary를 사용한다.
```python
df = pd.DataFrame({'col one':[100, 200], 'col two':[300, 400]})
df
```
```python
# 난수생성을 통핸 DF생성
pd.DataFrame(np.random.rand(4, 8))
```

### 열이름 변경하기

```python
# dictionary 형태로 변경하기
df = df.rename({'col one' : 'col_one','col two': 'col_two'}, axis = 'columns' ) # 적용할 axis지정 rename

df.add_prefix('X_') #컬럼에 접두어 X 추가
df.add_suffix('_Y') #컬럼에 접미어 Y 추가
```
```python
# list를 매핑해 변경하기
df.columns = ['col_one', 'col_two']
```


### 행순서 뒤집기
```python
drinks.loc[::-1].head()
```

### reverse column order
```python


drinks.loc[:, ::-1].head() # [start:end:(step)]에 대한 이해 필요
# start, end가 비어있고 step이 -1이기에 순서가 역순으로 바뀜

```

### datatype 기준으로 컬럼 선택하기
```python
drinks.dtypes # 모든 열의 dtype 확인
```
```python
drinks.select_dtypes(include='number').head() # dtype이 numeric인 데이터 추출

drinks.select_dtypes(include=['number', 'object', 'category', 'datetime']).head()
```
### 문자열 numeric으로 변환하기
```python
df = pd.DataFrame({'col_one':['1.1', '2.2', '3.3'],
                   'col_two':['4.4', '5.5', '6.6'],
                   'col_three':['7.7', '8.8', '-']})
df

# astype()을 활용한 변환
df.astype({'col_one':'float', 'col_two':'float'}).dtypes

# to_numeric을 활용한 변환
pd.to_numeric(df.col_three, errors='coerce')

# df 전체에 적용(numeric 변환 후 fillna)
df = df.apply(pd.to_numeric, errors='coerce').fillna(0)

# , 이 포함된 숫자형태의 문자열의 경우 replace사용
def toInt(string):
    string = int(string.replace(',',''))
    returen string

```
### DF 사이즈 줄이기

```python
# 메모리 사용정도 확인
drinks.info(memory_usage='deep')

# 컬럼지정을 활용한 데이터 줄이기
dtypes = {'continent':'category'}
smaller_drinks = pd.read_csv('http://bit.ly/drinksbycountry', usecols=cols, dtype=dtypes)
smaller_drinks.info(memory_usage='deep')
```
### Build a DataFrame from mulfiple files (row-wise)
```python
from glob import glob

# 정규식,와일드카드 관련문서 참고
# stocks로 시작하는 data폴더 내 모든 csv 파일 
stock_files = sorted(glob('data/stocks*.csv'))
stock_files

['data/stocks1.csv', 'data/stocks2.csv', 'data/stocks3.csv'] # 리스트 형태로 반환


```

```python
# 파일합치기
pd.concat((pd.read_csv(file) for file in stock_files), ignore_index=True) # ignore index는 각 파일의 index를 무시하고 초기화하는 옵션이다.


```
### Build a DataFrame from mulfiple files (column-wise)
```python

# 축옵션만 넣어주면 된다
pd.concat((pd.read_csv(file) for file in drink_files), axis='columns').head()


```

### 클립보드에서 df불러오기
```python
df = pd.read_clipboard()
df
```

### DF subsetting 하기
```python

# frac으로 원db의 75% 할당
movies_1 = movies.sample(frac=0.75, random_state=1234)

# 나머지
movies_2 = movies.drop(movies_1.index)


```

### isin을 활용한 DF필터링
```python
# inin을 사용해 특정열에 대해 값에 대한조건을 넣어줄 수 있다.

# 포함하고 뽑기
movies[movies.genre.isin(['Action','Drama','Western'])].head()

# 제외하고 뽑기
movies[~movies.genre.isin(['Action', 'Drama', 'Western'])].head()
```

### value_counts()를 관측값 구하기
```python
# 우선 카테고리(장르)별 관측값를 구한다
counts = movies.genre.value_counts()
counts

```
```python
# count에서 상위3개를 구한다.
counts.nlargest(3)

```
### 결측값 처리하기
```python

# 결측값 조건걸기
ufo = dropna(thresh = len(ufo)*0.9, axis = 'columns') # 90% 이상 값이 있는 컬럼만 유지

```
```python
# 열별로 결측값의 수 세기
ufo.isna().sum()
```
```python
# NA가 하나라도 있는 열 삭제
ufo.dropna(axis='columns').head()
```
### .split를 활용한 문자열 나누기
```python
df = pd.DataFrame({'name':['John Arthur Doe', 'Jane Ann Smith'],
                   'location':['Los Angeles, CA', 'Washington, DC']})
df
```
```python
df[['first', 'middle', 'last']] = df.name.str.split(' ', expand=True)
df
```
![](/image/output.png)
### 리스트를 DF로 변환하기
```python
df = pd.DataFrame({'col_one':['a', 'b', 'c'], 'col_two':[[10, 40], [20, 50], [30, 60]]})
df
```
![](/image/output2.png)
```python
df_new = df.col_two.apply(pd.Series) # apply를 활용한 df 생성
df_new
```
### Aggregate by multiple funtions
```python
# aggregate를 활용한 요약통계량 산출하기
orders.groupby('order_id').item_price.agg(['sum', 'count']).head()
```

### Combine the output of an aggregation by multiple funtions

```python
# transform()은 입력된 개체와 동일하게 인덱스된 객체를 반환하며 다중연산에 쓰인다.
total_price = orders.groupby('order_id').item_price.transform('sum')

# transform() 관련레퍼런스
# https://kongdols-room.tistory.com/169 
```
### .loc를 활용한 행열 슬라이싱
```python

titanic.describe().loc['min':'max']

titanic.describe().loc['min':'max', 'Pclass':'Parch']

```
### 계층적 index를 가지는 Series DF로 변환하기
- 부모자식 노드처럼 계층이 있는 인덱스를 가지는 DF를 만들 수있다
- 잘 쓰진 않는 것 같다
```python
# 계층적
# https://nittaku.tistory.com/122

titanic.groupby(['Sex', 'Pclass']).Survived.mean()

# changing multiple Series into a DF
titanic.groupby(['Sex', 'Pclass']).Survived.mean().unstack()

```
### 피벗테이블 만들기
```python

titanic.pivot_table(index='Sex', columns='Pclass', values='Survived', aggfunc='mean')
# pivot_table에서 aggfunc 파라미터를 'count' 으로 바꿀 경우 단순 crosstable을 반환한다

# margins = True option으로 행열합을 DF에 추가한다
titanic.pivot_table(index='Sex', columns='Pclass', values='Survived', aggfunc='mean',
                    margins=True)
```
### bin과 labels를 활용해 수치형 변수 범주형 변수로 바꾸기

```python
# use bin with the labels
pd.cut(titanic.Age, bins=[0, 18, 25, 99], labels=['child', 'young adult', 'adult']).head(10)
```
### DF 표시형식 바꾸기
```python
# set_option을 통해 표시형식 바꾸기
pd.set_option('display.float_format', '{:.2f}'.format)
```
### DF 꾸미기 (Style a DataFrame)
```python
format_dict = {'Date':'{:%m/%d/%y}', 'Close':'${:.2f}', 'Volume':'{:,}'}

df.style.format(format_dict) # 스타일 바꾸기

```
### ProfileReport를 통해 DF 구조, 통계량 한번에 확인하기

```python
i
mport pandas_profiling
pandas_profiliing.PrifileReport(titanic)

```

### glob을 사용해 여러 csv파일을 하나의 df로 합치기
-
```python

import pandas as pd
import glob

path = r'C:\DRO\DCL_rawdata_files' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

```
### DF에 컬럼 추가하기
```python

dic = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}
  
# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
  
# Declare a list that is to be converted into a column
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
  
# Using 'Address' as the column name
# and equating it to the list
df['Address'] = address

```
### apply 등을 활용한 파생변수 생성하기
-DF전체에 적용하거나 DF일부에 적용할 수 있다.
```python


```
### lambda를 활용한 함수 적용


### 


###
http://www.leejungmin.org/post/2018/04/21/pandas_apply_and_map/


https://wikidocs.net/46758

https://data-make.tistory.com/123

## 3. References
- https://www.geeksforgeeks.org/adding-new-column-to-existing-dataframe-in-pandas/
- https://www.youtube.com/watch?v=RlIiVeig3hc
- https://kongdols-room.tistory.com/169 
- https://www.delftstack.com/ko/howto/python-pandas/how-to-create-dataframe-column-based-on-given-condition-in-pandas/