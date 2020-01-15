# coding:utf-8

import requests
from common.round_rewrite import round_rewrite #点击查看该函数 四舍五入
from common.jsonp_to_json import jsonp_to_json #点击查看该函数 jsonp转成json

class Fund:

    fund_api_url = '接口地址url'

    """四个原始数据接口"""
    def api_strategy(self,day=''):
        """
　　　　　　接口1
        """
        url = Fund.fund_api_url+'api1.json'
        response = requests.get(url,params={"day":day}).json()
        return response

    def api_lastestinfo(self,code):
        """
　　　　　接口2
        """
        url = Fund.fund_api_url+'latestInfo/{0}.json'.format(code)
        response = requests.get(url).json()
        return response

    def api_trends(self,code,pattern,period):
        """
　　　　　接口3　　
　　　　 """
        identifier = "{code}_{pattern}_{period}".format(code=code,pattern=pattern,period=period)
        url = Fund.fund_api_url+"trends/{0}.json".format(identifier)
        jsonpstr = requests.get(url).text
        jsonstr = jsonp_to_json(jsonpstr)
        return jsonstr

    def api_timeline(self,code):
        """
　　　　　接口4
        """
        url = Fund.fund_api_url+"timeline/{0}.json".format(code)
        response = requests.get(url).json()
        return response