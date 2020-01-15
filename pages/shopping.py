#coding:utf-8

from common.base import Base
from pages.login_wx import Login
from common.sql_connect import SQL_conn
from common import parm as pa
from pages.get_school import School
from pages.coupon import Coupon
from _decimal import Decimal
import time

class Shopping(Base):

    #购物车内
    loc_shop = ("xpath",".//*[@class='ant-card-body']/div/div[2]/div/div/div/div/div/span") #判断购物车内商品数量
    loc_courseTitle1 = ("xpath",".//*[@class='ant-list ant-list-split']/div/div/span[last()]/div/div/span/div/div[2]/div[1]/div[1]")
    loc_price1 = ("xpath",".//*[@class='ant-list ant-list-split']/div/div/span[last()]/div/div/span/div/div[2]/div[1]/div[2]/span[2]")
    loc_price2 = ("xpath",".//*[@class='ant-spin-container']/span/div/div/span/div/div[2]/div[1]/div[2]/span[2]")  #购物车商品价格，返回多个元素
    loc_totalprice = ("xpath",".//*[@id='paysty']/div/div[2]/div[1]")
    loc_pay = ("xpath",".//*[text()='立即支付']/..")
    loc_payway1 = ("xpath",".//*[@id='radiogroup']/label[1]/span[1]")#微信
    loc_payway2 = ("xpath",".//*[@id='radiogroup']/label[2]/span[1]")#支付宝
    loc_erweima1 = ("xpath",".//*[text()='微信支付二维码']")
    loc_erweima2 = ("xpath",".//*[text()='支付宝支付二维码']")
    loc_error = ("xpath",".//*[@class='ant-message-custom-content ant-message-error']")
    loc_error_content = ("xpath",".//*[@class='ant-message-custom-content ant-message-error']/span")

    loc_coursetitle = ("xpath",".//*[@class='ant-spin-container']/span/div/div/span/div/div[2]/div[1]/div[1]")


    def shop_price(self,title):
        '''根据课程名称，获取购物车内课程价格'''
        time.sleep(1)
        eles_title = self.findElementsNew(self.loc_coursetitle)
        eles_price = self.findElementsNew(self.loc_price2)
        price = 0
        for i in range(len(eles_title)):
            t = eles_title[i].text
            if title == t:
                print("商品位于第:",i+1)
                p = eles_price[i].text
                price = Decimal(p[1:])*100
                break
        return price

    def get_minprice(self,courseid):
        '''只有共享课有最低价概念
        判断是否跨平台-》判断价格是否自定义
        自定义取course_share内价格，跟随原价取course表价格，返回课程最低价格'''

        #获取当前网校，平台id
        school_t = School().getSchool()
        schoolid = school_t[0][0]
        #获取课程原价,原网校，原平台
        course_t = School().getCourse(courseid)
        price = course_t[0][1]
        print("课程原价：",price)
        try:
            course_share_t = School().getCourseShare(courseid,schoolid)
            share_price=course_share_t[0][7]
            print("自定义共享价格，公司分成",share_price,course_share_t[0][2])

            source_platform_id = course_t[0][2]
            sale_platform_id = school_t[0][1]
            print("课程所属平台id对比，不同为跨平台共享",source_platform_id,sale_platform_id)
            if source_platform_id == sale_platform_id:
                '''平台内共享'''
                if course_share_t[0][8] == 0:
                    '''跟随原价'''
                    min_price =int(price*course_share_t[0][2]) #公司分成
                else:
                    '''自定义价格'''
                    min_price =int(share_price*course_share_t[0][2]) #公司分成
                    print(min_price)
                print("课程最低价格",min_price)
                return min_price
            else:
                '''跨平台共享'''
                if course_share_t[0][8] == 0:
                    '''跟随原价'''
                    min_price =int(price*course_share_t[0][2])+int(price*course_share_t[0][3])+int(price*course_share_t[0][4])  #公司分成+来源平台分成+来源网校分成
                else:
                    '''自定义价格'''
                    min_price =int(share_price*course_share_t[0][2])+int(share_price*course_share_t[0][3])+int(share_price*course_share_t[0][4]) #公司分成+来源平台分成+来源网校分成
                print("最终价格",min_price)
                return min_price
        except:
            print("该网校内共享课程不存在")
            return ""

    def get_vipprice(self,course_id,course_discount,isshare=0):
        '''若为共享课，判断最低价与会员价'''
        min_price = self.get_minprice(course_id)
        school_t = School().getSchool()
        schoolid = school_t[0][0]

        if isshare == 0:
            course_t = School().getCourse(course_id)
            price = course_t[0][1]
        else:
            course_share_t = School().getCourseShare(course_id,schoolid)
            if course_share_t[0][8] == 0:
                course_t = School().getCourse(course_id)
                share_price = course_t[0][1]
            else:
                share_price = course_share_t[0][7]
            price = share_price

        vip_price_old = int(price * course_discount)
        vip_price = max(vip_price_old,min_price)
        return vip_price

    def get_couponprice(self,course_id,title,dis=1,isshare=0):
        if isshare == 0:
            print('1:',title)
            coupon_price_old = Coupon(self.driver).choose_coupon(title,dis)
            coupon_price = coupon_price_old
        else:
            min_price = self.get_minprice(course_id)
            coupon_price_old = Coupon(self.driver).choose_coupon(title,dis)
            coupon_price = max(min_price,coupon_price_old)
        return coupon_price



    def is_totalprice(self):
        '''获取所有商品价格总和'''
        eles = self.findElementsNew(self.loc_price2)
        n = len(eles)
        print("购物车内商品个数为：",n)
        price = 0
        for i in range(n):
            p = eles[i].text
            price = price+ Decimal(p[1:])
        return price*100

    def totalprice(self):
        '''返回页面总价格'''
        time.sleep(2)
        self.js_scroll_end()
        p = self.get_text(self.loc_totalprice)
        print(p)
        print(p[1:])
        return Decimal(p[1:])*100

    def updata_price(self,course_name,school_id):
        '''修改课程价格'''
        sql="UPDATE course c SET c.price=20 WHERE c.course_name=%s AND c.school_id=%s",course_name,school_id
        S = SQL_conn()
        S.sql_conn()
        S.sql_search(sql)


    def creatorder(self,way=1):
        ''' 创建订单 1 微信   2 支付宝'''
        self.js_scroll_end()
        if way==1:
            self.click(self.loc_payway1)
            self.click(self.loc_pay)
            error =self.isElementExist(self.loc_error)
            if error:
                t = self.get_text(self.loc_error_content)
                print('创建订单失败：',t)
                exist = ''
            else:
                time.sleep(4)
                exist = self.isElementExist(self.loc_erweima1)
        else:
            self.click(self.loc_payway2)
            self.click(self.loc_pay)
            time.sleep(5)
            error =self.isElementExist(self.loc_error)
            if error:
                t = self.get_text(self.loc_error_content)
                print('创建订单失败',t)
                exist = ''
            else:
                exist = self.isElementExist(self.loc_erweima2)
        return  exist

    def is_creatorder_success(self,ordertype,paymentsourse,remark):
        '''判断订单创建是否成功'''
        sql="SELECT * from orders o WHERE o.remark= %s",remark
        S = SQL_conn()
        S.sql_conn()
        S.sql_search(sql)



if __name__=="__main__":
    name="测试课件收费课程"
    from selenium import webdriver
    driver = webdriver.Chrome()
    title = '哐当哐当哐当哐当哐当哐当哐当'
    L = Login(driver)
    # coon = SQL_conn()
    # coon.sql_conn()
    # coon.sql_search()
    S = Shopping(driver)
    L.login("shibing4","123456")
    time.sleep(2)
    driver.get(pa.host+"/pay/#/shopping")
    time.sleep(1)
    S.get_couponprice(course_id=510080,title=title,dis=1,isshare=0)
