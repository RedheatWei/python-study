#_*_ coding:utf-8 _*_
'''
Created on 2015��2��26��

@author: Redheat
'''
import _winreg
hkey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, \
                       r'System\CurrentControlSet\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}')
keyInfo = _winreg.QueryInfoKey(hkey)
for index in range(keyInfo[0]):
    hSubKeyName = _winreg.EnumKey(hkey, index)
    hSubKey = _winreg.OpenKey(hkey, hSubKeyName)
#    print hSubKeyName,hSubKey
    try:
        hNdiInfKey = _winreg.OpenKey(hSubKey, r'Ndi\Interfaces')
        lowerRange = _winreg.QueryValueEx(hNdiInfKey, 'LowerRange')
        if lowerRange[0] == 'ethernet':
            driverDesc = _winreg.QueryValueEx(hSubKey, 'DriverDesc')[0]
            print 'DriverDesc: ', driverDesc
            netCfgInstanceID = _winreg.QueryValueEx(hSubKey, 'NetCfgInstanceID')[0]
            print 'NetCfgInstanceID: ', netCfgInstanceID
            break
        _winreg.CloseKey(hNdiInfKey) # 关闭 RegKey
    except WindowsError:
        print r'Message: No Ndi\Interfaces Key'
    _winreg.CloseKey(hSubKey)
_winreg.CloseKey(hkey)
if netCfgInstanceID == None:
    print '修改IP失败 - 没有找到网络适配器'   
    exit()