#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年4月16日
Email: weipeng@sinashow.com
@author: Redheat

'''
class AddrBookEntry(object):
    'address book entry class'
    def __init__(self,nm,ph):
        self.name = nm
        self.phone = ph
        print 'Created instance for:', self.name
        
    def updatePhone(self,newph):
        self.phone = newph
        print 'Updated phone for:',self.name
        

john = AddrBookEntry('John Doe', '408-555-1212')
jane = AddrBookEntry('Jane Doe', '650-555-1212')

print john
print john.name
print john.phone
print jane.name
print jane.phone
john.updatePhone('415-555-1212')
print john.phone

class EmplAddrBookEntry(AddrBookEntry):
    'Employee Address Book Entry class'
    def __init__(self, nm, ph, id, em):
        AddrBookEntry.__init__(self,nm,ph)
        self.empid = id
        self.email = em
    
    def updateEmail(self,newem):
        print 'Updated e-mail address for:',self.name
        

john = EmplAddrBookEntry('John Doe','408-555-1212',42,'john@spam.doe')
print john
print john.name
print john.phone
print john.email
john.updatePhone('415-555-1212')
print john.phone
john.updateEmail('john@doe.spam')
print john.email
#print EmplAddrBookEntry.__doc__

print EmplAddrBookEntry.__name__