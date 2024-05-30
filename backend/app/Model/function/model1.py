import joblib
import numpy as np
import scipy.io as sio
from werkzeug.utils import secure_filename
import os
import random
#设置当前的目录结构，方便文件调用
os.chdir('E:/VsCode\Vue3/vue0323/backend/')
# 加载SVM模型
model_path = './app/Model/svm_model.pkl'
svm_model = joblib.load(model_path)

# 定义允许的文件扩展名
ALLOWED_EXTENSIONS = {'mat'}

# 检查文件扩展名的函数
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 封装处理和预测的逻辑
def process_model_1(file):
    # if file and allowed_file(file.filename):
    #     try:
    #         # 临时保存文件
    #         filename = secure_filename(file.filename)
    #         file_path = f"app/Data/Model_1/{filename}"
    #         file.save(file_path)

    #         # 加载.mat文件并进行预测
    #         mat_contents = sio.loadmat(file_path)
    #         summed_features = np.zeros((62, 0))
    #         for i in range(1, 16):
    #             table_name = f'de_LDS{i}'
    #             if table_name in mat_contents:
    #                 features_last_col = mat_contents[table_name][:, :, -1]
    #                 summed_features = np.hstack((summed_features, features_last_col))
            
    #         summed_features = np.array(summed_features).reshape(-1, 1)
    #         prediction = svm_model.predict(summed_features)

    #         # 删除临时文件
    #         os.remove(file_path)

    #         # 返回预测结果
    #         return {'prediction': prediction.tolist()}
    #     except Exception as e:
    #         return {'error': str(e)}
    # else:
    #     return {'error': 'must be mat file'}
    # 模拟返回一个随机数字
    return random.randint(0, 2)