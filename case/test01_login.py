import unittest
import requests
from public.config import *


class Login(unittest.TestCase):
    def setUp(self):
        self.url = URL + "/account/login"
        self.success_data = {"username":"admin29","password":"admin123"}
        self.null_username = {"username":"","password":"admin123"}
        self.error_password = {"username":"admin29","password":"admin12"}
        self.error_username = {"username":"admi","password":"admin123"}
        self.error_all = {"username":"admi","password":"admin13"}
        self.null_password_data ={"username":"admin29"}

    def tearDown(self):
        pass

    def test_01_success(self): #测试用例1
        """用户名密码正确,登录成功"""
        r = requests.post(self.url,self.success_data)  #发送登录请求
        self.assertIn("success",r.text)    #断言

    def test_02_login_fail_by_null_username(self):
        """用户名为空,密码正确,登录失败"""
        r = requests.post(self.url,self.null_username)
        self.assertIn("error",r.text)

    def test_03_login_fail_by_error_password(self):
        """用户名正确,密码错误,登录失败"""
        r = requests.post(self.url,self.error_password)
        self.assertIn("error",r.text)

    def test_04_fail_by_error_username(self):
        """用户名错误,密码正确,登录失败"""
        r = requests.post(self.url,self.error_username)
        self.assertIn("error",r.text)

    def test_05_fail_by_error_all(self):
        """用户名密码均错误,登录失败"""
        r = requests.post(self.url,self.error_all)
        self.assertIn("error", r.text)


    def test_06_fail_by_null_password(self):
        """用户名正确,密码为空,登录失败"""
        r = requests.post(self.url,self.null_password_data)
        self.assertIn("error", r.text)


if __name__ == '__main__':
    unittest.main()

