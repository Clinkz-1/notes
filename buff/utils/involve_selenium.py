import time,re
from data.config import config
from data.cookies import selenium_cookies
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BuffLogin:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.index_url ='https://buff.163.com/market/?game=dota2#tab=selling&page_num=1'
        self.tel = config['tel']
        self.password = config['password']

    def wait(self):
        return WebDriverWait(self.driver, 20)

    def close(self):
        self.driver.close()
        self.driver.quit()

    def login(self):
        self.driver.get(self.index_url)
        self.wait().until(EC.presence_of_element_located((By.XPATH, '//a[text()="登录"]'))).click()
        time.sleep(2.5)
        self.driver.switch_to.frame(0)
        self.wait().until(EC.presence_of_element_located((By.XPATH, '//a[text()="使用密码验证登录"]'))).click()
        self.wait().until(EC.presence_of_element_located((By.XPATH, '//input[@tabindex="1"]'))).send_keys(self.tel)
        self.wait().until(EC.presence_of_element_located((By.XPATH, '//input[@tabindex="2"]'))).send_keys(self.password)
        self._login()
        self.cookies = self.driver.get_cookies()
        time.sleep(3)

    def _login(self):
        try:
            self.wait().until(EC.presence_of_element_located((By.XPATH,'//div[@class="store-user"]')))
        except Exception:
            time.sleep(3)
            self._login()
        else:
            return

    def save_cookies(self):
        cookies = {cookie['name']: cookie['value'] for cookie in self.cookies}
        with open('../data/cookies.py','r')as f:
            f.write('selenium_cookies=')
            f.write(str(self.cookies))
            f.write('\n')
            f.write('cookies=')
            f.write(str(cookies))
    
    def run(self):
        self.login()
        self.save_cookies()
        self.close()

class BuffBuy:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # 开启无头模式
        options.add_argument("--disable-gpu")  # 关闭gpu
        self.driver = webdriver.Chrome(options=options)  # 使用配置
        for cookie in selenium_cookies:
            if 'expiry' in cookie:
                cookie['expiry'] = int(time.time())
            self.driver.add_cookie(cookie)

    def wait(self):
        return WebDriverWait(self.driver, 20)

    def close(self):
        self.driver.close()
        self.driver.quit()
    
    # 支付模块尚未完成
    def find_goods(self):
        for i in range(len(self.goods_url)):
            self.driver.get(self.goods_url[i])
            self.wait().until(EC.presence_of_element_located((By.CLASS_NAME, 'list_tb_dota2')))
            tr_list = self.driver.find_elements_by_xpath('//tbody[@class="list_tb_dota2"]/tr')
            for tr in tr_list[1:]:
                price = float(tr.find_elements_by_xpath('./td[6]/strong')[0].text[1:])
                if price <= self.my_price[i]:
                    tr.find_elements_by_xpath('./td[7]/a')[0].click()
                    self.pay()
                    print(f'spend {price} {self.goods_url[i]}')
                    break
            time.sleep(self.interval_time)

    def pay(self):
        '''暂时只支持支付宝'''
        qr = self.wait().until(EC.presence_of_element_located((By.XPATH, '//div[@id="j_popup_epay"]//a[text()="确认付款"]')))
        qr.click()
        time.sleep(2.5)

