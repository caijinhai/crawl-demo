#!/usr/bin/env python
# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# 使用已打开的浏览器窗口
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# 新建窗口
browser = webdriver.Chrome()


browser.get('https://www.baidu.com/')s
input = browser.find_element_by_id('kw')
input.send_keys('极客挖掘机')
input.send_keys(Keys.ENTER)
print(browser.current_url)
print(browser.get_cookies())
browser.close()

driver = webdriver.Chrome()
driver.get('https://www.jd.com/')
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(By.ID, 'key')
    )
finally:
    driver.quit()

