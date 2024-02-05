"""
文本嵌入层作用： 无论是源文本还是目标文本嵌入，都是为了将文本中词汇的数字表示转换为张量，以便在在词汇中测量距离
"""

import torch.nn as nn
import math
from torch.autograd import Variable


# 实现Embeddings类以实现文本嵌入层
class Embeddings(nn.Module):
    def __init__(self, d_model, vocab):
        super(Embeddings, self).__init__()
        self.lut = nn.Embedding(vocab, d_model)
        self.d_model = d_model

    # 向前传播逻辑，所有层都调用此函数
    def forward(self, x):
        return self.lut(x) * math.sqrt(self.d_model)
