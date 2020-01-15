#coding:utf_8
from _decimal import Decimal
from common.sql_connect import SQL_conn
from common.base import Base
from pages.login_wx import Login
import time
# a='¥11'
# b='￥11.00'
# a=float(a[1:])
# b=float(b[1:])
# print(a,b)

# a='0.11'
# b='0.11'
#
# a=Decimal(a)*Decimal('0.1')
# b=Decimal(b)
# print(a)

#
# a = r'https://test.1x.cn/pages/info.html?cid=1408004&diliater=PfriqrhxGZSlUzPVdH290A=='
# b =a.split("=",1)[1]
# c= b.split('&')[0]
# print (b)
# print (c)

# sql="SELECT c.price FROM course c WHERE c.course_id=%s AND c.school_id=%s",course_id
# t = sql_search2(sql)
# course_discount=0.11
# p = 20
# a=p * course_discount
# print(int(a))

# a=max(1,3)
# from selenium import webdriver
# driver = webdriver.Chrome()
# L = Login(driver)
# L.login("jingzhe88","123456")
# time.sleep(2)
# # b=Base()
# loc_price1 = ("class name","price_num___3MTH6")
#
# driver.get("https://test.1x.cn/pay/#/shopping")
# time.sleep(2)
# eles = L.findElementsNew(loc_price1)
#
# n = len(eles)
# print(n)
# price = 0
# for i in range(n):
#     p = eles[i].text
#     price = price+ float(p[1:])
#     print(i,price)


# a=[]
# for i in range(len(a)):
#     print(a[i])


# class A():
#     def __init__(self):
#         print('enter A')
#         print('leave A')
# class B(A):
#     def __init__(self):
#         print('enter B')
#         super().__init__()
#         print('leave B')
# class C(A):
#     def __init__(self):
#         print('enter C')
#         super().__init__()
#         print('leave C')
# class D(B, C):
#     def __init__(self):
#         print('enter D')
#         super().__init__()
#         print('leave D')
#
# d = D()


#
# lst = [(1,2),(1,3),(1,4)]
# for i in iter(lst):
#      print(i)


from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://test.1x.cn/pages/bundle.html?cid=1110003")
time.sleep(2)
loc_price = ("xpath",".//*[@class='cursered']")
a=driver.find_element_by_class_name("cursered").text
print(a)
a=a.split("￥")
print(a[1])