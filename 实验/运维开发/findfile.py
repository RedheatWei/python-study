#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''寻找相同名称文件'''
import os
class FindSameFile(object):
    def __init__(self,filename,startpath=None,endpath=None):
        self.filename = filename
        self.endpath = endpath
        self.startpath = startpath if startpath!=None else os.getcwd()
        self.local_path = os.path.expanduser('~')
        if self.local_path not in self.startpath:
            exit('当前目录不在用户目录下！')
    def findFile(self):
        num = 0
        for parent, dirname, filenames in os.walk(self.startpath):
            if self.filename in filenames:
                num += 1
                print "于%s发现了第%d个名为%s的文件！" % (parent, num, self.filename)
            if num >=2:
                exit("发现了至少2个文件，程序退出！")
            if os.path.expanduser('~') == self.startpath:
                exit('程序执行结束！')
        if num == 0:
            FindSameFile(self.filename,os.path.dirname(self.startpath),self.startpath).findFile()

def main(filename):
    findfileobj = FindSameFile(filename)
    findfileobj.findFile()

main('test')