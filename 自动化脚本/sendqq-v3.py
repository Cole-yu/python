#!/usr/bin/env python
# 原理是先将需要发送的文本放到剪贴板中，然后将剪贴板内容发送到qq窗口
# 之后模拟按键发送enter键发送消息

import win32gui
import win32con  
import win32clipboard as w
import os
from PIL import Image
import numpy as np
from ctypes import *
import time,datetime

#利用os模块打开QQ
# os.startfile("C:/Program Files (x86)/Tencent/QQ/Bin/QQ.exe")

def getText():
    """获取剪贴板文本"""
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_UNICODETEXT)
    w.CloseClipboard()
    return d

def setText(aString):
    """设置剪贴板文本"""
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()


def setImg(imgFile):
    """设置剪贴板图片"""
    im=Image.open("D:\\tmp\\picture\\"+imgFile)
    im.save('D:\\tmp\\pic_bmp\\send_pic.bmp')
    aString = windll.user32.LoadImageW(0, r"D:\\tmp\\pic_bmp\\send_pic.bmp", win32con.IMAGE_BITMAP, 0, 0, win32con.LR_LOADFROMFILE)
    # im.show()
    # print(aString)
    if aString != 0:  ## 由于图片编码问题  图片载入失败的话  aString 就等于0  
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_BITMAP, aString)
        w.CloseClipboard()


#发送图片
def send_img(to_who, imgFile):
    """发送qq消息
    to_who：qq消息接收人
    imgFile：需要发送的消息"""
    # 将图片写到剪贴板
    setImg(imgFile)
    qq = win32gui.FindWindow(None, qqQun)
    # 投递剪贴板消息到QQ窗体
    win32gui.SendMessage(qq, 258, 22, 2080193)
    win32gui.SendMessage(qq, 770, 0, 0)
    # 模拟按下回车键
    # win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    # win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


def send_msg(to_who, msg):
    """发送qq消息
    to_who：qq消息接收人
    msg：需要发送的消息
    """
    # 将消息写到剪贴板
    setText(msg)
    # 获取qq窗口句柄
    qq = win32gui.FindWindow(None, to_who)
    # 投递剪贴板消息到QQ窗体
    win32gui.SendMessage(qq, 258, 22, 2080193)
    win32gui.SendMessage(qq, 770, 0, 0)
    # 模拟按下回车键
    win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


current_time=datetime.datetime.now()
# print("current_time",current_time)

close_time = datetime.datetime(2018, 6, 6, 23, 59, 59)
# print("close_time",close_time)



if(current_time < close_time):
    # qqQuns_Name = input('请输入要群发的群名称:') #用户手动输入的方式
    qqQuns_Names = open('D:/tmp/qqQun.txt').read() #导入的形式
    # print(qqQuns_Names) #字符串形式，需要转为列表形式
    to_who=qqQuns_Names.split(',')
    # print(to_who) #列表形式，可进行interable迭代


    #更改文件路径
    path="D:\\tmp\\picture"
    files=os.listdir(path)


    for qqQun in to_who:
        for imgFile in files:
            send_img(qqQun, imgFile)


    # 测试成功
    # msg=input('请输入要发的内容:')
    msg=open('D:/tmp/content.txt').read()
    for qqQun in to_who:
        send_msg(qqQun, msg)



