#coding:utf-8
from common.base import Base
from pages.login_wx import Login
import  time

class Gallery(Base):
    loc_yygl=("xpath",".//*[@title='应用管理']")
    loc_tkzx=("link text","图库中心")
    loc_fabu=("xpath","//*[text()='发 布']/..")
    loc_1=("id","shopName")
    loc_2=("id","introduce")
    #添加分类
    loc_3=("xpath","//*[text()='添加分类']")
    loc_4=("id","ShopclassifyName")
    loc_5=("xpath",".//*[@class='ant-modal-footer']/div/button[2]")
    loc_6=("id","shopClassifyId")
    loc_7=("xpath",".//*[@class='ant-cascader-menu']")

    loc_7_1=("xpath",".//*[@class='ant-cascader-menu']/li[last()]")

    loc_8 = ("id","PicturePublishingbtns")
    loc_9 = ("name","file")
    loc_10 = ("id","deadline")
    loc_11 = ("id","price")
    loc_12 = ("id","isVipDiscount")
    loc_13 = ("xpath","//*[text()='确 定']/..")
    loc_upfile=("xpath","//*[@class='cwUpload']/div/span")
    loc_tiishi = ("xpath",".//*[@class='ant-notification-notice-content']/div/div[2]")
    url_pic = r"D:\liuling\wx\common\pic.jpg"
    url_file = r"D:\liuling\wx\common\Jain.mp4"
    loc_14 = ("xpath",".//*[@class='ReactVirtualized__Grid__innerScrollContainer']/div[1]/div/div/div/span/div/div[2]/h3/div/span")
    loc_15 = ("xpath",".//*[@class='ReactVirtualized__Grid__innerScrollContainer']/div[1]/div/div/div/span/div/div[3]/div[1]")
    loc_16 = ("xpath",".//*[@class='ant-modal-confirm-btns']/button[2]")
    loc_17 = ("xpath","//*[text()='确 定']/..")
    loc_bianji = ("xpath",".//*[@class='ReactVirtualized__Grid__innerScrollContainer']/div[1]/div/div/div/span/div/div[3]/div[2]/a[1]")
    loc_more = ("xpath",".//*[@class='ReactVirtualized__Grid__innerScrollContainer']/div[1]/div/div/div/span/div/div[3]/div[2]/a[2]")
    loc_up = ("xpath","//a[text()='上架']")
    loc_down = ("xpath","//a[text()='下架']")
    loc_delete = ("xpath","//a[text()='删除']")
    loc_ison=("xpath",".//*[@class='ReactVirtualized__Grid__innerScrollContainer']/div[1]/div/div/div/span/div/div[2]/div/div[3]/span/span[2]/span")
    timestr = time.strftime("%d_%H_%M_%S")


    def input_shopname(self,name):
        '''输入名称 '''
        self.sendKeys(self.loc_1,name)

    def input_introduce(self,itd):
        '''输入简介 '''
        self.sendKeys(self.loc_2,itd)

    def add_classify(self,cname):
        '''添加分类 '''
        self.click(self.loc_3)
        time.sleep(1)
        self.sendKeys(self.loc_4,cname)
        self.click(self.loc_5)

    def is_addclassify_success(self,cname):
        '''添加分类是否成功 '''
        self.click(self.loc_6)
        self.js_focus_element(self.loc_7_1)
        t=self.is_value_in_element(self.loc_7_1,cname)
        return t

    def choose_classify(self):
        '''选择分类 '''
        self.click(self.loc_6)
        self.js_focus_element(self.loc_7_1)
        self.click(self.loc_7_1)

    def input_picture(self,url):
        '''上传图片'''
        self.sendKeys(self.loc_8,url)

    def input_file(self,url2):
        '''上传附件'''
        self.sendKeys(self.loc_9,url2)
        try:
            time.sleep(1)
            self.is_text_in_element(self.loc_upfile,"100%")
        except:
            time.sleep(2)
            self.is_text_in_element(self.loc_upfile,"100%")
        else:
            print("上传附件失败")

    def input_deadline(self,t=1):
        '''输入商品有效期'''
        self.sendKeys(self.loc_10,t,True)

    def input_price(self,p=1):
        '''输入商品价格'''
        self.sendKeys(self.loc_11,p,True)

    def is_vip(self,y):
        '''0：不享受会员价，否则享受会员价'''
        if y == 0:
            self.click(self.loc_12)
        else:
            return ""

    def is_sure(self):
        '''添加确定'''
        self.click(self.loc_13)

    def add_gallery(self,name="图片",itd="图片",cname="分类",url=url_pic,url2=url_pic,t=1,p=1,y=1):
        '''添加商品'''
        time.sleep(2)
        self.click(self.loc_yygl)
        self.click(self.loc_tkzx)
        time.sleep(2)
        self.click(self.loc_fabu)
        self.input_shopname(name)
        self.input_introduce(itd)
        self.add_classify(cname+self.timestr)
        time.sleep(2)
        self.choose_classify()
        self.input_picture(url)
        self.input_file(url2)
        self.input_deadline(t)
        self.input_price(p)
        self.is_vip(y)
        self.is_sure()
        return name

    def is_gallery(self):
        '''判断商品是否存在，返回，最新商品的名称'''
        time.sleep(2)
        t = self.get_text(self.loc_14)
        return t
        # p = self.get_text(self.loc_15)
        # return t,p


    def gallery_operate(self,operate):
        '''1:上架  2：下架  3：删除'''
        time.sleep(1)
        self.js_scroll_top()
        self.move_to_element(self.loc_more)
        if operate==1:
            self.click(self.loc_up)
            time.sleep(2)
            self.click(self.loc_17)
        elif operate==2:
            self.click(self.loc_down)
            time.sleep(2)
            self.click(self.loc_17)
        else:
            self.click(self.loc_delete)
            time.sleep(2)
            self.click(self.loc_17)


    def is_on_sale_sucess(self):
        '''上架下架是否成功'''
        time.sleep(1)
        t = self.get_text(self.loc_ison)
        return t

    def delete_gallery(self):
        '''删除商品'''
        self.move_to_element(self.loc_more)
        self.click(self.loc_delete)



if __name__=="__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    L = Login(driver)
    G = Gallery(driver)
    L.login()
    n=G.add_gallery()
    t = G.is_gallery()
    print(t)
    G.gallery_operate(1)
    r=G.is_on_sale_sucess()
    print(r)
    if r=="销售中":
        print("上架成功")
    else:
        print("上架失败")




