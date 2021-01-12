# coding = utf8
import subprocess

from airtest.core.api import *
import re
import os

os.path.abspath(".")

"""
    @File:config.py
    @Author:Bruce
    @Date:2020/12/15
"""


# ['7c2440fd', 'b3e5b958']
def get_serial_number():
    devices_stream = os.popen("adb devices")
    devices = devices_stream.read()
    serial_no = re.findall("(.*)\tdevice", devices)
    devices_stream.close()
    return serial_no


# Return devices serial number
SERIAL_NUMBER = get_serial_number()


# 测试前安装所需APP
def install_app_necessary():
    files = os.popen("ls ./apk/")
    apks = re.findall("(.*).apk", files.read())
    for device_serial in SERIAL_NUMBER:
        for apk in apks:
            print("Device [{}] is install {}".format(device_serial, apk))
            screenData = subprocess.Popen("adb -s {} install ./apk/{}.apk".format(device_serial, apk), stdout=subprocess.PIPE, shell=True)
            while True:
                line = screenData.stdout.readline()
                print(line.decode("utf-8"))
                if line == b"" or subprocess.Popen.poll(screenData) == 0:
                    screenData.stdout.close()
                    break
