---
title: '[Python]Graph와 Graph Representation의 이해'
categories:
  - - Programming
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
- Preprocessing


#신경망이란 무엇인가?

https://www.youtube.com/watch?v=aircAruvnKk


#참고

https://cinema4dr12.tistory.com/1016?category=515283

https://www.kdnuggets.com/2021/07/top-python-data-science-interview-questions.html
-->

## 그래프

### Graph Concept
---
**_Concept_**

(용어정리)
- **그래프** : node(점)와 edge(간선)으로 이루어진 자료구조 . 추상자료형에 해당한다.
- **Directed Graph** : edge가 방향성이 있을 경우. 기본적으로 엣지가 순서가 있는 쌍으로 표현된다. 
  - leaf : Directed Graph는 순서가 있으므로 마지막 노드가 있다. leaf는 마지막 노드를 뜻한다.
- **Undirected Graph** : edge가 방향성이 없을 경우. 
  - 관계의 목적이 **상호교환** 일 경우 `Undirected Graph`가 가장 적합하다.
  - 항상 동일한 노드에 재방문 가능하기 때문에 순환 그래프에 속한다.
  - adjacency(인접) : 간선이 연결된 것
  - neighbor : 간선이 연결된 노드들을 이웃(neighbor) 이라고 한다.  
- **Cyclic  Graph** :그래프에 루프가 있을 경우
  - loop : 방문한 노드에 재방문 가능할 경우
- **Weighted Graph** : edge에 값(가중치)가 있을 경우. 최단거리 문제에 사용
  - 그래프에서 경로의 총 가중치가 높을 경우 비용이 늘어난다.
- **Directed Acyclic Graph** : 그래프가 순환되지 않고 단방향일 경우. 선형정렬 가능
- Adjacency List : 배열로 표현된 그래프 자료구조(연결리스트)
- Adjacency Matrix : 2차원 배열로 표현된 그래프 자료구조 

---


### Graph Representation

- 기본적으로 인접리스트와 인접행렬 두 가지 방법을 사용한다.

#### 인접리스트(adjacency list)


