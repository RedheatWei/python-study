#!/usr/bin/env python 
# coding=utf-8 
 
#------------------------------------------------------ 
# Name:         nginx 日志分析脚本 
# Purpose:      此脚本只用来分析nginx的访问日志 
# Version:      1.0 
# Author:       LEO 
# BLOG:         http://linux5588.blog.51cto.com 
# EMAIL:        chanyipiaomiao@163.com 
# Created:      2013-05-07 
# Modified:     2013-05-07 
# Copyright:    (c) LEO 2013 
#------------------------------------------------------ 
 
import sys 
import time 
 
sys_argv = ['nginx.py','active.show.sina.com.cn-access_log_20150727.log']
 
#该类是用来打印格式 
class displayFormat(object): 
 
    def format_size(self,size): 
        '''''格式化流量单位''' 
        KB = 1024           #KB -> B  B是字节 
        MB = 1048576        #MB -> B 
        GB = 1073741824     #GB -> B 
        TB = 1099511627776  #TB -> B 
        if size >= TB : 
            size = str(size / TB) + 'T' 
        elif size < KB : 
            size = str(size) + 'B' 
        elif size >= GB and size < TB: 
            size = str(size / GB) + 'G' 
        elif size >= MB and size < GB : 
            size = str(size / MB) + 'M' 
        else : 
            size = str(size / KB) + 'K' 
        return size 
 
    #定义字符串格式化 
    formatstring = '%-15s %-10s %-12s %8s %10s %10s %10s %10s %10s %10s %10s' 
 
    def transverse_line(self) : 
        '''''输出横线''' 
        print self.formatstring % ('-'*15,'-'*10,'-'*12,'-'*12,'-'*10,'-'*10,'-'*10,'-'*10,'-'*10,'-'*10,'-'*10) 
 
    def head(self): 
        '''''输出头部信息''' 
        print self.formatstring % ('IP','Traffic','Times','Times%','200','404','500','403','302','304','503') 
 
    def error_print(self) : 
        '''''输出错误信息''' 
        print 
        print 'Usage : ' + sys_argv[0] + ' NginxLogFilePath [Number]' 
        print 
        sys.exit(1) 
 
    def execut_time(self): 
        '''''输出脚本执行的时间''' 
        print 
        print "Script Execution Time: %.3f second" % time.clock() 
        print 
 
#该类是用来生成主机信息的字典 
class hostInfo(object): 
    host_info = ['200','404','500','302','304','503','403','times','size'] 
 
    def __init__(self,host): 
        self.host = host = {}.fromkeys(self.host_info,0) #结果大概是{'200': 0, '302': 0, '304': 0, 'times': 0, '404': 0, '403': 0, '503': 0, '500': 0, 'size': 0}
 
    def increment(self,status_times_size,is_size): 
        '''''该方法是用来给host_info中的各个值加1''' 
        if status_times_size == 'times': 
            self.host['times'] += 1 #给字典里的times加1
        elif is_size: 
            self.host['size'] = self.host['size'] + status_times_size 
        else: 
            self.host[status_times_size] += 1 
 
    def get_value(self,value): #在实例化对象
        '''''该方法是取到各个主机信息中对应的值''' 
        return self.host[value] 
 
