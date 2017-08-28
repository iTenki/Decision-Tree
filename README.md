决策树 (Decision Tree)
=====================
___
基于信息增益的特征选取是一种广泛使用在决策树(decision tree)分类算法中用到的特征选取。该特征选择的方法是通过计算每个特征值划分数据集获得信息增益，通过比较信息增益的大小选取合适的特征值。<br>
___
# 一、定义
## 1.1 熵

　　信息的期望值，可理解为数据集的无序度，熵的值越大，表示数据越无序，公式如下：<br>
　　　　　　熵的计算公式 : ![熵的计算公式][https://upload.wikimedia.org/math/d/b/7/db72f4463b48f5eb522c5bb92cae5028.png]<br>
　　其中H表示该数据集的熵值， pi表示类别i的概率， 若所有数据集只有一个类别，那么pi=1，H=0。因此H=0为熵的最小值，表示该数据集完全有序。<br>

　　熵的减少或者是数据无序度的减少。<br> 　
___

# 二、流程
## 1、计算原始数据的信息熵H1
## 2、选取一个特征，根据特征值对数据进行分类，再对每个类别分别计算信息熵，按比例求和，得出这种划分方式的信息熵H2
## 3、计算信息增益：
　　infoGain = H1 - H2
## 4、根据2，3计算所有特征属性对应的信息增益，保留信息增益较大的特征属性。

---

# 三、实例
**海洋生物数据**<br>
被分类项\特征  |  不浮出水面是否可以生存 | 是否有脚蹼 |  是否鱼类  |
------------ | -------------------| --------- |--------- |

## 3.1 原始数据信息熵
p(是鱼类) = p1 =0.4 <br>
p(非鱼类) = p2 =0.6 <br>
通过信息熵公式可得原始数据信息熵 H1 = 0.97095

## 3.2 根据特征分类计算信息熵
选择’不服出水面是否可以生存’作为分析的特征属性 <br>
可将数据集分为[1,2,3]与[4,5]，分别占0.6和0.4。<br>
[1,2,3]可计算该类数据信息熵为 h1=0.918295834054 <br>
[4,5] 可计算该类数据信息熵为 h2=0 <br>
计算划分后的信息熵 H2 = 0.6 \* h1 + 0.4 \* h2 = 0.550977500433

## 3.3 计算信息增益
infoGain\_0 = H1-H2 = 0.419973094022

## 3.4 特征选择
同理可得对特征’是否有脚蹼’该特征计算信息增益 infoGain\_1 = 0.170950594455 <br>
比较可得，’不服出水面是否可以生存’所得的信息增益更大，因此在该实例中，该特征是最好用于划分数据集的特征<br>

---

[image-1]:	https://upload.wikimedia.org/math/d/b/7/db72f4463b48f5eb522c5bb92cae5028.png