![](https://cdncontribute.geeksforgeeks.org/wp-content/uploads/listadjacency.png)

- 인접리스트는 그래프를 배열로 나타내는 방식이다.
- 인접리스트에서 그래프는 `전체 노드 목록`을 저장한다,
  - 배열의 크기는 노드의 수와 같다.
  - 배열의 i 번째 엔트리는 i번째 노드와 인접노드의 값을 리스트로 저장한다.
  - Weighted Graph 일 경우 리스트에 값이 아닌 값과 가중치의 페어들이 저장된다.



![](https://i.imgur.com/GiStmNh.jpg)

- Dictionarys로 인접리스트 구현하기
  - vertices는 **O(1)상수시간에 각 edge(간선)에 접근**할 수 있다.
  - edge가 set에 포함되어 있기 때문에 O(1) 상수 시간에 edge가 있는지 확인할 수 있다.
 

```python
# 위 그림에 대해 딕셔너리를 사용한 인접리스트 예시
# 노드가 키가 되고, 인접노드가 값이 되는 딕셔너리이다.
# 가장자리 노드들은 set으로 구현되어 있다.

class Graph:
    def __init__(self):
        self.vertices = {
                            "A": {"B"},   # 여기서 {"B"}가 set의 형태이다.
                            "B": {"C", "D"}, # {"B" : {}}의 형태는 딕셔너리
                            "C": {"E"},     # 즉, 딕셔너리 안에 set이 있는 것이다.
                            "D": {"F", "G"},
                            "E": {"C"},
                            "F": {"C"},
                            "G": {"A", "F"}
                        }
```

- List로 인접리스트 구현

```python
# 이웃노드를 반복적으로 접근해 탐색
# 시간복잡도(N)

a,b,c,d,e,f = range(6) # 6개노드

N = [[b,c,d,f],[a,d,f],[a,b,c],[a,e],[b,c,d,e]]

```

- class로 인접리스트 구현

```python

# 기본적으로 연결리스트처럼 초기화 클래스가 필요하다.
class adjnode:
  def __init__(self,data):
    self.node = data
    self.next = None

class Graph:
  def __init__(self,vertices):
    self.V = vertices
    self.gragh = [None] * self.V



  def add_edge(self,src,dest):
    # 시작지점(src)에 노드 추가
    # 기본적으로 Undirected Graph를 만든다.
    node = adjnode(dest)
    # 아래 코드로 두 노드를 연결시킨다.
    node.next = self.graph[src]
    self.graph[src] = node

  def print_graph(self):
    for i in range(self.V):
      print(f"노드 {i}의 인접리스트 \n")
      temp = self.graph[i]
      while temp:
        print(f"-> {temp.node}",end="" )
        temp = temp.next
      print("\n")

graph = Graph(5)

graph.add_edge(0,1) # 
graph.add_edge(0,4)
graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(1,4)
graph.add_edge(3,1)
graph.add_edge(2,3)
graph.add_edge(3,4)



```
```bash
노드 0의 인접리스트 

-> 4-> 1

노드 1의 인접리스트 

-> 4-> 3-> 2

노드 2의 인접리스트 

-> 3

노드 3의 인접리스트 

-> 4-> 1

노드 4의 인접리스트 

```

#### 인접행렬(adjacency matrix)

- N * N 크기의 2차원 배열로 나타낸다.
  - N 은 노드의 개수이다.
- 인접행렬은 2차원 배열을 활용해 그래프를 표현한 것이다.
  - `adj[i][j] : 노드 i에서 노드 j로 가는 간선이 있으면 1, 아니면 0`
  
- 파이썬에서는 중첩리스트로 구현한다.
- Undirected Graph의 인접행렬은 항상 대칭이다.
- 인접행령의 가중치를 추가할 경우 1과 0 값을 다른 숫자로 바꾼다.
- 인접행렬로 나타낸 그래프 구조들
<img src="https://www.researchgate.net/publication/347300725/figure/fig1/AS:969208926044162@1608088823984/Different-types-of-graphs-and-their-corresponding-adjacency-matrix-representations-The.ppm" alt="700"/>


![https://i.imgur.com/GiStmNh.jpg](https://i.imgur.com/GiStmNh.jpg)

- 위 그래프를 인접행렬로 만들 경우 우선 아래와 같은 그림을 만들 수 있다.

![https://github.com/Maiven/data-science/blob/main/%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%A5%E1%86%B8%E1%84%92%E1%85%A2%E1%86%BC%E1%84%85%E1%85%A7%E1%86%AF.png?raw=true](https://github.com/Maiven/data-science/blob/main/%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%A5%E1%86%B8%E1%84%92%E1%85%A2%E1%86%BC%E1%84%85%E1%85%A7%E1%86%AF.png?raw=true)

- List로 구현한 인접행렬
```python
# 리스트로 구현한 인접행렬
# 아래 코드처럼 위의 간선 가중치는 1이다.

class Graph:
    def __init__(self):
        self.edges = [[0,1,0,0,0,0,0],
                      [0,0,1,1,0,0,0],
                      [0,0,0,0,1,0,0],
                      [0,0,0,0,0,1,1],
                      [0,0,1,0,0,0,0],
                      [0,0,1,0,0,0,0],
                      [1,0,0,0,0,1,0]]

```



- 위에서 행렬은 리스트 안에 리스트가 있는 2차원 배열로 표현된다.
    - 구현을 통해 기본 제공되는 행렬 간에 **edge weights(간선 가중치)**를 알 수 있다.
    - **0은 관계가 없음**을 나타내지만 다른 값은 **edge label 또는 edge weight**를 나타낸다.
    - 인접행렬의 단점은 **노드 값과 해당 인덱스 사이에 연관성이 없다**는 것이다.
- 실제로 인접리스트와 인접행렬을 모두 구현하면 Vertex(정점) 및 Edge(간선) 클래스를 포함하여 더 많은 정보를 파악할 수 있다.

#### Weighted Graph 구현하기

- 리스트로 그래프 가중치를 표현하는 것 보다 행렬로 구현하는 것이 쉽다.

```python

# 인접리스트 구현

class Graph:
    def __init__(self):
        self.vertices = {
                            "A": {"B": 1},  # 가중치 부여
                            "B": {"C": 3, "D": 2},  # 가중치 부여
                            "C": {},
                            "D": {},
                            "E": {"D": 1}   # 가중치 부여
                        }
```


```python
# 인접행렬 구현

class Graph:
    def __init__(self):
        self.edges = [[0,1,0,0,0],
                      [0,0,3,2,0],
                      [0,0,0,0,0],
                      [0,0,0,0,0],
                      [0,0,0,1,0]]
```


### 그래프에서의 복잡도 계산

- 인접행렬은 특징은 **구현이 쉽다**는 것이다.
    - 때문에 인접행렬의 가장 큰 단점은 **특정노드에 방문한 노드들을 알기 위해서는 모든 노드를 확인**해야 한다는 것이다. (시간복잡도 O(N))
    - 이러한 단점을 위해 인접리스트로 표현방식이 생겼다.
- 인접리스트는 실제 연결된 관계만을 저장해주기 때문에 실행시간에 영향을 적게 준다.
    - 인접리스트의 단점은 **특정 노드간의 연결관계를 확인하기 위해서는 반복문이 활용되어야 하며 따라서 O(N) 이상의 시간복잡도** 가 발생한다는 것이다.

**References & annotation**
---
- [Graph Concept](https://youtu.be/ofykE5elSfI)
- [Graph Data Structure](https://ratsgo.github.io/data%20structure&algorithm/2017/11/18/graph/)
- [Graph Representaion](https://www.geeksforgeeks.org/graph-and-its-representations/)

