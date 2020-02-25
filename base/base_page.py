"""
PO 文件基类
"""
from utils import DriverUtil


class BasePage(object):
    """对象库层基类"""

    def __init__(self):
        self.driver = DriverUtil.get_driver()  # 获取浏览器对象

    def find_element_func(self, location):
        """
        元素定位方法
        :param location: 元素定位对象
        :return: 元素对象
        """
        return self.driver.find_element(location[0], location[1])


class BaseHandle(object):
    """操作层基类"""

    @staticmethod
    def input_text(element, text):
        """
        元素输入方法
        :param element: 元素对象
        :param text: 输入文本
        :return: 无
        """
        element.clear()  # 清空
        element.send_keys(text)  # 输入

    @staticmethod
    def click_func(element):
        """
        元素点击方法
        :param element: 元素对象
        :return: 无
        """
        element.click()
