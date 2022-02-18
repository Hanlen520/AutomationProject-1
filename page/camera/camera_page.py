# coding = utf8
import os
import sys

from page.system.system import System, sleep
from toolsbar.excel_tools import read_excel_for_page_element

os.path.abspath(".")
"""
    @File:camera_page.py
    @Author:Bruce
    @Date:2021/1/14
    @Description:Camera page，控制设备Camera应用的函数、控件
    @param:继承System，传入Main_Page实例完成设备Device、Poco初始化
"""


# 该函数用于简化元素获取操作
def get_element_parametrize(element_name="guide_page_text"):
    form_name = "./page/page_sheet.xlsx"
    element_data = read_excel_for_page_element(form=form_name, sheet_name="camera_page",
                                               element_name=element_name)
    return element_data


class Camera_Page(System):
    """
        @param:main_page:传入Main_Page实例完成设备的Device、Poco的初始化
    """

    def __init__(self, main_page):
        System.__init__(self, main_page)

        self.top_function_bar = self.poco(get_element_parametrize("top_function_bar"))
        self.camera_settings_ai_scene_detection = self.poco(text=get_element_parametrize("camera_settings_ai_scene_detection"))

    """
        @description:启动camera应用
    """

    def start_camera(self):
        self.logger.info("function:" + sys._getframe().f_code.co_name + ":启动camera app:")
        self.device.start_app("com.tcl.camera")
        sleep(1)

    """
        @description:关闭camera应用
    """

    def stop_camera(self):
        self.logger.info("function:" + sys._getframe().f_code.co_name + ":关闭camera app:")
        sleep(1)
        self.device.stop_app("com.tcl.camera")

    """
        @description:进入camera设置界面
    """

    def enter_camera_settings(self):
        try:
            self.logger.info("function:" + sys._getframe().f_code.co_name + ":进入camera设置界面:")
            camera_settings = self.top_function_bar.wait().children()[0]
            self.double_click_element(element_item=camera_settings)
        except Exception as ex:
            self.logger.error("function:" + sys._getframe().f_code.co_name + ":进入camera settings出现问题:" + str(ex))

    """
        @description:更改camera设置:Ai scene detection
    """

    def change_ai_scene_status(self):
        result = ""
        try:
            self.logger.info("function:" + sys._getframe().f_code.co_name + ":改变Ai scene status的值:")
            ai_scene_detection_switch = self.camera_settings_ai_scene_detection.wait().parent().parent().children()[
                1].children()
            ai_scene_detection_switch.click()
            ai_scene_detection_switch.invalidate()
            result = "AI scene detection" + ":" + str(ai_scene_detection_switch.attr("checked"))
        except Exception as ex:
            self.logger.error("function:" + sys._getframe().f_code.co_name + ":更改ai scene status出现问题:" + str(ex))
        return result
