import pandas as pd

data_file = 'data/missing_data.xls'
data = pd.read_excel(data_file,header=None)
a_data = data.iloc[:,[0]]    # 用户A的用电量
b_data = data.iloc[:,[1]]    # 用户B的用电量
c_data = data.iloc[:,[2]]    # 用户C的用电量


# 用户用电量的统计量
a_statistic = a_data.describe()
a_statistic.loc['missing_data_num'] = len(a_data)-a_statistic.loc['count']
b_statistic = b_data.describe()

b_statistic.loc['missing_data_num'] = len(b_data)-b_statistic.loc['count']
c_statistic = c_data.describe()

c_statistic.loc['missing_data_num'] = len(c_data)-c_statistic.loc['count']
print("用户A的统计量")
print(a_statistic)
print("----------------------")
print("用户B的统计量")
print(b_statistic)
print("----------------------")
print("用户C的统计量")
print(c_statistic)
print("----------------------")


# 三个用户的用电量折线图
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



