---
title: '[Algorithm]Hash Table과 Hash에 대한 이해'
categories:
  - Programming
tags:
  - Python
  - Algorithm
  - Data Structure
date:
updated:
---

<!--

<center>Kaggle Customer Score Dataset</center>

- Machine Learning
- Statistics , Math
- Data Engineering
- Programming
- EDA & Visualization
- Data Extraction & Wrangling


#신경망이란 무엇인가?

https://www.youtube.com/watch?v=aircAruvnKk


#참고

https://cinema4dr12.tistory.com/1016?category=515283

https://www.kdnuggets.com/2021/07/top-python-data-science-interview-questions.html
-->


### Hash table


---
**_Concept_**

- hash function : 데이터의 효율적 관리를 목적으로 임의의 길의의 데이터를 고정된 길이의 데이터로 매핑하는 함수.
  - key : 매핑 전 원래 데이터의 값
  - hashing value : 매핑 후 데이터의 값 
- hash table : 해시함수를 이용해 키를 해시값으로 매핑하고 이 해시값을 index로 해서 데이터의 값을 키와 함께 빠르게 저장 및 검색할 수 있는 **테이블 형태의 자료구조**
- hashing : 매핑하는 과정 자체를 뜻한다.해싱은 기본적으로 다 흩뜨려놓고, 키와 매칭되는 값을 검색하는 과정이다.
- hash collision(해시충돌) : 서로 다른 두개의 키에 대해 동일한 해시값을 내는 것
- Load Factor : 해시테이블에 저장된 항목 수(테이블에 입력된 키 갯수)를 슬롯 수 (해시테이블 전체 인덱스 갯수)로 나눈 값

---

:hash table은 기본적으로 **키를 활용하여 값에 직접 접근이 가능한 구조** 이다.

- key : value system을 활용해 자료를 정리함
  - -> 데이터 양에 영향을 덜 받으며 성능이 빠르다.
- 해싱의 목적은 기본적으로 **검색**이다. -> 해시 테이블은 검색알고리즘의 역할도 한다.
- Python Dictionary는 내부적으로 해시테이블 구조로 구현되어 있다.
  - hash table은 검색을 위한 역할도 하고 딕셔너리를 위한 자료구조의 역할도 한다.

- **hash table 사용이유**
  - 기본적으로 적은 리소르로 많은 데이터를 효율적으로 관리할 수 있다
    - 하드디스크나 클라우드에 존재하는 데이터(키) 들을 유한한 개수의 해시값으로 매핑함으로써 작은 크기의 캐쉬메모리로도 프로세스를 관리할 수 있게 된다.
    - **index에 해시값을 사용함으로서 모든 데이터를 살피지 않아도 검색과 삽입/삭제를 빠르게 수행할 수 있습니다.**
    - 해시함수는 언제나 동일한 해시값을 리턴하고 해당 index만 알면 해시테이블 크기에 상관 없이 데이터에 빠르게 접근할 수 있다.
      - index는 계산이 간단한 함수로 작동하기 때무에 매우 효율적이다.

- hash table in python

```python

# case 1 - 딕셔너리로 활용되는 hash table

test_code = {2.5: 'A' ,'2.0': 'B', '1.0': 'C'}
print(test_code[2.5]) 
print(test_code['1.0'])
print(test_code['2.0'])

```

```python

# case 2 - 리스트와 튜플을 활욯한 hash table
# 데이터는 튜플로 저장

test_code = [(2.5, 'A'), ('2.0', 'B'), ('1.0', 'C')]
 
def insert(item_list, key, value):
    item_list.append((key, value))


def search(item_list, key):
    for item in item_list:    
        if item[0] == key:
            return item[1]      
    print('not matching')       
    
print(search(test_code, '2.0'))
print(search(test_code, 2.5))
search(test_code, 2.5)    

```

- 딕셔너리를 활용한  hash table의 이해

```python
# 테이블에 값 할당

dict = {}

dict['a'] = 1
dict['b'] = 2
dict['c'] = 3

dict

```

