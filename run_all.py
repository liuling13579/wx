import unittest
from common import HTMLTestRunner_cn
import  time

# 用例的路径
casePath = "D:\\liuling\\wx\\case"
rule = "test_l*.py"
discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)


t = time.strftime("%Y-%m-%d %H-%M-%S")
reportPath = "D:\liuling\wx\\report\\"+"result%s.html"%t

fp = open(reportPath, "wb")

runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                           title="刘玲—网校自动化测试报告",
                                           description="描述你的报告干什么用",
                                           retry=1)
runner.run(discover)
fp.close()






