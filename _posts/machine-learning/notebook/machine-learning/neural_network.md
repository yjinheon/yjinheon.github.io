# Neural Network

- 딥러닝은 매우 복잡한 다변수 함수의 최적해를 경사 하강법을 통해 찾는 것

**머신러닝과 딥러닝의 차이**

![](https://assets.website-files.com/5fb24a974499e90dae242d98/60f6fcbbeb0b8f57a7980a98_5f213db7c7763a9288759ad1_5eac2d0ef117c236e34cc0ff_DeepLearning.jpeg)

선형 회귀는 n-차원 공간에서 선형 모델을 학습하기 위한 방법입니다. 물론 비선형(non-linear) 특성들도 다항식(polynomial)을 사용한 선형회귀모델을 사용하면 학습 가능합니다. 문제는 데이터의 차원이 매우 높으며 비선형 패턴을 가진 데이터를 학습하려면 그에 따라 매우 복잡한 다차원의 특성 조합이 필요하게 됩니다. 이렇게 차원이 높은 데이터의 예는 아래와 같은 이미지 데이터를 떠올리시면 됩니다.


지금까지 여러분들은 머신러닝을 수행하면서 여러분들이 지접 데이터에 대해 파악하여 그 특징에 맞는 특성들을 설계하고 찾아내었습니다. 여기서 컴퓨터가 학습과정을 통해 특성과 출력값 과의 관계를 찾아 주었지요.

반면에 **신경망 학습은 데이터에서 필요한 특성들을 신경망이 알아서 조합하여 찾아냅니다!** 즉 우리는 최소한의 데이터에 대한 전처리는 해야 하지만 심화된 특성 공학(Feature Engineering)을 사용해 특성들을 찾아낼 필요는 없다는 것입니다.

깊은 신경망, 즉 **딥러닝과 머신러닝의 차이는 표현학습(representation learning)**에 있습니다. **딥러닝은 데이터 특성(feature)을 우리가 풀고자 하는 문제를 풀기 쉽도록 표현(representation)하도록 학습하는 능력**이 있습니다. 신경망의 구조와 깊이를 변화시키며 데이터를 더욱 유용하게 표현할 수 있습니다.

- [일반인을 위한 딥러닝 영상 feat.역사 (0-15분까지만 시청)](https://www.youtube.com/watch?v=C2sqt9pG6K0)
  - 신경망의 역사에 대해서 배우고, 신경망의 원리를 '일반인'에게 설명할 수 있다는 학습목표를 가지고 공부하시면 이번 챕터를 수월하게 넘어가실 수 있습니다. 
- [신경망으로 Linear Regression (03:25~08:50까지)](https://youtu.be/PyzBX93icz0?t=204)
  - Section2에서 배웠던 Linear Regression에 대해서 배운 내용을 재확인하고, 신경망을 이용하여 Linear Regression를 표현한다면 어떻게 만들어 볼 수 있는 지, 수학적인 접근을 배워볼 수 있습니다. 
- 복습 : [머신러닝 개발자들의 일반적인 실수, 과적합 (Overfitting, 4분)](https://www.youtube.com/watch?v=f4sP7OE68-A)
- 복습 : [교차검증(Cross Validation, 3분)](https://www.youtube.com/watch?v=TIgfjmp-4BA)
- 복습 : [데이터 split & shuffle for ML (7분)](https://www.youtube.com/watch?v=JxFA_bZWPvU)
- 학습방법 : Section4를 공부하면서 메타인지가 중요합니다. 내가 아는 것과 모르는 것을 정확하게 구분하는 연습을 해보고, 정확한 개념이 맞는지 이해하고, 정리하고, 설명해보면 좋겠습니다.  [읽어볼 거리 1](https://m.blog.naver.com/PostView.nhn?blogId=hems97&logNo=220557131351&proxyReferer=https:%2F%2Fwww.google.com%2F) (웹페이지) / [읽어볼 거리 2](https://brunch.co.kr/@kamohaeng/53) (웹페이지)
  - 내가 무엇을 알고 무엇을 모르고 있는 지 확인하고, 필요한 것을 빠르게 획득하고자 노력해봅시다.

## Deep artifictial Network

---

**_Concept_**

- **Neuron:** :입력 신호를 받아 고유한 가중치를 곱해 그 값이 threshold를 넘으면 출력신호를 내보내는 것.
- **Perceptron**: 신경망에서 Neuron을 구현한 것.
- **Node** : 신경에서의 Node는 입력값을 받아 연산을 수행해 output을 내보내는 것.
- **Input Layer:** :신경망에서 Feature Vector가 들어가는 층을 말한다. **Feature Vector는 데이터 사이즈와 Feature로 구성된 n차원 배열이다.** input data이기 때문에 신경망 연산에서 상수취급 되며 가중치가 존재하지 않는다.
- **Hidden Layer:** :입력층과 출력층 사이에 존재하는 층 .기본적으로 입력된 Feature의 비선형 변환을 수행해 데이터를 구분하는 특징을 신경망에서 보다 더 잘 파악하게 만드는 역할을 한다. Hidden Layer를 통해 선형공간밖에 나타내지 못한다는 단층 퍼셉트론의 한계를 극복할 수 있다.
- **Output Layer:** :신경망의 연산 결과가 출력되는 층. `Activation Function`이 이 층에 있다.출력층의 node의 수는 target class의 수와 동일하다.
- **Activation Function:** :neuron의 출력값을 보정해서 어떻게 내보낼지 결정하는 함수. 예를 들어 RelU의 경우 입력이 특정 값을 넘으면 입력을 그대로 출력하고 그 이하면 0을 출력한다.
  + sigmoid
  + relu
  + tanh
  + leakyrelu
- **Back Propagation:** : 예측값과 실제값의 차이(에러)를 줄이기 위해  비용함수가 최소가 되도록 출력층으로부터 순전파의 역방향으로 편미분을 통해 가중치를 업데이트 하는 것.
- **가중치(Weight)** : 두 뉴런 사이의 연결강도. 머신러닝에서 실질적인 학습의 대상이다. (a weight decides how much influence the input will have on the output.)
- **편향(Bias)**: feature vector와 가중치 벡터의 내적에 더해주는 상수. bias가 전체적인 threshold의 높낮이를 조절한다.
  + [편향이 역전파과정에서 업데이트되는 방식](https://stackoverflow.com/questions/3775032/how-to-update-the-bias-in-neural-network-backpropagation)

---

Perceptron은 **여러 신호를 입력으로 받아 하나의 신호를 출력하는 일종의 뉴런**이다. 생물학에서 이야기하는 그 뉴런의 컨셉을 생각하면 이해가 쉽다.

**퍼셉트론의 계산구조**

- 한개의 뉴런으로 여러 입력신호(x0, x1, ...)가 입력되면 각각 고유한 가중치(weights, w0, w1, ...)가 곱해지고 더해진다.
- 가중합에 편향이 추가된다.
- 가중치가 곱해진 값들은 모두 더해져 정해진 임계값(threshold)을 넘을 경우에만 다음 노드들이 있는 층(layer)으로 신호가 전해진다.

아래 그림을 통해 기본적인 퍼셉트론 노드의 구조를 쉽게 이해할 수있다.

![](https://upload.wikimedia.org/wikipedia/commons/f/ff/Rosenblattperceptron.png)

<center><b>그림1. Perceptron 구조</b></center>

퍼셉트론은 수식으로 아래와 같이 간단히 나타낼 수 있다.


$$
\begin{align}
 y =activation(\sum(w_{1}x_{1} + w_{2}x_{2} + ... + w_{n}x_{n}) + bias)
\end{align}
$$

![](https://i.imgur.com/ExuC6j3.png)

<center><b>그림2. Perceptron Learning Algorithm</b></center>

### 최적화 관점에서의 Perceptron

**Perceptron은 정확히 말하면 Perceptron Learning Algorithm이다.**

최적화 관점으로 생각하면 Perceptron 또한 비용함수인 $f(h)-y$ 를 최소화 하는 목적을 가지고 있다고 볼 수 있다.

Perceptron 알고리즘에서의 비욯함수는 `0-1 loss`인데 이는 단순히 잘못된 예측에 대해 1의 패널티를 부여하고 제대로된 예측은 그대로 놔두는 것이다.

이를 수식으로 나타내면 아래와 같다

$$L(\hat{y}, y) = I(\hat{y} \ne y)$$

(여기서 I 는 indicator 함수로 0아니면 1의 결과를 반환한다.)

**이러한 비용함수의 문제는 gradient descent를 사용해 국소최적해(local optimum)를 찾기 어렵다는 것이다.**

![](https://i.imgur.com/1ne1C4K.png)

<center><b>그림3. Perceptron 의 학습</b></center>

### 논리게이트와 다층퍼셉트론

#### 논리게이트

- XOR 구현
- XOR은 퍼셉트론을 2개 쌓은 구조이다.

```python
def XOR(x1, x2):
    a = NAND(x1, x2)
    b = OR(x1, x2)
    res = AND(s1, s2)
    return res
```

#### 다층퍼셉트론

다층퍼셉트론의 구조적 특징

단층 퍼셉트론은 기본적으로 1,0의 출력값만 가지고 있기 때문에 직선하나로 나눈 선형영역만 표현할 수 있지만
**다층 퍼셉트론의 경우 퍼셉트론의 층을 쌓기 때문에 비선형영역도 분리해서 나타낼 수 있게 된다.**

이는 feature space에서 class를 구분하는 추가적인 특징을 추출할수 있다는 것이다.

이렇게 퍼셉트론의 층을 쌓아 input과 output 사이에 존재하게 되는 층을 은닉층이라 한다.

### 활성화 함수

활성화 함수는 입력벡터와 가중치벡터의 가중합인 net input을 받아 출력신호를 도출해내는 함수이다.

![](https://blog.kakaocdn.net/dn/OweTJ/btqMOxROJZi/L1VJ0bbL025lWkDcKbzVKk/img.png)

#### Sigmoid Function

$$
f_{\mathbf{\theta},b}(x) = g(\mathbf{\theta}\cdot \mathbf{x} + b)
$$

where function $g$ is the sigmoid function. The sigmoid function is defined as:

$$
g(z) = \frac{1}{1+e^{-z}}
$$
numpy로 구현하면 아래와 같다.

```python
import numpy as np

def sigmoid(x):
  return 1/ (1+np.exp(-x))
```

#### Softmax Function

: softmax 는 기본적으로 수치형 input vector를 확률로 변환하기 위한 활성화함수이다.

- multiclass classification 에 활용된다.

```python
import numpy as np

def softmax(input):
    return np.exp(x) / np.sum(np.exp(x),axis=0)

```



###### 기울기 소실과 편향 이동

**Gradient Vanishing 문제**

- 입력의 절대값이 크게 되면 0이나 1로 수렴하게 되는데, 이러한 뉴런들은 그래디언트를 소멸(kill) 시켜 버린다. 
- 그 이유는 수렴된 뉴런의 그래디언트 값은 0이기 때문에 역전파에서 0이 곱해지기 때문이다.
- 따라서, 역전파가 진행됨에 따라 아래 층(layer)에는 아무것도 전달되지 않는다.(시그모이드의 도함수는($\alpha$(1-$\alpha$))이므로 함수의 값이 0이나 1에 가까우면 도함수의 결과가 매우 작아진다.)

**편향 이동 문제**

- 원점 중심이 아니다(Not zero-centered).  따라서, 평균0이 아니라 0.5이며, **시그모이드 함수는 항상 양수를 출력하기 때문에 출력의 가중치 합이 입력의 가중치 합보다 커질 가능성이 높다.** 이것을 편향 이동(bias shift)이라 하며, 이러한 이유로 각 레이어를 지날 때마다 분산이 계속 커져 가장 높은 레이어에서는 활성화 함수의 출력이 0이나 1로 수렴하게 되어 그래디언트 소실 문제가 일어나게 된다

#### RelU Function

- Rectified Linear Function
- 지정한 max를 넘으면 입력값을 그대로 출력. 넘지 못하면 0 출력
- 0 이상인 곳에서는 수렴하는 구간이 없다.
- 단순히 입력값을 그대로 출력으로 내보내기 때문에 시그모이드 함수에 비해 계산 속도가 빠르다.

```python
def ReLU(x):
    return np.maximum(0, x)
```

#### tanh Funtion

- 중심을 원점으로 옮김
- tanh함수는 아래의 그림과 같이 입력값의 총합을 -1에서 1사이의 값으로 변환해 주며, 원점 중심(zero-centered)이기 때문에, 시그모이드와 달리 편향 이동이 일어나지 않는다.
- tanh함수 또한 입력의 절대값이 클 경우 -1이나 1로 수렴하게 되므로 그래디언트를 소멸시켜 버리는 문제가 있다. 

```python
def tanh(x):
    return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
```

#### LeakyRelu

- no blog : 따로

**Dead Relu문제**

- ReLU의 문제는 모델이 학습하는 동안 일부 뉴런이 0만을 출력하여 활성화 되지 않는 문제인데, 이러한 문제를 dead ReLU라고 한다. 
- 학습률(learning rate)이 클 경우, 모델의 뉴런이 절반정도가 죽기도(뉴런이 0만 출력) 한다.
- 이렇게 뉴런이 0만을 출력하는 이유는 학습이 진행되면서 뉴런의 가중치가 업데이트 되면서 가중치 합이 음수가 되는 순간 ReLU에 의해 그 이후로는 0만 출력하게 되며, 이때의 그래디언트 값이 0이 되기 때문이다.

이러한 dead ReLU문제를 해결하기 위해 ReLU함수를 조금씩 변형시켜 다양한 ReLU Family를 만들어 사용하기도 한다.

일반적으로 $\alpha$=0.01로 설정한다. 즉, 0 이하인 입력에 대해 활성화 함수가 0만을 출력하기 보다는 입력값에 $\alpha$만큼 곱해진 값을 출력으로 내보내어 dead ReLU문제를 해결한다.

```python
def Leaky_ReLU(x,alpha=0.01):
    return np.maximum(alpha*x, x)
```

#### Elu

- 조정을 통해 **Gradient가 0으로 수렴하지 않게끔 한다**
- X<0 때 ELU 활성화 함수 출력의 평균이 0(zero mean)에 가까워지기 때문에 편향 이동(bias shift)이 감소하여 그래디언트 소실 문제를 줄여준다. 
- 하이퍼파라미터인 $\alpha$는 x가 음수일 때 ELU가 수렴할 값을 정의하며 보통 1로 설정한다.

```python
def elu(x,alpha):
    return (x>0)*x + (x<=0)*(alpha*(np.exp(x) - 1))
```

![각 활성화함수 비교](https://www.researchgate.net/profile/Vivienne_Sze/publication/315667264/figure/fig3/AS:669951052496900@1536740186369/Various-forms-of-non-linear-activation-functions-Figure-adopted-from-Caffe-Tutorial.png)

### 신경망 층(Layerss)

#### Input Layers

- 입력층은 데이터셋으로부터 입력을 받습니다. 
- 보통 **입력층은 어떤 계산도 수행하지 않고** 그냥 값들을 전달하기만 한다.
- 입력 변수의 수와 입력 노드의 수는 같습니다. 
  + **신경망의 층수(깊이, depth)를 셀 때 입력층은 포함하지 않는다.**

#### Hidden Layers

계산이 일어나는 층이 둘 이상인 신경망을 다층(multilayer) 신경망 이라고 부른다.
계산이 없는 입력층과 마지막 출력층 사이에 있는 층들을 은닉층(Hidden Layers) 이라 한다.

- 딥러닝(deep learning)은 사실 두 개 이상의 (이때 부터 깊다(deep)라고 합니다) 은닉층들을 가진 신경망, 입력층을 제외하고 시작하여 3개 이상의 Layer를 갖는 신경망을 의미합니다. 

#### Output Layers

##### Output Layer의 활성화함수 정하기

> 일반적으로 ELU → LeakyReLU → ReLU → tanh → sigmoid 순으로 사용.  ReLU를 먼저 쓰고 , 그다음으로 LeakyReLU나 ELU 같은 ReLU Family를 쓰며, sigmoid는 사용하지않는다.(cs231n 강의)

**풀고자하는 문제에 따른 활성화함수**

- 회귀문제 

- 이진분류문제

- 다중중류 문제

- **회귀 문제에서 예측할 목표 변수가 실수값인 경우 활성화함수가 필요하지 않으며** 출력노드의 수는 출력변수의 갯수와 같습니다.

- **이진 분류(binary classification) 문제의 경우 시그모이드(sigmoid) 함수**를 사용해서 출력을 확률 값으로 변환하여 부류(label)를 결정하도록 합니다.  

- **다중클래스(multi-class)를 분류하는 경우 출력층 노드가 부류 수 만큼 존재하며 소프트맥스(softmax) 함수**를 활성화 함수로 사용합니다. 

### Python으로 Perceptron 구현하기

간단한 Perceptron을 Python으로 구현해보자

```python
class Perceptron:
    # niter = epoch
    def __init__(self, rate = 0.01, niter = 10):
        self.rate = rate
        self.niter = niter

    def fit(self, X, y):
        """Fit training data
        X : Training vectors, X.shape : [#samples, [[features]]]
        y : Target values, y.shape : [#samples]
        """

        # 초기 가중치 [0, 0, 0]
        self.weight = np.zeros(1 + X.shape[1])

        # Number of misclassifications
        self.errors = [] 

        for i in range(self.niter):
            err = 0
            for xi, target in zip(X, y):
                # adjusts
                delta_w = self.rate * (target - self.predict(xi))
                self.weight[1:] += delta_w * xi
                self.weight[0] += delta_w
                err += int(delta_w != 0.0)
            self.errors.append(err)
        return self

    def net_input(self, X):
        """Calculate net input"""
        return np.dot(X, self.weight[1:]) + self.weight[0]

    def predict(self, X):
        """Return class label after unit step"""
        """ Default Step Function"""
        return np.where(self.net_input(X) >= 0.0, 1, -1)
```

### 정리

- 퍼셉트론은 입출력을 가지는 일종의 알고리즘이다. 입력에 따라 정해진 규칙에 따른 값을 반환한다.
- 퍼셉트론은 가중치와 편향을 매개변수로 지정한다.
- 퍼셉트론으로 논리회로를 표현할 수 있다.
- XOR 게이트의 경우 퍼셉트론을 여러개 쌓아서 구현 가능하다.
- 퍼셉트론은 샘플을 입력받아 가중치 w를 연결하여 net input을 계산한다. 
- net input은 입력벡터와 가중치 벡터의 내적이다. 
- net input은 activation 함수로 전달되어 출력값이 보정된다.

**ref**

- https://en.wikipedia.org/wiki/Perceptron
- https://towardsdatascience.com/perceptron-learning-algorithm-d5db0deab975

## 역전파 알고리즘(Backpropagation)



**순전파가 입력층에서 신호를 받아 은닉층의 가중치(+bias)와 연산을 한 뒤 출력층에서 벡터를 출력하는 과정이라면 역전파는 예측값과 실제값의 차이(에러)를 줄이기 위해  손실함수가 최소가 되도록 출력층으로부터 순전파의 역방향으로 편미분을 통해 가중치를 업데이트 하는 것이다.**

역전파 알고리즘에서 가중치를 업데이트 한다는 것은 가중치 매개변수의 기울기(Graidant)를 예측값을 바탕으로 다시 계산한다는 것이다.

기본적으로 **타겟과 예측값의 차이를 줄이기 위해** 가중치를 업데이트한다.
$$
y = activiate(\sum(\theta_{1}x_{1} + \theta_{2}x_{2} + ... + \theta_{n}x_{n}) + bias)
$$

타겟과 예측값의 차이는 `loss function(cost function)`이라고 볼 수 있다.

비용함수는 수식으로 나타내면 아래와 같다.

$$
J(\theta) = y - h_\theta(x)
$$
여기서 $h_\theta(x)$ 는 가설함수(모형)이다.

역전파(backward Propagation)는 예측값의 국소적 미분값을 순전파(Forward Propagation)의 반대방향으로 곱한 후 다음노드로 전달하는 것이다.

비용함수의 편미분을 통해 기울기를 구하는 이유는 **기울기가 비용함수의 값을 최소화 하는 방향을 제시하기 때문이다.**

![](https://i.imgur.com/Olxv64J.png)

<center><b>그림 1. Gradiant Boosting을 통한 global optimum 찾기</b></center>

만약 모형의 loss function이 MSE(Mear Sqared Error)일 경우, 비용함수는 아래와 같이 나타낼 수 있다. (m은 sample의 수를 의미)

$$ J(\theta)=\frac{1}{2 m} \sum_{i=1}^{m}\left(y^{(i)}-\hat{y}^{(i)}\right)^{2}$$

이를 미분할 경우 직접 계산하기 어렵거나 불가능하기 때문에 Chain Rule을 사용한 합성함수의 편미분을 통해 구한다.

아래와 같은 신경망이 있고 output node의 활성화함수는 sigmoid라고 할 경우

![](https://i.imgur.com/bGCvYVJ.png)

<center><b>그림 2. 신경망으로 나타낸 backpropagation</b></center>

하나의 가중치에 대한 Gradiant를 아래와 같이 나타날 수 있다.

$$
 Gradiant=\frac{\partial J(\theta)}{\partial \theta_{i}}=\frac{\frac{1}{2 m} \sum_{i=1}^{m}\left(y^{(i)}-\hat{y}^{(i)}\right)} {\partial \theta_{i}}
$$


이 때 분자는 가중치 $\theta_i$에 대해 미분할 수 없기 때문에 아래와 같이 `Chain Rule` 을 사용해서 Gradiant를 도출한다.

$$
\frac{\partial J(\theta)}{\partial \theta_{i}} =\frac{\partial J(\theta)}{\partial z_{2}} \times \frac{\partial z_{2}}{\partial s_{2}} \times \frac{\partial s_{2}}{\partial \theta_{i}}
$$

**chain rule(연쇄법칙)**
chain rule은 합성함수의 미분규칙이며 역전파과정에서 Gradiant를 도출할 때 사용된다.

기본적으로 바깥함수의 도함수에 안쪽함수를 인자로 넣어주고 안쪽함수의 도함수를 곱해주면 된다.

![](https://i.imgur.com/4eSVZW0.png)

<center><b>그림 3. Chain Rule 예시</b></center>

**가중치 업데이트**

도출된 값을 learning rate와 곱해서 기존 가중치에서 빼주면 새로운 가중치는 다음과 같이 나타낼 수 있다.

$$
\theta_{j}=\theta_{j}-\eta \frac{\partial}{\partial \theta_{j}} J(\theta)
$$

**결국 순전파와 역전파를 통해 가중치와 편향을 훈련데이터에 적응하도록 조정하는 과정이  기계학습에서의 `학습`이라는 것을 알 수 있다.**

### 신경망 학습 알고리즘 절차 정리

퍼셉트론과 역전파 알고리즘에 대한 이해를 바탕으로 지금까지의 절차를 아래와 같이 정리할 수 있다.

1. 학습할 신경망 구조를 선택
   
   - 입력층 유닛의 수 = Feature 수 (input layer)
   - 출력층 유닛의 수 = target class 수 (output layer)
   - 은닉층 수, 각 은닉층의 노드 수 (hidden layer)
     - hyperparameter의 영역이다. 
     - sqrt(input layer 수 * output layer 수 ) 로 구해줄 수 있지만 방식이 정해진 것은 아니다.

2. 가중치 초기화

3. 순방향 전파를 통해 $h_{\theta}(x^{(i)})$(출력층 y값) 을 모든 입력 $x^{(i)}$에 대해 계산
   
   - 입력벡터와 가중치벡터의 내적을 산출 
     비용함수 $J(\theta)$를 계산

4. 역방향 전파를 통해 편미분 값들 $\frac{\delta}{\delta\theta_{jk}^{l}}{J(\theta)}$ 을 계산

5. optimizer를 통해 loss function을 최소화

6. 어떤 중지 기준을 충족하거나 비용함수를 최소화 할 때까지 단계 2-5를 반복한다.
   
   - 한번 학습할때의 sample의 size 를 `batch` 라고 한다.
   - 전체 sample에 대해 2-5 의 과정을 반복한 것을 `epoch`라고 한다.
   - `iteration`은 batch 기준으로 학습의 횟수를 카운팅 한 것이다. 100개의 sample의 batch가 50이고 epoch를 50으로 할 경우 전체 iteration의 수는 100이 된다.

### 머신러닝에서의 학습(매우 중요)

미분은 순간의 변화율을 구하는 것이다.
**역전파는 모형에서 계산한 예측값과 실제값의 차이를 바탕으로 미분을 통해 가중치를 보정하는 것을 최대한 반복해서 수행하는 것이다.** 
구체적으로는 손실함수의 국소적 미분값(local deravitive)를 구해서 학습률과 곱한 값을 기존 가중치에서 빼주는 것을 손실함수가 최소가 될 때까지 반복하는 것이다.
`손실함수의 각 피처에 대한 편미분을 벡터로 묶은 것을 그래디언트(Gradient)라고 부른다.`
결국 역전파는 Gradiant를 조정하는 것을 반복하는 것이라고 볼 수 있다.
결국 순전파와 역전파를 통해 가중치와 편향을 훈련데이터에 적응하도록 조정하는 과정이  기계학습에서의 `학습`이라는 것을 알 수 있다.

**ref**

- https://towardsdatascience.com/understanding-backpropagation-algorithm-7bb3aa2f95fd
- https://edgeaiguru.com/Feedforward-and-Backpropagation

## Pytorch

가능한 파이토치 기반으로 구현하고자 한다.



### Pytorch 소개

### pytorch 구성

- `torch`: 메인 네임스페이스, 텐서 등의 다양한 수학 함수가 포함
- `torch.autograd`: 자동 미분 기능을 제공하는 라이브러리
- `torch.nn`: 신경망 구축을 위한 데이터 구조나 레이어 등의 라이브러리
- `torch.multiprocessing`: 병럴처리 기능을 제공하는 라이브러리
- `torch.optim`: SGD(Stochastic Gradient Descent)를 중심으로 한 파라미터 최적화 알고리즘 제공
- `torch.utils`: 데이터 조작 등 유틸리티 기능 제공
- `torch.onnx`: ONNX(Open Neural Network Exchange), 서로 다른 프레임워크 간의 모델을 공유할 때 사용



### Tensor



![](https://www.tensorflow.org/static/guide/images/tensor/reshape-before.png)

- 데이터 표현을 위한 기본 구조로 텐서(tensor)를 사용

- 텐서는 데이터를 담기위한 컨테이너(container)로서  부동소수점 데이터를 저장
- 텐서는 다차원에 대한 일종의 표현방법이다. 
- 기본적으로 `torch.tensor` 함수를 사용해 작성
- GPU사용 연산 가속 가능
- 1d tensor는 vector라고 한다
- 2d tensor는 matrix라고 한다

#### shape , rank, size, axes

- shape :  `(2,3)` 처럼 각 차원의 원소들의 개수를 나타낸 것이다.
- rank :  텐서가 가진 차원의 수. ex) shape이 (1,3,3,3) 인 텐서의 rank는 4이다.
- size :  각 차원의 원소들의 개수를 size라 한다.
- axe :  텐서의 차원들중 특정 하나의 차원을 axe라 한다.

### 텐서 조작하기

#### linspace()
- `torch.linespace(start,end,step)` : numpy

#### view()
> 원소의 수를 유지하면서 텐서의 크기를 변경한다

- 기본적으로 변경전과 변경 후의 텐서 안의 원소의개수가 유지된다.
- size가 -1로 설정된 차원에 대해서는 다른 차원으로부터 해당 값을 유추한다.

#### inplace

> 기존의 값을 덮어쓰는 inplace 연산을 수행한다.



#### type casting

> 자료형을 변환한다



#### concat 

> 두 텐서를 연결한다.



#### stack



#### squeeze()

>  원소의 개수가 1인 차원을 없앤다.

#### unsqueeze()

> 원소의 개수가 1인 차원을 특정 위치에 추가한다



## Pytorch 기초 사용법



```python
nums = torch.arange(9)
```



## Autograd



> pytorch에서 제공하는 autograd에 대해 알아본다.

- toby autograd 참





다층퍼셉트론 구현

**ref**

- [Python Machine Learning](https://github.com/rasbt/python-machine-learning-book-3rd-edition)

