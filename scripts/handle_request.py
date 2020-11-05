# ======================
# -*- coding: utf-8 -*-
# @author:LiZhuo
# @time  :2020/10/12 17:01
# @email :358840393@qq.com
# 今天的你要比昨天的你更优秀！
# ======================
import requests
import json
from scripts.handle_log import HandleLogger
get_log = HandleLogger().get_logger()
import sys
sys.path.append("..")
class HandleRequest:
    def __init__(self):
        self.one_session = requests.Session()

    def to_request(self,url,method="post",data=None,headers=None,is_json=True):
        method = method.lower()
        if isinstance(data,str):
            try:
                data = json.loads(data)
            except Exception as e:
                get_log.info("传入的数据不是json数据，使用eval转换")
                data = eval(data)
                raise e
        if method == "get":
            res = self.one_session.get(url=url,params=data,headers=headers)
        elif method == "post":
            if is_json:
                res = self.one_session.post(url=url,json=data,headers=headers)
            else:
                res = self.one_session.post(url=url,data=data,headers=headers)
        else:
            res = None
            get_log.info(f"暂不支持{method}方法")
        return res
    def close(self):
        return self.one_session.close()
do_request = HandleRequest()

if __name__ == '__main__':
    url = "http://www.baidu.com"
    method = "ge"
    res = do_request.to_request(url,method=method)
    print(res)