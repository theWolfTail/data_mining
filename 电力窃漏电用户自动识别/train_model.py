import pandas as pd
import divide
import lm_model
import dt_model

data_file = 'data/model.xls'
data = pd.read_excel(data_file)
# 划分顺训练集和测试集
train,test = divide.divide_data(data)
# 构造LM神经网络模型
lm,result1 = lm_model.lm(train)
# 构造决策树模型
tree,result2 = dt_model.tree(train)