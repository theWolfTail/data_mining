import pandas as pd
from scipy.interpolate import lagrange

data_file = 'data/missing_data.xls'
output_file = 'data/missing_data_processed.xls'

data = pd.read_excel(data_file,header=None)

def ployinterp_column(s,n,k=5):
    '''
    自定义列向量插值函数
    :param s: 列向量
    :param n: 被插值的位置
    :param k: 取前后数据的个数
    :return:
    '''
    y = s[list(range(n-k,n)) + list(range(n+1,n+1+k))]      # 被插值的前K个数据和后K个数据，不包括缺失值
    y = y[y.notnull()]   # 剔除空值
    return lagrange(y.index,list(y))(n)

# 逐个元素判断是否需要插值


for i in data.columns:
   # 循环每一列
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            data[i][j] = ployinterp_column(data[i],j)

# data.to_excel(output_file,header=None,index=False)


# 插值后三个用户的用电量折线图
a_data = data.iloc[:,[0]]
b_data = data.iloc[:,[1]]
c_data = data.iloc[:,[2]]

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


plt.figure(1)
plt.subplot(311)
plt.xlabel(u'工作日')
plt.ylabel(u'用户A用电量')
plt.plot(a_data.index,a_data,'b-')
plt.subplot(312)
plt.xlabel(u'工作日')
plt.ylabel(u'用户B用电量')
plt.plot(b_data.index,b_data,'r-')
plt.subplot(313)
plt.xlabel(u'工作日')
plt.ylabel(u'用户C用电量')
plt.plot(c_data.index,c_data,'y-')
plt.show()