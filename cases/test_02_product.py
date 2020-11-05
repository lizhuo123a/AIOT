# ======================
# -*- coding: utf-8 -*-
# @author:LiZhuo
# @time  :2020/10/26 14:54
# @email :358840393@qq.com
# 今天的你要比昨天的你更优秀！
# ======================
import unittest
import sys
sys.path.append("..")
from scripts.handle_log import HandleLogger
from scripts.handle_request import do_request
from scripts.handle_excel import HandleExcel
from libs.ddt import ddt,data
from scripts.handle_config import do_config,HandleConfig
from scripts.constants import TEST_CONFIG_PATH,TESTCASE_PAHT
get_log = HandleLogger().get_logger()
cases = HandleExcel(TESTCASE_PAHT,"product").get_cases()

@ddt
class TestProduct(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        get_log.info("{:=^40s}".format("开始执行产品列表接口测试用例"))

    @classmethod
    def tearDownClass(cls) -> None:
        get_log.info("{:=^40s}".format("产品列表接口测试用例执行结束"))

    @data(*cases)
    def test_product(self,case):
        url = do_config.get_value("url","aiot") + case["url"]
        # data = case["data"]
        authorization = HandleConfig(TEST_CONFIG_PATH).get_value("info","authorization"); headers = {"authorization" :authorization}
        res = do_request.to_request(url,headers=headers)
        except_result = case["except"]
        real_result = res.json()["msg"]
        ms = case["title"]
        try:
            self.assertIn(except_result,real_result,msg=ms)
            get_log.info("{}执行通过".format(ms))
        except Exception as e :
            get_log.error("{}执行失败".format(ms))
            raise e
if __name__ == '__main__':
    unittest.main()