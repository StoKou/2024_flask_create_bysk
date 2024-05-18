import scipy.io
import json
import numpy as np

# 指定.mat文件的路径
img_path = 'E:\\pycharm\\demo\\my\\data\\SEED_process\\1_20131027\\de_LDS1_Split\\de_LDS1_0.mat'

def read_mat_to_json(mat_file_path):
    try:
        # 读取.mat文件
        mat_data = scipy.io.loadmat(mat_file_path)
        
        # 将.mat文件中的数据转换为JSON格式
        # 假设.mat文件中只有一个变量，我们将其转换为列表
        # mat_data.values() 获取所有值的列表
        # 我们假设只有一个值，取第一个值
        for value in mat_data.values():
            if isinstance(value, np.ndarray) and value.shape[0] == 1:
                # 将一维NumPy数组的值添加到Python列表中
                value_list = value.flatten().tolist()
                # 将列表转换为JSON格式
                json_data = json.dumps(value_list)
                return json_data
        return None
    except Exception as e:
        return str(e)

# 调用函数并打印结果
result = read_mat_to_json(img_path)
print(result)