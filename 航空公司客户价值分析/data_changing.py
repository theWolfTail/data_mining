import pandas as pd

datafile = 'data/data_protocoled.xls'
outputfile = 'data/standardization_data.xls'

data = pd.read_excel(datafile,index_col=0)

data['L'] = (data['LOAD_TIME'] - data['FFP_DATE']).map(lambda x :x.days)

# 数据变换
data = data[['L','LAST_TO_END','FLIGHT_COUNT','SEG_KM_SUM','avg_discount']]
data.columns = [u'L[单位：天]','R[单位：月]','F[单位：次]','M[单位：公里]','C[单位：无]']
# print(data)       # 输出变换后的数据

# 标准化处理

data = (data - data.mean(axis = 0))/data.std(axis = 0) # 参数axis=0时是按列取平均值，axis=1时是按行取平均值

data.columns = ['Z'+ i[0] for i in data.columns]
# print(list(data.columns))
data.to_excel(outputfile)