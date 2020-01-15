#coding:utf-8
from common.base import Base
from pages.login_wx import Login
import time

class OpenCourseFw(Base):
    '''开通服务'''
    loc_kf = ("xpath",".//*[@title='客户服务']")
    loc_yf = ("link text","用户服务")
    loc_yl = ("xpath",".//*[@role='tab'][2]")
    loc_1 = ("id","keyword")
    loc_2 = ("xpath","//*[text()='查 询']/..")
    loc_3 = ("link text","更多")
    loc_4 = ("link text","开通服务")
    loc_5 = ("xpath",".//*[@class='courseModule_list-1ybFa '][1]/label")
    loc_6 = ("xpath","//*[text()='确 定']/..")
    loc_13 = ("xpath",".//*[@class='ant-message-notice-content']/div/span")

    # 查询
    loc_7 = ("id","classifyName")
    loc_8 = ("xpath",".//*[contains(@class,'ant-cascader-menus-placement-bottomLeft')]/div/ul[1]/li[1]")
    loc_9 = ("id","course")
    loc_10 = ("xpath",".//*[@role='listbox']/li[1]")
    loc_11 = ("xpath",".//*[@placeholder='搜索课程']")
    loc_12 = ("xpath",".//*[@class='ant-row courseModule_rowForm-28MIM']/div[4]/span/button")



    loc_70 = ("","")

    user1="xiaoman39"

    def user_xc(self,user=user1):
        '''列表查询用户'''
        try:
            self.sendKeys(self.loc_1,user)
            self.click(self.loc_2)
        except:
            return  ""


    def course_xc(self,c):
        '''查询课程
        a;
        课程分类
        b:
        课程：1
        课程包：2
        共享课程：3
        共享课程包;4
        c:
        关键字
        '''
        time.sleep(2)
        self.click(self.loc_7)
        self.click(self.loc_9)
        self.click(self.loc_10)

        self.sendKeys(self.loc_11,c,True)
        self.click(self.loc_12)

    def is_open_success(self):
        '''判断是否开通成功'''
        try:
            t=self.findElementNew(self.loc_13).text
            return t+"ssss"
        except:
            return "获取提示失败"


    def open_course(self,c="课程"):

        self.click(self.loc_kf)
        self.click(self.loc_yf)
        self.click(self.loc_yl)
        self.user_xc()
        time.sleep(1)
        self.move_to_element(self.loc_3)
        self.click(self.loc_4)
        self.course_xc(c)
        time.sleep(1)
        self.click(self.loc_5)
        self.click(self.loc_6)


if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    L = Login(driver)
    L.login()
    Op = OpenCourseFw(driver)
    Op.open_course()
    t=Op.is_open_success()
    print(t)
    driver.quit()





