"""
公共方法类
"""
from selenium import webdriver

def switch_new_window():
    """切换新窗口方法"""
    driver = DriverUtil.get_driver()
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])


def get_text_element(text):
    """通过特定文字信息定位目标元素方法"""
    xpath = '//*[contains(text(), "{}")]'.format(text)
    driver = DriverUtil.get_driver()
    try:
        element = driver.find_element_by_xpath
        return element
    except Exception:
        return False

class DriverUtil(object):
    """浏览器驱动对象工具类"""

    driver = None  # 驱动对象初始化状态
    status = True # 浏览器对象退出方法附加条件

    @classmethod
    def get_driver(cls):
        """获取驱动对象方法"""
        # 判断浏览器对象不存在时再进行创建操作
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            # 由于判断条件下的代码只会执行一次, 因此将打开和最大化和隐式等待的设置暂时放置到这里
            cls.driver.get('http://127.0.0.1')
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        """退出驱动对象方法"""
        # 判断驱动对象存在时再执行退出操作
        if cls.driver and cls.status:
            cls.driver.quit()
            cls.driver = None

    @classmethod
    def change_quit_status(cls, type):
        """修改浏览器对象附加条件状态方法"""
        cls.status = type


if __name__ == '__main__':
    DriverUtil.get_driver()
    DriverUtil.quit_driver()
