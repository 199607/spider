import time
import os
from selenium import webdriver
import csv



def get_product(keyword):
    '''搜索商品'''
    driver.find_element_by_css_selector('#key').send_keys(keyword)   #找到输入框，输入关键字
    driver.find_element_by_css_selector('.button').click()


    driver.implicitly_wait(10) # 等待隐式等待
    driver.maximize_window() #最大化浏览器



# 数据懒加载（浏览器向下拉动，下面的数据才会加载）
def drop_down():  #模拟向下拉动
    for x in range(1,11,2):
        j = x/10
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)


# 数据分析采集并且保存
def parse_data():
    lis = driver.find_elements_by_css_selector('.gl-item')

    for y in lis:
        try:
            name = y.find_element_by_css_selector('div.p-name a em').text      #商品名称
            price = y.find_element_by_css_selector('div.p-price strong i').text #商品价格
            deal = y.find_element_by_css_selector('div.p-commit strong a').text #商品评论数量
            title = y.find_element_by_css_selector('span.J_im_icon a').text     #商品的店铺
            # print(name,price,deal,title)
            with open('shuju/京东电脑',mode='a',encoding='utf-8',newline='') as f:
                csv_write = csv.writer(f)
                csv_write.writerow([name,price,deal,title])
        except Exception as e:
            print(e)


def get_next():
    driver.find_element_by_css_selector('#J_bottomPage > span.p-num > a.pn-next > em').click()

word = input("请输入爬取商品名称 ")
# word = '笔记本'
driver = webdriver.Chrome(executable_path="D:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
driver.get("https://www.jd.com")
#搜索商品
get_product(word)
for page in range(1,30):

     # 调用页面滚动
    drop_down()
    time.sleep(1)
    #调用解析函数
    parse_data()
    get_next()
# # 调用页面滚动
# drop_down()
# #调用解析函数
# parse_data()
# get_next()

# 退出
driver.quit()