```python

# hash table에 반복문 적용

for key in dict.keys():
  print(dict[key])

# {키, 쌍} 출력

for k, v in dict.items():
  print(f"key : {k} , value : {v}")


```

#### hash function

- 해시함수는 보통 문자열 입력값에 정수형 출력값을 반환한다.
- 정수형에서 문자열로 변환하기 위해 해시함수는 문자열에 해당하는 개별 단어들을 활용한
- 삽입, 검색, 삭제 무엇을 하든지 해시함수는 키를 통해 저장된 값에 연관된 인덱스를 반환한다.(키와 인덱스가 매칭되어야 한다.)
  - -> 만약 해시테이블이 하나의 요소를 갖고 잇다면, 해시테이블 인덱스 갯수에 관계 겂이 프로그래밍 수행시간이 비슷하다

```python

# 굳이 리스트로 hash를 구현할 경우
# 파이썬의 hash table 은 Dictionary이다.
# Dictionary method로 삽입, 삭제, 검색을 수행할 수 있다.

def hash_func(str,list_size):
    bytes_repr = str.encode()

    #print(f"str : {str}")
    #print(f"str_encode : {str.encode()}")
    #print(f"byte_repr : {bytes_repr}")

    sum = 0

    for byte in bytes_repr:
        sum += byte

    return sum % list_size


my_list = [None] * 5 # 리스트 초기화: 중요 테크닉


my_list[hash_func("aqua",len(my_list))] = "#00FFFF" # 삽입


#print(my_list[hash_func("aqua",len(my_list))]) # 리스트 값 출력
print(my_list[hash_func("aqua",len(my_list))])
print(my_list)
# print(hash_func("aqua",len(my_list)))

```
- Python Hash table 구현하기

```python
# python hash table 구현
class hash_table:
    # 키에 따른 값 초기화
    def __init__(self):
        self.table = [None] * 5
    
    # 기능3) name에 따라 특정값을 반환해주는 해시함수
    def hash_function(self, name):
        table_sum = 0

        encoded = name.encode() # 문자열을 
        for byte in encoded:
            table_sum += byte

        return table_sum % len(self.table) # 반환된 정수 값이 리스틔 인덱스(키) 가 된다

    # name에 따라 num이 매칭되게끔 삽입
    def hash_insert(self, name, num):
        hash_key = self.hash_function(name) #
        self.table[hash_key] = num # 

    # name에 따라 매칭되는 num 검색
    def hash_search(self, name):
        return self.table[self.hash_function(name)]

ht = hash_table()

ht.hash_insert('Kim', 1234)
ht.hash_insert('Johne', 5678)
ht.hash_insert('Smith', 1526)
ht.hash_insert('Michael', 3748)


print(ht.hash_search('Johne'))

```


#### hash 충돌

- 해시함수가 서로 다른 두 개의 키에 대해 동일한 해시값을 내는 것을 해시 충돌이라고 한다.
- 해시충돌은 보통 해쉬값의 개수보다 많은 키값을 해쉬값으로 변환하는 일대다 대응 때문에 발생한다.
  - 키가 들어갈 자리(버킷)이 없는 경우에 발생한다.

- 아래 그림의 경우 Sandra와 Jonn의 키가 같아 버킷 152에서 충돌이 발생한다.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Hash_table_5_0_1_1_1_1_1_LL.svg/675px-Hash_table_5_0_1_1_1_1_1_LL.svg.png" alt="700"/>


#### hash 충돌 방지 - chaining 활용

- chaining은 충돌이 발생한 위 그림처럼 해시테이블에서 동일한 해시 값에 대해 충돌이 일어나면, 해당 위치에 있던 버킷에 키값을 뒤이어 연결하는 것이다.
- 이때 데이터는 **해시값이 같은 노드를 연결하는** 연결리스트의 형태를 가진다.
  - 따라서 특정 해시값에 대해 충돌이 발생하여도, 체이닝을 통해 값을 찾을 수 있다.

