#coding:utf-8

from selenium import webdriver
import unittest
from pages.login_wx import Login

class LoginTest(unittest.TestCase):
    '''登录测试用例'''

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.L = Login(cls.driver)

    def test_01(self):
        '''
        "yingxiong","123456"
        '''
        self.L.login("yingxiong","123456")
        t = self.L.get_login_username()
        print("获取的结果：%s"%t)
        self.assertIn("yingxiong",t)

    def test_02(self):
        '''
        "xiaoman88","123456"
        '''
        self.L.login("xiaoman88","123456")
        t = self.L.get_login_username()
        print("获取的结果：%s"%t)
        self.assertIn("xiaoman88",t)


    def test_03(self):
        '''
        "",""
        '''
        self.L.login("","")
        a= self.L.get_alert_text()
        print("提示：%s"%a)
        self.assertIsNot(a,"")

    def test_04(self):
        '''
        "yingxiong2","123456"
        '''
        self.L.login("yingxiong2","123456")
        a=self.L.get_alert_text()
        print("提示：%s"%a)
        self.assertIsNot(a,"")



    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "main":
    unittest.main()

