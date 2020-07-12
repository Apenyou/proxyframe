import subprocess
import os
import configilb
import sys

class BasicAbility():

    def __int__(self):
        configobj = configilb.configurationData()
        self.configobj = configobj

    def cmd(self, command, outime=None):
        subp = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="gbk")
        if outime != None:
            # subp.wait(outime)
            return subp.communicate(), subp.poll(), subp.pid
        print(subp.pid)
        print('-==========')
        return subp.pid

    def mitmproxy_init(self):


        if sys.platform == 'win32':
            '''windwos '''
            PID_rcmd, err, pid = self.cmd("netstat -ano|findstr 8888",outime=1)
            pid = (str(PID_rcmd).split(' ')[-2][:-4])
            os.kill(int(pid), 9)
        else:
            '''linux '''
            # PID_rcmd, err, pid = self.cmd('lsof -i tcp:8888',outime=0.5)
            # print(str(PID_rcmd).split(' ')[-19])
            configobj = configilb.configurationData()
            pid = configobj.configurationRead('mitmproxyPID', 'pid')
            os.kill(int(pid), 9)


    #TODO:启动后没有返回，处理(子进程一直通信？？)
    '''linux中启动子进程运行mitmdump会在子进程内运行'''
    def mitmproxy_start(self):
        print(os.getcwd())
        pid = self.cmd('mitmdump -s addons.py -p 8888')

        if sys.platform == 'win32':
            return True
        configobj = configilb.configurationData()
        configobj.dataModification('mitmproxyPID', 'pid', str(pid))

    '''Windows启动子进程后运行会再启动一个孙进程执行'''

if __name__ == '__main__':
    inittest = BasicAbility()
    inittest.mitmproxy_init()
    # inittest.mitmproxy_start()


