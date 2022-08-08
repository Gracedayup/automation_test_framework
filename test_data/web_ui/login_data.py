# -*- coding: utf-8 -*-
"""
@Time : 2022/8/8 14:10
@Author : name
@File : login_data.py
"""
# 正确的登录信息
normal_data = [{
    "username": "admin",
    "password": "admin123456"
}]

# 错误的登录信息
incorrect_data = [
    {
        "username": "admin",
        "password": "admin",
        "check": "用户名或密码错误"},
    {
        "username": "admin12",
        "password": "admin",
        "check": "用户名或密码错误"
    }
]