# -*- coding: utf-8 -*-
"""
@Time : 2022/7/28 18:15
@Author : name
@File : test_login.py
"""
import allure
import pytest

from page_objects.login_page import LoginPage
from common.handle_data import HandleFileData
import test_data.web_ui.login_data as test_data
from common.project_path import config_path


flow_login_url = HandleFileData(config_path).read_yaml()["web_url"]["flow_login_url"]


@allure.epic("项目名称：JugoFlow WEB自动化测试项目")
@allure.feature("模块名称：用户管理")
class TestLogin:
    @pytest.mark.run(order=1)
    @pytest.mark.dependency(name='testUserLogin')
    @allure.title("登录成功")
    @allure.description("正确的账号密码，成功登录")
    @pytest.mark.parametrize("data", test_data.normal_data)
    def test_001_login_success(self, data, driver):
        driver.get(flow_login_url)
        self.lg = LoginPage(driver)
        self.lg.login(data["username"], data["password"])
        assert self.lg.check_text_login_success()





