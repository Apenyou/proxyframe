import subprocess
import os

pid=''
def cmd(command, outime=None):
    subp = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    if outime != None:
        subp.wait(outime)
        return subp.communicate(), subp.poll(), subp.pid
    print(subp.pid)
    print('-==========')
    global pid
    pid = subp.pid
    return subp.pid

def mitmproxy_init():
    PID_rcmd, err, pid = cmd('lsof -i tcp:8888',outime=0.5)
    # print(str(PID_rcmd).split(' ')[-19])
    if err != 0:
        return True
    else:
        PID = str(PID_rcmd).split(' ')[-19]
        cmd('kill -9 {0}'.format(PID))
        # os.kill(PID)
        return True

#TODO:启动后没有返回，处理(子进程一直通信？？)
def mitmproxy_start():
    print(os.getcwd())
    cmd('mitmdump -s addons.py -p 8888')


if __name__ == '__main__':
    # mitmproxy_init()
    mitmproxy_start()
    print(pid)
