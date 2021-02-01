import time
from selenium import webdriver
from info import *


def checkin(uid, pwd):
    driver_url = r"浏览器驱动绝对路径"
    driver = webdriver.Edge(executable_path=driver_url)
    driver.get("https://stuhealth.jnu.edu.cn/#/login")
    # 填入学号密码
    driver.find_element_by_id("zh").send_keys(uid)
    driver.find_element_by_id("passw").send_keys(pwd)
    # 提交
    driver.find_element_by_css_selector('[type=submit]').click()
    # 等待页面加载完成
    time.sleep(5)
    driver.find_element_by_id('10000').click()
    driver.find_element_by_id('tj').click()
    # 另一种元素定位方式
    # driver.find_element_by_css_selector('[type=checkbox]').click()
    # driver.find_element_by_css_selector('[type=submit]').click()
    driver.close()


if __name__ == "__main__":
    checkin(UID, PWD)
