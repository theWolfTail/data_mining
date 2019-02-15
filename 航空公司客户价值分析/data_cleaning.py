import pandas as pd

datafile = 'data/air_data1.csv'
outputfile = 'data/data_cleaned.xls'

data = pd.read_csv(datafile,encoding='utf-8')

# 票价为非空值才保留
data = data[data['SUM_YR_1'].notnull()&data['SUM_YR_2'].notnull()]

# 只保留票叫非零的，或者平均折扣价与总飞行公里数同时为0的记录
index1 = data['SUM_YR_1'] != 0
index2 = data['SUM_YR_2'] != 0
index3 = (data['avg_discount'] == 0) &(data['SEG_KM_SUM'] == 0)

data = data[index1 | index2 | index3]

data.to_excel(outputfile)