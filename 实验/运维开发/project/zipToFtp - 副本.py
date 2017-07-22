#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2016年7月22日
Email: weipeng@sinashow.com
@author: Redheat

'''
import zipfile,sys,glob,os,shutil
from macpath import split
##########conf##########
pwd_jpg='/data0/web_root/admin.vqj.9bak.com/www/financing/extensions/weibopay/py/'
######################
if len(sys.argv) == 3:
    jpgpath=sys.argv[1] #图片路径
    print jpgpath
    zipfilename = sys.argv[2] #压缩后的文件名
    if jpgpath[-1] != '/':
        jpgpath += '/'
else:
    print '''
    Usage: python zipToFtp.py path zipfilename.
    Example: python zipToFtp.py /home/jpg/ zipfile.zip
    '''
    sys.exit()
#文件列表
def createFileList():
    os.chdir=jpgpath
    jpgfilelist = []
    for rt, dirs, files in os.walk(jpgpath):
        for f in files:
            if f.split('.')[-1] == 'jpg':
                jpgfilelist.append(f)
        break
    if len(jpgfilelist) != 0:
        jpgfile=' '.join(jpgfilelist)
        print "jpg file list: %s" % jpgfile
        return jpgfilelist
    else:
        print "can not find jpg file!"
        sys.exit('program exit!')
#复制需要压缩的文件
def copyJpgFile(jpgfilelist):
    now_path=pwd_jpg
    faildfile = []
    for j in jpgfilelist:
        try:
            shutil.copyfile(jpgpath+j,now_path+'/'+j)
        except Exception,e:
            faildfile.append(j)
            print "Error! %s:%s. move %s to %s faild!" %  (Exception,e,j,now_path)
        else:
            print "move %s to %s success!" % (j,now_path)
    return list(set(jpgfilelist).difference(set(faildfile)))
#压缩文件
def zipFile(filenamelist):
    if os.path.exists(pwd_jpg+zipfilename):
        try:
            print "%s is exist,remove it!" % zipfilename
            os.remove(pwd_jpg+zipfilename)
        except Exception,e:
            print "Error! %s:%s. remove file faild!" %  (Exception,e)
        else:
            print "%s remove success!" % zipfilename
    try:    
        z = zipfile.ZipFile(pwd_jpg+zipfilename, 'w')
        for filename in filenamelist:
            z.write(pwd_jpg+filename,zipfilename+'/'+filename)
            os.remove(pwd_jpg+filename)
    except Exception,e:
        print "Error! %s:%s. zip file faild!" %  (Exception,e)
        sys.exit()
    else:
        z.close()
        print "zip file success!"
#主函数
def main():
    filenamelist = createFileList()
    cpfile = copyJpgFile(filenamelist)
    zipFile(cpfile)
#开始
main()
        
