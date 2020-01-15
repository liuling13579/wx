#coding:utf-8

from selenium import webdriver
import unittest
from pages.login_wx import Login
from pages.shopping import Shopping
from common import parm as pa
from pages.coupon import Coupon
from pages.course_detail import Course_Detail
from pages.learn_center import LearnCenter
import time

class ShoppingCartTest(unittest.TestCase):
    '''登录测试用例'''

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.L = Login(cls.driver)
        cls.LC = LearnCenter(cls.driver)
        cls.CD = Course_Detail(cls.driver)
        cls.S = Shopping(cls.driver)
        cls.C = Coupon(cls.driver)
        cls.L.login(pa.loc_name_s,pa.loc_pwd_s)
        time.sleep(2)


    def test_01(self):
        '''
        本校课程使用优惠券
        '''
        course_id = self.LC.search_course(pa.loc_course)
        print(course_id)
        self.CD.buy_now()
        p1 = self.S.get_couponprice(course_id=course_id,title=pa.loc_course)
        p2 = self.S.shop_price(pa.loc_course)
        self.assertEquals(p1,p2)

    def test_02(self):
        '''
        本校课程包使用优惠券
        '''
        course_id = self.LC.search_course(pa.loc_bundle)
        self.CD.buy_now()
        p1 = self.S.get_couponprice(course_id=course_id,title=pa.loc_bundle,dis=2)
        p2 = self.S.shop_price(pa.loc_bundle)
        self.assertEquals(p1,p2)

    def test_03(self):
        '''
        跨平台课程使用优惠券
        '''
        course_id = self.LC.search_course(pa.loc_share_course1)
        self.CD.buy_now()
        p1 = self.S.get_couponprice(course_id=course_id,title=pa.loc_share_course1,dis=2,isshare=1)
        p2 = self.S.shop_price(pa.loc_share_course1)
        self.assertEquals(p1,p2)

    # def tearDown(self):
    #     self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "main":
    unittest.main()

