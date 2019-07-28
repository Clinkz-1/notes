import time,re,os
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
        self.get_config_and_data()
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
        self.cookies = self.driver.get_cookies()
        time.sleep(3)
        if self.open_web =="F":
            self.reconnect()

    def _login(self):
        try:
            self.wait().until(EC.presence_of_element_located((By.XPATH,'//div[@class="store-user"]')))
        except Exception:
            time.sleep(3)
            self._login()
        else:
            return

    def get_config_and_data(self):
        with open('./config','r',encoding='utf8')as f:
            lines = f.readlines()
        for line in lines:
            interval_time = re.findall(r'interval_time\s*=\s*(\d+)\s*',line)
            all_time = re.findall(r'all_time\s*=\s*(\d+)\s*',line)
            wifi_name = re.findall(r'wifi_name\s*=(.+)', line)
            open_web = re.findall(r'open_web\s*=\s*(\w)', line)
            if interval_time:
                self.interval_time = float(interval_time[0])
            elif all_time:
                self.all_time = float(all_time[0])
            elif wifi_name:
                self.wifi_name = wifi_name[0].strip()
            elif open_web:
                self.open_web = open_web[0].upper()

        with open('./goods_price.txt','r',encoding='utf8')as f:
            lines = f.readlines()
        self.goods_url = []
        self.my_price = []
        for line in lines:
            match = re.search(r'(?P<goods>https.+\b)\s* <\s*(?P<price>\d+\.\d+|\d+)',line)
            if match:
                self.goods_url.append(match['goods'])
                self.my_price.append(float(match['price']))

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

    def reconnect(self):
        time.sleep(4)
        os.system('netsh wlan connect name='+self.wifi_name)
        time.sleep(6)
        if self.driver:
            self.close()
        if self.open_web == "F":
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")  # 开启无头模式
            options.add_argument("--disable-gpu")  # 关闭gpu
            self.driver = webdriver.Chrome(options=options)  # 使用配置
        else:
            self.driver = webdriver.Chrome()
        self.driver.get(self.index_url)
        time.sleep(2)
        self.driver.delete_all_cookies()
        for cookie in self.cookies:
            if 'expiry' in cookie:
                cookie['expiry'] = int(time.time())
            self.driver.add_cookie(cookie)

    def run_recover(self):
        try:
            if self.all_time:
                length = int(self.all_time * 60 / self.interval_time)-self.num
                if length<=0:return
                for i in range(length):
                    self.find_goods()
                    self.num += 1
                    print(f'查询了{self.num}轮')
            else:
                while True:
                    self.find_goods()
                    self.num += 1
                    print(f'查询了{self.num}轮')
        except Exception as e:
            print(e)
            self.reconnect()
            self.run_recover()

    def run(self):
            self.login()
            self.run_recover()
            self.close()

if __name__ == '__main__':
    b = Buff('17714552601','caowo1996')
    b.run()


