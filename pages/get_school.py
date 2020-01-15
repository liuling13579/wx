#coding:utf-8

from common.sql_connect import SQL_conn
from common import parm as pa
from pages.login_wx import Login

class School(SQL_conn):

   def getSchool(self):
        '''获取网校信息'''
        host1 = pa.host.split("//")[1]
        sql1="SELECT s.school_id,s.platform_id FROM school s WHERE s.second_level_domain = %s;"
        info1 = (host1)
        school_t = self.sql_search2(sql1,info1)
        return school_t

   def getCourse(self,course_id):
        '''获取课程信息'''
        sql_course="SELECT c.course_id,c.price,c.platform_id,c.school_id,is_vip_discount FROM course c WHERE c.course_id=%s;"
        info = (course_id)
        course_t = self.sql_search2(sql_course,info)
        return course_t

   def getCourseShare(self,course_id,schoolid):
        '''获取共享课程信息'''
        sql_share="SELECT cs.school_id,cs.course_id,cs.company_scale,cs.source_platform_scale,cs.source_school_scale,cs.sale_platform_scale,cs.sale_school_scale,cs.price,cs.is_custom_price FROM course_share cs WHERE cs.course_id=%s AND cs.school_id=%s;"
        info = (course_id,schoolid)
        course_share_t = self.sql_search2(sql_share,info)
        return course_share_t

if __name__ == "__main__":
   from selenium import webdriver
   driver = webdriver.Chrome()
   # L = Login("shibing4","123456")
   S = School()
   t = S.getCourse('25255555')
   print(t)
