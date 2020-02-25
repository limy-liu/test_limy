"""
商品详情页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle
from utils import DriverUtil


class GoodsDetailPage(BasePage):
    """商品详情-对象库层"""

    def __init__(self):
        super().__init__()  # 获取父类浏览器对象

        self.add_cart_btn = (By.ID, 'join_cart')  # 加入购物车
        self.add_cart_result = (By.CSS_SELECTOR, '.conect-title > span:nth-child(1)')  # 加入购物车结果
        self.frame1 = (By.TAG_NAME, 'iframe')  # 定位frame

    def find_add_cart_btn(self):
        """定位加入购物车方法"""
        return self.find_element_func(self.add_cart_btn)

    def find_add_cart_result(self):
        """定位加入购物车结果方法"""
        return self.find_element_func(self.add_cart_result)

    def find_frame1(self):
        """定位frame"""
        return self.find_element_func(self.frame1)


class GoodsDetailHandle(BaseHandle):
    """商品详情-操作层"""

    def __init__(self):
        self.goods_detail_page = GoodsDetailPage()  # 元素对象

    def click_add_cart_btn(self):
        """加入购物车点击方法"""
        self.click_func(self.goods_detail_page.find_add_cart_btn())

    def get_add_cart_result(self):
        """加入购物车结果获取"""
        # frame切换
        # driver = DriverUtil.get_driver() # 获取浏览器对象
        # frame_element = driver.find_element_by_tag_name('iframe')
        # driver.switch_to.frame(frame_element)
        return self.goods_detail_page.find_add_cart_result().text

    def get_frame1(self):
        """frame元素定位"""
        return self.goods_detail_page.find_frame1()


class GoodsDetailProxy(object):
    """商品详情-业务层"""

    def __init__(self):
        self.goods_detail_handle = GoodsDetailHandle()  # 元素定位方法

    def join_cart_func(self):
        """加入购物车方法"""
        self.goods_detail_handle.click_add_cart_btn()

    def get_add_cart_result_func(self):
        """获取加入购物车结果方法"""
        return self.goods_detail_handle.get_add_cart_result()

    def get_frame1_func(self):
        """frame元素定位"""
        return self.goods_detail_handle.get_frame1()
