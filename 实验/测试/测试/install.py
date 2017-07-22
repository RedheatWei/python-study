# -*- coding: cp936 -*-
#
# 新浪Show服务器信息收集系统。
# 创    建：2011年08月01日
"""
文件: update.py
作者: Pei Wenhao <peiwenhao@sinashow.com>
语言: Python
摘要:
    本模块用于新浪Show服务器信息收集安装脚本。
"""
########################################################################
#import
########################################################################
import os,sys
import tarfile
import socket
import ftplib,subprocess
import re,random
############## add custom model ###################
########################################################################
#global
########################################################################
rootpath = os.path.abspath(os.path.dirname(sys.argv[0]))
timeout = 10
#in seconds
socket.setdefaulttimeout(timeout)
########################################################################
#function
########################################################################
def getconfigfilebyftp(ip, user, password, path, filename, rootpath):
    try:
        ftp = ftplib.FTP(ip)
        ftp.login(user, password)
        ftp.cwd(path)
        df = 'RETR %s' % filename
        wf = rootpath+"/"+filename
        ftp.retrbinary(df, open(wf, 'wb').write)
        ftp.quit()
        return True
    except:
        print "Get file fail"
        return False
    
def install_unpackage(rootpath, tarpath):
    tar = tarfile.open(tarpath)
    names = tar.getnames()
    for name in names:
        print name
        if name.find(".svn") != -1:
            continue
        tar.extract(name, path = rootpath)
    tar.close()

def reconfig(mfile):
    r = open(mfile)
    afile = r.read()
    num = random.randint(0,60)
    refile = re.sub('cnum',str(num),afile)
    r.close()
    refile1 = open(mfile,'w')
    refile1.write(refile)
    refile1.close()
########################################################################
#main
########################################################################
if __name__ == '__main__' :
    # 设定和改变根目录
    tarpath = ""
    rootpath = "/data0/monitorsys"
    tarpath = rootpath+"/linuxinstall.tar.gz"
    if os.path.exists(rootpath) == False:
        os.mkdir(rootpath)
    os.chdir(rootpath)
    #下载安装包
    if getconfigfilebyftp('minfo.sinashow.com','showmonitor','linuxshow_#', \
            'machine_monitor','linuxinstall.tar.gz', rootpath) == False:
        sys.exit(1)
    install_unpackage(rootpath, tarpath)
    # 替换配置文件
    monitorfile = rootpath+"/conf/monitorconf.txt"
    if os.path.isfile(monitorfile):
        reconfig(monitorfile)
    # 设置随机启动和crontab等工作
    print "call shell"
    sh = subprocess.Popen(args = "/bin/sh"+" "+rootpath+"/tools/installset.sh",shell=True,stdout=subprocess.PIPE)
    sh.stdout.close()
    sys.exit(0)
