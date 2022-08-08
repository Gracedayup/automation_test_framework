# -*- coding: utf-8 -*-
"""
@Time : 2022/8/8 11:00
@Author : name
@File : test_node_management.py
"""

import allure
import pytest


from page_objects.account_page import Account_page


@allure.epic("项目名称：JugoFlow WEB自动化测试项目")
@allure.feature("模块名称：我的账户")
class TestNodeManagement:
    @pytest.mark.dependency(depends=["testUserLogin"], scope='session')
    @allure.title("我的账户-网络节点管理")
    @allure.description("点击我的账户-网络节点管理，检查节点列表")
    def test_001_node_management_list(self, driver):
        self.account_page = Account_page(driver)
        self.account_page.click_node_management_icon()
        # 检查网络节点管理列表页面是否存在“添加”按钮
        assert self.account_page.check_page_message()


