import os
import subprocess
import sys
import configlib

config = configlib.configurationData()
proxyhost = config.configurationRead('mitmproxy', 'proxyhost')
proxyport = config.configurationRead('mitmproxy', 'proxyport')
ProxyOverride = config.configurationRead('mitmproxy', 'ProxyOverride')

# mac OS 代理控制

def Proxy_on(ethernet):
    os.system('networksetup -setwebproxy {0} {1} {2}'.format(ethernet, proxyhost, proxyport))
    os.system('networksetup -setsecurewebproxy {0} {1} {2}'.format(ethernet, proxyhost, proxyport))


def Proxy_off(ethernet):
    os.system('networksetup -setwebproxystate {0} off'.format(ethernet))
    os.system('networksetup -setsecurewebproxystate {0} off'.format(ethernet))


def getEthernet():
    command = 'networksetup -listallnetworkservices'
    subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="gbk")
    Ethernet = str(subp.communicate()).split("\\")[1:3]
    for i in Ethernet:
        yield i[1:]


def proxyswitch(TorF):
    '''

    :param TorF: True or False
    :return:
    '''
    if sys.platform == 'win32':
        import winreg
        import ctypes
        # #########################################################################
        KEY_ProxyEnable = "ProxyEnable"
        KEY_ProxyServer = "ProxyServer"
        # KEY_ProxyOverride = "ProxyOverride"
        KEY_XPATH = "Software\Microsoft\Windows\CurrentVersion\Internet Settings"
        # #########################################################################
        # 如果从来没有开过代理 有可能健不存在 会报错
        INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                           r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                                           0, winreg.KEY_ALL_ACCESS)
        # 设置刷新
        INTERNET_OPTION_REFRESH = 37
        INTERNET_OPTION_SETTINGS_CHANGED = 39
        internet_set_option = ctypes.windll.Wininet.InternetSetOptionW

        def set_key(name, value):  # 修改键值
            _, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
            winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)

        # 代理控制
        def SetProxy(Enable):
            set_key('ProxyEnable', Enable)  # 启用
            set_key('ProxyOverride', ProxyOverride)  # 绕过本地
            set_key('ProxyServer', '{0}:{1}'.format(proxyhost, proxyport))  # 代理IP及端口
            internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
            internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)

        # 获取当前代理状态
        def GetProxyStatus():
            hKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, KEY_XPATH, 0, winreg.KEY_READ)
            retVal = winreg.QueryValueEx(hKey, KEY_ProxyEnable)
            winreg.CloseKey(hKey)
            return retVal[0] == 1

        if TorF:
            SetProxy(1)
        else:
            SetProxy(0)
    else:
        if TorF:
            for ethernet in getEthernet():
                Proxy_on(ethernet)
        else:
            for ethernet in getEthernet():
                Proxy_off(ethernet)

proxyswitch(False)
# def main():
#     if GetProxyStatus():
#         SetProxy(0, '127.0.0.1:8888', '*.local')
#         print("关闭代理")
#     else:
#         SetProxy(1, '127.0.0.1:8888', '*.local')
#         print("打开代理")
#
# if __name__ == '__main__':
#     main()
# proxyswitch(False)
