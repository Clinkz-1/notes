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


'''{
  "code": "OK", 
  "data": {
    "goods_infos": {
      "5486": {
        "appid": 570, 
        "description": null, 
        "game": "dota2", 
        "goods_id": 5486, 
        "icon_url": "https://g.fp.ps.netease.com/market/file/5a0e98d38b742710cd289b41FvaIar2M", 
        "item_id": 7703, 
        "market_hash_name": "Inscribed Shattertooth", 
        "market_min_price": "0", 
        "name": "\u94ed\u523b \u65ad\u7259\u517d", 
        "original_icon_url": "https://g.fp.ps.netease.com/market/file/59926d125e60273b4cf3f007h863xlFl", 
        "steam_price": "0.03", 
        "steam_price_cny": "0.21", 
        "steam_price_custom": "0.03", 
        "tags": {
          "hero": {
            "category": "hero", 
            "internal_name": "npc_dota_hero_luna", 
            "localized_name": "\u9732\u5a1c"
          }, 
          "quality": {
            "category": "quality", 
            "internal_name": "strange", 
            "localized_name": "\u94ed\u523b"
          }, 
          "rarity": {
            "category": "rarity", 
            "internal_name": "rare", 
            "localized_name": "\u7a00\u6709"
          }, 
          "slot": {
            "category": "slot", 
            "internal_name": "mount", 
            "localized_name": "\u5750\u9a91"
          }, 
          "type": {
            "category": "type", 
            "internal_name": "wearable", 
            "localized_name": "\u53ef\u4f69\u5e26"
          }
        }
      }
    }, 
    "has_market_stores": {
      "U1092662570": true, 
      "U1092702738": true, 
      "U1093998360": true, 
      "U1094046319": true, 
      "U1094292095": true, 
      "U1094628447": true, 
      "U1094703859": true
    }, 
    "items": [
      {
        "allow_bargain": true, 
        "appid": 570, 
        "asset_info": {
          "action_link": "", 
          "appid": 570, 
          "assetid": "16427123636", 
          "classid": "800899912", 
          "contextid": 2, 
          "goods_id": 5486, 
          "has_tradable_cooldown": false, 
          "info": {
            "gems": [
              {
                "color": "#dedede", 
                "img_url": "https://g.fp.ps.netease.com/market/file/5a990d36ee4c0fc75df48e43g6TBUYaK", 
                "name": "\u94ed\u523b\u5b9d\u77f3", 
                "text": "\u6708\u8680\u51fb\u6740\u6570\uff1a0"
              }
            ], 
            "icon_url": "https://g.fp.ps.netease.com/market/file/5a0e98d38b742710cd289b41FvaIar2M", 
            "original_icon_url": "https://g.fp.ps.netease.com/market/file/59926d125e60273b4cf3f007h863xlFl", 
            "unlock_style": []
          }, 
          "instanceid": "3348980888", 
          "paintwear": "", 
          "tradable_cooldown_text": "\u7acb\u5373\u53ef\u53d6\u56de", 
          "tradable_unfrozen_time": null
        }, 
        "bookmarked": false, 
        "can_bargain": false, 
        "cannot_bargain_reason": "\u8be5\u7c7b\u9970\u54c1\u4e0d\u5141\u8bb8\u8fd8\u4ef7", 
        "created_at": 1563255772, 
        "description": "", 
        "featured": 0, 
        "fee": "0", 
        "game": "dota2", 
        "goods_id": 5486, 
        "id": "190716T1109929764", 
        "income": "0", 
        "lowest_bargain_price": "0.03", 
        "mode": 2, 
        "price": "0.04", 
        "recent_average_duration": 8134.0, 
        "recent_deliver_rate": 0.974359, 
        "state": 1, 
        "supported_pay_methods": [
          3, 
          1, 
          6, 
          7
        ], 
        "tradable_cooldown": null, 
        "updated_at": 1563255772, 
        "user_id": "U1094046319"
      }, 
      {
        "allow_bargain": true, 
        "appid": 570, 
        "asset_info": {
          "action_link": "", 
          "appid": 570, 
          "assetid": "16427123138", 
          "classid": "800899912", 
          "contextid": 2, 
          "goods_id": 5486, 
          "has_tradable_cooldown": false, 
          "info": {
            "gems": [
              {
                "color": "#dedede", 
                "img_url": "https://g.fp.ps.netease.com/market/file/5a990d36ee4c0fc75df48e43g6TBUYaK", 
                "name": "\u94ed\u523b\u5b9d\u77f3", 
                "text": "\u6708\u5149\u51fb\u6740\u6570\uff1a0"
              }
            ], 
            "icon_url": "https://g.fp.ps.netease.com/market/file/5a0e98d38b742710cd289b41FvaIar2M", 
            "original_icon_url": "https://g.fp.ps.netease.com/market/file/59926d125e60273b4cf3f007h863xlFl", 
            "unlock_style": []
          }, 
          "instanceid": "3348980890", 
          "paintwear": "", 
          "tradable_cooldown_text": "\u7acb\u5373\u53ef\u53d6\u56de", 
          "tradable_unfrozen_time": null
        }, 
        "bookmarked": false, 
        "can_bargain": false, 
        "cannot_bargain_reason": "\u8be5\u7c7b\u9970\u54c1\u4e0d\u5141\u8bb8\u8fd8\u4ef7", 
        "created_at": 1563255772, 
        "description": "", 
        "featured": 0, 
        "fee": "0", 
        "game": "dota2", 
        "goods_id": 5486, 
        "id": "190716T1109929772", 
        "income": "0", 
        "lowest_bargain_price": "0.03", 
        "mode": 2, 
        "price": "0.04", 
        "recent_average_duration": 8134.0, 
        "recent_deliver_rate": 0.974359, 
        "state": 1, 
        "supported_pay_methods": [
          3, 
          1, 
          6, 
          7
        ], 
        "tradable_cooldown": null, 
        "updated_at": 1563255772, 
        "user_id": "U1094046319"
      }, 
      {
        "allow_bargain": true, 
        "appid": 570, 
        "asset_info": {
          "action_link": "", 
          "appid": 570, 
          "assetid": "14160821334", 
          "classid": "800899912", 
          "contextid": 2, 
          "goods_id": 5486, 
          "has_tradable_cooldown": false, 
          "info": {
            "gems": [
              {
                "color": "#dedede", 
                "img_url": "https://g.fp.ps.netease.com/market/file/5a990d36ee4c0fc75df48e43g6TBUYaK", 
                "name": "\u94ed\u523b\u5b9d\u77f3", 
                "text": "\u6708\u8680\u51fb\u6740\u6570\uff1a0"
              }
            ], 
            "icon_url": "https://g.fp.ps.netease.com/market/file/5a0e98d38b742710cd289b41FvaIar2M", 
            "original_icon_url": "https://g.fp.ps.netease.com/market/file/59926d125e60273b4cf3f007h863xlFl", 
            "unlock_style": []
          }, 
          "instanceid": "1626514579", 
          "paintwear": "", 
          "tradable_cooldown_text": "\u7acb\u5373\u53ef\u53d6\u56de", 
          "tradable_unfrozen_time": null
        }, 
        "bookmarked": false, 
        "can_bargain": false, 
        "cannot_bargain_reason": "\u8be5\u7c7b\u9970\u54c1\u4e0d\u5141\u8bb8\u8fd8\u4ef7", 
        "created_at": 1563757109, 
        "description": "", 
        "featured": 0, 
        "fee": "0", 
        "game": "dota2", 
        "goods_id": 5486, 
        "id": "190722T1111219957", 
        "income": "0", 
        "lowest_bargain_price": "0.03", 
        "mode": 2, 
        "price": "0.04", 
        "recent_average_duration": 11190.0, 
        "recent_deliver_rate": 1.0, 
        "state": 1, 
        "supported_pay_methods": [
          3
        ], 
        "tradable_cooldown": null, 
        "updated_at": 1563757109, 
        "user_id": "U1094628447"
      }, 
      {
        "allow_bargain": true, 
        "appid": 570, 
        "asset_info": {
          "action_link": "", 
          "appid": 570, 
          "assetid": "15946722398", 
          "classid": "800899912", 
          "contextid": 2, 
          "goods_id": 5486, 
          "has_tradable_cooldown": false, 
          "info": {
            "gems": [
              {
                "color": "#dedede", 
                "img_url": "https://g.fp.ps.netease.com/market/file/5a990d36ee4c0fc75df48e43g6TBUYaK", 
                "name": "\u94ed\u523b\u5b9d\u77f3", 
                "text": "\u6708\u8680\u51fb\u6740\u6570\uff1a0"
              }
            ], 
            "icon_url": "https://g.fp.ps.netease.com/market/file/5a0e98d38b742710cd289b41FvaIar2M", 
            "original_icon_url": "https://g.fp.ps.netease.com/market/file/59926d125e60273b4cf3f007h863xlFl", 
            "unlock_style": []
          }, 
          "instanceid": "1626514579", 
          "paintwear": "", 
          "tradable_cooldown_text": "\u7acb\u5373\u53ef\u53d6\u56de", 
          "tradable_unfrozen_time": null
        }, 
        "bookmarked": false, 
        "can_bargain": false, 
        "cannot_bargain_reason": "\u8be5\u7c7b\u9970\u54c1\u4e0d\u5141\u8bb8\u8fd8\u4ef7", 
        "created_at": 1561998358, 
        "description": "", 
        "featured": 0, 
        "fee": "0", 
        "game": "dota2", 
        "goods_id": 5486, 
        "id": "190702T1140382905", 
        "income": "0", 
        "lowest_bargain_price": "0.07", 
        "mode": 2, 
        "price": "0.09", 
        "recent_average_duration": 522.0, 
        "recent_deliver_rate": 1.0, 
        "state": 1, 
        "supported_pay_methods": [
          3, 
          1, 
          6, 
          7
        ], 
        "tradable_cooldown": null, 
        "updated_at": 1563037243, 
        "user_id": "U1093998360"
      }, 
      {
        "allow_bargain": true, 
        "appid": 570, 
        "asset_info": {
          "action_link": "", 
          "appid": 570, 
          "assetid": "16421356062", 
          "classid": "800899912", 
          "contextid": 2, 
          "goods_id": 5486, 
          "has_tradable_cooldown": false, 
          "info": {
            "gems": [
              {
                "color": "#dedede", 
                "img_url": "https://g.fp.ps.netease.com/market/file/5a990d36ee4c0fc75df48e43g6TBUYaK", 
                "name": "\u94ed\u523b\u5b9d\u77f3", 
                "text": "\u6708\u8680\u51fb\u6740\u6570\uff1a0"
              }
            ], 
            "icon_url": "https://g.fp.ps.netease.com/market/file/5a0e98d38b742710cd289b41FvaIar2M", 
            "original_icon_url": "https://g.fp.ps.netease.com/market/file/59926d125e60273b4cf3f007h863xlFl", 
            "unlock_style": []
          }, 
          "instanceid": "1626514579", 
          "paintwear": "", 
          "tradable_cooldown_text": "\u7acb\u5373\u53ef\u53d6\u56de", 
          "tradable_unfrozen_time": null
        }, 
        "bookmarked": false, 
        "can_bargain": false, 
        "cannot_bargain_reason": "\u8be5\u7c7b\u9970\u54c1\u4e0d\u5141\u8bb8\u8fd8\u4ef7", 
        "created_at": 1562557723, 
        "description": "", 
        "featured": 0, 
        "fee": "0", 
        "game": "dota2", 
        "goods_id": 5486, 
        "id": "190708T1136959164", 
        "income": "0", 
        "lowest_bargain_price": "0.07", 
        "mode": 2, 
        "price": "0.09", 
        "recent_average_duration": 1029.0, 
        "recent_deliver_rate": 1.0, 
        "state": 1, 
        "supported_pay_methods": [
          3, 
          1, 
          6, 
          7
        ], 
        "tradable_cooldown": null, 
        "updated_at": 1562557723, 
        "user_id": "U1092662570"
      }, 
      {
        "allow_bargain": true, 
        "appid": 570, 
        "asset_info": {
          "action_link": "", 
          "appid": 570, 
          "assetid": "16421399706", 
          "classid": "800899912", 
          "contextid": 2, 
          "goods_id": 5486, 
          "has_tradable_cooldown": false, 
          "info": {
            "gems": [
              {
                "color": "#dedede", 
                "img_url": "https://g.fp.ps.netease.com/market/file/5a990d36ee4c0fc75df48e43g6TBUYaK", 
                "name": "\u94ed\u523b\u5b9d\u77f3", 
                "text": "\u6708\u5149\u51fb\u6740\u6570\uff1a0"
              }
            ], 
            "icon_url": "https://g.fp.ps.netease.com/market/file/5a0e98d38b742710cd289b41FvaIar2M", 
            "original_icon_url": "https://g.fp.ps.netease.com/market/file/59926d125e60273b4cf3f007h863xlFl", 
            "unlock_style": []
          }, 
          "instanceid": "1626850993", 
          "paintwear": "", 
          "tradable_cooldown_text": "\u7acb\u5373\u53ef\u53d6\u56de", 
          "tradable_unfrozen_time": null
        }, 
        "bookmarked": false, 
        "can_bargain": false, 
        "cannot_bargain_reason": "\u8be5\u7c7b\u9970\u54c1\u4e0d\u5141\u8bb8\u8fd8\u4ef7", 
        "created_at": 1562558295, 
        "description": "", 
        "featured": 0, 
        "fee": "0", 
        "game": "dota2", 
        "goods_id": 5486, 
        "id": "190708T1136961312", 
        "income": "0", 
        "lowest_bargain_price": "0.07", 
        "mode": 2, 
        "price": "0.09", 
        "recent_average_duration": 1029.0, 
        "recent_deliver_rate": 1.0, 
        "state": 1, 
        "supported_pay_methods": [
          3, 
          1, 
          6, 
          7
        ], 
        "tradable_cooldown": null, 
        "updated_at": 1562558295, 
        "user_id": "U1092662570"
      }, 
      {
        "allow_bargain": true, 
        "appid": 570, 
        "asset_info": {
          "action_link": "", 
          "appid": 570, 
          "assetid": "16421398494", 
          "classid": "800899912", 
          "contextid": 2, 
          "goods_id": 5486, 
          "has_tradable_cooldown": false, 
          "info": {
            "gems": [
              {
                "color": "#dedede", 
                "img_url": "https://g.fp.ps.netease.com/market/file/5a990d36ee4c0fc75df48e43g6TBUYaK", 
                "name": "\u94ed\u523b\u5b9d\u77f3", 
                "text": "\u6708\u5149\u51fb\u6740\u6570\uff1a0"
              }
            ], 
            "icon_url": "https://g.fp.ps.netease.com/market/file/5a0e98d38b742710cd289b41FvaIar2M", 
            "original_icon_url": "https://g.fp.ps.netease.com/market/file/59926d125e60273b4cf3f007h863xlFl", 
            "unlock_style": []
          }, 
          "instanceid": "1626850993", 
          "paintwear": "", 
          "tradable_cooldown_text": "\u7acb\u5373\u53ef\u53d6\u56de", 
          "tradable_unfrozen_time": null
        }, 
        "bookmarked": false, 
        "can_bargain": false, 
        "cannot_bargain_reason": "\u8be5\u7c7b\u9970\u54c1\u4e0d\u5141\u8bb8\u8fd8\u4ef7", 
        "created_at": 1562558295, 
        "description": "", 
        "featured": 0, 
        "fee": "0", 
        "game": "dota2", 
        "goods_id": 5486, 
        "id": "190708T1136961313", 
        "income": "0", 
        "lowest_bargain_price": "0.07", 
        "mode": 2, 
        "price": "0.09", 
        "recent_average_duration": 1029.0, 
        "recent_deliver_rate": 1.0, 
        "state": 1, 
        "supported_pay_methods": [
          3, 
          1, 
          6, 
          7
        ], 
        "tradable_cooldown": null, 
        "updated_at": 1562558295, 
        "user_id": "U1092662570"
      }, 
      {
        "allow_bargain": true, 
        "appid": 570, 
        "asset_info": {
          "action_link": "", 
          "appid": 570, 
          "assetid": "13519024686", 
          "classid": "800899912", 
          "contextid": 2, 
          "goods_id": 5486, 
          "has_tradable_cooldown": false, 
          "info": {
            "gems": [
              {
                "color": "#dedede", 
                "img_url": "https://g.fp.ps.netease.com/market/file/5a990d36ee4c0fc75df48e43g6TBUYaK", 
                "name": "\u94ed\u523b\u5b9d\u77f3", 
                "text": "\u6708\u8680\u51fb\u6740\u6570\uff1a3"
              }
            ], 
            "icon_url": "https://g.fp.ps.netease.com/market/file/5a0e98d38b742710cd289b41FvaIar2M", 
            "original_icon_url": "https://g.fp.ps.netease.com/market/file/59926d125e60273b4cf3f007h863xlFl", 
            "unlock_style": []
          }, 
          "instanceid": "3197880860", 
          "paintwear": "", 
          "tradable_cooldown_text": "\u7acb\u5373\u53ef\u53d6\u56de", 
          "tradable_unfrozen_time": null
        }, 
        "bookmarked": false, 
        "can_bargain": false, 
        "cannot_bargain_reason": "\u8be5\u7c7b\u9970\u54c1\u4e0d\u5141\u8bb8\u8fd8\u4ef7", 
        "created_at": 1556183938, 
        "description": "", 
        "featured": 0, 
        "fee": "0", 
        "game": "dota2", 
        "goods_id": 5486, 
        "id": "190425T1124711446", 
        "income": "0", 
        "lowest_bargain_price": "0.08", 
        "mode": 2, 
        "price": "0.1", 
        "recent_average_duration": null, 
        "recent_deliver_rate": null, 
        "state": 1, 
        "supported_pay_methods": [
          3, 
          1, 
          6, 
          7
        ], 
        "tradable_cooldown": null, 
        "updated_at": 1556183938, 
        "user_id": "U1094703859"
      }, 
      {
        "allow_bargain": true, 
        "appid": 570, 
        "asset_info": {
          "action_link": "", 
          "appid": 570, 
          "assetid": "16410235421", 
          "classid": "800899912", 
          "contextid": 2, 
          "goods_id": 5486, 
          "has_tradable_cooldown": false, 
          "info": {
            "gems": [
              {
                "color": "#dedede", 
                "img_url": "https://g.fp.ps.netease.com/market/file/5a990d36ee4c0fc75df48e43g6TBUYaK", 
                "name": "\u94ed\u523b\u5b9d\u77f3", 
                "text": "\u6708\u8680\u51fb\u6740\u6570\uff1a0"
              }
            ], 
            "icon_url": "https://g.fp.ps.netease.com/market/file/5a0e98d38b742710cd289b41FvaIar2M", 
            "original_icon_url": "https://g.fp.ps.netease.com/market/file/59926d125e60273b4cf3f007h863xlFl", 
            "unlock_style": []
          }, 
          "instanceid": "1626514579", 
          "paintwear": "", 
          "tradable_cooldown_text": "\u7acb\u5373\u53ef\u53d6\u56de", 
          "tradable_unfrozen_time": null
        }, 
        "bookmarked": false, 
        "can_bargain": false, 
        "cannot_bargain_reason": "\u8be5\u7c7b\u9970\u54c1\u4e0d\u5141\u8bb8\u8fd8\u4ef7", 
        "created_at": 1562546108, 
        "description": "", 
        "featured": 0, 
        "fee": "0", 
        "game": "dota2", 
        "goods_id": 5486, 
        "id": "190708T1136928025", 
        "income": "0", 
        "lowest_bargain_price": "0.08", 
        "mode": 2, 
        "price": "0.1", 
        "recent_average_duration": 415.0, 
        "recent_deliver_rate": 1.0, 
        "state": 1, 
        "supported_pay_methods": [
          3, 
          1, 
          6, 
          7
        ], 
        "tradable_cooldown": null, 
        "updated_at": 1562546108, 
        "user_id": "U1094292095"
      }, 
      {
        "allow_bargain": true, 
        "appid": 570, 
        "asset_info": {
          "action_link": "", 
          "appid": 570, 
          "assetid": "13164524587", 
          "classid": "800899912", 
          "contextid": 2, 
          "goods_id": 5486, 
          "has_tradable_cooldown": false, 
          "info": {
            "gems": [
              {
                "color": "#dedede", 
                "img_url": "https://g.fp.ps.netease.com/market/file/5a990d36ee4c0fc75df48e43g6TBUYaK", 
                "name": "\u94ed\u523b\u5b9d\u77f3", 
                "text": "\u6708\u5149\u51fb\u6740\u6570\uff1a0"
              }
            ], 
            "icon_url": "https://g.fp.ps.netease.com/market/file/5a0e98d38b742710cd289b41FvaIar2M", 
            "original_icon_url": "https://g.fp.ps.netease.com/market/file/59926d125e60273b4cf3f007h863xlFl", 
            "unlock_style": []
          }, 
          "instanceid": "1626850993", 
          "paintwear": "", 
          "tradable_cooldown_text": "\u7acb\u5373\u53ef\u53d6\u56de", 
          "tradable_unfrozen_time": null
        }, 
        "bookmarked": false, 
        "can_bargain": false, 
        "cannot_bargain_reason": "\u8be5\u7c7b\u9970\u54c1\u4e0d\u5141\u8bb8\u8fd8\u4ef7", 
        "created_at": 1547631003, 
        "description": "", 
        "featured": 0, 
        "fee": "0", 
        "game": "dota2", 
        "goods_id": 5486, 
        "id": "190116T1081589886", 
        "income": "0", 
        "lowest_bargain_price": "0.16", 
        "mode": 1, 
        "price": "0.2", 
        "recent_average_duration": null, 
        "recent_deliver_rate": null, 
        "state": 1, 
        "supported_pay_methods": [
          3, 
          1, 
          6, 
          7
        ], 
        "tradable_cooldown": null, 
        "updated_at": 1547631003, 
        "user_id": "U1092702738"
      }
    ], 
    "page_num": 1, 
    "page_size": 10, 
    "sort_by": "price.asc", 
    "total_count": 18, 
    "total_page": 2, 
    "user_infos": {
      "U1092662570": {
        "avatar": "https://g.fp.ps.netease.com/market/file/5ac1c7b216b6d4851b2ded2eQI4vcVaM", 
        "avatar_safe": "https://g.fp.ps.netease.com/market/file/5ac1c7b216b6d4851b2ded2eQI4vcVaM", 
        "nickname": "\u7231\u98de\u7684\u9c7c", 
        "seller_level": 0, 
        "shop_id": "1092662570", 
        "user_id": "U1092662570"
      }, 
      "U1092702738": {
        "avatar": "https://g.fp.ps.netease.com/market/file/5a8444a3143cfa4529ce743djboBWPj7", 
        "avatar_safe": "https://g.fp.ps.netease.com/market/file/5a8444a3143cfa4529ce743djboBWPj7", 
        "nickname": "U15175632902", 
        "seller_level": 0, 
        "shop_id": "1092702738", 
        "user_id": "U1092702738"
      }, 
      "U1093998360": {
        "avatar": "https://g.fp.ps.netease.com/market/file/5c52826f6f049448938bbd00XVY7U3ub02", 
        "avatar_safe": "https://g.fp.ps.netease.com/market/file/5c52826f6f049448938bbd00XVY7U3ub02", 
        "nickname": "\u6781\u901f\u53d1\u8d27\u4e2d", 
        "seller_level": 0, 
        "shop_id": "1093998360", 
        "user_id": "U1093998360"
      }, 
      "U1094046319": {
        "avatar": "https://g.fp.ps.netease.com/market/file/5cc2eb425e6027e7cbf648e5TboKjVYA02", 
        "avatar_safe": "https://g.fp.ps.netease.com/market/file/5cc2eb425e6027e7cbf648e5TboKjVYA02", 
        "nickname": "Facet", 
        "seller_level": 0, 
        "shop_id": "1094046319", 
        "user_id": "U1094046319"
      }, 
      "U1094292095": {
        "avatar": "https://g.fp.ps.netease.com/market/file/5bacf8e77f9d2ae88e73a621jfrYtZG8", 
        "avatar_safe": "https://g.fp.ps.netease.com/market/file/5bacf8e77f9d2ae88e73a621jfrYtZG8", 
        "nickname": "\u5e73\u6c11\u81ea\u7528\u73a9\u5bb6", 
        "seller_level": 0, 
        "shop_id": "1094292095", 
        "user_id": "U1094292095"
      }, 
      "U1094628447": {
        "avatar": "https://g.fp.ps.netease.com/market/file/5b7a00657f9d2ada9096770aIAQ2SeYB", 
        "avatar_safe": "https://g.fp.ps.netease.com/market/file/5b7a00657f9d2ada9096770aIAQ2SeYB", 
        "nickname": "\u9e7f\u795e", 
        "seller_level": 0, 
        "shop_id": "1094628447", 
        "user_id": "U1094628447"
      }, 
      "U1094703859": {
        "avatar": "https://g.fp.ps.netease.com/market/file/5b8978fd6f0494210272c940EjB5UQTk", 
        "avatar_safe": "https://g.fp.ps.netease.com/market/file/5b8978fd6f0494210272c940EjB5UQTk", 
        "nickname": "\u5e03\u62c9\u62c9\u5e03\u62c9\u591a", 
        "seller_level": 0, 
        "shop_id": "1094703859", 
        "user_id": "U1094703859"
      }
    }
  }, 
  "msg": null
}'''