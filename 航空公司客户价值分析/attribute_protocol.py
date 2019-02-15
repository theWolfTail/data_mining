import pandas as pd
import datetime
from datetime import timedelta

datafile = 'data/data_cleaned.xls'
outputfile = 'data/data_protocoled.xls'

data = pd.read_excel(datafile)
data = data[['FFP_DATE','LOAD_TIME','FLIGHT_COUNT','avg_discount','SEG_KM_SUM','LAST_TO_END']]


# 将FFP_DATE和LOAD_TIME转换成datetime格式
data['FFP_DATE'] = pd.to_datetime(data['FFP_DATE'],format='%Y-%m-%d %H:%M:%S')
data['LOAD_TIME'] = pd.to_datetime(data['LOAD_TIME'],format='%Y-%m-%d %H:%M:%S')
print(data.info())

# data.to_excel(outputfile)

