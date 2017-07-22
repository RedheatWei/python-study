#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年4月12日

@author: Redheat
'''
import json

commodity_dict = {'1':['Potato',3.6],'2':['Chicken',12],'3':['Haagen Dazs',33],\
                  '4':['Clothes',588],'5':['Apple Watch',4588],'6':['BMW',780000],\
                  '7':[None,None],'8':[None,None]}

wage = 12888#Just a dream.



show_list = '''\033[1;31;40m
  Which one did you want to buy ？
#################################  
    1.Potato:3.6$              
    2.Chicken:12$              
    3.Haagen Dazs:33$
    4.Clothes：588$            
    5.Apple Watch：4588$        
    6.BMW：Just for show!      
    7.Checkout.                  
    8.Quit.                      
#################################
Enter a choice:\033[0m'''#红色字体，红色么，宰客专用！
    
def get_surplus(commodity_buy):#获取commodity_buy列表的最后一个列表元素的最后一个元素，也就是剩余钱数
    return commodity_buy[-1][-1]
    
def calculation(choice,commodity_buy):#计算剩余工资
    surplus = get_surplus(commodity_buy)
    if surplus > commodity_dict[choice][-1]:
        surplus -= commodity_dict[choice][-1]
        buy_list = [commodity_dict[choice][0],commodity_dict[choice][-1],surplus]
#        return buy_list
    else:
        buy_list = ['No money',None, surplus]
        print 'Have no enough money!'
    return buy_list#分别为商品名，商品价格，剩余工资


def checkout(commodity_buy):
    for list in commodity_buy:
        print 'Commodity %s,Price %s,surplus %s' % (list[0],list[1],list[-1])
    
def read_json(file_name):
    f = open(file_name)
    commodity_buy = json.load(f)
    f.close()
    return commodity_buy


def write_json(commodity_buy,file_name):
    f = open(file_name,'wb')
    json.dump(commodity_buy,f)
    f.close()

def main():
    commodity_buy = [[wage,None,wage]]
    write_json(commodity_buy,'buy_file')
    while True:
        choice = raw_input(show_list)
        while choice not in commodity_dict.keys():
            print 'Have no this commodity,please try again.'
            break
        else:
            if choice == '8':
                commodity_buy = read_json('buy_file')
                checkout(commodity_buy)
                print 'Look Forward Next.\nBye Bye!'
                break
            elif choice == '7':
                commodity_buy = read_json('buy_file')
                checkout(commodity_buy)
            else:
                buy_list = calculation(choice,commodity_buy)
                commodity_buy.append(buy_list)
                write_json(commodity_buy,'buy_file')
                print 'Commodity %s,Price %s,surplus %s' % (buy_list[0],buy_list[1],buy_list[-1])
#                checkout(commodity_buy)
if __name__ == '__main__':
    main()
