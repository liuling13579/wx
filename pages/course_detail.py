#coding:utf-8

from common.base import Base
from pages.login_wx import Login
from common.sql_connect import SQL_conn
from pages.learn_center import LearnCenter
from pages.get_school import School
from _decimal import Decimal
import time

class Course_Detail(Base,SQL_conn):

    loc_shoppingcart = ("class name","curshop")  #加入成功之后按钮置灰curshop huise
    loc_isfree = ("class name","curselv") #判断课程是否免费
    loc_buy = ("class name","cursign")  #立即购买，免费报名
    loc_queren = ("class name","layui-layer-btn0") #确认跳转
    loc_courseTitle = ("xpath",".//*[@class='curhtit']")  #课程标题
    loc_price = ("xpath",".//*[@class='cursered']")


    def shoppingcart(self):
        '''加入购物车'''
        n = self.get_attribute(self.loc_shoppingcart,'class')
        if "huise" in n:
            print("商品已加入购物车")
            return ""
        else:
            self.click(self.loc_shoppingcart)
            t = self.is_shoppingcart_success()
            return t

    def openCourse(self):
        '''立即购买'''
        isfree = self.isElementExist(self.loc_isfree)
        if isfree:
            '''免费开通'''
            self.buy_now()
            self.click(self.loc_queren)
            LC = LearnCenter(self.driver)
            title =LC.is_open_free_course_succesee()
            print(title)
            return title
        else:
            '''加入购物车立即跳转至购物车'''
            price = self.get_price()
            title = self.get_title()
            self.buy_now()
            print ("课程价格，名称：",price,title)
            return price,title

    def get_price(self):
        '''获取课程价格'''
        p1=self.get_text(self.loc_price)
        print(p1)
        p1=p1.split("￥")
        price = Decimal(p1[1])*100
        print("页面课程价格：",price)
        return price

    def get_title(self):
        '''获取课程名称'''
        title=self.get_text(self.loc_courseTitle)
        return title

    def buy_now(self):
        '''立即购买'''
        self.click(self.loc_buy)


    def is_shoppingcart_success(self):
        '''判断是否成功加入购物车'''
        time.sleep(1)
        n = self.get_attribute(self.loc_shoppingcart,'class')
        print(n)
        if "huise" in n:
            return  True
        else:
            return  False


    def is_course_vip(self):
        '''判断课程是否享受vip'''


    # def is_share(self,course_id):
    #     '''判断课程是否共享'''
    #     try:


    def is_price(self,course_discount=1,shope_discount=1,isshare=False):
        '''判断课程价格是否正确'''
        #获取页面courseid
        course_id= self.get_course_id()

        #获取当前网校，平台id
        school_t = School().getSchool()
        school_id = school_t[0][0]

        #获取课程原价,原网校，原平台
        course_t = School().getCourse(course_id)

        price = course_t[0][1]
        is_vip_discount = course_t[0][4]
        price_vip = int(price * course_discount) #课程会员后价格
        print("课程原价：",price)

        if not isshare:
            '''如果本校课程，返回课程会员价'''
            if is_vip_discount == 1:
                '''是否享受会员价只作用于本校课程，不限制共享课'''
                return price_vip
            else:
                return price
        else:
            '''如果共享课程，判断是否跨平台-》判断价格是否自定义
            自定义取course_share内价格，跟随原价取course表价格，返回课程价格'''
            try:
                course_share_t = School().getCourseShare(course_id,school_id)
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
                        price_vip = max(min_price,price_vip)
                    else:
                        '''自定义价格'''
                        min_price =int(share_price*course_share_t[0][2]) #公司分成
                        print(min_price)
                        price_vip =int(share_price * course_discount) #共享自定义价格会员价
                    price = max(min_price,price_vip)  #会员价低于最低价，取最低价，否则直接取会员价
                    print("最终价格",min_price,price_vip,price)
                    return price
                else:
                    '''跨平台共享'''
                    if course_share_t[0][8] == 0:
                        '''跟随原价'''
                        min_price =int(price*course_share_t[0][2])+int(price*course_share_t[0][3])+int(price*course_share_t[0][4])  #公司分成+来源平台分成+来源网校分成
                    else:
                        '''自定义价格'''
                        min_price =int(share_price*course_share_t[0][2])+int(share_price*course_share_t[0][3])+int(share_price*course_share_t[0][4]) #公司分成+来源平台分成+来源网校分成
                        price_vip =int(share_price * course_discount) #共享自定义价格会员价
                    price = max(min_price,price_vip)
                    print("最终价格",min_price,price_vip,price)
                    return price
            except:
                print("该网校内共享课程不存在")
                return ""



if __name__=="__main__":
    name="拿破仑蛋糕"
    from selenium import webdriver
    driver = webdriver.Chrome()
    L = Login(driver)
    C = Course_Detail(driver)

    L.login("jingzhe28","123456")
    time.sleep(2)
    driver.get("https://test.1x.cn/pages/info.html?cid=30037")
    time.sleep(1)
    C.openCourse()
