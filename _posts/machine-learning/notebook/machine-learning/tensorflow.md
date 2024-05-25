## Tensorflow

### Tensor 연산

#### Tensor

---

**_Concept_**

- **tensor** :
- **rank** :
- 

---

#### Rank

TensorFlow 시스템에서, tensor는 *rank*라는 차원 단위로 표현된다.
Tensor rank는 행렬의 rank와 다르다.
Tensor rank(*order*, *degree*, *-n_dimension* 으로도 언급됨)는 tensor의 차원수다.
예를 들어, 아래 tensor(Python 리스트로 정의)의 rank는 2다.

    t = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rank 2인 tensor는 행렬, rank 1인 tensor는 벡터로 생각할 수 있다. 
rank 2인 tensor는 `t[i, j]` 형식으로 원소에 접근할 수 있다.
rank 3인 tensor는 `t[i, j, k]` 형식으로 원소를 지정할 수 있다.

#### Shape

TensorFlow 문서는 tensor 차원을 표현할 때 세 가지 기호를 사용한다. rank, shape, Demension number.
아래 표는 그 세 가지의 관계를 보여준다:

| Rank | Shape              | Dimension number | Example                                 |
| ---- | ------------------ | ---------------- | --------------------------------------- |
| 0    | []                 | 0-D              | A 0-D tensor.  A scalar.                |
| 1    | [D0]               | 1-D              | A 1-D tensor with shape [5].            |
| 2    | [D0, D1]           | 2-D              | A 2-D tensor with shape [3, 4].         |
| 3    | [D0, D1, D2]       | 3-D              | A 3-D tensor with shape [1, 4, 3].      |
| n    | [D0, D1, ... Dn-1] | n-D              | A tensor with shape [D0, D1, ... Dn-1]. |

### Tensorflow 전처리 파이프라인 구현

**ref**

