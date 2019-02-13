from keras.models import Sequential
from keras.layers.core import Dense,Activation

def lm(train,grable=False):
    '''
    :param train: 训练集
    :param test: 测试集
    :param grabel 是否输出混淆矩阵，默认为false
    :return: 返回训练好的模型和预测的分类
    '''
    netfile = 'model/net.model'
    net = Sequential()      # 创建lm神经网络
    net.add(Dense(input_dim=3,units=10))    # 添加输入层（3节点）到隐藏层（10节点）的连接
    net.add(Activation('relu')) # 隐藏层使用relu激活函数
    net.add(Dense(input_dim=10,units=1))    # 添加隐藏层（10节点）到输出层（1节点）的连接
    net.add(Activation('sigmoid'))  # 输出层使用sigmoid激活函数
    net.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
    # 编译模型，使用adam优化方法
    net.fit(train[:,:3],train[:,3],nb_epoch=1000,batch_size=1)  # 训练模型，循环1000次，batch大小为1
    net.save(netfile)   # 保存模型

    predict_result = net.predict_classes(train[:,:3]).reshape(len(train))   # 预测结果变形
    '''
    这里要提醒的是，keras用predict给出预测概率，predict_classes才是给出预测类型，
    而且两者的预测结果都是n*1为数组，而不是通常的1*n维数组
    '''
    # 输出混淆矩阵
    if grable:
        pass
    return net,predict_result
