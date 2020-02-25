"""
核对订单页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class CheckOrderPage(BasePage):
    """核对订单--对象库层"""

    def __init__(self):
        super().__init__()  # 获取父类浏览器对象

        self.submit_order_btn = (By.CLASS_NAME, 'Sub-orders')  # 提交订单按钮

    def find_submit_order_btn(self):
        """定位提交订单按钮方法"""
        return self.find_element_func(self.submit_order_btn)


class CheckOrderHandle(BaseHandle):
    """核对订单--操作层"""

    def __init__(self):
        self.check_order_page = CheckOrderPage()  # 元素定位对象

    def click_submit_order_btn(self):
        """点击提交订单方法"""
        self.click_func(self.check_order_page.find_submit_order_btn())


class CheckOrderProxy(object):
    """核对订单--业务层"""

    def __init__(self):
        self.check_order_handle = CheckOrderHandle()  #元素操作对象

    def go_to_order_payment_func(self):
        """跳转到订单支付页面方法"""
        self.check_order_handle.click_submit_order_btn()