```python

# python hashtable chaining 구현


chain_hash_table = [[] for _ in range(20)]

def chain_hash_func():
  return key % len(chain_hash_table)

# 키 값 쌍을 해시테이블에 삽입

def chain_insert_func(chain_hash_table, key, value):
  hash_key = chain_hash_func(key)
  chain_hash_table[hash_key].extend(value)


chain_insert_func(chain_hash_table,20,"C")
print(chain_hash_table)

```

#### hash 충돌 방지 - open addressing

- 하나의 버켓에 하나의 entry만 들어갈 수 있는 형태이다.(저장공간이 정해져있다.)
- 기본적인 로직은 비어있는 배열 슬롯이 발견될 때까지 배열의 위치를 검색하는 것이다.
- Chaining은 연결문제를 해결하여 충돌을 해결하고 Open Addressing은 내부적으로 공간이 정해진 배열을 활용하여 빈공간을 찾는 식으로 충돌을 해결한다.
- close hashing이라고도 불린다.
- 파이썬 자료형으로 구현된 hash table이 Dictionary이다.
-   Dictioanary는 내부적으로 open addressing 방식을 활용한다.

- **로드 팩터** : (Number of items in hash table) / (Total Number of Slots)
  - 해시테이블에 저장된 항목 수(테이블에 입력된 키 갯수)를 슬롯 수 (해시테이블 전체 인덱스 갯수)로 나눈 값
  - open addressing을 사용하면 최대 로드 팩터는 1정도 나온다.
  - 체이닝을 사용할 경우 로드 팩터는 open addressing보다 좋은 성능을 보인다.
  - 로드 팩터를 낮추면 해시에 대한 성능이 올라간다.

```python
# 파이썬으로 구현한 open addressing
class open_address:
    def __init__(self, table_size):
        self.size = table_size
        self.hash_table = [0 for a in range(self.size)]
        
    def getKey(self, data):
        self.key = ord(data[0])
        return self.key
    
    def hashFunction(self, key):
        return key % self.size

    def getAddress(self, key):
        myKey = self.getKey(key)
        hash_address = self.hashFunction(myKey)
        return hash_address
    
    def save(self, key, value):
        hash_address = self.getAddress(key)
        
        if self.hash_table[hash_address] != 0:
            for a in range(hash_address, len(self.hash_table)):
                if self.hash_table[a] == 0:
                    self.hash_table[a] = [key, value]
                    return
                elif self.hash_table[a][0] == key:
                    self.hash_table[a] = [key, value]
                    return
            return None
        else:
            self.hash_table[hash_address] = [key, value]
            
    def read(self, key):
        hash_address = self.getAddress(key)
        
        for a in range(hash_address, len(self.hash_table)):
            if self.hash_table[a][0] == key:
                return self.hash_table[a][1]
        return None
    
    def delete(self, key):
        hash_address = self.getAddress(key)
        
        for a in range(hash_address, len(self.hash_table)):
            if self.hash_table[a] == 0:
                continue
            if self.hash_table[a][0] == key:
                self.hash_table[a] = 0
                return
        return False
        
        
#Test Code
#h_table = CloseHash(8)

h_table = open_address(8)

data1 = 'aa'
data2 = 'ad'
print(ord(data1[0]), ord(data2[0]))

h_table.save('aa', '3333')
h_table.save('ad', '9999')
print(h_table.hash_table)

h_table.read('ad')

h_table.delete('aa')
print(h_table.hash_table)

h_table.delete('ad')
print(h_table.hash_table)

```

**References & annotation**
---

- [hash table wikipedia](https://en.wikipedia.org/wiki/Hash_table)
- [참조 블로그](https://ratsgo.github.io/data%20structure&algorithm/2017/10/25/hash/)
- [hashnet hash](http://wiki.hash.kr/index.php/%ED%95%B4%EC%8B%9C_%ED%85%8C%EC%9D%B4%EB%B8%94)

