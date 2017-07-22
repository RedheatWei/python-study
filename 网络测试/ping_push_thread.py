#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年3月26日

@author: Redheat
'''
import sys
import urllib
import threading
if len(sys.argv) == 1:#判断脚本后有没有跟文件名
    print '请脚本后跟文件名并用空格隔开！\n'
    sys.exit()
else:
    ip_list = sys.argv[1:]

def get_area(area_ip):#获取ip地址信息
    result = urllib.urlopen("http://ip.taobao.com/service/getIpInfo.php?ip=%s" % area_ip)
    res = result.readlines()
    result.close()
    res_data = eval((res[0]))['data']#将含有ip信息的数据转为字典
    return res_data['country'].decode("unicode_escape").encode("UTF-8")+res_data['region'].decode("unicode_escape").encode("UTF-8")+\
                        res_data['city'].decode("unicode_escape").encode("UTF-8")+res_data['isp'].decode("unicode_escape").encode("UTF-8")
                    
def handle_data(ip):
    data18 = []
    lost18 = 0.0
    number18 = 0
    data19 = []
    lost19 = 0.0
    number19 = 0
    data20 = []
    lost20 = 0.0
    number20 = 0
    data21 = []
    lost21 = 0.0
    number21 = 0
    data22 = []
    lost22 = 0.0
    number22 = 0
    data_other = []
    lost_other = 0.0
    number_other = 0
    
    try:
        f = file('/home/redheat/'+ip)
        content = f.readlines()
        f.close()
    except IOError,e:#打开错误的时候提示用户脚本后跟文件名
        print 'have no file named %s' % ip
        sys.exit()   
    for line in content:
        if line.split()[3].split(':')[0] == '18':
            number18 += 1 #计算总次数       
            if 'request' not in line: #查找不丢包数据
                ping_data18 = float(line.split()[-2].split('=')[-1]) #获取ping值
                data18.append(ping_data18)
            else:
                lost18 += 1
    
    
        elif line.split()[3].split(':')[0] == '19':
            number19 += 1 #计算总次数       
            if 'request' not in line: #查找不丢包数据
                ping_data19 = float(line.split()[-2].split('=')[-1]) #获取ping值
                data19.append(ping_data19)
            else:
                lost19 += 1
    
        elif line.split()[3].split(':')[0] == '20':
            number20 += 1 #计算总次数       
            if 'request' not in line: #查找不丢包数据
                ping_data20 = float(line.split()[-2].split('=')[-1]) #获取ping值
                data20.append(ping_data20)
            else:
                lost20 += 1
    
        elif line.split()[3].split(':')[0] == '21':
            number21 += 1 #计算总次数       
            if 'request' not in line: #查找不丢包数据
                ping_data21 = float(line.split()[-2].split('=')[-1]) #获取ping值
                data21.append(ping_data21)
            else:
                lost21 += 1
    
        elif line.split()[3].split(':')[0] == '22':
            number22 += 1 #计算总次数       
            if 'request' not in line: #查找不丢包数据
                ping_data22 = float(line.split()[-2].split('=')[-1]) #获取ping值
                data22.append(ping_data22)
            else:
                lost22 += 1
    
        else:
            number_other += 1
            if 'request' not in line: #查找不丢包数据
                ping_data_other = float(line.split()[-2].split('=')[-1]) #获取ping值
                data_other.append(ping_data_other)
            else:
                lost_other += 1
            
    MAX18 = max(data18)
    AVG18 = sum(data18) / len(data18)
    LOST18 = float(lost18 / number18) * 100
    
    MAX19 = max(data19)
    AVG19 = sum(data19) / len(data19)
    LOST19 = float(lost19 / number19) * 100
    
    MAX20 = max(data20)
    AVG20 = sum(data20) / len(data20)
    LOST20 = float(lost20 / number20) * 100
    
    MAX21 = max(data21)
    AVG21 = sum(data21) / len(data21)
    LOST21 = float(lost21 / number21) * 100
    
    MAX22 = max(data22)
    AVG22 = sum(data22) / len(data22)
    LOST22 = float(lost22 / number22) * 100
    
    MAX_other = max(data_other)
    AVG_other = sum(data_other) / len(data_other)
    LOST_other = float(lost_other / number_other) * 100
    
    
    MAX_ALL = max(MAX18,MAX19,MAX20,MAX21,MAX22,MAX_other)
    AVG_ALL = sum(data18+data19+data20+data21+data22+data_other) / len(data18+data19+data20+data21+data22+data_other)
    LOST_ALL = float((lost18+lost19+lost20+lost21+lost22+lost_other) / (number18+number19+number20+number21+number22+number_other)) * 100
    
    print '\33[32m%s %s' % (ip,get_area(ip))
    print '以下数据分别为最大值  平均值  丢包率\33[0m'
    print '''18点-19点%10s   %.2f   %.2f%%
19点-20点%10s   %.2f   %.2f%%
20点-21点%10s   %.2f   %.2f%%
21点-22点%10s   %.2f   %.2f%%
22点-23点%10s   %.2f   %.2f%%
其他时段 %10s   %.2f   %.2f%%
总数据   %10s   %.2f   %.2f%%
    ''' % (MAX18,AVG18,LOST18,MAX19,AVG19,LOST19,MAX20,AVG20,LOST20,MAX21,AVG21,LOST21,MAX22,AVG22,LOST22,MAX_other,AVG_other,LOST_other,MAX_ALL,AVG_ALL,LOST_ALL)


def main():
    threads = []
    nloops = range(len(ip_list))
    for i in nloops:
        t = threading.Thread(target=handle_data,args=(ip_list[i],))
        threads.append(t)
        
    for i in nloops:
        threads[i].start()
        
    for i in nloops:
        threads[i].join()
        
if __name__ == '__main__':
    main()
