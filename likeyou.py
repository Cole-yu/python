#! /usr/bin/env python
# -*- coding: utf-8 -*-
#python3.65下是小写的tkinter，不是大写的Tkinter
import tkinter
import random

def center_window(w = 500, h = 300):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)    
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))

def ran(self):
	wx=800-btnUnlike['width']*14
	wy=600-btnUnlike['height']*18
	plx=random.randint(0,wx)
	ply=random.randint(0,wy)	
	btnUnlike.place(x=plx,y=ply)

root = tkinter.Tk(className='小哥哥喜欢我吗？')
center_window(800, 600)

label= tkinter.Label(root,text="小哥哥，你喜欢我吗？",font=("Microsoft YaHei",16),width=30,height=2)
label.place(x=220,y=100)

btnlike=tkinter.Button(root,text="喜欢",bg='pink',font=("Microsoft YaHei",14),width=5,height=1,)
btnlike.place(x=200,y=250)

btnUnlike=tkinter.Button(root,text="不喜欢",bg='blue',font=("Microsoft YaHei",14),width=6,height=1,fg='white')
btnUnlike.place(x=550,y=250)

# 鼠标移入不喜欢时随机跳走
btnUnlike.bind("<Enter>",ran)

def formlike(self):	
	like=tkinter.Toplevel()
	like.title('爱你呦')	
	like.geometry('450x300')
	liketext=tkinter.Label(like,text="我也喜欢你！真是太开心了(*^▽^*)！",font=("Microsoft YaHei",14),width=28,height=1)
	liketext.place(x=53,y=80)
	btnlike=tkinter.Button(like,text="爱你呦",font=("Microsoft YaHei",14),width=7,height=1,bg='pink')
	btnlike.place(x=270,y=180)
	def likeclose(self):
		like.destroy()
	btnlike.bind("<Button-1>",likeclose)

# “喜欢”点击事件，打开弹窗
btnlike.bind("<Button-1>",formlike)


def formUnlike(self):	
	unlike=tkinter.Toplevel()
	unlike.title('惊讶')	
	unlike.geometry('450x300')
	unliketext=tkinter.Label(unlike,text="真佩服你的手速！你是唯一的Σ(°△°|||)！",font=("Microsoft YaHei",14),width=32,height=1)
	unliketext.place(x=53,y=80)
	btnunlike=tkinter.Button(unlike,text="注孤生去吧",font=("Microsoft YaHei",14),width=10,height=1,bg='blue',fg='white')
	btnunlike.place(x=270,y=180)
	def unlikeclose(self):
		unlike.destroy()
	btnunlike.bind("<Button-1>",unlikeclose)

# “不喜欢”点击事件
btnUnlike.bind("<Button-1>",formUnlike)

root.mainloop()