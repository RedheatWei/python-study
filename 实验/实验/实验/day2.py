#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年4月9日

@author: Redheat
'''
'''
wpf = [['21195','wpf','wpf','yw','yw','130'],['10750','wp','wp','net','net','186']]



list_id = []


for i in wpf:
    list_id.append(i[0])

#list_id.append(wpf[0][0])
#list_id.append(wpf[1][0])

print list_id

check_id = raw_input('serch:')

for id in list_id:
    if check_id in id:
        for info in wpf:
            if id in info:
                print info
                
                
'''


wpf = {'21195':['wpf','wpf','yw','yw','130'],'10750':['wp','wp','net','net','186']}

check_id = raw_input('serch:')

for key in wpf:
    if check_id in key:
        print '%s %s %s %s %s %s' % (key,wpf[key][0],wpf[key][1],wpf[key][2],wpf[key][3],wpf[key][4])