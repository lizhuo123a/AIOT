# ======================
# -*- coding: utf-8 -*-
# @author:LiZhuo
# @time  :2020/10/12 11:23
# @email :358840393@qq.com
# 今天的你要比昨天的你更优秀！
# ======================
from configparser import ConfigParser
from scripts.constants import AIOT_CONFIG_PATH,TEST_CONFIG_PATH
import sys
sys.path.append("..")
class HandleConfig:
    def __init__(self,filename):
        self.filename = filename
        self.config = ConfigParser()
        self.config.read(self.filename,encoding="utf8")

    def get_value(self,section,option):
        return self.config.get(section,option)

    def get_int(self,section,option):
        return self.config.getint(section,option)

    def get_float(self,section,option):
        return self.config.getfloat(seciton,option)

    def get_boolean(self,seciton,option):
        return self.config.getboolean(section,option)

    @staticmethod
    def write_config(datas,filename):
        if isinstance(datas,dict):
            for value in datas.values():
                if not isinstance(value,dict):
                    return "数据不合法，数据类型应为嵌套字典的字典"
                config = ConfigParser()
                for key in datas:
                    config[key] = datas[key]
                with open(filename,"w") as file:
                    config.write(file)
do_config = HandleConfig(AIOT_CONFIG_PATH)

if __name__ == '__main__':
    a = do_config.get_value("info","authorization")
    print(a)
