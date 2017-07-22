#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import os,sys,re,datetime,time,json

CHAT_LIST = "/home/maintain/AllChatService/ChatList" #用ChatList来判断编号
SAVE_PATH = "/data0/TT_ratio/" #处理后文件的保存路径
DIFF_SIZE = 0 #文件大小比对，设置为0不进行比对
WAIT_TIME = 60 #等待时间
LOG_LING_FILE = ".log_line.json" #保存读取位置
MAX_RATIO = 5.0 #丢包率大小限制,设置为0为全部收集

# save_day = datetime.datetime.now().strftime("%Y%m%d")
class FileProcessAbout(object):
    '''文件处理类，包含了处理文件所需的函数'''
    def __init__(self):
        self.listfile = CHAT_LIST
        self.new_count_lines = 0
        if not os.path.exists(SAVE_PATH):
            os.makedirs(SAVE_PATH,0755)
        if os.path.exists(SAVE_PATH+LOG_LING_FILE):
            with open(SAVE_PATH+LOG_LING_FILE) as json_file:
                try:
                    self.file_line = json.load(json_file)
                except:
                    self.file_line = {}
                    self.file_line[self._getTime()] = {}
        else:
            self.file_line={}
            self.file_line[self._getTime()]={}
    # 获取当前日期
    def _getTime(self):
        return datetime.datetime.now().strftime("%Y%m%d")
    # 处理不是今天的json行数
    def _delJson(self):
        nowdata = self._getTime()
        for key,value in self.file_line.items():
            if key != nowdata:
                del self.file_line[key]
    # 获取房间id
    def getRoomId(self,logname):
        logname = logname.split('/')[-1]
        return logname.split('_')[1]
    # 读取文件内容
    def openFile(self,logname):
        logcontent = []
        try:
            f = open(logname,'r')
        except Exception:
            pass
        else:
            for i in f.readlines():
                logcontent.append(i)
            f.close()
        return logcontent
    #比对文件大小
    def checkFileSize(self,old_file,new_file):
        deffzise = os.path.getsize(old_file)-os.path.getsize(new_file)
        return abs(deffzise)
    #json方法获取差异内容
    def newContentJson(self,roomid,old_file):
        try:
            linenum = int(self.file_line[self._getTime()][roomid])
        except Exception:
            linenum = 0
        finally:
            return  old_file[linenum:]
    # 获取差异内容
    def newContent(self,old_file,new_file):
        old_file_line = len(old_file)
        new_file_line = len(new_file)
        if old_file_line > new_file_line:
            return old_file[new_file_line:]
    # 改变文件内容，增加房间ID
    def addId(self, contentlist, roomid):
        new_content_list = []
        try:
            self.new_count_lines = len(contentlist)
        except:
            self.new_count_lines = 0
        if contentlist != None:
            for i in contentlist:
                i = i.split(' ')
                if float(i[-3]) >= MAX_RATIO:
                    ip = i[-1].split('_')[0]
                    port = i[-1].split('_')[-1]
                    new_line = "%s %s %s %s %s %s" % (roomid, i[0], i[1], i[-3],ip,port)
                    new_content_list.append(new_line)
        return new_content_list
    # 追加写入文件,更新json数据
    def writeFile(self,file_name,addcontent,roomid):
        f = open(file_name,'a')
        f.write(''.join(addcontent))
        f.close()
        if addcontent!=None:
            if self.file_line.has_key(self._getTime()):
                pass
            else:
                self.file_line[self._getTime()] = {}
            try:
                self.file_line[self._getTime()][roomid] = int(self.file_line[self._getTime()][roomid]) + self.new_count_lines
            except Exception:
                self.file_line[self._getTime()][roomid] = self.new_count_lines
            finally:
                self._delJson()
                with open(SAVE_PATH+LOG_LING_FILE, 'w') as json_file:
                    json_file.write(json.dumps(self.file_line))
    def newLogName(self):
        return SAVE_PATH+'ratio_'+self._getTime()+'.log'
    def logNameList(self):
        ttpath = []
        logname = []
        lists = open(self.listfile)
        for line in lists:
            if re.search(r'^#|^\s*$', line):
                continue
            elif re.search(r'TransTrans', line):
                ttpath.append(line.rstrip('TransTrans\n'))
        for path in ttpath:
            os.chdir(path + "TT_log")
            for parent, dirname, filenames in os.walk(os.getcwd()):
                for name in filenames:
                    if "ratio" in name and self._getTime() in name:
                        logname.append(os.getcwd() + "/" + name)
        return logname
# 主函数
def main():
    file_process = FileProcessAbout()
    while True:
        new_log_name = file_process.newLogName()
        log_name_list = file_process.logNameList()
        for log in log_name_list:
            roomid = file_process.getRoomId(log)#获取房间ID
            if DIFF_SIZE ==0 or DIFF_SIZE=='':
                old_log_content = file_process.openFile(log)#获取老日志内容
                # new_log_content = file_process.openFile(new_log_name)#获取新日志内容
                # add_content = file_process.newContent(old_log_content,new_log_content)#获取新增日志
                add_content = file_process.newContentJson(roomid,old_log_content)#获取新增日志
                new_add_content = file_process.addId(add_content,roomid)#增加房间ID到新日志
                # file_process.writeFile(new_log_name,new_add_content)#写入新内容到日志
                file_process.writeFile(new_log_name,new_add_content,roomid)#写入新内容到日志
            else:
                deff_log_size = file_process.checkFileSize(log,new_log_name)#获取新旧文件差值
                if deff_log_size>=DIFF_SIZE:
                    old_log_content = file_process.openFile(log)#获取老日志内容
                    # new_log_content = file_process.openFile(new_log_name)#获取新日志内容
                    # add_content = file_process.newContent(old_log_content,new_log_content)#获取新增日志
                    add_content = file_process.newContentJson(roomid, old_log_content)  # 获取新增日志
                    new_add_content = file_process.addId(add_content,roomid)#增加房间ID到新日志
                    # file_process.writeFile(new_log_name,new_add_content)#写入新内容到日志
                    file_process.writeFile(new_log_name, new_add_content,roomid)  # 写入新内容到日志
        time.sleep(WAIT_TIME)
if __name__ == '__main__':
    #控制是否自动后台运行，1：后台运行、0：终端运行
    damoe = 1
    if damoe == 1 :
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError, e:
            print >>sys.stderr, "fork #1 failed: %d (%s)" % (e.errno, e.strerror)
            sys.exit(1)
        os.setsid()
        os.umask(0)
    main()