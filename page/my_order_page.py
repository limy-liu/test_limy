"""
我的订单页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class MyOrderPage(BasePage):
    """我的订单--对象库层"""

    def __init__(self):
        super().__init__()  # 获取父类浏览器对象

        self.wait_payment = (By.LINK_TEXT, '待付款')  # 待付款
        self.pay_now_btn = (By.LINK_TEXT, '立即支付')  # 立即支付

    def find_wait_payment(self):
        """定位待付款链接方法"""
        return self.find_element_func(self.wait_payment)

    def find_pay_now_btn(self):
        """定位立即支付按钮方法"""
        return self.find_element_func(self.pay_now_btn)


class MyOrderHandle(BaseHandle):
    """我的订单--操作层"""

    def __init__(self):
        self.my_order_page = MyOrderPage()  # 元素定位对象

    def click_wait_payment(self):
        """点击待付款方法"""
        self.click_func(self.my_order_page.find_wait_payment())

    def click_pay_now_btn(self):
        """点击立即支付按钮方法"""
        self.click_func(self.my_order_page.find_pay_now_btn())


class MyOrderProxy(object):
    """我的订单--业务层"""

    def __init__(self):
        self.my_order_handle = MyOrderHandle()  # 元素操作对象

    def go_to_order_payment_func(self):
        """跳转到订单支付页面方法"""
        self.my_order_handle.click_wait_payment()  # 点击待付款
        self.my_order_handle.click_pay_now_btn()  # 点击立即支付
