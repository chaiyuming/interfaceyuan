import unittest

import requests

from public.get_token import get_token

from public.config import *


class Orderinquiry(unittest.TestCase):
    def setUp(self):
        # url = "http://appapi.fecshop.com/v1/account/login"
        # name = {"username": "admin29", "password": "admin123"}
        # login_data = requests.post(url, name)
        # c = json.loads(login_data.text)["access-token"]
        self.token = get_token()

        self.url = URL + "/order/list"
        self.order_success_data = {"page":1}
        self.order_fail_null_page_data = {"page":""}
        self.token_null = {"acess-token": ""}
        self.token_error = {"acess-token": "aa"}

    def test_01_inquiry_success(self):
        """设置查询第一页的数据,参数正确,查询成功"""
        r =requests.post(self.url, self.order_success_data,headers=self.token)
        self.assertIn("1100000001",r.text)

    def test_02_inquiry_null_page(self):
        """设置查询订单数据，页面设置为空，获取的是第一页数据"""
        r = requests.post(self.url,self.order_fail_null_page_data,headers=self.token)
        self.assertIn("1100000001", r.text)

    def test_03_inquiry_error_token(self):
        """token为空,其他参数正确,查询订单失败"""
        r = requests.post(self.url,self.order_success_data,self.token_null)
        self.assertIn("token is time out", r.text)

    def test_04_inquiry_null_token(self):
        """token无效,其他参数正确,查询订单失败"""
        r = requests.post(self.url,self.order_success_data,self.token_error)
        self.assertIn("token is time out", r.text)






if __name__ == "__main__":
    unittest.main()