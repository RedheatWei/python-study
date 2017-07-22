# -*- coding: cp936 -*-
#
# ����Show��������Ϣ�ռ�ϵͳ��
# ��    ����2011��08��01��
"""
�ļ�: update.py
����: Pei Wenhao <peiwenhao@sinashow.com>
����: Python
ժҪ:
    ��ģ����������Show��������Ϣ�ռ���װ�ű���
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
    # �趨�͸ı��Ŀ¼
    tarpath = ""
    rootpath = "/data0/monitorsys"
    tarpath = rootpath+"/linuxinstall.tar.gz"
    if os.path.exists(rootpath) == False:
        os.mkdir(rootpath)
    os.chdir(rootpath)
    #���ذ�װ��
    if getconfigfilebyftp('minfo.sinashow.com','showmonitor','linuxshow_#', \
            'machine_monitor','linuxinstall.tar.gz', rootpath) == False:
        sys.exit(1)
    install_unpackage(rootpath, tarpath)
    # �滻�����ļ�
    monitorfile = rootpath+"/conf/monitorconf.txt"
    if os.path.isfile(monitorfile):
        reconfig(monitorfile)
    # �������������crontab�ȹ���
    print "call shell"
    sh = subprocess.Popen(args = "/bin/sh"+" "+rootpath+"/tools/installset.sh",shell=True,stdout=subprocess.PIPE)
    sh.stdout.close()
    sys.exit(0)
