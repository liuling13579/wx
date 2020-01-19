#coding:utf-8

from selenium import webdriver
import unittest
from pages.login_wx import Login
from pages.course_detail import Course_Detail
from pages.learn_center import LearnCenter
from pages.memberDetail import Member
from pages.shopping import Shopping
from common import parm as pa
import time

class CourseDetailTest(unittest.TestCase):
    '''课程详情页面测试用例'''

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.L = Login(cls.driver)
        cls.LC = LearnCenter(cls.driver)
        cls.CD = Course_Detail(cls.driver)
        cls.M = Member(cls.driver)
        cls.S = Shopping(cls.driver)
        cls.L.login(pa.loc_name_s,pa.loc_pwd_s)
        time.sleep(2)
        cls.course_discount,cls.shope_discount=cls.M.is_vip()
        print("会员折扣是：",cls.course_discount,cls.shope_discount)

    def test_01(self):
        '''
        本校课程价格校验
        '''
        courseid = self.LC.search_course(pa.loc_course)
        p1 = self.CD.get_price()
        p2 = self.S.get_vipprice(courseid,self.course_discount,isshare=0)
        print(p1,p2)
        self.assertEquals(p1,p2)


    def test_02(self):
        '''
        平台内共享课程价格校验
        '''
        courseid = self.LC.search_course(pa.loc_share_course1)
        p1 = self.CD.get_price()
        p2 = self.S.get_vipprice(courseid,self.course_discount,isshare=0)
        print(p1,p2)
        self.assertEquals(p1,p2)

    def test_03(self):
        '''
        跨平台共享课程价格校验
        '''
        courseid = self.LC.search_course(pa.loc_share_course2)
        p1 = self.CD.get_price()
        p2 = self.S.get_vipprice(courseid,self.course_discount,isshare=1)
        print(p1,p2)
        self.assertEquals(p1,p2)

    def test_11(self):
        '''
        课程bao价格校验
        '''
        courseid = self.LC.search_course(pa.loc_bundle)
        p1 = self.CD.get_price()
        p2 = self.S.get_vipprice(courseid,self.course_discount,isshare=0)
        print(p1,p2)
        self.assertEquals(p1,p2)

    def test_12(self):
        '''
        平台内共享课程bao价格校验
        '''
        courseid = self.LC.search_course(pa.loc_share_bundle1)
        p1 = self.CD.get_price()
        p2 = self.S.get_vipprice(courseid,self.course_discount,isshare=1)
        print(p1,p2)
        self.assertEquals(p1,p2)

    def test_13(self):
        '''
        跨平台共享课程bao价格校验
        '''
        courseid = self.LC.search_course(pa.loc_share_bundle2)
        p1 = self.CD.get_price()
        p2 = self.S.get_vipprice(courseid,self.course_discount,isshare=1)
        print(p1,p2)
        self.assertEquals(p1,p2)


    def test_04(self):
        '''
        购买免费课程
        '''
        self.LC.search_course(pa.loc_freecourse)
        t = self.CD.openCourse()
        self.assertIn(pa.loc_freecourse,t)

    def test_05(self):
        '''
        添加购物车，本校课程
        '''
        self.LC.search_course(pa.loc_course)
        t = self.CD.shoppingcart()
        self.assertTrue(t)

    def test_06(self):
        '''
        添加购物车，平台内共享课程
        '''
        self.LC.search_course(pa.loc_share_course1)
        t = self.CD.shoppingcart()
        self.assertTrue(t)

    def test_07(self):
        '''
        添加购物车，跨平台共享课程
        '''
        self.LC.search_course(pa.loc_share_course2)
        t = self.CD.shoppingcart()
        self.assertTrue(t)

    def test_14(self):
        '''
        添加购物车，共享课程bao
        '''
        self.LC.search_course(pa.loc_bundle)
        t = self.CD.shoppingcart()
        self.assertTrue(t)

    def test_15(self):
        '''
        添加购物车，平台内共享课程bao
        '''
        self.LC.search_course(pa.loc_share_bundle1)
        t = self.CD.shoppingcart()
        self.assertTrue(t)

    def test_16(self):
        '''
        添加购物车，跨平台共享课程bao
        '''
        self.LC.search_course(pa.loc_share_bundle2)
        t = self.CD.shoppingcart()
        self.assertTrue(t)

    def test_08(self):
        '''
        立即购买收费课程，跳转至购物车
        课程存在，且课程价格相等
        '''
        self.LC.search_course(pa.loc_course)
        price1,title1 = self.CD.openCourse()
        price2 = self.S.shop_price(title1)
        self.assertEquals(price1,price2)


    def test_09(self):
        '''
        立即购买平台内共享课程，跳转至购物车
        课程存在，且课程价格相等
        '''
        self.LC.search_course(pa.loc_share_course1)
        price1,title1 = self.CD.openCourse()
        price2 = self.S.shop_price(title1)
        self.assertEquals(price1,price2)



    def test_10(self):
        '''
        立即购买跨平台共享课程，跳转至购物车
        课程存在，且课程价格相等
        '''
        self.LC.search_course(pa.loc_share_course2)
        price1,title1 = self.CD.openCourse()
        price2 = self.S.shop_price(title1)
        self.assertEquals(price1,price2)

    def test_17(self):
        '''
        立即购买跨平台共享课程，跳转至购物车
        课程存在，且课程价格相等
        '''
        self.LC.search_course(pa.loc_bundle)
        price1,title1 = self.CD.openCourse()
        price2 = self.S.shop_price(title1)
        self.assertEquals(price1,price2)

    def test_18(self):
        '''
        立即购买跨平台共享课程，跳转至购物车
        课程存在，且课程价格相等
        '''
        self.LC.search_course(pa.loc_share_bundle1)
        price1,title1 = self.CD.openCourse()
        price2 = self.S.shop_price(title1)
        self.assertEquals(price1,price2)

    def test_19(self):
        '''
        立即购买跨平台共享课程，跳转至购物车
        课程存在，且课程价格相等
        '''
        self.LC.search_course(pa.loc_share_bundle2)
        price1,title1 = self.CD.openCourse()
        price2 = self.S.shop_price(title1)
        self.assertEquals(price1,price2)



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "main":
    unittest.main()