- [Tensorflow 데이터 로딩 및 전처리 파이프라인 구현하기](https://doubly8f.netlify.app/%EA%B0%9C%EB%B0%9C/2020/08/19/tf-loading-preprocessing-data/)

<!--
tensorflow를 사용하면서 가장 까다로운 부분이 입력데이터 파이프라인 처리해서 모델까지 데이터 흐르는 구간을 만드는게 아닌가 싶다. 데이터의 양이 많을때, 적을때, 그리고 형태에 따라 다양하게 구현을 해야하기 때문에 A라는 방법을 써서 구현하다 보면 모델에 데이터를 넣는 부분이 막힐때가 있다. 그래서 텐서플로우에서 입력데이터를 어떻게 처리해야 하는지에 대한 내용을 정리-->

- **Dataset class 확인(tensorflow에서 데이터를 읽을 때 중심이 됨)**

```python
for m in dir(tf.data.Dataset):
    if not (m.startswith("_") or m.endswith("_")):
        func = getattr(tf.data.Dataset, m)
        if hasattr(func, "__doc__"):
            print("● {:21s}{}".format(m + "()", func.__doc__.split("\n")[0]))
```

- **tfds 관련함수들**

```python
X = tf.range(10)
dataset = tf.data.Dataset.from_tensor_slices(X)
dataset

tf.data.Dataset.Range(10) # 위와 동일

for item in dataset: # Tensor의 형태를 출력
  print(item)

# repeat(): 원본 데이터셋의 아이템을 N차례 반복하는 새로운 데이터셋을 반환 (복사하는 것은 아님)
# batch() : 아이템을 N개의 그룹으로 묶는다
# batch(drop_remainder=True): 마지막에 N보다 부족한 길이의 배치는 버림 (=모든 배치의 크기가 동일)
dataset = dataset.repeat(3).batch(7)
for item in dataset:
    print(item)

# 데이터에 원하는 전처리 작업에도 적용 (이미지 크기 변환, 회전계산)
# map(num_parallel_calls) 를 하면 여러개의 스레드로 나누어서 속도를 높여 처리 가능
dataset = dataset.map(lambda x: x*2)

# map은 각 아이템에 변환을 적용하지만 apply는 데이터셋 전체에 변환을 적용
# dataset = dataset.apply(tf.data.experimental.unbatch()) # deprecated
dataset = dataset.unbatch()

# filter 할때
dataset = dataset.filter(labmda x: x <10)

# 데이터셋에 있는 몇개의 아이템만 보고싶을때
for item in dataset.take(3):
    print(item)
```

#### **데이터 셔플하기**

- 경사 하강법은 훈련 세트에 있는 샘플이 독립적이고 동일한 분포일때 최고의 성능을 발휘 (=shuffle이 필요한 이유)
- 동작순서
  + 원본 데이터셋의 처음 아이템을 buffer_size 개수만큼 추출하여 버퍼에 채운다.
  + 새로운 아이템이 요청되면 이 버퍼에서 랜덤하게 하나를 꺼내 반환
  + 원본 데이터셋에서 새로운 아이템을 추출하여 비워진 버퍼를 채운다.
  + 원본 데이터셋의 모든 아이템이 사용될 때까지 반복
  + 버퍼가 비워질 때까지 계속하여 랜덤하게 아이템을 반환
- 버퍼의 크기를 충분히 크게 하는 것이 중요하다. (=셔플링 효과를 올리기 위해서), 메모리의 크기를 넘지 않도록, 데이터의 크기를 넘지 않도록
- 완벽한 셔플링을 위해서는 버퍼크기가 데이터셋의 크기와 동일
- 셔플링되는 순서를 동일하게 만들기 위해 랜덤 시드를 부여
  + **반드시 suffle을 먼저 한뒤에 repeat를 해야함**
  + **일단 아래 순서로 할 것 : shuffle , repeat, map, batch**
  + [순서레퍼런스](https://stackoverflow.com/questions/51485781/tf-dataset-api-is-the-following-sequence-correct-map-cache-shuffle-batch-repea)

**ref**

- [Tensorflow 데이터 로딩 및 전처리 파이프라인 구현하기](https://doubly8f.netlify.app/%EA%B0%9C%EB%B0%9C/2020/08/19/tf-loading-preprocessing-data/)

tensorflow를 사용하면서 가장 까다로운 부분이 입력데이터 파이프라인 처리해서 모델까지 데이터 흐르는 구간을 만드는게 아닌가 싶다. 데이터의 양이 많을때, 적을때, 그리고 형태에 따라 다양하게 구현을 해야하기 때문에 A라는 방법을 써서 구현하다 보면 모델에 데이터를 넣는 부분이 막힐때가 있다. 그래서 텐서플로우에서 입력데이터를 어떻게 처리해야 하는지에 대한 내용을 정리

- **Dataset class 확인(tensorflow에서 데이터를 읽을 때 중심이 됨)**

```python
for m in dir(tf.data.Dataset):
    if not (m.startswith("_") or m.endswith("_")):
        func = getattr(tf.data.Dataset, m)
        if hasattr(func, "__doc__"):
            print("● {:21s}{}".format(m + "()", func.__doc__.split("\n")[0]))
```

- **tfds 관련함수들**

```python
X = tf.range(10)
dataset = tf.data.Dataset.from_tensor_slices(X)
dataset

tf.data.Dataset.Range(10) # 위와 동일

for item in dataset: # Tensor의 형태를 출력
  print(item)

# repeat(): 원본 데이터셋의 아이템을 N차례 반복하는 새로운 데이터셋을 반환 (복사하는 것은 아님)
# batch() : 아이템을 N개의 그룹으로 묶는다
# batch(drop_remainder=True): 마지막에 N보다 부족한 길이의 배치는 버림 (=모든 배치의 크기가 동일)
dataset = dataset.repeat(3).batch(7)
for item in dataset:
    print(item)

# 데이터에 원하는 전처리 작업에도 적용 (이미지 크기 변환, 회전계산)
# map(num_parallel_calls) 를 하면 여러개의 스레드로 나누어서 속도를 높여 처리 가능
dataset = dataset.map(lambda x: x*2)

# map은 각 아이템에 변환을 적용하지만 apply는 데이터셋 전체에 변환을 적용
# dataset = dataset.apply(tf.data.experimental.unbatch()) # deprecated
dataset = dataset.unbatch()

# filter 할때
dataset = dataset.filter(labmda x: x <10)

# 데이터셋에 있는 몇개의 아이템만 보고싶을때
for item in dataset.take(3):
    print(item)
```

#### **데이터 셔플하기**

- 경사 하강법은 훈련 세트에 있는 샘플이 독립적이고 동일한 분포일때 최고의 성능을 발휘 (=shuffle이 필요한 이유)
- 동작순서
  + 원본 데이터셋의 처음 아이템을 buffer_size 개수만큼 추출하여 버퍼에 채운다.
  + 새로운 아이템이 요청되면 이 버퍼에서 랜덤하게 하나를 꺼내 반환
  + 원본 데이터셋에서 새로운 아이템을 추출하여 비워진 버퍼를 채운다.
  + 원본 데이터셋의 모든 아이템이 사용될 때까지 반복
  + 버퍼가 비워질 때까지 계속하여 랜덤하게 아이템을 반환
- 버퍼의 크기를 충분히 크게 하는 것이 중요하다. (=셔플링 효과를 올리기 위해서), 메모리의 크기를 넘지 않도록, 데이터의 크기를 넘지 않도록
- 완벽한 셔플링을 위해서는 버퍼크기가 데이터셋의 크기와 동일
- 셔플링되는 순서를 동일하게 만들기 위해 랜덤 시드를 부여
  + **반드시 suffle을 먼저 한뒤에 repeat를 해야함**
  + **일단 아래 순서로 할 것 : shuffle , repeat, map, batch**
  + [순서레퍼런스](https://stackoverflow.com/questions/51485781/tf-dataset-api-is-the-following-sequence-correct-map-cache-shuffle-batch-repea)

```python
tf.random.set_seed(42) # 셔플링 순서를 동일하게

# (2) shuffle하고 repeat
dataset = tf.data.Dataset.range(10)
dataset = dataset.shuffle(buffer_size=3, seed=42).repeat(3).batch(7) # 반복마다 순서가 달라지도록
for item in dataset:
    print(item)
```

#### 여러 파일에서 한줄씩 번갈아 읽기

```python
[[여러]] 파일로 데이터 나누기

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

housing = fetch_california_housing()
X_train_full, X_test, y_train_full, y_test = train_test_split(
    housing.data, housing.target.reshape(-1, 1), random_state=42)
X_train, X_valid, y_train, y_valid = train_test_split(
    X_train_full, y_train_full, random_state=42)

scaler = StandardScaler()
scaler.fit(X_train)
X_mean = scaler.mean_
X_std = scaler.scale_

def save_to_multiple_csv_files(data, name_prefix, header=None, n_parts=10):
    housing_dir = os.path.join("datasets", "housing")
    os.makedirs(housing_dir, exist_ok=True)
    path_format = os.path.join(housing_dir, "my_{}_{:02d}.csv")

    filepaths = []
    m = len(data)
    for file_idx, row_indices in enumerate(np.array_split(np.arange(m), n_parts)):
        part_csv = path_format.format(name_prefix, file_idx)
        filepaths.append(part_csv)
        with open(part_csv, "wt", encoding="utf-8") as f:
            if header is not None:
                f.write(header)
                f.write("\n")
            for row_idx in row_indices:
                f.write(",".join([repr(col) for col in data[row_idx]]))
                f.write("\n")
    return filepaths

train_data = np.c_[X_train, y_train]
valid_data = np.c_[X_valid, y_valid]
test_data = np.c_[X_test, y_test]
header_cols = housing.feature_names + ["MedianHouseValue"]
header = ",".join(header_cols)

train_filepaths = save_to_multiple_csv_files(train_data, "train", header, n_parts=20)
valid_filepaths = save_to_multiple_csv_files(valid_data, "valid", header, n_parts=10)
test_filepaths = save_to_multiple_csv_files(test_data, "test", header, n_parts=10)

import pandas as pd

pd.read_csv(train_filepaths[0]).head()
with open(train_filepaths[0]) as f:
    for i in range(5):
        print(f.readline(), end="")

데이터 나눠서 읽기

filepath_dataset = tf.data.Dataset.list_files(train_filepaths, seed=42) # default: shuffle=True
n_reader = 5
# skip(1): header
# interleave(): filepath_dataset에 있는 다섯개의 파일 경로에서 데이터를 읽는 데이터셋을 생성,TextLineDataset 5개를 순회하면서 한줄씩 읽는다.
# 파일 길이가 동일할때 interleave를 사용하는게 좋음 (각파일에서 한줄씩 읽음)
# num_parallel_calls 매개변수에 원하는 스레드 개수를 지정
# tf.data.experimental.AUTOTUNE: 을 지정하면 텐서플로가 가용한 CPU를 기반으로 동적으로 적절한 스레드 개수를 선택할 수 있다.
# cycle_length: 동시에 처리할 입력 개수를 지정
dataset = filepath_dataset.interleave(lambda filepath: tf.data.TextLineDataset(filepath).sip(1), cycle_length=n_readers)

# 각 TextLineDataset의 순서가 랜덤으로 첫번째 해당하는 행을 읽음 (순서가 랜덤)
for line in dataset.take(5):
  print(line.numpy())
```

- 데이터 전처리

```python
# 평균과 표준편차를 미리 계산했다고 가정함
X_mean, X_std = [...]
n_inputs = 8

@tf.fuction
def preprocess(line):
  defs = [0.] * n_inputs + [tf.constant([], dtype=tf.float32)]
  fields = tf.io.decode_csv(line, record_defaults=defs) # csv의 한 라인을 받아 파싱
  # stack() 모든 텐서를 쌓아 1D 배열을 생성
  x = tf.stack(fields[:-1]) # <tf.Tensor: shape=(6,), dtype=int32, numpy=array([1, 2, 3, 4, 5, 6], dtype=int32)>
  y = tf.stack(fields[-1:]) # <tf.Tensor: shape=(1,), dtype=int32, numpy=array([7], dtype=int32)>
  return (x - X_mean) / X_std, y

preprocess(b'4.2083, 44.0, 5.332,....')


record_defaults=[0, np.nan, tf.constant(np.nan, dtype=tf.float64), "Hello", tf.constant([])]
parsed_fields = tf.io.decode_csv('1,2,3,4,5', record_defaults)
'''
[<tf.Tensor: shape=(), dtype=int32, numpy=1>,
 <tf.Tensor: shape=(), dtype=float32, numpy=2.0>,
 <tf.Tensor: shape=(), dtype=float64, numpy=3.0>,
 <tf.Tensor: shape=(), dtype=string, numpy=b'4'>,
 <tf.Tensor: shape=(), dtype=float32, numpy=5.0>]
'''

parsed_fields = tf.io.decode_csv(',,,,5', record_defaults)
'''
[<tf.Tensor: shape=(), dtype=int32, numpy=0>,
 <tf.Tensor: shape=(), dtype=float32, numpy=nan>,
 <tf.Tensor: shape=(), dtype=float64, numpy=nan>,
 <tf.Tensor: shape=(), dtype=string, numpy=b'Hello'>,
 <tf.Tensor: shape=(), dtype=float32, numpy=5.0>]
'''

# Exception
try:
    parsed_fields = tf.io.decode_csv(',,,,', record_defaults) # case 1
    parsed_fields = tf.io.decode_csv('1,2,3,4,5,6,7', record_defaults) # case 2
except tf.errors.InvalidArgumentError as ex:
    print(ex)

# case 1 : Field 4 is required but missing in record 0! [Op:DecodeCSV]
# case 2 : Expect 5 fields but have 7 in record 0 [Op:DecodeCSV]
```

#### 데이터 적재와 전처리 한번에

- 위 코드를 재사용하기 위해서 하나의 함수로 생성

- CSV파일에서 캘리포니아 주택 데이터셋을 효율적으로 적재하고 전처리, 셔플링, 반복, 배치를 적용한 데이터셋을 만들어 반환

- `prefetch()`
  
  + 훈련 속도를 더 빠르게
  + prefetch(1)을 호출하면 데이터셋은 항상 한 배치가 미리 준비되도록 최선을 (=알고리즘이 한 배치로 작업하는 동안 이 데이터셋이 동시에 다음 배치를 준비)
  + GPU에서 훈련하는 스텝을 수행하는 것보다 짧은 시간안에 한 배치 데이터를 준비할 수 있다. (=GPU 100%활용하는 방법)
  + nterleave와 map에 num_parallel_calls을 함께 사용하면 데이터를 적재하고 전처리할때 CPU의 멀티코어를 사용해 더 빠르게 준비 가능
  + prefetch는 일반적으로 하나도 충분, tf.data.experimental.AUTOTUNE을 전달하면 텐서플로가 자동으로 결정 

```python
def csv_reader_dataset(filepaths, repeat=1, n_readers=5,
                       n_read_threads=None, shuffle_buffer_size=10000,
                       n_parse_threads=5, batch_size=32):
    dataset = tf.data.Dataset.list_files(filepaths).repeat(repeat)
    dataset = dataset.interleave(
        lambda filepath: tf.data.TextLineDataset(filepath).skip(1),
        cycle_length=n_readers, num_parallel_calls=n_read_threads)
    dataset = dataset.shuffle(shuffle_buffer_size)
    dataset = dataset.map(preprocess, num_parallel_calls=n_parse_threads)
    dataset = dataset.batch(batch_size)
    return dataset.prefetch(1) # 학습 성능에 아주 중요한 역할

tf.random.set_seed(42)

train_set = csv_reader_dataset(train_filepaths, batch_size=3)
for X_batch, y_batch in train_set.take(2):
    print("X =", X_batch)
    print("y =", y_batch)
    print()
```

- csv_reader_dataset()함수로 훈련 세트로 사용할 데이터셋을 만들기
- https://doubly8f.netlify.app/%EA%B0%9C%EB%B0%9C/2020/08/19/tf-loading-preprocessing-data/

## Modeling with Keras

### Layers Function

- [Unit,Shape,Input Shape,Dimention에 대한 자세한 설명](https://stackoverflow.com/questions/44747343/keras-input-explanation-input-shape-units-batch-size-dim-etc)
- [Keras 한국어문서](https://github.com/keras-team/keras-docs-ko/blob/master/sources/layers/core.md)

---

**_Concept_**

- **shape** : 배열의 각 차원에 몇개의 요소가 있는지에 대한 정보를 담고있는 tuple
  + `(40,4,10)` 은 1차원에 40개, 2차원에 4개 , 3차원에 10개의 요소들을 담고있는 3차원 텐서를 의미한다.
- **input_shape** : 기본적으로 첫번째 차원을 제외한 배열의 차원정보.
- **unit** : 출력층의 차원 수. output layer의 shape을 결정함.
- **kernel** : 층에서 만들어진 `가중치 행렬weight matrix`
- **Dense** :`activation(dot(input, kernel) + bias)` 계산
- **Input** : 텐서 생성
- **Activation** : 출력값에 활성화함수 적용
- **Dropout** : 입력에 Dropout 적용.Dropout은 노드를 지정한 비율만큼 랜덤으로 드롭해서 너무 많은 노드들이 학습\되어 과적합 되는 것을 방지해 준다.노드를 랜덤으로끄고 나머지 노드를 학습을 더 시켜서 퍼포먼스를 향상시킨다.
- **Reshape** : 출력을 특정형태로 변환.
- **Flatten** : 입력을 1차원 텐서로 변환. batch size에는 영향을 주지 않음.
- **Masking** : 시퀀스를 마스킹. 따로 정리

---

#### Input

- 케라스 텐서 생성
- 케라스 텐서는 백엔드(Theano, TensorFlow 혹은 CNTK)에서 사용되는 텐서에 몇가지 속성을 추가한 것으로, 이를 통해 모델의 입력과 출력을 아는 것만으로도 케라스 모델을 만들 수 있습니다.

예를 들어 a, b와 c가 케라스 텐서라고 하면 model = Model(input=[a, b], output=c)만으로도 모델을 생성할 수 있습니다.

케라스 텐서에 추가된 속성은 다음과 같습니다.
`_keras_shape: 케라스의 형태 유추를 통해 전파되는 정수 튜플.`
`_keras_history: 텐서에 적용되는 마지막 층. 해당 층에서 전체 모델 전체의 그래프를 추출할 수 있습니다.`

**인자**

- `shape`: int로 이루어진 튜플. 배치 축을 포함하지 않습니다. 예를 들어 shape=(32,)는 입력이 32차원 벡터의 배치라는 것을 나타냅니다.
- `batch_shape`: int로 이루어진 튜플. 배치 축을 포함합니다. 예를 들어 batch_shape=(10, 32)는 입력이 10개의 32차원 벡터로 이루어진 배치라는 것을 나타냅니다. batch_shape=(None, 32)는 임의의 수의 32차원 벡터로 이루어진 배치를 뜻합니다.
- `name`: str, 층의 문자열 이름. 모델 내에서 이름은 고유해야 하며 이미 사용한 이름은 다시 사용할 수 없습니다. 따로 지정하지 않을 경우, 자동으로 생성됩니다.
- `dtype`: str, 입력 데이터의 자료형(float32, float64, int32...) 입니다.
- `sparse`: bool, 생성할 플레이스홀더가 희소sparse한지 여부를 나타냅니다.
- `tensor`: 해당 인자가 주어진 경우 Input 층은 해당 텐서의 래퍼로 사용되며, 새로운 플레이스홀더 텐서를 만들지 않습니다.

#### Dense

- `output = activation(dot(input, kernel) + bias)을 실행` 
  
  + `activation`은 activation 인자로 전달되는 원소별element-wise 활성화 함수 
  + `kernel`은 층에서 만들어진 `가중치 행렬weight matrix` 
  + `bias`는 층에서 만들어진 편향bias 벡터이며 'use_bias=True'인 경우에만 적용 가능

- layer의 입력텐서의 rank가 2보다 클 경우 가중치 행렬과 내정을 하기 전에 1d 벡터로 형태를 변환해야함

- **unit(출력층의 차원 수)과 `(*,입력층의 차원)` 형태의 배열을 인자로 받고 `(*,units)` 형태의 배열을 출력한다.**

- input_shape 예시
  
  ```python
  input_shape = (50,50,3) # regardless of how many images I have, each image has this shape  
  input_shape = (50,50,3)
    [[regardless]] of how many images I have, each image has this shape  
  ```

```
- Dense 예시

```python
model = Sequential([
                   Dense(32, input_shape = (16,))
                   # (*,16)  형태의 배열을 받아서
                   # (*,32) 형태의 배열을 출력한다.
                   Dense(10)
                   ]
```

```python
keras.layers.Dense(units,
 activation=None,
 use_bias=True,
 kernel_initializer='glorot_uniform',
 bias_initializer='zeros',
 kernel_regularizer=None,
 bias_regularizer=None, 
 activity_regularizer=None, 
 kernel_constraint=None, 
 bias_constraint=None)
```

**Dense Parameters**

- `units`: 양의 int. 출력값의 차원 크기를 결정.
- `activation`: 사용할 활성화 함수. 기본값은 None이며, 이 경우 활성화 함수가 적용되지 않는다.(a(x) = x).
- `use_bias`: bool. 층의 연산에 편향을 적용할지 여부를 결정.
- `kernel_initializer`: kernel 가중치 행렬의 초기화 함수를 결정. 이 가중치는 입력값에 곱해져서 선형변환하는 연산에 사용.
- `bias_initializer`: 편향 벡터의 초기화 함수를 결정.
- `kernel_regularizer`: kernel 가중치 행렬에 적용할 규제 함수regularizer를 결정.
- `bias_regularizer`: 편향 벡터에 적용할 규제 함수를 결정.
- `activity_regularizer`: 층의 출력값에 적용할 규제 함수를 결정.
- `kernel_constraint`: kernel 가중치 행렬에 적용할 제약constraints을 결정. 
- `bias_constraint`: 편향 벡터에 적용할 제약을 결정.
- `units`: 양의 int. 출력값의 차원 크기를 결정.

#### Activation

```python
keras.layers.Activation(activation)
```

- 출력값에 활성화함수 적용
- 모델의 첫 번째 층으로 Activation층을 사용하려면 input_shape로 형태를 지정해야 한다.
- `input_shape`는 int로 이루어진 튜플로 **배치 축을 포함하지 않는다.**

#### Flatten

- input을 1차원으로 바꾼다.
- layer의 입력텐서의 rank 가 2보다 클 경우 가중치와 내적을 하기 전에 1차원 배열로 형태를 변환할때 사용한다.

#### Conv2d

### Sequential API

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

model1 = keras.Sequential(
                          []

                          )
```
