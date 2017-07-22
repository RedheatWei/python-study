#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年3月27日

@author: Redheat
'''
import urllib

f = file('/data0/testsend/test_ip.txt')
ip_list = f.readlines()
f.close()
ratio_high = 0.0

def get_area(area_ip):
    result = urllib.urlopen("http://ip.taobao.com/service/getIpInfo.php?ip=%s" % area_ip)
    res = result.readlines()
    result.close()
    res_data = eval((res[0]))['data']#将含有ip信息的数据转为字典
    return res_data['country'].decode("unicode_escape").encode("UTF-8")+res_data['region'].decode("unicode_escape").encode("UTF-8")+\
                        res_data['city'].decode("unicode_escape").encode("UTF-8")+res_data['isp'].decode("unicode_escape").encode("UTF-8")

for ip in ip_list:
    ip = ip.strip('\n')
    area = get_area(ip)
    print 'this is %s %s' % (ip,area)
    file_name = '/data0/testsend/'+ip+'/temp_sendd.log'
    r = file(file_name)
    ratio_list = r.readlines()
    r.close()
    ratio_data = []
    print '以下为丢包超过5%的时间点'
    for line in ratio_list:
        ratio_data_number = float(line.split()[-1].strip('%%'))
        ratio_data.append(ratio_data_number)
        if ratio_data_number > 5.0:
            ratio_high += 1
            print line,
    lost_more = (ratio_high / len(ratio_data))*100
    areavge_lost = sum(ratio_data) / len(ratio_data)
    max_lost = max(ratio_data)
    print 'ratio lost more than 5%% is %s%%' % (lost_more)
    print 'ratio lost areavge is %s%%' % (areavge_lost)
    print 'max ratio lost is %s%%' % (max_lost)
    print '\n'