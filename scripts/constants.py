# ======================
# -*- coding: utf-8 -*-
# @author:LiZhuo
# @time  :2020/10/12 11:13
# @email :358840393@qq.com
# 今天的你要比昨天的你更优秀！
# ======================
import os
import sys
sys.path.append("..")

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 用例文件所在路径
DATAS_PATH = os.path.join(BASE_PATH,"datas")
TESTCASE_PAHT = os.path.join(DATAS_PATH,"test.xlsx")
# print(TESTCASE_PAHT)

# 配置文件所在路径
CONFIGS_PATH = os.path.join(BASE_PATH,"configs")
TEST_CONFIG_PATH = os.path.join(CONFIGS_PATH,"test.ini")
AIOT_CONFIG_PATH = os.path.join(CONFIGS_PATH,"aiot.conf")

# 日志文件所在路径
LOGS_PATH = os.path.join(BASE_PATH,"logs")
LOGS_FILE_PATH = os.path.join(LOGS_PATH,"test.log")

# 执行用例所在目录
CASES_PATH = os.path.join(BASE_PATH,"CASES")

# 测试报告所在目录
REPORTS_PATH =os.path.join(BASE_PATH,"reports")