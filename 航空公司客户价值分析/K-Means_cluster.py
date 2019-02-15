import pandas as pd
from sklearn.cluster import KMeans

if __name__ == "__main__":
    data_file = 'data/standardization_data.xls'
    outputfile = 'data/cluster_data.xls'
    k = 5          # 需要进行的聚类类别数
    data = pd.read_excel(data_file,index_col=0)
    # 调用kmeans算法，进行聚类分析
    kmodel = KMeans(n_clusters=k,n_jobs=4)      # n_jobs是并行数，一般等于CPU数较好
    kmodel.fit(data)

    # print('聚类中心')
    # print(kmodel.cluster_centers_)
    # print('各样本对应的类别')
    # print(kmodel.labels_)

    # 简单打印结果
    r1 = pd.Series(kmodel.labels_).value_counts()   # 统计各类别的数目
    r2 = pd.DataFrame(kmodel.cluster_centers_)  # 找出聚类中心
    r = pd.concat([r2,r1],axis=1)   # 横向连接
    r.columns = list(data.columns)+[u'类别数目']    # 重命名表头
    r.to_excel(outputfile)