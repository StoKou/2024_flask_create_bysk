import os
#设置当前的目录结构，方便文件调用
os.chdir('E:/VsCode\Vue3/vue0323/backend/')
# 定义要检查的路径
path = 'app/Data/Model_1/'

# 检查路径是否存在
if os.path.exists(path):
    print(f"路径 '{path}' 存在。")
    # 检查它是一个文件还是一个目录
    if os.path.isfile(path):
        print(f" '{path}' 是一个文件。")
    elif os.path.isdir(path):
        print(f" '{path}' 是一个目录。")
    else:
        print(f" '{path}' 是一个不同的类型。")
else:
    print(f"路径 '{path}' 不存在。")
