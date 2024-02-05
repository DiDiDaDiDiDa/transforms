# transforms
解读transforms和代码实现


![images\img.png](images/img.png)

- transforms总架构分为四个部分

  - 输入部分

  - 输出部分

  - 编码器

  - 解码器

    

![images\总架构.png](images/总架构.png)



- 输入部分

![images\输入部分.png](images/输入部分.png)

- 输出部分

  ![images\输出部分.png](images/输出部分.png)

  添加线性层将上一步的输出向量（例如，词嵌入）映射到一个新的向量空间，添加softmax将线性层的输出转换成概率分布，提取出概率最大的值。

  总的来说，Linear层负责将输入数据映射到新的特征空间，而Softmax层则将这个映射转换成概率分布，使得模型可以以概率的形式表达其预测结果。

- 编码器

![images\编码器.png](images/编码器.png)


- 解码器

![images\解码器.png](images/解码器.png)
