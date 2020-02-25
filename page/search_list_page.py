"""
搜索列表页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


# 如果要限定目标元素的显示区域，可以考虑使用xpath层级定位策略
# //*[@class="shop_name2"]/a[contains(text(),'小米手机5')]

class SearchListPage(BasePage):
    """搜索列表-对象库层"""

    def __init__(self):
        super().__init__()  # 获取父类浏览器对象
        # self.goods = (By.XPATH, "//*[@class='shop_name2']/a[contains(text(),'{小米手机5}')]")  # 商品
        self.goods = (By.XPATH, "//*[@class='shop_name2']/a[contains(text(),'{}')]")  # 商品

    def find_goods(self, kw):
        """搜索到的商品定位方法"""
        location = (self.goods[0], self.goods[1].format(kw))
        return self.find_element_func(location)


class SearchListHandle(BaseHandle):
    """搜索列表-操作层"""

    def __init__(self):
        self.search_list = SearchListPage()  # 元素定位对象

    def click_goods(self, kw):
        """商品点击方法"""
        self.click_func(self.search_list.find_goods(kw))


class SearchListProxy(object):
    """搜索列表-业务层"""

    def __init__(self):
        self.search_handle = SearchListHandle()  # 元素操作对象

    def go_to_search_detail(self, kw):
        """跳转商品详情页面方法"""
        self.search_handle.click_goods(kw)
