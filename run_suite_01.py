"""
测试套件(测序入口)
"""
import unittest
from tool.HTMLTestRunnerCN import HTMLTestReportCN  # 中文模板

suite = unittest.defaultTestLoader.discover('./script/', pattern='hm*.py')

report_name = './report/tpshop_main_process.html'

with open(report_name, 'wb') as f:
    runner = HTMLTestReportCN(stream=f,
                              verbosity=2,
                              title='TPShop_Main_Process Web自动化测试报告',
                              description='系统: macOS, 浏览器: 谷歌浏览器, 语言: Python',
                              tester='limy')
    runner.run(suite)






