# -*- coding: utf-8 -*-
"""
@Time : 2022/7/28 18:16
@Author : name
@File : login_page.py
"""
import time

from page_locators.login_page_locs import LoginPageLocs as loc
from page_locators.account_page_locs import AccountPageLocs
from base.basepage import BasePage
from base.get_token import GetToken


class LoginPage(BasePage):
    def login(self, username, password):
        self.click_element(loc.home_login_btn, "首页_点击登录按钮")
        # 识别验证码
        time.sleep(2)
        captcha_base64 = self.find_element_presence(loc=loc.captcha).get_attribute("src").split("base64,")[1]
        captcha_text = GetToken().recognize_text(captcha_base64)
        self.input_text(loc.user_input, username, "登录页面_输入用户名")
        self.input_text(loc.pwd_input, password, "登录页面_输入密码")
        self.input_text(loc.captcha_input, captcha_text, "登录页面_输入验证码")
        self.click_element(loc.login_btn, "登录页面_点击登录按钮")

    def check_text_login_success(self):
        # 检查是否登录成功(页面右侧头部是否包含账户图标)
        result = self.find_element(AccountPageLocs.user_icon)
        print("check_text_login_success:检查登录后的页面是否包含元素结果为：{}".format(result))
        return result




