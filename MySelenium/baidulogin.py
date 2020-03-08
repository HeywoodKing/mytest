import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class BaiduAutoLogin(object):
    def __init__(self, url='https://www.baidu.com'):
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        self.url = url

    def login(self, url=None):
        self.driver.get(url if url else self.url)
        self.driver.maximize_window()

        # assert "登录" in self.driver.title
        self.driver.find_element_by_partial_link_text('登录').click()
        time.sleep(1)

        # 用户名登录
        # self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div/div/div[3]/p[2]').click()
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()
        time.sleep(1)

        # 扫码登录
        # self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerQrcodeBtn"]').click()
        # print('+' * 100)
        # time.sleep(2)

        # 获取用户名对象并输入
        username_ele = self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__userName"]')
        username_ele.clear()
        username_ele.send_keys('flack')
        time.sleep(1)

        # 获取密码对象并输入
        password_ele = self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__password"]')
        password_ele.clear()
        password_ele.send_keys('123456')

        # 点击回车按钮
        password_ele.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source

        time.sleep(3)
        # self.driver.close()
        # self.driver.quit()


if __name__ == '__main__':
    browser = BaiduAutoLogin()
    browser.login()


