"""
支付成功页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class PaymentSuccessPage(BasePage):
    """支付成功--对象库层"""

    def __init__(self):
        super().__init__()  # 获取父类浏览器对象

        self.order_success_message = (By.CLASS_NAME, 'erhuh')

    def find_order_success_message(self):
        """定位订单成功信息方法"""
        return self.find_element_func(self.order_success_message)


class PaymentSuccessHandle(BaseHandle):
    """支付成功--操作层"""

    def __init__(self):
        self.payment_success_page = PaymentSuccessPage()  # 元素定位对象

    def get_order_success_message(self):
        """获取订单成功信息方法"""
        return self.payment_success_page.find_order_success_message().text


class PaymentSuccessProxy(object):
    """支付成功--业务层"""
    def __init__(self):
        self.payment_success_handle = PaymentSuccessHandle() # 元素操作方法

    def get_order_success_message_func(self):
        """订单提交成功信息"""
        return self.payment_success_handle.get_order_success_message()
