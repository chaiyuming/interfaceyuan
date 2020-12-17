import unittest
import requests
import json
from public.get_token import get_token
from public.config import *

class Details(unittest.TestCase):
    def setUp(self):
    #     url = "http://appapi.fecshop.com/v1/account/login"
    #     name = {"username":"admin29","password":"admin123"}
    #     r = requests.post(url,name)
    #     t = json.loads(r.text)["access-token"]
        self.token = get_token()

        self.url = URL + "/product/fetchone"
        self.idea = {"id":"57bab0d5f656f2940a3bf56e"}
        self.idea_error_data = {"id":"abahgahjagha"}
        self.idea_null_data = {"id":""}
        self.token_error = {"acess-token":"aa"}
        self.token_null = {"acess-token":""}

    def test_01_details_success(self):
        """参数正确,查询商品详情成功"""
        r = requests.post(self.url,self.idea,headers=self.token)
        self.assertIn("success",r.text)

    def test_02_details_fail_id_error(self):
        """id错误,其他参数正确,查询商品详情失败"""
        r = requests.post(self.url,self.idea_error_data,headers=self.token)
        self.assertIn("Invalid argument", r.text)

    def test_03_details_fail_id_null(self):
        """id为空,其他参数正确,查询商品详情失败"""
        r = requests.post(self.url,self.idea_null_data,headers=self.token)
        self.assertIn("can not all empty", r.text)

    def test_04_details_fail_token_error(self):
        """token无效,其他参数正确,查询商品详情失败"""
        r = requests.post(self.url,self.idea,headers=self.token_error)
        self.assertIn("token is time out", r.text)

    def test_05_details_fail_token_null(self):
        """token为空,其他参数正确,查询商品详情失败"""
        r = requests.post(self.url,self.idea,headers=self.token_null)
        self.assertIn("token is time out", r.text)






if __name__ == "__main__":
    unittest.main()
