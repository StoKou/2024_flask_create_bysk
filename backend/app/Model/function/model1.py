import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from app.Model.function.utils.tools import build_preprocessed_eeg_dataset_CNN_test, RawEEGDataset_test, subject_independent_data_split_test
from werkzeug.utils import secure_filename
import os
from app.Model.function.CNN import ConvNet
#设置当前的目录结构，方便文件调用
os.chdir('E:/VsCode\Vue3/vue0323/backend/')
# 加载SVM模型
model_path = './app/Model/model.ckpt'

# 定义允许的文件扩展名
ALLOWED_EXTENSIONS = {'mat'}

# 检查文件扩展名的函数
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 封装处理和预测的逻辑
def process_model_1(file):
    if file and allowed_file(file.filename):
        try:
            # 临时保存文件
            filename = secure_filename(file.filename)
            file_path = f"app/Data/Model_1/{filename}"
            # file_path = f"app/Data/Model_1/1_20131027_djc_eeg1.mat"
            file.save(file_path)

            feature_vector_dict = build_preprocessed_eeg_dataset_CNN_test(file_path)
            test_feature = subject_independent_data_split_test(feature_vector_dict)

            desire_shape = [1, 62, 200]
            test_data = RawEEGDataset_test(test_feature, desire_shape)
            # 超参数设置
            device = 'cpu'
            num_classes = 3
            batch_size = 24

            test_data_loader = DataLoader(test_data, batch_size=batch_size, shuffle=True, drop_last=False)
            
            # 加载模型
            
            model = ConvNet(num_classes).to(device)
            model.load_state_dict(torch.load(model_path))
            model.eval()
            results = []  # 初始化一个列表来保存所有的预测结果

            with torch.no_grad():  # 确保不会计算梯度
                for features in test_data_loader:
                    features = features.to(device)  # 将数据移动到相应的设备
                    output = model(features)  # 获取模型的输出
                    _, predicted = torch.max(output.data, 1)  # 获取每个样本的最高概率类别
                    results.extend(predicted.cpu().numpy())  # 将预测结果添加到列表中
            # 初始化一字典来存储每个元素的出现次数
            count_dict = {}

            # 遍历列表，计算每个元素的出现次数
            for item in results:
                if item in count_dict:
                    count_dict[item] += 1
                else:
                    count_dict[item] = 1

            # 找到出现次数最多的元素
            most_common_element = None
            most_common_count = -1
            for item, count in count_dict.items():
                if count > most_common_count:
                    most_common_count = count
                    most_common_element = item
            # 删除临时文件
            os.remove(file_path)

            # 返回预测结果
            return {most_common_element.tolist()}
        except Exception as e:
            return {'error': str(e)}
    else:
        return {'error': 'must be mat file'}