from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,re

index_url ='https://buff.163.com/market/?game=dota2#tab=selling&page_num=1'
url = 'https://fanyi.baidu.com/?aldtype=85#en/zh/a'
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # 开启无头模式
# options.add_argument("--disable-gpu")  # 关闭gpu
# driver = webdriver.Chrome(options=options)  # 使用配置
# driver = webdriver.Chrome()
# driver.get(url)
# wait = WebDriverWait(driver, 20)
# a = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'language-selected')))
# print(a.text)
# time.sleep(10)
# def t(wait):
#     try:
#         wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="store-user"]')))
#     except Exception:
#         time.sleep(3)
#         t(wait)
#     else:
#         return
# t(wait)
#
#
# url_list=['https://buff.163.com/market/goods?goods_id=3556&from=market#tab=selling&tag_ids=1410',
#           'https://buff.163.com/market/goods?goods_id=23444&from=market#tab=selling&tag_ids=7992',
#           'https://buff.163.com/market/goods?goods_id=3521&from=market#tab=selling&tag_ids=12994',
#           'https://buff.163.com/market/goods?goods_id=24157&from=market#tab=selling&tag_ids=1534']
# my_price_list = [8,4.9,4,15.8]
# flag = True
# num = 0
# while flag:
#     for i in range(len(url_list)):
#         driver.get(url_list[i])
#         wait.until(EC.presence_of_element_located((By.CLASS_NAME,'list_tb_dota2')))
#         tr_list = driver.find_elements_by_xpath('//tbody[@class="list_tb_dota2"]/tr')
#         for tr in tr_list[1:]:
#             price = float(tr.find_elements_by_xpath('./td[6]/strong')[0].text[1:])
#             if price<=my_price_list[i]:
#                 tr.find_elements_by_xpath('./td[7]/a')[0].click()
#                 time.sleep(3)
#                 qr = driver.find_elements_by_xpath('//div[@id="j_popup_epay"]//a[text()="确认付款"]')[0]
#                 qr.click()
#                 time.sleep(3)
#                 driver.get(url)
#                 # flag = False
#                 break
#         time.sleep(5)
#     num+=1
#     print(num)
# cookies = driver.get_cookies()
# print(cookies)
# time.sleep(10)
# driver.close()
# driver.quit()

# # driver = webdriver.Chrome()
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # 开启无头模式
# options.add_argument("--disable-gpu")  # 关闭gpu
# driver = webdriver.Chrome(options=options)  # 使用配置
# driver.get(url)
# driver.delete_all_cookies()
# for cookie in cookies:
#     if 'expiry'in cookie:
#         cookie['expiry'] = int(time.time())
#     driver.add_cookie(cookie)
# wait = WebDriverWait(driver, 20)
# a = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'language-selected')))
# print(a.text)
# time.sleep(6)
# driver.close()
# driver.quit()

