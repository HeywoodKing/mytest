#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import json
import os
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

flag = 0
distance = 210
offset = 5
times = 0

def get_track(distance):
	track = []
	current = 0
	mid = distance * 4 / 5
	t = 0.5
	v = 0
	while current < distance:
		if current < mid:
			a = 2
		else:
			a = -3
		v0 = v
		v = v0 + a * t
		move = v0 * t + 1 / 2 * a * t * t
		current += move
		track.append(round(move))
	return track


headers={"User-Agent" : "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
  "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "Accept-Language" : "en-us",
  "Connection" : "keep-alive",
  "Accept-Charset" : "GB2312,utf-8;q=0.7,*;q=0.7"}

url = 'http://www.infinigo.cn'

driver = webdriver.Chrome()
driver.get(url)

driver.find_element_by_xpath("/html/body/div/div/div/header/div/div[2]/span").click()
time.sleep(2)
#obj = driver.find_element_by_css_selector(".el-input__inner")
username_obj = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div[1]/div[2]/fieldset/div/input")
print(username_obj, username_obj.tag_name, username_obj.get_attribute('class'))
time.sleep(2)
username_obj.send_keys('15994765446')

driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[1]/div[3]/button').click()
time.sleep(2)
iframe_captcha = driver.find_element_by_xpath('/html/body/div[3]/iframe')
driver.switch_to.frame(iframe_captcha)  # 切换到iframe

button = driver.find_element_by_id('tcaptcha_drag_thumb')    # 找到“蓝色滑块”
action = ActionChains(driver)          # 实例化一个action对象
print(action)
action.click_and_hold(button).perform()
action.reset_actions()


print(distance)
track = get_track(distance)
for i in track:
    action.move_by_offset(xoffset=i, yoffset=0).perform()
    action.reset_actions()
time.sleep(2)
action.release().perform()
time.sleep(5)

# 判断某元素是否被加载到DOM树里，并不代表该元素一定可见
try:
    alert = driver.find_element_by_class_name('tcaptcha-title').text
except Exception as e:
    print
    'get alert error: %s' % e
    alert = ''
if alert:
    print
    u'滑块位移需要调整: %s' % alert
    distance -= offset
    times += 1
    sleep(5)
else:
    print
    '滑块验证通过'
    flag = 1
    driver.switch_to.parent_frame()  # 验证成功后跳回最外层页面


####
time.sleep(3)
password_obj = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[1]/div[2]/fieldset/div/input')
print(password_obj, password_obj.tag_name, password_obj.get_attribute('class'))
time.sleep(2)
password_obj.send_keys('Wangychy163()')

time.sleep(2)
driver.find_element_by_xpath('//*[@id="v-content"]/div/div[1]/div[3]/button').click()

driver.get_screenshot_as_file('D:\汪迎春\devops\selenium\screenImg\screenImg.png')



time.sleep(10)
driver.quit()
