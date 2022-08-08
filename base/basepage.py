# -*- coding: utf-8 -*-
"""
@Time : 2022/7/1 17:45
@Author : name
@File : basepage.py
"""
import time
import os

from selenium.common import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from common.project_path import project_path
from common.handle_log import logger
from setting import IMAGE_DIR, GLOBAL_TIMEOUT, FREQUENCY

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def find_element_presence(self, loc, timeout=GLOBAL_TIMEOUT, frequency=FREQUENCY, mark=None):

        """
        等待页面元素存在
        :param loc:元素定位表达
        :param timeout:等待超时时间
        :param frequency:轮询频率
        :param mark:功能标注
        """
        logger.info("在{}等待元素{}存在：".format(mark, loc))
        try:
            return WebDriverWait(self.driver, timeout, frequency).until(EC.presence_of_element_located(loc))
        except Exception as e:
            logger.exception("查找元素失败！")
            self.save_images(mark)
            raise e

    def wait_element_clickable(self, loc, mark=None, timeout=GLOBAL_TIMEOUT, frequency=FREQUENCY):
        """
        等待元素可点击
        :param loc:元素定位
        :param mark:功能标注
        :param timeout:超时时间
        :param frequency:轮询频率
        """
        try:
            logger.info("开始等待页面元素{}是否可点击！".format(loc))
            ele = WebDriverWait(self.driver, timeout, frequency).until(EC.element_to_be_clickable(loc))
            return ele
        except Exception as e:
            self.save_images(mark=mark)
            logger.exception("等待页面元素可点击失败！")
            raise

    def find_element(self, loc, mark=None):
        """
        查找元素
        :param loc:元素定位表达
        :param mark:功能标注
        """
        logger.info("{}查找元素{}".format(mark, loc))
        try:
            print("find_element的数据类型：{}".format(self.driver.find_element(*loc)))
            return self.driver.find_element(*loc)
        except Exception as e:
            logger.exception("查找元素失败！")
            self.save_images(mark)
            raise e

    def find_elements(self, loc, mark=None):
        """
        查找元素集
        :param loc:元素定位表达
        :param mark:功能标注
        """
        logger.info("{}查找元素{}".format(mark, loc))
        try:
            return self.driver.find_elements(*loc)
        except Exception as e:
            logger.exception("查找元素失败！")
            self.save_images(mark)
            raise e

    def get_element_attribute(self, loc, attr, mark=None):
        """
        获取属性值
        :param loc:元素定位表达
        :param attr: 属性名
        :param mark: 功能标注
        :return ele_attribute:属性值
        """
        ele = self.find_element_presence(loc=loc, mark=mark)
        logger.info("{}在元素{}中获取属性值".format(mark, loc))
        try:
            ele_attribute = ele.get_attribute(attr)
            logger.info("{}元素{}的属性为:{}".format(mark, loc, ele_attribute))
            return ele_attribute
        except Exception as e:
            logger.exception("获取元素{}的属性值失败".format(loc))
            self.save_images(mark)
            raise

    def input_text(self, loc, text, mark=None):
        """
        输入框输入文本
        :param loc:元素定位表达
        :param text:输入的文本内容
        :param mark:功能标注
        """
        ele = self.find_element_presence(loc=loc, mark=mark)
        logger.info("{}在元素{}中输入文本：{}".format(mark, loc, text))
        try:
            ele.send_keys(text)
        except Exception as e:
            logger.exception("输入操作失败")
            self.save_images(mark)
            raise e

    def clear_input_text(self, loc, mark=None):
        """
        清除文本框内容
        :param loc:元素定位表达
        :param mark:功能标注
        """
        try:
            ele = self.find_element_presence(loc=loc, mark=mark)
            logger.info("{} 在元素 {} 中清除".format(mark, loc))
            ele.send_keys(Keys.CONTROL, "a")
            ele.send_keys(Keys.BACKSPACE)
        except Exception as e:
            logger.exception("清除操作失败")
            self.save_images(mark)
            raise e

    def click_element(self, loc, mark=None):
        """
        点击元素
        :param loc:元素定位表达
        :param mark:功能标注
        """
        ele = self.find_element_presence(loc=loc, mark=mark)
        logger.info("{}在元素{}中输点击".format(mark, loc))
        print("查找出的元素：{}".format(ele))
        try:
            ele.click()
        except Exception as e:
            logger.exception("点击操作失败")
            self.save_images(mark)
            raise e

    def get_text(self, loc, mark=None):
        """
        获取文本内容
        :param loc:元素定位表达
        :param mark:功能标注
        :return text:文本内容

        """
        ele = self.find_element_presence(loc=loc, mark=mark)
        logger.info("{}在元素{}中获取文本".format(mark, loc))
        try:
            text = ele.text
            logger.info("{}元素{}的文本内容为{}".format(mark, loc, text))
            return text
        except Exception as e:
            logger.exception('获取元素 {} 的文本内容失败!'.format(loc))
            self.save_images(mark)
            raise

    def check_text(self, loc, text, mark=None):
        """
        检查文本信息
        :param loc:元素定位
        :param text:文本内容
        :param mark:功能标注
        :return result:bool True:存在此文本；false：不存在此文本
        """
        try:
            result_text = self.find_element_presence(loc=loc, mark=mark).text
            return result_text == text
        except Exception as e:
            logger.exception("检查文本信息失败")
            self.save_images(mark=mark)
            raise

    def select_set_option(self, select_type, content, loc, mark=None):
        """
        下拉框选择元素
        :param select_type:select类型：
                      index：下拉索引
                      value：value值
                      其他：选项内容
        :param content:select_by_方法的入参
        :param loc:元素定位
        :param mark:功能标注
        """
        try:
            ele = self.find_element_presence(loc=loc, mark=mark)
            select = Select(ele)
            print("下拉框中所有选项内容：{}".format(select.options))
            if select_type == "index":
                select.select_by_index(content)
            elif select_type == "value":
                select.select_by_value(content)
            else:
                select.select_by_visible_text(content)
        except Exception as e:
            logger.exception("选择下拉元素失败")
            self.save_images(mark=mark)
            raise

    def suspend_mouse(self, loc, mark=None, timeout=GLOBAL_TIMEOUT, poll_frequency=FREQUENCY):
        """
        鼠标悬浮
        :param loc:元素定位
        :param mark:功能标注
        :param timeout:超时时间
        :param poll_frequency:轮询频率
        """
        try:
            logger.info("在{}上根据{}进行悬浮".format(mark, loc))
            self.wait_element_clickable(loc)
            ele = self.find_element(loc=loc, mark=mark)
            ActionChains(self.driver).move_to_element(ele).perform()
        except Exception as e:
            logger.exception("鼠标悬浮失败")
            self.save_images(mark=mark)
            raise

    def switch_iframe(self, loc=None, name=None, timeout=GLOBAL_TIMEOUT, poll_frequency=FREQUENCY, mark=None):
        """
        :param loc:iframe元素定位
        :param name:切换方式 default：切换至默认iframe，parent：切换至上一层，其他：切换至其他iframe页面
        :param timeout:超时时间
        :param poll_frequency:轮询频率
        :param mark:功能标注
        """
        logger.info("iframe切换操作")
        try:
            if name == "default":
                self.driver.switch_to.default_content()
            elif name == "parent":
                self.driver.switch_to.parent_frame()
            else:
                WebDriverWait(self.driver, timeout, poll_frequency).until(
                    EC.frame_to_be_available_and_switch_to_it(loc))
        except Exception as e:
            logger.exception("iframe切换失败！")
            self.save_images(mark)
            raise

    def switch_window(self, name="new", timeout=GLOBAL_TIMEOUT, poll_frequency=FREQUENCY, mark=None):
        """
        切换窗口
        :param name: new表示最新打开的窗口，default表示第一个窗口，其他值表示为窗口的handles
        :param timeout:超时时间
        :param poll_frequency:轮询频率
        :param mark:功能标注
        """
        window_handles = self.driver.window_handles
        try:
            if name == "new":
                logger.info("切换到最新页面")
                self.driver.switch_to.window(window_handles[-1])
            elif name == "default":
                logger.info("切换到默认页面")
                self.driver.switch_to.window(self.driver.window_handles[0])
            else:
                logger.info("切换到handles窗口")
                self.driver.switch_to.window(name)
        except Exception as e:
            logger.exception("切换窗口失败")
            self.save_images(mark)
            raise

    def switch_alert(self, option, input_text=None, timeout=GLOBAL_TIMEOUT, poll_frequency=FREQUENCY):
        """
        切换弹窗进行文本输入、取消、关闭弹窗操作
        :param option:对弹窗进行的操作
                      accept:同意操作，当有input_text时，则先输入文本内容再同意
                      其他：进行关闭操作
        :param input_text:输入的文本内容
        :param timeout:超时时间
        :param poll_frequency:轮询频率
        """
        try:
            logger.info("切换弹窗")
            ele = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.alert_is_present())
            if option == "accept":
                if input_text is not None:
                    ele.send_keys(Keys.CONTROL, "a")
                    ele.send_keys(Keys.BACKSPACE)
                    ele.send_keys(input_text)
                    ele.accept()
                else:
                    ele.accept()
            else:
                ele.dismiss()
        except Exception as e:
            self.save_images(mark="切换弹窗失败")
            raise

    def back(self, mark=None):
        """
        页面后退
        """
        logger.info("在{}后退".format(mark))
        self.driver.back()

    def forward(self, mark=None):
        """
        页面前进
        """
        logger.info("在{}前进".format(mark))
        self.driver.forward()

    def refresh(self, mark=None):
        """
        页面刷新
        """
        logger.info("在{}刷新".format(mark))
        self.driver.refresh()

    def close_windows(self):
        """
        清理窗口，只保留当前窗口
        """
        try:
            current_window = self.driver.current_window_handle
            handles = self.driver.window_handles
            for handle in handles:
                if handle != current_window:
                    self.driver.switch_to.window(handle)
                    self.driver.close()
            self.driver.switch_to.window(current_window)
        except Exception as e:
            logger.exception("关闭窗口失败！")

    def quit_browser(self):
        """
        关闭浏览器
        """
        self.driver.quit()

    def is_enable(self, loc, mark=None):
        """
        查看元素是否可用、可点击
        :param loc:元素定位
        :param mark:功能标注
        :return bool: True 可点击可用 false：不可点击不可用
        """
        logger.info("检查{}元素{}中是否可用、可点击".format(mark, loc))
        return self.find_element(loc=loc, mark=mark).is_enabled()

    def scroll_page(self, option=None, loc=None):
        """
        滚动页面
        :param option:操作类型
                      "bottom":滚动至页面底部
                      "top":滚动至页面顶部
                      None:则需要传递loc，滚动到定位元素附近
        :param loc:
        """
        try:
            logger.info("操作滚动条")
            if option == "bottom":
                self.driver.execute_script("scrollTo(0,document.body.scrollHeight)")
            elif option == "top":
                self.driver.execute_script("scrollTo(document.body.scrollHeight,0)")
            else:
                ele = self.find_element_presence(loc=loc)
                js = "arguments[0].scrollIntoView(false);"
                self.driver.execute_script(js, ele)
        except Exception as e:
            logger.exception("操作滚动条失败")
            self.save_images(mark="操作滚动条失败")
            raise

    def save_images(self, mark=None):
        """
        保存截图
        :param mark:功能标注
        """
        current_time = str(time.strftime("%Y%m%d%H%M%S"))
        image_dir = os.path.join((os.path.join(project_path, "images")), str(time.strftime("%Y%m%d")))
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)
        img_path = os.path.join(image_dir, '{}_{}.png'.format(current_time,mark))
        try:
            self.driver.save_screenshot(img_path)
            logger.info("截屏成功，图片路径为:{}".format(img_path))
        except Exception as e:
            logger.exception("截屏失败")
            raise e

    def check_element_contains_text(self, loc, check_text, mark=None, timeout=GLOBAL_TIMEOUT, poll_frequency=FREQUENCY):
        """
        查看元素中是否存在文本
        :param loc:元素定位
        :param check_text:检查的文件
        :param mark:功能标注
        :param timeout:超时时间
        :param poll_frequency:轮询频率
        """
        try:
            logger.info("在{}检查元素{}的文本内容".format(mark, loc))
            check_result = self.wait_element_contains_text(loc=loc,
                                                           check_text=check_text,
                                                           timeout=timeout,
                                                           poll_frequency=poll_frequency)
            return check_result
        except WebDriverException:
            self.save_images(mark=mark)
            logger.exception("检查元素文本失败")
            raise

    def wait_element_contains_text(self, loc, check_text, mark=None, timeout=GLOBAL_TIMEOUT, poll_frequency=FREQUENCY):
        """
        等待元素中包含文本
        :param loc:元素定位
        :param check_text:检查的文件
        :param mark:功能标注
        :param timeout:超时时间
        :param poll_frequency:轮询频率
        """
        try:
            logger.info("在{}等待元素{}的文本内容存在".format(mark, loc))
            result = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.text_to_be_present_in_element(loc, check_text))
            return result
        except WebDriverException:
            self.save_images(mark=mark)
            logger.exception("等待元素文本存在失败")
            raise




