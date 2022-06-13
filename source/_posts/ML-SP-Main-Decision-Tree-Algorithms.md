---
title: '[Tree]주요 Decision Tree 알고리즘'
categories:
  -  Machine Learning
tags:
  - Decision Tree
  - Supervised Learning
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

주요 의사결정트리 알고리즘 4개에 대해 간단히 살펴보자.

---

## Main Decision Tree Algorithms

### **CHAID**

The Chi-squared Automatic Interaction Detection (CHAID) is one of the oldest DT algorithms methods that produces multiway DTs (splits can have more than two branches) suitable for classification and regression tasks. When building Classification Trees (where the dependent variable is categorical in nature), CHAID relies on the Chi-square independence tests to determine the best split at each step. Chi-square tests check if there is a relationship between two variables, and are applied at each stage of the DT to ensure that each branch is significantly associated with a statistically significant predictor of the response variable.
**In other words, it chooses the independent variable that has the strongest interaction with the dependent variable.**

### **CART**
CART is a DT algorithm that produces binary Classification or Regression Trees, depending on whether the dependent (or target) variable is categorical or numeric, respectively. It handles data in its raw form (no preprocessing needed), and can use the same variables more than once in different parts of the same DT, which may uncover complex interdependencies between sets of variables.

**Prepare Data for CART**
- The **splitting of numerical features** can be performed by sorting the features in the ascending order and trying each value as the threshold point and calculating the information gain for each value as the threshold. Finally, if that value obtained is equal to the threshold which gives the maximum I.G value then hurray..!!

- Feature scaling(column standardization) not necessary to perform in decision trees. However, it helps with data visualization/manipulation and might be useful if you intend to compare performance with other data or other methods like SVM.

- In order to handle categorical features in Decision trees, we must never perform one hot encoding on a categorical variable even if the categorical variables are nominal since most of the libraries can handle categorical variables automatically. we can still assign a number for each variable if desired.

- If height or depth of the tree is exactly one then such a tree is called as a decision stump.

- Imbalanced class does have a detrimental impact on the tree’s structure so it can be avoided by either using upsampling or by using downsampling depending upon the dataset.

- Apart from skewed classes, high dimensionality can also have an adverse effect on the structure of the tree if dimensionality is very high that means we have a lot of features which means that to find the splitting criterion on each node it will consume a lot of time.
- Outliers also impact the tree’s structure as the depth increases the chance of outliers in the tree increases.

- Feature importance can be determined by calculating the normalized sum at every level as we have t reduce the entropy and we then select the feature that helps to reduce the entropy by the large margin. so for whichever feature the normalized sum is highest, we can then think of it as the most important feature. similarly, feature which has the second highest normalized sum can be thought of as a second important feature.


### **ID3**

The Iterative Dichotomiser 3 (ID3) is a DT algorithm that is mainly used to produce Classification Trees. Since it hasn’t proved to be so effective building Regression Trees in its raw data, ID3 is mostly used for classification tasks (although some techniques such as building numerical intervals can improve its performance on Regression Trees).

### **C4.5**
C4.5 is the successor of ID3 and represents an improvement in several aspects. C4.5 can handle both continuous and categorical data, making it suitable to generate Regression and Classification Trees. Additionally, it can deal with missing values by ignoring instances that include non-existing data.

Unlike ID3 (which uses Information Gain as splitting criteria), C4.5 uses Gain Ratio for its splitting process. Gain Ratio is a modification of the Information Gain concept that reduces the bias on DTs with huge amount of branches, by taking into account the number and size of the branches when choosing an attribute. Since Information Gain shows an unfair favoritism towards attributes with many outcomes, Gain Ratio corrects this trend by considering the intrinsic information of each split (it basically “normalizes” the Information Gain by using a split information value). This way, the attribute with the maximum Gain Ratio is selected as the splitting attribute.
Additionally, C4.5 includes a technique called windowing, which was originally developed to overcome the memory limitations of earlier computers. Windowing means that the algorithm randomly selects a subset of the training data (called a “window”) and builds a DT from that selection. This DT is then used to classify the remaining training data, and if it performs a correct classification, the DT is finished. Otherwise, all the misclassified data points are added to the windows, and the cycle repeats until every instance in the training set is correctly classified by the current DT. This technique generally results in DTs that are more accurate than those produced by the standard process due to the use of randomization, since it captures all the “rare” instances together with sufficient “ordinary” cases.


## References


- https://towardsdatascience.com/the-complete-guide-to-decision-trees-28a4e3c7be14
