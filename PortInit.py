import subprocess
import os
import configilb


class BasicAbility():

    def __int__(self):
        configobj = configilb.configurationData()
        self.configobj = configobj

    def cmd(self, command, outime=None):
        subp = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
        if outime != None:
            subp.wait(outime)
            return subp.communicate(), subp.poll(), subp.pid
        print(subp.pid)
        print('-==========')
        return subp.pid

    def mitmproxy_init(self):
        configobj = configilb.configurationData()
        aa = configobj.configurationRead('mitmproxyPID', 'pid')
        print(aa)
        # os.kill()
        # PID_rcmd, err, pid = self.cmd('lsof -i tcp:8888',outime=0.5)
        # # print(str(PID_rcmd).split(' ')[-19])
        # if err != 0:
        #     return True
        # else:
        #     PID = str(PID_rcmd).split(' ')[-20]
        #     print(PID)
        #     self.cmd('kill -9 {0}'.format(PID))
        #     # os.kill(PID)
        #     return True

    #TODO:启动后没有返回，处理(子进程一直通信？？)
    def mitmproxy_start(self):
        print(os.getcwd())
        pid = self.cmd('mitmdump -s addons.py -p 8888')

        # configobj = configilb.configurationData()
        self.configobj.dataModification('mitmproxyPID', 'pid', str(pid))



if __name__ == '__main__':
    inittest = BasicAbility()
    inittest.mitmproxy_init()
    # inittest.mitmproxy_start()

