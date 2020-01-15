#coding:utf-8

from pages.login_wx import Login
from common import parm as pa
from common.base import Base
from pages.message import Message
import time

class LearnCenter(Base):

    loc_learncenter = ("link text","学习中心")
    loc_xuanke = ("xpath",".//*[@class='ant-tabs-nav ant-tabs-nav-animated']/div/div[2]")
    loc_notice = ("class name","ant-notification-notice-content")
    loc_search = ("xpath",".//*[@title='搜索']") #搜索课程
    loc_input = ("xpath",".//*[@class='filterrig']/../div[1]/div/input")
    loc_course = ("xpath",".//*[@class='ant-list ant-list-split ant-list-grid']/div/div/div/div/div/div/div")
    loc_alt = ("xpath",".//*[@class='ant-modal-body']/div/img") #温馨提示
    loc_closealt = ("xpath",".//*[@class='ant-modal-body']/div/div")  #关闭弹窗
    loc_title = ("xpath",".//*[@class='ant-card-body']/div[1]/div/div/p")

    def search_course(self,coursename):
        '''学习中心搜索课程,成功返回课程id，失败返回‘’'''
        time.sleep(2)
        self.driver.get(pa.host+"/myroom/#/main")
        time.sleep(2)
        try:
            self.click(self.loc_learncenter)
            self.click(self.loc_xuanke)
            M = Message(self.driver)
            M.is_message_exist()
            time.sleep(1)
            self.click(self.loc_search)
            # print ("点击了")
            self.sendKeys(self.loc_input,coursename)
            time.sleep(1)
            self.click(self.loc_course)
            handles=self.driver.window_handles
            self.switch_handle(handles[-1])
            #获取页面courseid
            course_id= self.get_course_id()
            return course_id
        except:
            print("查询失败")
            return ""

    def get_course_id(self):
        '''获取页面课程id'''
        course_url = self.driver.current_url
        a =course_url.split("=",1)[1]
        course_id= a.split('&')[0]
        return course_id

    def is_alt_exist(self):
        print ("1")
        r = self.isElementExist(self.loc_alt)
        print(r)
        print ("2")
        if r:
            print ("3")
            js='document.getElementsByClassName("ant-modal-wrap")[0].scrollTop=10000'
            self.driver.execute_script(js)
            self.click(self.loc_closealt)
            print ("关闭温馨提示")
        else:
            return ""

    def is_open_free_course_succesee(self):
        '''判断课程是否已开通'''
        time.sleep(5)
        M = Message(self.driver)
        M.is_message_exist()
        time.sleep(1)
        self.is_alt_exist()
        t = self.get_text(self.loc_title)
        return t



if __name__=="__main__":
    name="拿破仑蛋糕"
    from selenium import webdriver
    driver = webdriver.Chrome()
    L = Login(driver)
    LC = LearnCenter(driver)

    L.login("jingzhe21","123456")
    time.sleep(2)
    LC.search_course(name)