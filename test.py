import time
import win32api, win32con
import sys


def log(func):
    def wrapper(*args, **kw):
        # print('call %s():' % func.__name__)
        print(args[0])
        return func(*args, **kw)

    return wrapper


@log
def testdel(a):
    print(123123123)


# testdel(6666)

def Notification(style):
    if style == 'news':
        import tinyWinToast.tinyWinToast
        toast = tinyWinToast.tinyWinToast.Toast()
        toast.setHeroImage("F:\codeprivate\proxyframe\qqq.png")
        toast.setImage("F:\codeprivate\proxyframe\qqq.png")
        toast.setTitle("测试标题", maxLines=1)
        toast.setMessage("哈哈哈哈哈哈哈E", maxLines=1)
        toast.addText("MORE TEXT", maxLines=1)
        toast.setIcon('F:\codeprivate\proxyframe\qqq.png')
        toast.show()
    if style == 'messagebox':
        # 提醒OK消息框
        win32api.MessageBox(0, "这是一个测试提醒OK消息框", "提醒", win32con.MB_OK)

        win32api.SendMessage(123, 342)
        # 是否信息框
        win32api.MessageBox(0, "这是一个测试是否信息框", "提醒", win32con.MB_YESNO)

        ##说明信息框
        win32api.MessageBox(0, "这是一个测试说明信息框", "提醒", win32con.MB_HELP)

        ####警告信息框
        win32api.MessageBox(0, "这是一个测试警告信息框", "提醒", win32con.MB_ICONWARNING)

        ##疑问信息框
        win32api.MessageBox(0, "这是一个测试疑问信息框", "提醒", win32con.MB_ICONQUESTION)

        ##提示信息框
        win32api.MessageBox(0, "这是一个测试提示信息框", "提醒", win32con.MB_ICONASTERISK)

        ##确认信息框
        win32api.MessageBox(0, "这是一个测试确认信息框", "提醒", win32con.MB_OKCANCEL)

        ##重试信息框
        win32api.MessageBox(0, "这是一个测试重试信息框", "提醒", win32con.MB_RETRYCANCEL)

        ##是否取消信息框
        win32api.MessageBox(0, "这是一个测试是否取消信息框", "提醒", win32con.MB_YESNOCANCEL)
