# #########################################################################
KEY_ProxyEnable = "ProxyEnable"
KEY_ProxyServer = "ProxyServer"
# KEY_ProxyOverride = "ProxyOverride"
KEY_XPATH = "Software\Microsoft\Windows\CurrentVersion\Internet Settings"
# #########################################################################

import winreg
import ctypes
#如果从来没有开过代理 有可能健不存在 会报错
INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                   r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                                   0, winreg.KEY_ALL_ACCESS)
#设置刷新
INTERNET_OPTION_REFRESH = 37
INTERNET_OPTION_SETTINGS_CHANGED = 39
internet_set_option = ctypes.windll.Wininet.InternetSetOptionW
def set_key(name, value):#修改键值
    _, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
    winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)
#代理控制
def SetProxy(Enable, Server, Override):
    set_key('ProxyEnable', Enable) #启用
    set_key('ProxyOverride', Override) # 绕过本地
    set_key('ProxyServer', Server) #代理IP及端口
    internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
    internet_set_option(0,INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)

# 获取当前代理状态
def GetProxyStatus():
    hKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, KEY_XPATH, 0, winreg.KEY_READ)
    retVal = winreg.QueryValueEx(hKey, KEY_ProxyEnable)
    winreg.CloseKey(hKey)
    return retVal[0]==1

def proxyswitch(TorF):
    if TorF:SetProxy(1, '127.0.0.1:8888', '*.local')
    else:SetProxy(0, '127.0.0.1:8888', '*.local')

def main():
    if GetProxyStatus():
        SetProxy(0, '127.0.0.1:8888', '*.local')
        print("关闭代理")
    else:
        SetProxy(1, '127.0.0.1:8888', '*.local')
        print("打开代理")

if __name__ == '__main__':
    # main()
    proxyswitch(True)
