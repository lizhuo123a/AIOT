# ======================
# -*- coding: utf-8 -*-
# @author:LiZhuo
# @time  :2020/10/10 17:22
# @email :358840393@qq.com
# 今天的你要比昨天的你更优秀！
# ======================
import unittest
from datetime import datetime
from libs.HTMLTestRunnerNew import HTMLTestRunner
from scripts.constants import CASES_PATH,REPORTS_PATH
import sys
sys.path.append("..")

one_suite = unittest.defaultTestLoader.discover(CASES_PATH)
file_name = REPORTS_PATH +"/report_"+f"{datetime.now():%Y%m%d%H%M%S}"+".html"
one_file = open(file_name,"wb")
one_runner = HTMLTestRunner(stream=one_file,
                            verbosity=2,
                            title="AIOT平台接口测试报告",
                            description="一轮测试",
                            tester="李卓")
one_runner.run(one_suite)
one_file.close()

