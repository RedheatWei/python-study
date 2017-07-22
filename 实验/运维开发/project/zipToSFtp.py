#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2016年7月22日
Email: weipeng@sinashow.com
@author: Redheat

'''
import zipfile,sys,os,shutil,paramiko
##########conf##########
ftp_server='222.73.39.37' #ftp地址
ftp_port=50022
username='200004227922' #ftp用户名
private_key_file='/data0/web_root/admin.vqj.9bak.com/www/financing/extensions/weibopay/newkey/id_rsa'
uploadpath = './upload' #上传文件路径
ftp_reconnect = 3 #ftp失败重连次数
pwd_jpg='/data0/web_root/admin.vqj.9bak.com/www/financing/extensions/weibopay/py/' #脚本所在目录
######################
if len(sys.argv) == 3:
    jpgpath=sys.argv[1] #图片路径
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
            z.write(pwd_jpg+filename,filename)
            os.remove(pwd_jpg+filename)
    except Exception,e:
        print "Error! %s:%s. zip file faild!" %  (Exception,e)
        sys.exit()
    else:
        z.close()
        print "zip file success!"
#连接ftp
def ftpconnect():
    try:
        t=paramiko.Transport(ftp_server,ftp_port)
        private_key = paramiko.RSAKey.from_private_key_file(private_key_file)
        t.connect(username=username,pkey=private_key)
    except Exception,e:
        print "Error! %s:%s. ftp connect faild!" %  (Exception,e)
        return 0
    else:
        print "connect ftp success!"
        return t
#上传文件
def uploadFile(t):
    try: 
        sftp=paramiko.SFTPClient.from_transport(t)
        sftp.put(os.path.join(pwd_jpg,zipfilename),os.path.join(uploadpath,zipfilename))
        t.close() 
    except Exception,e:
        print "Error! %s:%s. upload file faild!" % (Exception,e)
#主函数
def main():
    filenamelist = createFileList()
    cpfile = copyJpgFile(filenamelist)
    for i in range(1,ftp_reconnect+1):
        ftp = ftpconnect()
        if ftp != 0:
            zipFile(cpfile)
            uploadFile(ftp)
            sys.exit()
        else:
            print 'connect ftp faild %s!' % i
#开始
main()
        
