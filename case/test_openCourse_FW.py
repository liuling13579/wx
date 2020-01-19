#coding:utf-8

from selenium import webdriver
import unittest
from pages.login_wx import Login
from pages.open_course_fw import OpenCourseFw
from common import parm as pa
import time

class OpenCourseFWTest(unittest.TestCase):
    '''登录测试用例'''

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.L = Login(cls.driver)
        cls.Op = OpenCourseFw(cls.driver)
        cls.L.login()
        time.sleep(2)

    def test_01(self):
        '''
        开通课程
        '''
        self.Op.open_course(courseType=0,key='课程')
        t=self.Op.is_open_success()
        print(t)
        self.assertEqual(t,"开通成功")


    def test_02(self):
        '''
        开通课程包
        '''
        self.Op.open_course(courseType=1,key='课程')
        t=self.Op.is_open_success()
        print(t)
        self.assertEqual(t,"开通成功")

    def test_03(self):
        '''
        开通课程包
        '''
        self.Op.open_course(courseType=2,key='课程')
        t=self.Op.is_open_success()
        print(t)
        self.assertEqual(t,"开通成功")

    def test_04(self):
        '''
        开通课程包
        '''
        self.Op.open_course(courseType=3,key='课程')
        t=self.Op.is_open_success()
        print(t)
        self.assertEqual(t,"开通成功")


    def tearDown(self):
        time.sleep(2)
        self.driver.refresh()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "main":
    unittest.main()

