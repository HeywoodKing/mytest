# 导包
from time import time, sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import string

class Search(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.infinigo.cn/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_search(self):
        driver = self.driver
        input_obj = driver.find_element_by_xpath('//input[@class="el-input__inner"]')
        for word in string.ascii_lowercase:
            print(word)
            for i in word:
                input_obj.send_keys(i)
                sleep(2)
                dl = driver.find_element_by_xpath('//dl[@class="shadow searchList"]')
                part_numbers = str(dl.text).split('\n')
                use_part_number = part_numbers[:-1]
                print(use_part_number)
                for item in use_part_number:
                    input_obj.clear()
                    input_obj.send_keys(item)
                    input_obj.send_keys(Keys.RETURN)
                    sleep(5)
                    Infinigo=driver.find_element_by_partial_link_text('Infinigo')
                    Infinigo.click()



    def tearDown(self):
        sleep(3)
        self.driver.quit()
