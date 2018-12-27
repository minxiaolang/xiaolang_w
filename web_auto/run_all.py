#coding=utf-8
import unittest
from common import HTMLTestRunner_cn
#用例的路径
casePath='D:\develop\pycharm\web_auto\case'
rule="test*.py"
discover=unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)

reportPath='D:\\develop\\pycharm\web_auto\\report\\'+'result.html'
fp=open(reportPath,'wb')
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title='报告的名称',description='描述你的报告干什么用哈')
#runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title='报告的名称',description='描述你的报告干什么用哈',retry=1)


runner.run(discover)
fp.close()