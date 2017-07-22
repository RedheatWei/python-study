#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import os
import time
import datetime

def avg_list(list): #求列表平均值
    avg = sum(list) / len(list)
    return avg

def read_file(file_name): #获取日志内容
    f = open(file_name)
    f_con = f.readlines()
    f.close()
    return f_con

def write_file(file_name,write_count): #写入内容到日志
    w = file(file_name,'a')
    w.write(write_count+'\n')
    w.close()
    
def get_num(ping_time_list): #获取有效ping值
    ping_number_list = []
    for i in ping_time_list:
        if i != 'request time out':
            ping_number_list.append(i)
    return ping_number_list

def get_ping_time(final_str):
    final_str_list = final_str.split()
    if len(final_str_list) == 13:
        ping_time = float(final_str_list[-2].split('=')[-1])#获取ping值并转换为浮点数
    else:
        ping_time = 'request time out'
    ping_time_list.append(ping_time) #将ping值加入列表
    return ping_time_list
    
    
           
input_ip = raw_input('IP list:')
ping_number = input('How many time to ping:')
ping_time_space = '1' #ping间隔时间，单位是秒
sleep_time = 1 #间隔时间
packet_loss = 0
starttime = datetime.datetime.now()#开始时间


ip_list = input_ip.split()#将ip地址处理成列表

for ip in ip_list:
    ping_cmd = 'ping -c '+ping_time_space+' '+ip #生成ping命令
    file_name = 'res_ping_'+str(ip)#定义日志文件名
    ping_time_list = []
    f = file(file_name,'a') #以追加模式创建日志文件
    for i in range(ping_number):
        res = os.popen(ping_cmd).read().split('\n') #取出ping数据
        
        
        if len(res[1].split()) == 8:
            disp_str = res[1]
#            final_str = time.asctime()+' '+disp_str # 当前时间+ping数据
#            ping_time_list = get_ping_time(final_str)
#            print final_str
        else:
            disp_str = 'request time out'
            packet_loss += 1
#            print final_str,
        final_str = time.asctime()+' '+disp_str
        print final_str
        f.write(final_str+'\n')
        ping_time_list = get_ping_time(final_str)
        time.sleep(sleep_time) #休眠1秒
    f.close()
##    file_con = read_file(file_name)
#    read_file = file(file_name)
#    file_con = read_file.readlines()
#    read_file.close()
##    packet_loss = 0 #定义丢包 
##    ping_time_list = []
##    for line in file_con[(-3 - ping_number):-3]: #迭代
##       if 'time=' in line: #如果返回值包括‘time=’，则判断数据为不丢包数据
##            ping_time = float(line.split()[-2].split('=')[-1]) #获取ping值并转换为浮点数
 ##           ping_time_list.append(ping_time) #将ping值加入列表
#            print ping_time_list
##        else: #如果返回其他数据，判断为丢包
#            pri_str = 'request time out\n' 
#            print pri_str, #显示请求超时
##            ping_time_list.append('request time out')
#            write_file(file_name, pri_str)
##            packet_loss += 1 #丢包次数+1
##            break
#    print ping_time_list
    ping_number_list = get_num(ping_time_list)#获取有效的ping值
    if len(ping_number_list) > 0:
    #    print ping_number_list
        max_ping_time = max(ping_number_list) #最大延迟
        min_ping_time = min(ping_number_list) #最小延迟
        avg_ping_time = avg_list(ping_number_list) #平均延迟
    else:
        max_ping_time = 0
        min_ping_time = 0
        avg_ping_time = 0
    packet_loss_rate = (float(packet_loss) / ping_number) * 100 #丢包率
    received_number = ping_number - packet_loss #收到包数
    endtime = datetime.datetime.now()#结束时间
    ping_time_sum = (endtime - starttime).seconds * 1000 #消耗时间，毫秒
    
    summary = '''  %s packets transmitted, %s received, %s%% packet loss, time %s ms,
          max/min/avg/=%s/%s/%s ms''' % (ping_number,received_number,packet_loss_rate,ping_time_sum,max_ping_time,min_ping_time,avg_ping_time)
    
    write_file(file_name, summary)
    print summary