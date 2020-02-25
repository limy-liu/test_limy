"""
登录页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class LoginPage(BasePage):
    """登录-对象库层"""

    def __init__(self):
        super().__init__()  # 获取父类浏览器方法

        self.username = (By.ID, 'username')  # 用户名
        self.pwd = (By.ID, 'password')  # 密码
        self.code = (By.ID, 'verify_code')  # 验证码
        self.login_btn = (By.NAME, 'sbtbutton')  # 登录按钮

    def find_username(self):
        """用户名定位方法"""
        return self.find_element_func(self.username)

    def find_pwd(self):
        """密码定位方法"""
        return self.find_element_func(self.pwd)

    def find_code(self):
        """验证码定位方法"""
        return self.find_element_func(self.code)

    def find_login_btn(self):
        """登录按钮定位方法"""
        return self.find_element_func(self.login_btn)


class LoginHandle(BaseHandle):
    """登录-操作层"""

    def __init__(self):
        self.login_page = LoginPage()  # 元素定位对象

    def input_username(self, username):
        """用户名输入方法"""
        self.input_text(self.login_page.find_username(), username)

    def input_pwd(self, pwd):
        """密码输入方法"""
        self.input_text(self.login_page.find_pwd(), pwd)

    def input_code(self, code):
        """验证码输入方法"""
        self.input_text(self.login_page.find_code(), code)

    def click_login_btn(self):
        """登录按钮点击方法"""
        self.click_func(self.login_page.find_login_btn())


class LoginProxy(object):
    """登录-业务层"""

    def __init__(self):
        self.login_handle = LoginHandle()  # 元素操作对象

    def login_func(self, username, pwd, code):
        """登录功能方法"""
        self.login_handle.input_username(username)  # 输入用户名
        self.login_handle.input_pwd(pwd)  # 输入密码
        self.login_handle.input_code(code)  # 输入验证码
        self.login_handle.click_login_btn()  # 点击登录按钮
