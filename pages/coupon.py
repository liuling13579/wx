#coding:utf-8

from common.base import Base
from pages.login_wx import Login
from common.sql_connect import SQL_conn
from pages.learn_center import LearnCenter
from pages.get_school import School
from common import parm as pa
from _decimal import Decimal
import time

class Coupon(Base):

    loc_coupon = ("xpath",".//*[@class='ant-spin-container']/span/div/div/span/div/div/div[2]/div[2]") #优惠券标签
    loc_titl5e = ("xpath",".//*[@class='ant-spin-container']/span/div/div/span/div/div[2]/div[1]/div[1]")  #课程标题
    loc_coupon_daijin = ("xpath",".//*[@class='card_coupon___1Lm6S left___2RtmO']")  #
    loc_coupon_dis = ("xpath",".//*[@class='card_discount___c3Gl0 left___2RtmO']")  #
    loc_coupon_discount = ("xpath",".//*[@role='document']/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div[1]")
    loc_price1 = ("xpath",".//*[@class='ant-spin-container']/span/div/div/span/div/div[2]/div[1]/div[2]/span[3]")  #购物车商品原价，返回多个元素
    loc_price2 = ("xpath",".//*[@class='ant-spin-container']/span/div/div/span/div/div[2]/div[1]/div[2]/span[2]")  #购物车商品价格，返回多个元素
    loc_ok = ("xpath",".//*[@class='ant-btn ant-btn-primary']")  #确定

    def shop_order(self,title):
        '''商品位于购物车位置'''
        time.sleep(2)
        eles_title = self.findElementsNew(self.loc_titl5e)
        time.sleep(2)
        L = len(eles_title)
        print('hahhhhhhh',L)
        n = 0
        for i in range(L):
            t = eles_title[i].text
            if title == t:
                print("商品位于第:",i+1)
                n = i
                print(eles_title[i].text)
                break
        return n

    def get_oldprice(self,n):
        '''获取页面课程原价'''
        exist = self.isElementExist2(self.loc_price1)
        if exist:
            eles_oldprice = self.findElementsNew(self.loc_price1)
        else:
            eles_oldprice = self.findElementsNew(self.loc_price2)
        print(eles_oldprice)
        p=eles_oldprice[n].text
        price = Decimal(p[1:])*100
        print("原价是：",price)
        return price

    def use_coupon(self,title,dis=1):
        '''使用优惠券'''
        n = self.shop_order(title)
        time.sleep(1)
        eles_coupon = self.findElementsNew(self.loc_coupon)
        eles_coupon[n].click()
        if dis == 1:
            try:
                lcu= self.findElementsNew(self.loc_coupon_dis)
                lcu[0].click()  #默认选择第一个匹配的优惠券
            except:
                print("用户暂时无折扣优惠券")
        else:
            try:
                lcu= self.findElementsNew(self.loc_coupon_daijin)
                lcu[0].click()  #默认选择第一个匹配的优惠券
            except:
                print("用户暂时无满减优惠券")
        time.sleep(1)
        self.click(self.loc_ok)
        time.sleep(2)

    def choose_coupon(self,title,dis=1):
        '''选择使用优惠券
        n:该商品位于购物车第i+1个    dis:1折扣优惠，2满减优惠
        '''
        n = self.shop_order(title)
        time.sleep(1)
        eles_coupon = self.findElementsNew(self.loc_coupon)
        #获取课程原价
        old_price = self.get_oldprice(n)
        eles_coupon[n].click()
        time.sleep(1)
        lcu= self.findElementsNew(self.loc_coupon_discount)
        try:
            if dis == 1:
                for i in range(len(lcu)):
                    t = lcu[i].text
                    if  '折' in t :
                        discount = Decimal(t[:-1])*Decimal(0.1)
                        price = int(old_price * discount)
                        lcu[i].click()
                        break
            else:
                for i in range(len(lcu)):
                    t = lcu[i].text
                    if  '¥' in t :
                        discount = Decimal(t[1:])*100
                        price = old_price - discount
                        lcu[i].click()
                        break
            print("使用优惠券,以及使用之后价格：",t,price)
            self.click(self.loc_ok)
            return price
        except:
            print("用户暂无该类型优惠券")
            return ''

    def choose_coupon_old(self,title,dis=1):
        '''选择使用优惠券
        n:该商品位于购物车第i+1个    dis:1折扣优惠，2满减优惠
        '''
        n = self.shop_order(title)
        time.sleep(1)
        eles_coupon = self.findElementsNew(self.loc_coupon)
        #获取课程原价
        old_price = self.get_oldprice(n)
        eles_coupon[n].click()
        time.sleep(1)
        try:
            if dis == 1:
                try:
                    lcu= self.findElementsNew(self.loc_coupon_dis)
                    print(lcu)
                    lcu[0].click()  #默认选择第一个匹配的优惠券
                    t = lcu[0].text
                    discount = Decimal(t[:-1])*Decimal(0.1)
                    price = int(old_price * discount)
                    print("用户使用优惠券为",t)
                except:
                    price = -99999
                    print("用户暂时无折扣优惠券")
            else:
                try:
                    lcu= self.findElementsNew(self.loc_coupon_daijin)
                    print(lcu)
                    lcu[0].click()  #默认选择第一个匹配的优惠券
                    t = lcu[0].text
                    discount = Decimal(t[1:])*100
                    price = old_price - discount
                    print("用户使用优惠券为",t)
                except:
                    price = -99999
                    print("用户暂时无满减优惠券")
            print("使用优惠券之后价格：",price)
            self.click(self.loc_ok)
            return price
        except:
            print("用户暂无的优惠券")



    def shop_price(self,title):
        '''使用优惠券之后商品页面价格'''
        n = self.shop_order(title)
        eles_price = self.findElementsNew(self.loc_price2)
        p = eles_price[n].text
        price = Decimal(p[1:])*100
        return price


if __name__ =="__main__":
    name="哐当哐当哐当哐当哐当哐当哐当"
    from selenium import webdriver
    driver = webdriver.Chrome()
    L = Login(driver)
    C = Coupon(driver)
    L.login("shibing5","123456")
    time.sleep(2)
    driver.get(pa.host+"/pay/#/shopping")
    time.sleep(2)
    C.choose_coupon('测试课件收费课程',dis=2)
    # i=C.shop_order("哐当哐当哐当哐当哐当哐当哐当")
    # print(i)
    # p1=C.choose_coupon("哐当哐当哐当哐当哐当哐当哐当")
    # p1 = C.get_couponprice(title=name)
    # print(p1)
    # p2=C.use_coupon_price(i)
    # print(p1,p2)




