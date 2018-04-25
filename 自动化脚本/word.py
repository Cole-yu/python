#! /usr/bin/env python

#读取docx中的文本代码示例
import docx
from selenium import webdriver
import os
import time

#获取文档对象
file=docx.Document("D:\\desktop\\python.docx")
print("段落数:"+str(len(file.paragraphs)))#段落数为13，每个回车隔离一段

#输出每一段的内容
for para in file.paragraphs:
    print(para.text)

#输出段落编号及段落内容
for i in range(len(file.paragraphs)):
    print("第"+str(i)+"段的内容是："+file.paragraphs[i].text)

txt=file.paragraphs[i].text
print(txt)

url="http://win.gupiaotech.com/wap2/xbzg0424/index.html"

driver = webdriver.Chrome() #模拟打开浏览器
driver.implicitly_wait(20)  
driver.get(url)
driver.find_element_by_id("stock")
driver.find_element_by_id("stock").send_keys("600120")
driver.find_element_by_class_name("btn").click()
# time.sleep(10)
driver.find_element_by_class_name("close").click()
# driver.quit()
