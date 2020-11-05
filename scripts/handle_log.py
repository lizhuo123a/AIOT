# ======================
# -*- coding: utf-8 -*-
# @author:LiZhuo
# @time  :2020/10/12 13:50
# @email :358840393@qq.com
# 今天的你要比昨天的你更优秀！
# ======================
import logging
from scripts.constants import LOGS_FILE_PATH
import sys
sys.path.append("..")
class HandleLogger:
    def __init__(self):
        self.case_logger = logging.getLogger("case")
        if not self.case_logger.handlers:
            self.case_logger.setLevel("DEBUG")
            self.console_handle = logging.StreamHandler()
            self.file_handle = logging.FileHandler(LOGS_FILE_PATH,encoding="utf8")
            self.console_handle.setLevel("WARNING")
            self.file_handle.setLevel("DEBUG")
            self.simple_format = logging.Formatter("%(asctime)s - [%(levelname)s]- msg:%(message)s -%(module)s - "
                                                   "%(lineno)d")
            self.verbose_format = logging.Formatter("%(asctime)s -[%(module)s]- [%(levelname)s]- msg:%(message)s"
                                                    "-%(name)s - %(lineno)d")
            self.console_handle.setFormatter(self.simple_format)
            self.file_handle.setFormatter(self.verbose_format)
            self.case_logger.addHandler(self.console_handle)
            self.case_logger.addHandler(self.file_handle)

    def get_logger(self):
        return self.case_logger
if __name__ == "__main__":
    get_logger = HandleLogger().get_logger()
    get_logger.debug("这是个DEBUG级别的日志")
    get_logger.critical("这是个critical级别的日志")
