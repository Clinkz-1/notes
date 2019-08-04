import time,re,os,requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib import parse

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
        self.driver.get('https://buff.163.com/market/goods?goods_id=5486')
        self.csrf_token = self.wait().until(
            EC.presence_of_element_located((By.XPATH, '//meta[@name="csrf_token"]'))).get_attribute('content')
        print(self.csrf_token)

        self.cookies = self.driver.get_cookies()
        url = f'https://buff.163.com/api/market/goods/sell_order?game=dota2&goods_id=5486&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
        cookies = {cookie['name']: cookie['value'] for cookie in self.cookies}
        resp = requests.get(url,headers=headers,cookies=cookies)
        print(resp.content.decode())
        print(resp.cookies)


        url = f'https://buff.163.com/api/market/goods/buy/preview?game=dota2&sell_order_id=190730T1109261968&goods_id=5486&price=0.02&allow_tradable_cooldown=0&cdkey_id='
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
        resp = requests.get(url, headers=headers, cookies=cookies)

        url = f'https://buff.163.com/api/activity/coupon/my/?state=unuse&coupon_type=reduction&order_amount=0.02&sell_order_id=190730T1109261968'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
        resp = requests.get(url, headers=headers, cookies=cookies)



        headers = {'Host': 'buff.163.com',
'Connection': 'keep-alive',
'Content-Length': '149',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'X-CSRFToken': self.csrf_token,
'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
'Sec-Fetch-Mode': 'cors',
'Content-Type': 'application/json',
'Origin': 'https://buff.163.com',
'Sec-Fetch-Site': 'same-origin',
'Referer': 'https://buff.163.com/market/goods?goods_id=5486&from=market',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'}
        buy_url = 'https://buff.163.com/api/market/goods/buy'
        data ={"game":"dota2","goods_id":5486,"sell_order_id":"190730T1109261968","price":0.02,"pay_method":3,"allow_tradable_cooldown":0,"token":"","cdkey_id":""}
        resp = requests.post(buy_url, headers=headers, cookies=cookies,data=data)
        print(resp.content.decode())

    def run(self):
        self.login()
        self.get_price()
        self.close()

if __name__ == '__main__':
    b = Buff('17714552601','caowo1996')
    b.run()
    # print(parse.parse_qs('https://buff.163.com/market/goods?goods_id=3556&from=market#tab=selling&tag_ids=1410'))
    # print(parse.parse_qs('https://buff.163.com/api/market/goods/sell_order?game=dota2&goods_id=770362&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&tag_ids=1410'))
    # print(parse.parse_qs('https://buff.163.com/api/market/goods/sell_order?game=dota2&goods_id=5486&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1'))
    'https://buff.163.com/api/market/goods/buy'
    '''POST /api/market/goods/buy HTTP/1.1
Host: buff.163.com
Connection: keep-alive
Content-Length: 149
Accept: application/json, text/javascript, */*; q=0.01
X-CSRFToken: ImQwOWYwOWJkMTQyYTk0ZWM4MWVmNWQzOTY4YmFiODc3ZTM1ODhjYzUi.EChc3A.D5MIW8ri8NcRlAvP8kqz8xMP30Q
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36
Sec-Fetch-Mode: cors
Content-Type: application/json
Origin: https://buff.163.com
Sec-Fetch-Site: same-origin
Referer: https://buff.163.com/market/goods?goods_id=5486&from=market
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
'''
    '''{"game":"dota2","goods_id":5486,"sell_order_id":"190730T1109261971","price":0.02,"pay_method":3,"allow_tradable_cooldown":0,"token":"","cdkey_id":""}'''

    '{"code":"OK","data":{"appid":570,"asset_info":{"action_link":"","appid":570,"assetid":"16934164656","classid":"800899912","contextid":2,"goods_id":5486,"has_tradable_cooldown":false,"info":{"gems":[{"color":"#dedede","img_url":"https://g.fp.ps.netease.com/market/file/5a990d36ee4c0fc75df48e43g6TBUYaK","name":"\u94ed\u523b\u5b9d\u77f3","text":"\u6708\u5149\u51fb\u6740\u6570\uff1a0"}],"icon_url":"","unlock_style":[]},"instanceid":"1626850993","paintwear":"","tradable_cooldown_text":"\u7acb\u5373\u53ef\u53d6\u56de","tradable_unfrozen_time":null},"bundle_info":{},"buyer_cancel_timeout":null,"buyer_cookie_invalid":false,"buyer_id":"U1094711142","buyer_pay_time":1564921053,"buyer_send_offer_timeout":-1,"can_replace_asset":false,"coupon_info":null,"created_at":1564921053,"deliver_expire_timeout":-1,"error_text":null,"fail_confirm":null,"fee":"0","game":"dota2","goods_id":5486,"has_bargain":false,"has_sent_offer":false,"id":"190804T1136833713","income":"0","is_seller_asked_to_send_offer":false,"mode":2,"original_price":null,"pay_expire_timeout":-1,"pay_method":3,"pay_method_text":"BUFF\u4f59\u989d-\u652f\u4ed8\u5b9d","price":"0.02","progress":102,"receive_expire_timeout":-1,"sell_order_id":null,"seller_can_cancel":false,"seller_cookie_invalid":false,"seller_id":"U1094272341","state":"PAYING","state_text":"\u8ba2\u5355\u72b6\u6001\u786e\u8ba4\u4e2d","trade_offer_trace_url":null,"trade_offer_url":null,"tradeofferid":null,"transact_time":null,"type":1,"updated_at":1564921053},"msg":null}'