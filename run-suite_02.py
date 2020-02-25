"""
测试套件2（程序入口）
"""
# 导包
import unittest
from script.hm_01_tpshop_login import TPShopLogin
from script.hm_02_tpshop_add_cart import TPShopAddCart
from script.hm_03_tpshop_order import TPShopOrder

# 实例化套件对象
from utils import DriverUtil

suite = unittest.TestSuite()

# 调用方法组装测试用例
suite.addTest(unittest.makeSuite(TPShopLogin))  # 登录脚本
suite.addTest(unittest.makeSuite(TPShopAddCart))  # 添加购物车
suite.addTest(unittest.makeSuite(TPShopOrder))  # 提交订单

# 关闭浏览器对象退出方法
DriverUtil.change_quit_status(False)

# 实例化测试执行对象并调用执行方法
unittest.TextTestRunner().run(suite)

# 打开浏览器对象退出方法
DriverUtil.change_quit_status(True)

# 手动退出浏览器对象
DriverUtil.quit_driver()
