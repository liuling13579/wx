#coding:utf-8

from common.base import Base
from pages.login_wx import Login
import time

class Message(Base):

    loc_message = ("class name","ant-notification-notice-message")
    loc_closemess =("xpath",".//*[@class='ant-notification-notice-close']/i")

    def is_message_exist(self):
        r = self.isElementExist(self.loc_message)
        if r:
            self.click(self.loc_closemess)
            print ("关闭网校通知")
        else:
            return ""


if __name__=="__main__":
    name="拿破仑蛋糕"
    from selenium import webdriver
    driver = webdriver.Chrome()
    L = Login(driver)
    M = Message(driver)

    L.login("jingzhe88","123456")
    time.sleep(2)
    M.is_message_exist()


