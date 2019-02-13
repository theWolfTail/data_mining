from random import shuffle
def divide_data(x):
    '''
    把数据分为训练集和测试集
    :param x: 原始数据
    :return: 返回训练集和测试集
    '''
    x = x.as_matrix()    # 将表格转换为矩阵
    shuffle(x)  # 打乱数据
    p = 0.8     # 训练集的占比
    train = x[:int(len(x)*p),:]
    test = x[int(len(x)*p):,:]
    return train,test