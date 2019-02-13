from sklearn.metrics import roc_curve       #导入ROC曲线函数
from keras.models import load_model
import pandas as pd
import divide
from sklearn.externals import joblib
import matplotlib.pyplot as plt

data_file = 'data/model.xls'
data = pd.read_excel(data_file)
# 划分顺训练集和测试集
_,test = divide.divide_data(data)

net = load_model('model/net.model')
net_predict_result = net.predict(test[:,:3]).reshape(len(test))
lm_fpr,lm_tpr,lm_thresholds = roc_curve(test[:,3],net_predict_result,pos_label=1)

tree = joblib.load('model/tree.pkl')
tree_predict_result = tree.predict_proba(test[:,:3])[:,1]

t_fpr,t_tpr,t_thresholds = roc_curve(test[:,3],tree_predict_result,pos_label=1)

plt.figure(1)
plt.subplot(121)
plt.plot(lm_fpr,lm_tpr,linewidth=2,label='ROC of LM')       # 做ROC曲线
plt.xlabel('False Positive Rate')   # 坐标轴标签
plt.ylabel('True Positive Rate')    # 坐标轴标签
plt.ylim(0,1.05)    # 边界范围
plt.xlim(0,1.05)    # 边界范围
plt.legend(loc=4)   # 图例

plt.subplot(122)
plt.plot(t_fpr,t_tpr,linewidth=2,label='ROC of CART')       # 做ROC曲线
plt.xlabel('False Positive Rate')   # 坐标轴标签
plt.ylabel('True Positive Rate')    # 坐标轴标签
plt.ylim(0,1.05)    # 边界范围
plt.xlim(0,1.05)    # 边界范围
plt.legend(loc=4)   # 图例

plt.show()
