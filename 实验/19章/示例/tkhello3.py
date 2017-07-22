#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年6月29日
Email: weipeng@sinashow.com
@author: Redheat

'''
import Tkinter
top = Tkinter.Tk()

hello = Tkinter.Label(top,text='hello world')
hello.pack()

quit = Tkinter.Button(top,text='QUIT',command = top.quit,bg='black',fg='white')
quit.pack(fill=Tkinter.X,expand=1)

Tkinter.mainloop()