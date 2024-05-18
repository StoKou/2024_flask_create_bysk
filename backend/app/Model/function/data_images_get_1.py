import scipy.io
import numpy as np
import json
def data_images_get_1(mat_file_path):
    """
    读取指定路径下的 .mat 文件，并将数据转换为JSON格式。
    
    参数:
    - mat_file_path: .mat 文件的路径
    
    返回:
    - 如果文件成功读取，返回一个包含数据的JSON格式的字典。
    - 如果发生错误，返回一个包含错误信息的字典。
    """
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
                value_list=value.flatten().tolist()
                sequence_list=list(range(1, len(value_list) + 1))
                # 创建一个二维列表，第一个维度是递增序列，第二个维度是 value_list
                two_dimensional_list={
                    'time':sequence_list,
                    'values':value_list
                }
                # 将列表转换为JSON格式
                json_data=json.dumps(two_dimensional_list)
                return json_data
        return None
    except Exception as e:
        # 如果读取.mat文件时发生错误，返回错误信息
        return {'error': str(e)}