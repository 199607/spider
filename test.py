from datetime import time
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="D:\Program Files (x86)\chromedriver_win32\chromedriver.exe")

def get_product(keyword):
    '''搜索商品'''
    driver.find_element_by_css_selector('#key').send_keys(keyword)   #找到输入框，输入关键字
    driver.find_element_by_css_selector('.button').click()


    driver.implicitly_wait(10) # 等待隐式等待
    driver.maximize_window() #最大化浏览器

driver.get('https://www.jd.com')
word = '笔记本'
get_product(word)
time.sleep(5)
lis = driver.find_elements_by_css_selector('.gl-item')
for i in range(0,200):
    driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_DOWN)#在这里使用模拟的下方向键
    time.sleep(0.1)
for y in lis:
    htmnode=y.find_element_by_css_selector('div.p-name a em').text
    print(htmnode)

