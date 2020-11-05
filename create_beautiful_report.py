# ======================
# -*- coding: utf-8 -*-
# @author:LiZhuo
# @time  :2020/10/13 11:55
# @email :358840393@qq.com
# 今天的你要比昨天的你更优秀！
# ======================
import unittest
from datetime import datetime
from BeautifulReport import BeautifulReport
from scripts.constants import CASES_PATH,REPORTS_PATH
import sys
sys.path.append("..")

one_suite = unittest.defaultTestLoader.discover(CASES_PATH)
file_name = "report_"+f"{datetime.now():%Y%m%d%H%M%S}"+".html"
result = BeautifulReport(one_suite)
result.report(filename=file_name,
              description="接口测试",
              report_dir=REPORTS_PATH)