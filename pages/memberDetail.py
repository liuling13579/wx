#coding:utf-8

from common.base import Base
from pages.login_wx import Login
from common import parm as pa
from _decimal import Decimal
import time

class Member(Base):

    #个人中心-会员卡
    loc_member = ("xpath",".//*[@class='ant-card-body']/div[2]/div[1]/div/div/div/div/div/div[4]")
    loc_ismember_exist = ("xpath",".//*[@data-on='true']/div[2]")
    loc_detail = ("xpath",".//*[@data-on='true']/div[2]/div[2]/div/span")


    #会员卡折扣信息
    loc_discount_course = ("xpath",".//*[@class='discount']/span[1]")
    loc_discount_shop = ("xpath",".//*[@class='discount']/span[2]")


    def memberdetail(self):
        '''会员卡详情页,返回会员卡折扣'''
        time.sleep(2)
        c = self.get_text(self.loc_discount_course)
        s = self.get_text(self.loc_discount_shop)
        print(c,s)
        course_discount = Decimal(c[5:-1])*Decimal('0.1')
        shope_discount = Decimal(s[5:-1])*Decimal('0.1')
        return course_discount,shope_discount


    def is_vip(self):
        '''判断用户是否是会员卡用户，是的话，跳转到会员卡详情页，返回折扣，否就返回1'''
        self.driver.get(pa.host+'/myroom/#/personal/purse')
        self.click(self.loc_member)
        isexist =self.isElementExist(self.loc_ismember_exist)
        if isexist :
            self.move_to_element(self.loc_ismember_exist)
            self.click(self.loc_detail)
            handles = self.driver.window_handles
            self.switch_handle(handles[-1])
            time.sleep(1)
            course_discount,shope_discount=self.memberdetail()
            return course_discount,shope_discount
        else:
            print("该用户非会员")
            discount_course = 1
            discount_shop =1
            return discount_course,discount_shop



if __name__=="__main__":
    name="测试课件收费课程"
    from selenium import webdriver
    driver = webdriver.Chrome()
    L = Login(driver)
