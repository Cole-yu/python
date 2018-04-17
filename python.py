#!/usr/bin/env python
#-*- coding:utf-8 -*-

#下载一张图片
# import urllib.request
# abs_url="http://imgsrc.baidu.com/forum/w%3D580/sign=5687e5bf8e01a18bf0eb1247ae2e0761/7859252dd42a2834e9c8559852b5c9ea15cebf33.jpg"
# html=urllib.request.urlopen(abs_url) 
# #print(dir(html))
# #print(html.url)
# #print(html.read())
# f=open("D:\\meinv.jpg","wb")
# print(dir(f))
# f.write(html.read())
# f.close()

import urllib.request
def grab(url):
	headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}
	url=r'http://www.baidu.com/'
	req = urllib.request.Request(url=url,headers=headers)
	# 打开传入的网址
	resp = urllib.request.urlopen(url)
	# 读取网页源码内容
	data = resp.read()
	# 输入存储文件名
	name = input("请定义文件名")
	# 打开文件
	file_name = open(name, "wb")
	# 将代码写入文件
	file_name.write(data)
	# 关闭文件
	file_name.close()

	print("下载源码完成")

if __name__ == '__main__':
	# 按照格式输入网址
	web_addr = input("请输入你要抓取的网址(例如http://www.baidu.com/):")
	try:
		grab(web_addr)
	except:
		print("网址输入有误")