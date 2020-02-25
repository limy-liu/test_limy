"""
购物车--测试用例
"""
import unittest
import time
from page.goods_detail_page import GoodsDetailProxy
from page.index_page import IndexProxy
from page.login_page import LoginProxy
from page.my_count_page import MyCountProxy
from page.search_list_page import SearchListProxy
from utils import DriverUtil


class TPShopAddCart(unittest.TestCase):
    """购物车测试用例类"""

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver() # 获取浏览器对象
        cls.index_proxy = IndexProxy() # 首页页面业务执行对象
        cls.login_proxy = LoginProxy()
        cls.search_list_proxy = SearchListProxy() # 搜索列表页面业务执行对象
        cls.goods_detail_proxy = GoodsDetailProxy()# 商品详情页面业务执行对象
        cls.my_count_proxy = MyCountProxy()

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver() # 退出浏览器对象

    def setUp(self):
        self.driver.get('http://127.0.0.1')# 打开首页
        # self.index_proxy.go_to_login()
        # self.login_proxy.login_func('18955768578', '123456', '8888')
        # time.sleep(5)
        # self.my_count_proxy.go_to_index_func()

    def test_add_cart(self):
        """加入购物车方法"""
        self.index_proxy.go_to_search_list('小米手机')# 搜索商品
        time.sleep(3)
        self.search_list_proxy.go_to_search_detail('小米手机5')# 跳转商品详情
        time.sleep(3)
        self.goods_detail_proxy.join_cart_func()# 添加购物车
        time.sleep(3)

        # frame切换
        # frame1 = self.driver.find_element_by_tag_name('iframe')
        frame1 = self.goods_detail_proxy.get_frame1_func()
        self.driver.switch_to.frame(frame1)

        # 断言
        time.sleep(5)
        msg = self.goods_detail_proxy.get_add_cart_result_func()
        time.sleep(8)
        print("msg:", msg)
        self.assertIn('添加成功', msg)


if __name__ == '__main__':
    unittest.main()
