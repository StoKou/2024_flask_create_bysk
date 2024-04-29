import joblib
import numpy as np
import scipy.io as sio

# 加载SVM模型
model_path = './app/Model/svm_model.pkl'
svm_model = joblib.load(model_path)

# 加载.mat文件
data_path = './app/Data/1_20131027.mat'
mat_contents = sio.loadmat(data_path)

# 初始化累加数组，大小为 (62, 0)，用于存放累加后的数据
summed_features = np.zeros((62, 0))

# 遍历所有的子表
for i in range(1, 16):  # 从1到15
    table_name = f'de_LDS{i}'
    # 检查子表是否存在
    if table_name in mat_contents:
        features_last_col = mat_contents[table_name][:, :, -1]  # 提取最后一列特征
        summed_features = np.hstack((summed_features, features_last_col))  # 水平堆叠所有子表的最后一列特征
    
summed_features=np.array(summed_features).reshape(-1, 1)
# 使用SVM模型进行预测
prediction = svm_model.predict(summed_features)#(输入特征为（62*K）)

print("预测结果：", prediction)