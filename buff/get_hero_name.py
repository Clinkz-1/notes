import time,re,os,requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Buff:
    def __init__(self,tel,password):
        self.tel = tel
        self.password = password
        self.driver = webdriver.Chrome()
        self.index_url ='https://buff.163.com/market/?game=dota2#tab=selling&page_num=1'
        self.num = 0

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
        time.sleep(3)


    def _login(self):
        try:
            self.wait().until(EC.presence_of_element_located((By.XPATH,'//div[@class="store-user"]')))
        except Exception:
            time.sleep(3)
            self._login()
        else:
            return

    def get_price(self):
        # self.driver.get('https://buff.163.com/market/goods?goods_id=3556&from=market#tab=selling&tag_ids=1410')
        self.cookies = self.driver.get_cookies()
        url = f'https://buff.163.com/api/market/goods/sell_order?game=dota2&goods_id=3556&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&tag_ids=1410'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
        cookies = {cookie['name']: cookie['value'] for cookie in self.cookies}
        resp = requests.get(url,headers=headers,cookies=cookies)
        print(resp.content.decode())

    def run(self):
        self.login()
        self.get_price()
        self.close()

if __name__ == '__main__':
    b = Buff('17714552601','caowo1996')
    b.run()