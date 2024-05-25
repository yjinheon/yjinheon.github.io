---
title: "[pandas]Pandas Groupby용법 간단히 정리"
date: 
updated:
categories: 
      - Preprocessing
tags:
  - [pandas]
---

## Intro
pandas에서 제공하는 groupby는 기본적으로 데이터 범주별 요약통계량을 계산하는 일을 한다. sql의 groupby나 R dplyr의 groupby와 유사하다고 생각하면 된다.  
여기서는 전처리과정에서 자주쓰게 되는 groupby 용법을 살펴본다.

---

## 기본적인 용법들


```python
# 데이터 불러오기
import pandas as pd
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
```


```python
drinks.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>beer_servings</th>
      <th>spirit_servings</th>
      <th>wine_servings</th>
      <th>total_litres_of_pure_alcohol</th>
      <th>continent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>Asia</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Albania</td>
      <td>89</td>
      <td>132</td>
      <td>54</td>
      <td>4.9</td>
      <td>Europe</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Algeria</td>
      <td>25</td>
      <td>0</td>
      <td>14</td>
      <td>0.7</td>
      <td>Africa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Andorra</td>
      <td>245</td>
      <td>138</td>
      <td>312</td>
      <td>12.4</td>
      <td>Europe</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Angola</td>
      <td>217</td>
      <td>57</td>
      <td>45</td>
      <td>5.9</td>
      <td>Africa</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 기초적인 용법 : 대륙별 beer_servings 평균
drinks.groupby('continent').beer_servings.mean()
```




    continent
    Africa            61.471698
    Asia              37.045455
    Europe           193.777778
    North America    145.434783
    Oceania           89.687500
    South America    175.083333
    Name: beer_servings, dtype: float64



.agg()와 같은 집계함수를 사용해 한 변수의 여러 요약통계량을 구하는 것이 가능하다.


```python
drinks[drinks.continent=='Asia'].beer_servings.agg(['count','mean','max','min'])
```




    count     44.000000
    mean      37.045455
    max      247.000000
    min        0.000000
    Name: beer_servings, dtype: float64




```python
drinks.groupby('continent').beer_servings.agg(['count','mean','max','min'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>max</th>
      <th>min</th>
    </tr>
    <tr>
      <th>continent</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Africa</th>
      <td>53</td>
      <td>61.471698</td>
      <td>376</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Asia</th>
      <td>44</td>
      <td>37.045455</td>
      <td>247</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Europe</th>
      <td>45</td>
      <td>193.777778</td>
      <td>361</td>
      <td>0</td>
    </tr>
    <tr>
      <th>North America</th>
      <td>23</td>
      <td>145.434783</td>
      <td>285</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Oceania</th>
      <td>16</td>
      <td>89.687500</td>
      <td>306</td>
      <td>0</td>
    </tr>
    <tr>
      <th>South America</th>
      <td>12</td>
      <td>175.083333</td>
      <td>333</td>
      <td>93</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 분석할 칼럼을 지정해주지 않으면 모든 numeric의 평균을 그룹별로 반환한다.
drinks.groupby('continent').mean()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>beer_servings</th>
      <th>spirit_servings</th>
      <th>wine_servings</th>
      <th>total_litres_of_pure_alcohol</th>
    </tr>
    <tr>
      <th>continent</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Africa</th>
      <td>61.471698</td>
      <td>16.339623</td>
      <td>16.264151</td>
      <td>3.007547</td>
    </tr>
    <tr>
      <th>Asia</th>
      <td>37.045455</td>
      <td>60.840909</td>
      <td>9.068182</td>
      <td>2.170455</td>
    </tr>
    <tr>
      <th>Europe</th>
      <td>193.777778</td>
      <td>132.555556</td>
      <td>142.222222</td>
      <td>8.617778</td>
    </tr>
    <tr>
      <th>North America</th>
      <td>145.434783</td>
      <td>165.739130</td>
      <td>24.521739</td>
      <td>5.995652</td>
    </tr>
    <tr>
      <th>Oceania</th>
      <td>89.687500</td>
      <td>58.437500</td>
      <td>35.625000</td>
      <td>3.381250</td>
    </tr>
    <tr>
      <th>South America</th>
      <td>175.083333</td>
      <td>114.750000</td>
      <td>62.416667</td>
      <td>6.308333</td>
    </tr>
  </tbody>
</table>
</div>




```python
# m
%matplotlib inline
drinks.groupby('continent').mean().plot(kind='bar')
```


![](https://i.imgur.com/KvoD6CS.png)    


## 응용하기
- Groupby에서 특정 그룹에 접근하기
- Groupby에서 특정 그룹에 접근 후 필터링 하기 (filter 사용)
- pd.cut 을 사용한 파생변수 만들기


```python
# 아시아 그룹만 
drinks.groupby('continent').get_group('Asia').head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>beer_servings</th>
      <th>spirit_servings</th>
      <th>wine_servings</th>
      <th>total_litres_of_pure_alcohol</th>
      <th>continent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>Asia</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Bahrain</td>
      <td>42</td>
      <td>63</td>
      <td>7</td>
      <td>2.0</td>
      <td>Asia</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Bangladesh</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>Asia</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Bhutan</td>
      <td>23</td>
      <td>0</td>
      <td>0</td>
      <td>0.4</td>
      <td>Asia</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Brunei</td>
      <td>31</td>
      <td>2</td>
      <td>1</td>
      <td>0.6</td>
      <td>Asia</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 여러 그룹의 통계량을 조건걸어서 구할 경우
drinks.groupby(['wine_servings', 'continent']).get_group((0, 'Asia')).total_litres_of_pure_alcohol.sum()
```




    6.2




```python
# pd.cut을 활용한 연속형 변수의 구간화 변수생성
drinks['Range'] = drinks.groupby('country').beer_servings.apply(pd.cut, bins=2)
```


```python
drinks.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>beer_servings</th>
      <th>spirit_servings</th>
      <th>wine_servings</th>
      <th>total_litres_of_pure_alcohol</th>
      <th>continent</th>
      <th>Range</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>Asia</td>
      <td>(-0.001, 0.0]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Albania</td>
      <td>89</td>
      <td>132</td>
      <td>54</td>
      <td>4.9</td>
      <td>Europe</td>
      <td>(88.911, 89.0]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Algeria</td>
      <td>25</td>
      <td>0</td>
      <td>14</td>
      <td>0.7</td>
      <td>Africa</td>
      <td>(24.975, 25.0]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Andorra</td>
      <td>245</td>
      <td>138</td>
      <td>312</td>
      <td>12.4</td>
      <td>Europe</td>
      <td>(244.755, 245.0]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Angola</td>
      <td>217</td>
      <td>57</td>
      <td>45</td>
      <td>5.9</td>
      <td>Africa</td>
      <td>(216.783, 217.0]</td>
    </tr>
  </tbody>
</table>
</div>



TF를 반환하는 lamba 함수를 작성할 경우 any()나 all()을 써서 값을 반환해줄 필요가 있다.

```python
## filter를 사용한 조건식. 위의 결과와 같은 값을 리턴한다.
drinks.groupby(['wine_servings','continent']).filter(lambda x : ((x.wine_servings == 0) & (x.continent=='Asia') ).any()).total_litres_of_pure_alcohol.sum()

```




    6.2


## References
* https://www.youtube.com/watch?v=qy0fDqoMJx8
* https://pandas.pydata.org/docs/reference/groupby.html


## 다음에 정리할 것
* any()와 all() 관련 함수
* filter
* assign
* pd.cut과 np.digitize를 활용한 연속형 변수의 구간화
* pandas query as dplyr filter
