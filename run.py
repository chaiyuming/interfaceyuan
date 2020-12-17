import unittest
from BeautifulReport import BeautifulReport as BR
import time

report_name = time.strftime("%Y-%m-%d-%H-%M-%S")+"-report.html"
if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover(r".\case")
    res = BR(suite)
    res.report("Fecshop接口自动化测试", filename=report_name, log_path=r".\report")
