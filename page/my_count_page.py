"""
我的账户页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class MyCountPage(BasePage):
    """我的账户--对象库层"""

    def __init__(self):
        super().__init__()  # 获取父类的浏览器对象

        self.index_link = (By.LINK_TEXT, '首页')  # 首页链接

    def find_index_link(self):
        """定位首页链接方法"""
        return self.find_element_func(self.index_link)


class MyCountHandle(BaseHandle):
    """我的账户--操作层"""

    def __init__(self):
        self.my_count_page = MyCountPage()  # 元素定位对象

    def click_index_link(self):
        """点击首页链接方法"""
        self.click_func(self.my_count_page.find_index_link())


class MyCountProxy(object):
    """我的账户--业务层"""
    def __init__(self):
        self.my_count_handle = MyCountHandle() # 元素操作对象

    def go_to_index_func(self):
        """跳转首页链接方法"""
        self.my_count_handle.click_index_link()

