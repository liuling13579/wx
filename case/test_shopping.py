#coding:utf-8

from selenium import webdriver
import unittest
from pages.login_wx import Login
from pages.shopping import Shopping
from pages.coupon import Coupon
from common import parm as pa
import time

class ShoppingCartTest(unittest.TestCase):
    '''登录测试用例'''

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.L = Login(cls.driver)
        cls.S = Shopping(cls.driver)
        cls.C = Coupon(cls.driver)
        cls.L.login(pa.loc_name_s,pa.loc_pwd_s)
        time.sleep(2)
        cls.driver.get(pa.host+"/pay/#/shopping")

    def test_01(self):
        '''
        判断总价显示是否正确
        '''
        p1 = self.S.totalprice()
        p2 = self.S.is_totalprice()
        self.assertEquals(p1,p2)


    def test_02(self):
        '''
        本校课程微信订单
        '''
        self.driver.refresh()
        time.sleep(2)
        t = self.S.creatorder()
        self.assertTrue(t)

    def test_03(self):
        '''
        支付宝订单
        '''
        self.driver.refresh()
        time.sleep(2)
        t = self.S.creatorder(2)
        self.assertTrue(t)

    def test_04(self):
        '''
        本校课程-优惠券，支付宝订单
        '''

        self.C.use_coupon(pa.loc_course)
        t = self.S.creatorder(2)
        self.assertTrue(t)

    def test_05(self):
        '''
        本校课程包-优惠券，支付宝订单
        '''

        self.C.use_coupon(pa.loc_bundle,dis=1)
        t = self.S.creatorder(2)
        self.assertTrue(t)

    def test_06(self):
        '''
        共享课程-优惠券，支付宝订单
        '''

        self.C.use_coupon(pa.loc_share_course1,dis=1)
        t = self.S.creatorder(2)
        self.assertTrue(t)

    def test_07(self):
        '''
        共享课程-优惠券，支付宝订单
        '''

        self.C.use_coupon(pa.loc_share_course2,dis=1)
        t = self.S.creatorder(2)
        self.assertTrue(t)

    def test_08(self):
        '''
        共享课程bao-优惠券，支付宝订单
        '''

        self.C.use_coupon(pa.loc_share_bundle1,dis=1)
        t = self.S.creatorder(2)
        self.assertTrue(t)

    def test_09(self):
        '''
        跨平台共享课程bao-优惠券，支付宝订单
        '''
        self.C.use_coupon(pa.loc_share_bundle2,dis=1)
        t = self.S.creatorder(2)
        self.assertTrue(t)



    #
    # def test_04(self):
    #     '''
    #     验证价格更新，金额校验
    #     '''
    #     self.driver.refresh()
    #     time.sleep(2)
    #     t = self.S.creatorder(2)
    #     self.assertTrue(t)
    #
    # def test_05(self):
    #     '''
    #     验证商品删除，金额校验
    #     '''
    #     self.driver.refresh()
    #     time.sleep(2)
    #     t = self.S.creatorder(2)
    #     self.assertTrue(t)

    def tearDown(self):
        self.driver.refresh()
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "main":
    unittest.main()

