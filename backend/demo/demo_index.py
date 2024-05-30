import os
#设置当前的目录结构，方便文件调用
os.chdir('E:/VsCode\Vue3/vue0323/backend/')
def export_directory_structure(path, output_file):
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(path):
            level = root.replace(path, '').count(os.sep)
            indent = ' ' * 4 * level
            f.write(f'{indent}{os.path.basename(root)}/\n')
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                f.write(f'{subindent}{file}\n')

# 设置当前目录和输出文件名
current_directory = '.'
output_filename = 'directory_structure.txt'

# 导出目录结构
export_directory_structure(current_directory, output_filename)

print(f"目录结构已导出到 '{output_filename}' 文件中。")