#该类是用来分析文件 
class fileAnalysis(object): 
    def __init__(self): 
        '''''初始化一个空字典''' 
        self.report_dict = {} 
        self.total_request_times,self.total_traffic,self.total_200,\
        self.total_404,self.total_500,self.total_403,self.total_302,\
        self.total_304,self.total_503 = 0,0,0,0,0,0,0,0,0 
 
    def split_eachline_todict(self,line): 
        '''''分割文件中的每一行，并返回一个字典''' 
        split_line = line.split() 
        split_dict = {'remote_host':split_line[0],'status':split_line[8],\
        'bytes_sent':split_line[9],} 
        return split_dict 
 
    def generate_log_report(self,logfile): 
        '''''读取文件，分析split_eachline_todict方法生成的字典''' 
        for line in logfile:#取每行做处理
            try: 
                line_dict = self.split_eachline_todict(line)#用split_eachline_todict分割文件，得出的数据大概是{'status': '200', 'bytes_sent': '32', 'remote_host': '118.194.193.222'}
                host = line_dict['remote_host'] #118.194.193.222
                status = line_dict['status'] #200
            except ValueError : #忽略值错误并继续
                continue 
            except IndexError : #忽略值错误并继续 
                continue 
 
            if host not in self.report_dict : #判断有没有遇到过这个host
                host_info_obj = hostInfo(host) #实例化hostInfo
                self.report_dict[host] = host_info_obj #实例化，实际上是给120行做准备
            else : 
                host_info_obj = self.report_dict[host] 
 
            host_info_obj.increment('times',False)  #host_info_obj是实例化之后的对象，相当于hostInfo(host).increment('times',False)，false应该是没有实际意义，只是为了凑两个参数不报错
            if status in host_info_obj.host_info : #如果状态值在上面的字典里
                host_info_obj.increment(status,False)  #执行increment，效果是给对应的状态+1，这里的false有作用，是为了跳过elif这一块
            try: 
                bytes_sent = int(line_dict['bytes_sent']) #bytes_sent=32
            except ValueError: #没法转换的话，发送的大小格式化为0
                bytes_sent = 0 
            host_info_obj.increment(bytes_sent,True)  #执行elif代码块了，size变成了0+bytes_sent
        return self.report_dict #返回生成的字典
 
    def return_sorted_list(self,true_dict): 
        '''''计算各个状态次数、流量总量，请求的总次数，并且计算各个状态的总量 并生成一个正真的字典，方便排序''' 
        for host_key in true_dict : #对主机列表进行了遍历
            host_value = true_dict[host_key] #取出对应主机的数据
            times = host_value.get_value('times')#取出对于主机的times值            
            self.total_request_times = self.total_request_times + times  #更新times值
            size = host_value.get_value('size') #获取对于主句的size                       
            self.total_traffic = self.total_traffic + size   #更新size
 #下面这一部分是更新这些值的
            o200 = host_value.get_value('200') 
            o404 = host_value.get_value('404') 
            o500 = host_value.get_value('500') 
            o403 = host_value.get_value('403') 
            o302 = host_value.get_value('302') 
            o304 = host_value.get_value('304') 
            o503 = host_value.get_value('503') 
 
            true_dict[host_key] = {'200':o200,'404':o404,'500':o500,\
            '403':o403,'302':o302,'304':o304,'503':o503,'times':times,\
            'size':size} 
 
            self.total_200 = self.total_200 + o200 
            self.total_404 = self.total_404 + o404 
            self.total_500 = self.total_500 + o500 
            self.total_302 = self.total_302 + o302 
            self.total_304 = self.total_304 + o304 
            self.total_503 = self.total_503 + o503 
 #排序
        sorted_list = sorted(true_dict.items(),key=lambda t:(t[1]['times'],\
            t[1]['size']),reverse=True) 
 
        return sorted_list #返回排序的结果
 
class Main(object): 
    def main(self) : 
        '''''主调函数''' 
        display_format = displayFormat() #实例化displayFormat
        arg_length = len(sys_argv) #判断传进来的参数个数
        if arg_length == 1 : #如果没有传进参数
            display_format.error_print() #输出错误信息
        elif arg_length == 2 or arg_length == 3: #传进参数
            infile_name = sys_argv[1] #日志文件名
            try : 
                infile = open(infile_name,'r') #尝试打开文件
                if arg_length == 3 : #如果传进来两个参数
                    lines = int(sys_argv[2])#最后一个参数就是lines
                else : #如果传进来一个参数
                    lines = 0 
            except IOError,e : #IO错误，输出错误信息
                print 
                print e 
                display_format.error_print() 
            except ValueError : #输入值错误，输出错误信息。（这个值错误没遇到过，不知道具体什么意思）
                print 
                print "Please Enter A Volid Number !!" 
                display_format.error_print() 
        else : #传入参数不是1、2、3，输出错误信息。
            display_format.error_print() 
 
        fileAnalysis_obj = fileAnalysis() #实例化fileAnalysis
        not_true_dict = fileAnalysis_obj.generate_log_report(infile) #{'118.194.193.222': <__main__.hostInfo object at 0x025EC7D0>} 
        log_report = fileAnalysis_obj.return_sorted_list(not_true_dict) #把{'118.194.193.222': <__main__.hostInfo object at 0x025EC7D0>}带进了return_sorted_list
        total_ip = len(log_report) #判断ip总个数？
        if lines : #如果传进了参数
            log_report = log_report[0:lines] #每次显示的ip个数？
        infile.close() #关闭文件
 
        print 
        total_traffic = display_format.format_size(fileAnalysis_obj.total_traffic) #格式化输出
        total_request_times = fileAnalysis_obj.total_request_times #程序执行时间
        #都是格式化输出
        print 'Total IP: %s   Total Traffic: %s   Total Request Times: %d' \
        % (total_ip,total_traffic,total_request_times) 
        print 
        display_format.head() 
        display_format.transverse_line() 
 
        for host in log_report : 
            times = host[1]['times'] 
            times_percent = (float(times) / float(fileAnalysis_obj.total_request_times)) * 100 
            print display_format.formatstring % (host[0],\
                display_format.format_size(host[1]['size']),\
                times,str(times_percent)[0:5],\
                host[1]['200'],host[1]['404'],\
                host[1]['500'],host[1]['403'],\
                host[1]['302'],host[1]['304'],host[1]['503']) 
                                                  
        if (not lines) or total_ip == lines : 
            display_format.transverse_line() 
            print display_format.formatstring % (total_ip,total_traffic,\
                total_request_times,'100%',\
                fileAnalysis_obj.total_200,\
                fileAnalysis_obj.total_404,\
                fileAnalysis_obj.total_500,\
                fileAnalysis_obj.total_403,\
                fileAnalysis_obj.total_302,\
                fileAnalysis_obj.total_304,\
                fileAnalysis_obj.total_503) 
 
        display_format.execut_time() 
 
if __name__ == '__main__': 
    main_obj = Main() 
    main_obj.main() 
