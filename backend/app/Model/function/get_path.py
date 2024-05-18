
path_images="E:\\pycharm\\demo\\my\\data\\SEED_process\\1_20131027\\de_LDS1_Split\\de_LDS1_0.mat"


def get_path(option=None):
    """
    根据提供的选项返回.mat文件的路径。
    
    参数:
    - option: 一个字符串，指定返回路径的类型。如果为 'images'，则返回 path_images 参数。
    - path_images: 当 option 为 'images' 时，返回此参数的值作为路径。
    
    返回:
    - 根据option参数返回对应的路径。
    """
    if option == 'images':
        return path_images
    else:
        # 默认返回的路径，当option不是'images'或path_images未提供时
        return 