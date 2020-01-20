# coding:utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

class Base():
    '''定义一个基本类，对常用方法进行二次封装，省时，简洁'''
    def __init__(self,driver=webdriver.Chrome):   #driver只是个形参，加：映射过去，就可以调用方法
        self.driver = driver
        self.timeout =10
        self.t =0.5

    def findElement(self,locator):
        '''用来查找元素 locator 参数是定位方式，如("id", "kw"),把两个参数合并为一个 *号是把两个参数分开传值'''
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            print("正在定位元素信息：定位方式->%s, value值->%s"%(locator[0], locator[1]))
            ele = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x:x.find_element(*locator))
            return ele

    def findElements(self,locator):
        '''用来查找元素 locator 参数是定位方式，如("id", "kw"),把两个参数合并为一个 *号是把两个参数分开传值'''
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            try:
                print("正在定位元素信息：定位方式->%s, value值->%s"%(locator[0], locator[1]))
                eles = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x:x.find_elements(*locator))
                return eles
            except:
                return []

    def findElementNew(self,locator):
        '''定位到元素返回对象，没定位到，返回timeout异常'''
        # 注意是locator元祖
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            print("正在定位元素信息：定位方式->%s, value值->%s"%(locator[0], locator[1]))
            ele = WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_element_located(locator))
            return ele

    def findElementsNew(self,locator):
        '''定位到一组元素返回对象，没定位到，返回timeout异常'''
        # 注意是locator元祖
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            try:
                print("正在定位元素信息：定位方式->%s, value值->%s"%(locator[0], locator[1]))
                eles = WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_all_elements_located(locator))
                return eles
            except:
                return []

    def click(self,locator):
        '''点击元素'''
        ele = self.findElementNew(locator)
        ele.click()

    def clicks(self,locator,i=1):
        '''点击复数元素'''
        eles = self.findElementsNew(locator)
        eles[i].click()

    def double_click(self,locator):
        '''双击事件'''
        element = self.findElementNew(locator)
        ActionChains(self.driver).double_click(element).perform()

    def clear(self,locator):
        '''清空文本框'''
        ele = self.findElementNew(locator)
        ele.clear()

    def sendKeys(self,locator,text,is_clear_first=False):
        '''输入文本'''
        ele = self.findElementNew(locator)
        if is_clear_first:
            ele.clear()
        ele.send_keys(text)

    def isSelected(self, locator):
        '''判断元素是否被选中，返回bool值'''
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r

    def isElementExist(self, locator):
        try:
            self.findElementNew(locator)
            return True
        except:
            return False

    def isElementExist2(self, locator):
        eles = self.findElementsNew(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print("定位到元素的个数：%s"%n)
            return True

    def is_title(self,_title=""):
        '''头部是不是，返回bool值'''
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_title_contains(self,_title=""):
        '''头部是否包含，返回bool值'''
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_text_in_element(self,locator,_text):
        '''判断这个文本在不在元素里面，返回bool值'''
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element(locator,_text))
            return result
        except:
            return False

    def is_value_in_element(self,locator,_value):
        '''value为空，返回false，返回bool值'''
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element_value(locator,_value))
            return result
        except:
            return False

    def is_alert(self):
        '''返回alert对象'''
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def is_alert_exist(self):
        '''判断弹窗是否存在'''
        try:
            time.sleep(2)
            alert = self.driver.switch_to.alert
            t = alert.text
            print(t)
            alert.accept()
            return t
        except:
            return ""

    def get_title(self):
        '''获取title'''
        return self.driver.title

    def get_text(self, locator):
        '''获取文本'''
        try:
            t = self.findElementNew(locator).text
            return t
        except:
            print("获取text失败，返回'' ")
            return ""

    def get_attribute(self, locator, name):
        '''获取属性'''
        try:
            element = self.findElement(locator)
            return element.get_attribute(name)
        except:
            print("获取%s属性失败，返回'' "%name)
            return ""

    def js_focus_element(self, locator):
        '''聚焦元素'''
        target = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self,x=0):
        '''滚动到底部'''
        js = "window.scrollTo(%s,document.body.scrollHeight)"%x
        self.driver.execute_script(js)

    def select_by_index(self, locator, index=0):
        '''通过索引,index是索引第几个，从0开始，默认选第一个'''
        element = self.findElement(locator)  # 定位select这一栏
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        '''通过value属性'''
        element = self.findElement(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        '''通过文本值定位'''
        element = self.findElement(locator)
        Select(element).select_by_visible_text(text)

    def switch_iframe(self, id_index_locator):
        '''切换iframe'''
        try:
            if isinstance(id_index_locator, int):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, str):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, tuple):
                ele = self.findElement(id_index_locator)
                self.driver.switch_to.frame(ele)
        except:
             print("iframe切换异常")

    def switch_handle(self, window_name):
        self.driver.switch_to.window(window_name)

    def switch_alert(self):
        r = self.is_alert()
        if not r:
            print("alert不存在")
        else:
            # alert = self.driver.switch_to.alert
            t = r.text
            print(t)
            r.accept()
            return t

    def move_to_element(self, locator):
        '''鼠标悬停操作'''
        ele = self.findElement(locator)
        ActionChains(self.driver).move_to_element(ele).perform()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    # driver.get("http://www.ebh.net/")
    #
    # ebh = Base(driver)
    # loc1 = ("xpath", ".//*[text()='合作政策']")
    # loc2 = ("css selector", "[name='password']")
    # loc3 = ("xpath", ".//*[text()='互联网+教育，势在必行']")
    # ebh.js_scroll_end()
    # time.sleep(2)
    # ebh.js_scroll_top()
    # time.sleep(2)
    # ebh.js_focus_element(loc3)

    driver.get("https://www.baidu.com")

    baidu = Base(driver)
    loc1 = ("link text", "设置")
    loc2 = ("link text", "搜索设置")
    loc3 = ("id", "nr")
    loc4 = ("id", "issw1")
    loc5 = ("id", "sh_1")
    loc6 = ("xpath", ".//*[text()='保存设置']")
    baidu.move_to_element(loc1)
    time.sleep(2)
    baidu.click(loc2)
    time.sleep(2)

    baidu.select_by_index(loc3,2)
    time.sleep(2)
    baidu.select_by_index(loc4,1)

    time.sleep(2)
    baidu.click(loc5)
    time.sleep(2)
    baidu.click(loc6)
    time.sleep(2)
    a=baidu.switch_alert()
    # a.accept()
    # baidu.is_alert_exist()








    time.sleep(5)
    driver.quit()




    # zentao.sendKeys(loc1, "admin")
    # zentao.sendKeys(loc2, "123456")
    # zentao.click(loc3)
    # print(11111111111)
    #
    # r = zentao.is_alert()
    # print(r)
    # print(2222222222222)




    # def switch_frame(self,locator):
    #     '''判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False'''
    #     try:
    #         result = WebDriverWait(self.driver,10).until(EC.frame_to_be_available_and_switch_to_it(locator))
    #         return result
    #     except:
    #         return False











