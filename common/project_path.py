# – coding: utf-8 --
import os


project_path = os.path.dirname(os.path.dirname(__file__))
# config文件
config_dir = os.path.join(project_path, "config")
config_path = os.path.join(config_dir, "config.yml")
# 日志
logs_path = os.path.join(project_path, "logs")

# 测试用例
case_path = os.path.join(project_path, "test_case")

# 测试数据
testData_dir = os.path.join(project_path, "test_data")
login_test_data_path = os.path.join(testData_dir, "api", "user_management", "login_test_data.csv")

# images目录
image_path = os.path.join(project_path, "images")

print(image_path)



