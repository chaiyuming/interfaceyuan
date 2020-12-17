import unittest
import requests
from public.config import *
from public.get_token import get_token


class Query(unittest.TestCase):
    def setUp(self):
        # url = "http://appapi.fecshop.com/v1/account/login"
        # name = {"username":"admin29","password":"admin123"}
        # login_data = requests.post(url,name)
        # c = json.loads(login_data.text)["access-token"]
        self.token = get_token()

        self.url = URL + "/article/list"
        self.success_data = {"page":1,"passwore":"admin123"}
        self.error_password_data = {"page":1,"password":"admin12"}
        self.null_password_data = {"page":1}
        self.error_token_data = {"access-token":"11"}
        self.null_page_data = {"password":"admin123"}

    def test_01_query_success(self):
        """参数正确,查询商品列表成功"""
        r = requests.get(self.url,self.success_data,headers=self.token)
        self.assertIn("success",r.text)

    def test_02_query_fail_error_password(self):
        """密码错误,其他参数正确,查询商品列表失败"""
        r = requests.get(self.url, self.error_password_data, headers=self.token)
        self.assertIn("error",r.text)

    def test_03_query_fail_error_null_password(self):
        """密码为空,其他参数正确,查询商品列表失败"""
        r = requests.get(self.url,self.null_password_data,headers=self.token)
        self.assertIn("error", r.text)

    def test_04_query_fail_error_token(self):
        """token无效,其他参数正确,查询商品列表失败"""
        r = requests.get(self.url,self.success_data,headers=self.error_token_data)
        self.assertIn("token is time out", r.text)

    def test_05_query_fail_null_token(self):
        """token为空,其他参数正确,查询商品列表失败"""
        r = requests.get(self.url,self.success_data)
        self.assertIn("token is time out", r.text)

    def test_06_query_fail_null_page(self):
        """page为空,其他参数正确,查询列表首页成功"""
        r = requests.get(self.url,self.null_page_data,headers=self.token)
        self.assertIn("success",r.text)


if __name__ == '__main__':
    unittest.main()