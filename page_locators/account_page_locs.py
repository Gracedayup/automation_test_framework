# -*- coding: utf-8 -*-
"""
@Time : 2022/8/4 16:24
@Author : name
@File : account_page_locs.py
"""
from selenium.webdriver.common.by import By


class AccountPageLocs:
    user_icon = (By.XPATH, '//*[@id="dataExchange"]/div/div[1]/div[1]/div[3]/div/span/span')
    node_mamager = (By.XPATH, '/html/body/div[2]/div/div/section/ul/li[1]/span')
    add_btn = (By.CSS_SELECTOR, '.el-button.el-button--primary.el-button--mini')
