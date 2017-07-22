#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年6月29日
Email: weipeng@sinashow.com
@author: Redheat

'''
from Tkinter import *
def resize(ev=None):
    Label.config(font='Helvetica -%d bold' % Scale.get())
    
top = Tk()
top.geometry('250 X 150')

label = Label(top,text='hello world',font='Helvetica -12 bold')
label.pack(fill=Y,expand=1)

scale = Scale(top,from_=10,to=40,orient=HORIZONTAL,command=resize)
scale.set(12)
scale.pack(fill=X,expand=1)

quit = Button(top,text="QUIT",command=top.quit,activeforeground='white',activebackground='red')
quit.pack()
mainloop() 