# -*- coding: utf-8 -*-
"""
@Time : 2022/8/4 16:24
@Author : name
@File : account_page.py
"""
from base.basepage import BasePage
from page_locators.account_page_locs import AccountPageLocs as loc


class Account_page(BasePage):
    def click_node_management_icon(self):
        self.click_element(loc.user_icon, mark="点击我的账户图标")
        self.click_element(loc.node_mamager, mark="点击网络节点管理")

    def check_page_message(self):
        result = self.check_element_contains_text(loc.add_btn, check_text="添加", mark="网络节点管理列表_检查[添加按钮]文本")
        print("检查结果：{}".format(result))
        return result



