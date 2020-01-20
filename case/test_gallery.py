#coding:utf-8

from selenium import webdriver
import unittest
from pages.login_wx import Login
from pages.gallery_add import Gallery
import  time

class Gallery_Add(unittest.TestCase):
    '''登录测试用例'''

    timestr = time.strftime("%d_%H_%M_%S")
    name="桃花酥"+timestr

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.L = Login(cls.driver)
        cls.G = Gallery(cls.driver)
        cls.L.login()

    def test_01(self):
        '''
        新增商品
        '''
        name=self.G.add_gallery(self.name)
        n = self.G.is_gallery()
        print(n)
        self.assertEquals(name,n)

    # def test_02(self):
    #     '''
    #     上架
    #     '''
    #     self.G.gallery_operate(1)
    #     r=self.G.is_on_sale_sucess()
    #     print(r)
    #     self.assertEquals(r,"销售中")
    #
    #
    # def test_03(self):
    #     '''
    #     下架
    #     '''
    #     self.G.gallery_operate(2)
    #     r=self.G.is_on_sale_sucess()
    #     print(r)
    #     self.assertEquals(r,"已下架")
    #
    # def test_04(self):
    #     '''
    #     删除
    #     '''
    #     self.G.gallery_operate(3)
    #     r=self.G.is_gallery()
    #     print(r)
    #     self.assertNotEqual(r,self.name)




    def tearDown(self):
        # self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "main":
    unittest.main()

