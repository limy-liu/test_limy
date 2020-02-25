"""
登录测试用例
"""
import json
import unittest
import time

from config import BASE_DIR
from page.index_page import IndexProxy
from page.login_page import LoginProxy
from utils import DriverUtil
from parameterized import parameterized


def build_login_data():
    """登录数据构造方法"""
    # with open('../data/login_data.json', encoding='utf-8') as f:
    with open(BASE_DIR + '/data/login_data.json', encoding='utf-8') as f:
        data = json.load(f)
        data_list = list()
        for i in data:
            data_list.append((i.get('username'),
                              i.get('password'),
                              i.get('code'),
                              i.get('expect')))
        print(data_list)
        return data_list


class TPShopLogin(unittest.TestCase):
    """登录测试用例"""

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()  # 获取浏览器对象
        cls.index_proxy = IndexProxy()  # 首页页面业务执行对象
        cls.login_proxy = LoginProxy()  # 登录页面业务执行对象

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        DriverUtil.quit_driver()  # 退出浏览器对象

    def setUp(self):
        self.driver.get('http://127.0.0.1')  # 打开首页
        self.index_proxy.go_to_login()  # 跳转登录页面

    @parameterized.expand(build_login_data())
    def test_login(self, username, pwd, code, expect):
        """登录测试方法"""
        self.login_proxy.login_func(username, pwd, code)  # 执行登录
        time.sleep(10)
        title = self.driver.title  # 获取页面标题
        print("title：", title)
        self.assertIn(expect, title)  # 断言判断结果


if __name__ == '__main__':
    unittest.main()
