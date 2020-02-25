"""
下订单-支付--测试用例
"""
import unittest
import time
from page.cart_page import CartProxy
from page.check_order_page import CheckOrderProxy
from page.index_page import IndexProxy
from page.login_page import LoginProxy
from page.my_count_page import MyCountProxy
from page.my_order_page import MyOrderProxy
from page.order_payment_page import OrderPaymentProxy
from page.payment_success_page import PaymentSuccessProxy
from utils import DriverUtil, get_text_element, switch_new_window


class TPShopOrder(unittest.TestCase):
    """下订单-支付测试类"""

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()  # 获取浏览器对象
        cls.index_proxy = IndexProxy()  # 首页页面业务执行对象
        cls.login_proxy = LoginProxy()
        cls.cart_proxy = CartProxy()  # 购物车页面业务执行对象
        cls.check_order_proxy = CheckOrderProxy()  # 订单确认页面业务执行对象
        cls.order_payment_proxy = OrderPaymentProxy()  # 订单支付页面执行对象
        cls.my_count_proxy = MyCountProxy()
        cls.my_order_proxy = MyOrderProxy()  # 我的订单页面业务执行对象
        cls.payment_success_proxy = PaymentSuccessProxy()

        # cls.index_proxy.go_to_login()  # 进入登陆页面
        # cls.login_proxy.login_func('18955768578', '123456', '8888')  # 登录账号
        # time.sleep(3)
        # cls.my_count_proxy.go_to_index_func()  # 调转到首页
        # time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        DriverUtil.quit_driver()  # 退出浏览器对象

    def setUp(self):
        self.driver.get('http://127.0.0.1')  # 打开首页
        time.sleep(3)

    def test_01order(self):
        """下订单测试方法"""
        self.index_proxy.go_to_cart()  # 点击购物车
        time.sleep(3)
        self.cart_proxy.go_to_check_order_func()  # 点击去结算跳转到核对订单页面
        time.sleep(3)
        self.check_order_proxy.go_to_order_payment_func()  # 点击提交订单跳转到支付页面
        time.sleep(8)

        # msg = self.order_payment_proxy.get_order_submit_success_message_func()  # 获取提交结果
        # print('msg:', msg)
        # self.assertIn('订单提交成功，请您尽快付款', msg)  # 断言判断
        # time.sleep(8)

        result = get_text_element('订单提交成功')  # 获取提交结果
        print('result=', result)
        self.assertTrue(result)  # 断言判断

    def test_02payment(self):
        """支付方法"""
        self.index_proxy.go_to_my_order_func()  # 点击我的订单
        time.sleep(3)

        # 转换窗口1-句柄
        switch_new_window()
        time.sleep(3)
        # handles1 = self.driver.window_handles
        # print(handles1)
        # self.driver.switch_to.window(handles1[-1])  # 转换窗口

        self.my_order_proxy.go_to_order_payment_func()  # 点击待付款，点击立即支付
        time.sleep(3)

        # 转换窗口2-句柄
        switch_new_window()
        time.sleep(3)
        # handles2 = self.driver.window_handles
        # print(handles2)
        # self.driver.switch_to.window(handles2[2])  # 转换窗口

        self.order_payment_proxy.go_to_payment_success_func(2)  # 点击付款方式、确认支付方式

        time.sleep(8)
        msg = self.payment_success_proxy.get_order_success_message_func()
        print('msg:', msg)  # 获取支付成功信息
        self.assertIn('订单提交成功，我们将在第一时间给你发货', msg)  # 断言


if __name__ == '__main__':
    unittest.main()
