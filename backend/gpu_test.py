import torch
import torch.nn as nn

# 检查CUDA是否可用
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 创建一个简单的卷积神经网络模型
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv = nn.Conv2d(1, 32, kernel_size=5, stride=1, padding=2)

    def forward(self, x):
        x = self.conv(x)
        return x

# 实例化模型并将其移动到GPU（如果可用）
model = SimpleCNN().to(device)

# 创建一个假的输入数据，batch_size=1, channels=1, height=28, width=28
input_tensor = torch.randn(1, 1, 28, 28).to(device)

# 尝试进行前向传播
try:
    output = model(input_tensor)
    print("Convolution ran successfully.")
    print(device)
except RuntimeError as e:
    print("RuntimeError occurred:", e)