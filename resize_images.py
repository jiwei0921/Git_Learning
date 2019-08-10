# coding=utf-8
# 批量修改图片尺寸
# imageResize(r"D:\tmp", r"D:\tmp\3", 0.7)

from PIL import Image
import os


def imageResize(input_path, output_path, scale):
    # 获取输入文件夹中的所有文件/夹，并改变工作空间
    files = os.listdir(input_path)
    os.chdir(input_path)    #更改为当前路径Input_path
    # 判断输出文件夹是否存在，不存在则创建
    if (not os.path.exists(output_path)):
        os.makedirs(output_path)
    for file in files:
        # 判断是否为文件，文件夹不操作
        if (os.path.isfile(file)):
            img = Image.open(file)
            # width = int(img.size[0] * scale)
            # height = int(img.size[1] * scale)
            width = 256
            height = 256
            img = img.resize((width, height), Image.ANTIALIAS)
            img.save(os.path.join(output_path, file))
    return 0

imageResize('/Users/muscle/Desktop/SIP/test_images','/Users/muscle/Desktop/SIP/test_images',0)


