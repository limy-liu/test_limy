"""
订单支付页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class OrderPaymentPage(BasePage):
    """订单支付--对象库层"""

    def __init__(self):
        super().__init__()  # 获取父类浏览器对象

        self.order_submit_success_message = (By.CLASS_NAME, 'erhuh')  # 订单提交成功信息
        self.select_payment_method = (By.XPATH, '//li[{}]//div[1]//input[1]')  # 货到付款按钮
        self.Confirm_payment_method = (By.LINK_TEXT, '确认支付方式')  # 确认支付方式按钮

    def find_order_submit_success_message(self):
        """定位订单提交成功信息方法"""
        return self.find_element_func(self.order_submit_success_message)

    def find_select_payment_method(self, num):
        """定位选择支付方式按钮方法"""
        location = self.select_payment_method[0], self.select_payment_method[1].format(num)  # 货到付款num=2
        return self.find_element_func(location)

    def find_confirm_payment_method(self):
        """定位确认支付方法按钮方法"""
        return self.find_element_func(self.Confirm_payment_method)


class OrderPaymentHandle(BaseHandle):
    """订单支付--操作层"""

    def __init__(self):
        self.order_payment_page = OrderPaymentPage()  # 元素定位对象

    def get_order_submit_success_message(self):
        """获取订单提交成功方法"""
        return self.order_payment_page.find_order_submit_success_message().text

    def click_select_payment_method(self, num):
        """点击选择支付方式方法"""
        self.click_func(self.order_payment_page.find_select_payment_method(num))

    def click_confirm_payment_method(self):
        """点击确认支付方法方法"""
        self.click_func(self.order_payment_page.find_confirm_payment_method())


class OrderPaymentProxy(object):
    """订单支付--业务层"""

    def __init__(self):
        self.order_payment_handle = OrderPaymentHandle()  # 元素操作对象

    def get_order_submit_success_message_func(self):
        """获取订单"""
        return self.order_payment_handle.get_order_submit_success_message()

    def go_to_payment_success_func(self, num):
        """跳转到支付成功页面"""
        self.order_payment_handle.click_select_payment_method(num)  # 点击选择支付方式
        self.order_payment_handle.click_confirm_payment_method()  # 点击确认支付方式
