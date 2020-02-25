"""
购物车页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class CartPage(BasePage):
    """购物车--对象库层"""

    def __init__(self):
        super().__init__()

        self.check_all = (By.CLASS_NAME, 'checkCartAll')  # 全选框
        self.go_settlement_btn = (By.LINK_TEXT, '去结算')  # 去结算按钮

    def find_check_all(self):
        """全选框定位方法"""
        return self.find_element_func(self.check_all)

    def find_go_settlement_btn(self):
        """定位去结算按钮方法"""
        return self.find_element_func(self.go_settlement_btn)


class CartHandle(BaseHandle):
    """购物车--操作层"""

    def __init__(self):
        self.cart_page = CartPage()  # 定位元素对象

    def click_check_all(self):
        """全选框点击方法"""
        check_element = self.cart_page.find_check_all()
        # 判断全选框未选中时点击
        if not check_element.is_selected():
            self.click_func(check_element)

    def click_go_settlement_btn(self):
        """点击去结算按钮方法"""
        self.click_func(self.cart_page.find_go_settlement_btn())


class CartProxy(object):
    """购物车--业务层"""

    def __init__(self):
        self.cart_handle = CartHandle()  # 元素操作对象

    def go_to_check_order_func(self):
        """跳转到提交订单页面"""
        self.cart_handle.click_check_all()  # 确认全选
        self.cart_handle.click_go_settlement_btn()  # 点击去结算
