from sklearn.tree import DecisionTreeClassifier # 导入决策树模型

def tree(train,grable=False):
    '''

    :param train: 训练集
    :param grable: 是否输出混淆矩阵，默认为false
    :return: 训练好的模型和预测值
    '''
    treefile = 'model/tree.pkl'
    tree = DecisionTreeClassifier()     # 建立决策树模型
    tree.fit(train[:,:3],train[:,3])    # 训练

    #保存模型
    from sklearn.externals import joblib
    joblib.dump(tree,treefile,compress=3)

    if grable:
        pass
    return tree,tree.predict(train[:,:3])
    # 注意，scikit-learn使用predict方法直接给出预测结果

