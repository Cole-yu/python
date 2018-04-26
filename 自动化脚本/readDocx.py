#! /usr/bin/env python
import os
import zipfile
import time
from PIL import Image

# path="D:\\desktop"
# os.chdir(path)       				   #首先改变目录到文件的目录
# os.rename('python.docx','python.zip')  #重命名为zip文件

# f=zipfile.ZipFile('python.zip','r')  #进行解压
# for file in f.namelist():
#     f.extract(file)
# time.sleep(3)

path="D:\\desktop\\word\\media"
os.chdir(path)    

im = Image.open('image1.png')
im.show()


#file=open('D:\desktop\word\media\image1.jpeg','rb').read() #进入文件路径，读取二进制文件
# for f in file:
#     print(f)