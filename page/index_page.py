"""
首页页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class IndexPage(BasePage):
    """首页-对象库层"""

    def __init__(self):
        super().__init__()  # 获取父类浏览器对象

        self.login_link = (By.LINK_TEXT, '登录')  # 登录链接
        self.search_bar = (By.ID, 'q')  # 搜索框
        self.sch_btn = (By.CLASS_NAME, 'ecsc-search-button')  # 搜索按钮
        self.my_cart_btn = (By.CLASS_NAME, 'c-n')  # 我的购物车按钮
        self.my_order_link = (By.LINK_TEXT, '我的订单')  # 我的订单链接
        self.safe_exit = (By.LINK_TEXT, '安全退出')  # 安全退出

    def find_login_link(self):
        """登录链接定位方法"""
        return self.find_element_func(self.login_link)

    def find_search_bar(self):
        """搜索框定位方法"""
        return self.find_element_func(self.search_bar)

    def find_sch_btn(self):
        """搜索按钮定位方法"""
        return self.find_element_func(self.sch_btn)

    def find_my_cart_btn(self):
        """定位我的购物车按钮方法"""
        return self.find_element_func(self.my_cart_btn)

    def find_my_order_link(self):
        """定位我的订单链接方法"""
        return self.find_element_func(self.my_order_link)

    def find_safe_exit(self):
        """定位安全退出链接方法"""
        return self.find_element_func(self.safe_exit)


class IndexHandle(BaseHandle):
    """首页-操作层"""

    def __init__(self):
        self.index_page = IndexPage()  # 元素定位对象

    def click_login_link(self):
        """登录链接点击方法"""
        self.click_func(self.index_page.find_login_link())

    def input_search_bar(self, kw):
        """搜索框输入方法"""
        self.input_text(self.index_page.find_search_bar(), kw)

    def click_sch_btn(self):
        """搜索按钮点击方法"""
        self.click_func(self.index_page.find_sch_btn())

    def click_my_cart_btn(self):
        """我的购物车点击方法"""
        self.click_func(self.index_page.find_my_cart_btn())

    def click_my_order_link(self):
        """我的订单链接点击方法"""
        self.click_func(self.index_page.find_my_order_link())

    def exist_safe_exit(self):
        """安全退出存在方法"""
        return self.index_page.find_safe_exit().text

    def exist_login_link(self):
        """登录存在"""
        return self.index_page.find_login_link().text


class IndexProxy(object):
    """首页-业务层"""

    def __init__(self):
        self.index_handle = IndexHandle()  # 元素操作对象

    def go_to_login(self):
        """跳转登录页方法"""
        self.index_handle.click_login_link()

    def go_to_search_list(self, kw):
        """跳转商品列表页方法"""
        self.index_handle.input_search_bar(kw)
        self.index_handle.click_sch_btn()

    def go_to_cart(self):
        """跳转到购物车页面"""
        self.index_handle.click_my_cart_btn()

    def go_to_my_order_func(self):
        """跳转到我的订单页面方法"""
        self.index_handle.click_my_order_link()

    def safe_exit_func(self):
        """安全推出"""
        return self.index_handle.exist_safe_exit()

    def login_text_func(self):
        """登录文字"""
        return self.index_handle.exist_login_link()
