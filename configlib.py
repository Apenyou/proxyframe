import configparser


class configurationData():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini',encoding='gbk')
        self.config = config

    def dataModification(self, section, option, value):
        '''
        配置文件修改项
        :return:
        '''

        self.config.set(section, option, value)
        with open('config.ini', 'w') as f:
            self.config.write(f)

    def configurationRead(self, section, option):
        return self.config.get(section, option)


if __name__ == '__main__':
    testconfig = configurationData()
    # testconfig.dataModification('mitmproxyPID', 'pid', '234324')
    print(testconfig.configurationRead('mitmproxyPID', 'pid'))
