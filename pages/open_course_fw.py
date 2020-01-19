#coding:utf-8
from common.base import Base
from pages.login_wx import Login
from common import parm as pa
import time

class OpenCourseFw(Base):
    '''开通服务'''
    loc_kf = ("xpath",".//*[@title='客户服务']")
    loc_yf = ("link text","用户服务")
    loc_yl = ("xpath",".//*[@role='tab'][2]")
    loc_searchUser = ("id","keyword")
    loc_search = ("xpath","//*[text()='查 询']/..")
    loc_more = ("link text","更多")
    loc_more_openFW = ("link text","开通服务")
    loc_choose = ("xpath",".//*[@class='ant-modal-body']/div/div/div[1]/div[1]/label")
    loc_open = ("xpath","//*[text()='确 定']/..")
    loc_tishi = ("xpath",".//*[@class='ant-message-notice-content']/div/span")

    # 查询
    loc_opentype = ("xpath",".//*[@class='ant-modal-content']/div[1]/div/div/div/div")
    loc_opentype_vip = ("xpath",".//*[@role='listbox']/li[2]")

    loc_classify = ("id","classifyName")
    loc_8 = ("xpath",".//*[contains(@class,'ant-cascader-menus-placement-bottomLeft')]/div/ul[1]/li[1]")

    loc_courseType = ("id","course")
    loc_courseTypes = ("xpath",".//*[@role='listbox']/li")
    loc_keyCourse = ("id","keyword_course")
    loc_keyVip = ("id","keyword_vipcard")
    loc_cx_course = ("xpath",".//*[@class='ant-form ant-form-horizontal']/div/div/div[4]/span/button")
    loc_cx_vip = ("xpath",".//*[@class='ant-form ant-form-horizontal']/div/div/div[2]/span/button")



    loc_70 = ("","")

    def searchUser(self,user):
        '''列表查询用户'''
        try:
            self.sendKeys(self.loc_searchUser,user)
            self.click(self.loc_search)
        except:
            return  ""


    def searchCourse(self,courseType,key):
        '''查询课程
        courseType: 课程：0    课程包：1
                    共享课程：2  共享课程包;3
        key: 关键字
        '''
        time.sleep(2)
        self.click(self.loc_courseType)
        self.clicks(self.loc_courseTypes,courseType)

        self.sendKeys(self.loc_keyCourse,key,True)
        self.click(self.loc_cx_course)

    def searchVip(self,key):
        '''查询会员卡
        key: 关键字
        '''
        time.sleep(2)
        self.click(self.loc_opentype)
        self.clicks(self.loc_opentype_vip)
        self.sendKeys(self.loc_keyVip,key,True)
        self.click(self.loc_cx_vip)

    def is_open_success(self):
        '''判断是否开通成功'''
        try:
            t=self.findElementNew(self.loc_tishi).text
            return t
        except:
            return "获取提示失败"


    def open_course(self,key,courseType=0,user=pa.loc_name_s):
        '''
        开通课程
        '''
        self.click(self.loc_kf)
        self.click(self.loc_yf)
        self.click(self.loc_yl)
        self.searchUser(user)
        time.sleep(1)
        self.move_to_element(self.loc_more)
        self.click(self.loc_more_openFW)
        self.searchCourse(courseType,key)
        time.sleep(2)
        self.click(self.loc_choose)
        self.click(self.loc_open)

    def open_vip(self,key,user=pa.loc_name_s):
        '''
        开通会员卡
        '''
        self.click(self.loc_kf)
        self.click(self.loc_yf)
        self.click(self.loc_yl)
        self.searchUser(user)
        time.sleep(1)
        self.move_to_element(self.loc_more)
        self.click(self.loc_more_openFW)
        self.searchVip(key)
        time.sleep(2)
        self.click(self.loc_choose)
        self.click(self.loc_open)


if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    L = Login(driver)
    L.login()
    Op = OpenCourseFw(driver)
    Op.open_course(courseType=3,key='课程')
    t=Op.is_open_success()
    print(t)
    driver.quit()






