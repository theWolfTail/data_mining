import pandas as pd

data_file = 'data/air_data1.csv'
output_file = 'data/air_explore.xls'

data = pd.read_csv(data_file,encoding='utf-8')      # 读取原始数据，制定UTF-8编码(需要用文本编辑器将数据转换为utf-8棉麻
explore = data.describe(percentiles=[], include='all').T    # 包括对数据的基本描述，percentiles参数是指定计算多少的分位数表（
# 比如1/4分位数，中位数等);T是转置转置后更方便查阅
explore['null'] = len(data)-explore['count']

explore = explore[['null','max','min']]
explore.columns = [u'空值','最大值','最小值']       # 这里只取自动计算出的最大最小值和自己添加的空值

explore.to_excel(output_file)
