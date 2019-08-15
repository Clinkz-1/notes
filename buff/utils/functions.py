import re

from deal_xls import XlReader
from mysql_test import MysqlClient
from redis_test import RedisClient
from aiohttp_test import AiohttpClient


def get_config():
    with open('../config','r',encoding='utf8')as f:
        lines = f.readlines()
    config_dict = {}
    for line in lines:
        match = re.search(r'(?P<key>.*\b)\s*=\s*(?P<val>\b.*)',line)
        if match:
            config_dict[match['key'].strip()] = match['val'].strip()
    with open('../data/config.py','w')as f:
        f.write('config=')
        f.write(str(config_dict))

def excel2mysql():
    r = XlReader('../data/goods.xlsx')
    goods_dict = r.read('goods')
    from data.config import config
    s = MysqlClient(config['mysql_user'],config['mysql_password'],config['mysql_database_name'])
    s.drop_table()
    s.create_table()
    for goods in goods_dict:
        goods_id = re.findall('goods_id=(\d+)',goods['URL'])
        tag_ids = re.findall('tag_ids=(\d+)',goods['URL'])
        if not goods_id:continue
        goods_id = goods_id[0]
        if tag_ids:
            tag_ids = tag_ids[0]
            query_url = f'https://buff.163.com/api/market/goods/sell_order?game=dota2&goods_id={goods_id}&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&tag_ids={tag_ids}'
        else:
            tag_ids = None
            query_url = f'https://buff.163.com/api/market/goods/sell_order?game=dota2&goods_id={goods_id}&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1'
        s.insert_one(0,int(goods_id),int(tag_ids),goods['Price'],goods['URL'],query_url)
    s.close()

def mysql2redis():
    r = RedisClient(zset_name='query_url_price')
    from data.config import config
    s = MysqlClient(config['mysql_user'], config['mysql_password'], config['mysql_database_name'])
    r.zremall()
    goods_querys = s.find(col_list=['query_url','price'])
    for query_one in goods_querys:
        r.zadd(*query_one)
    s.close()
    r.close()

def query2redis():
    rq = RedisClient(zset_name='query_url_price')
    rb = RedisClient(zset_name='buy_id_price')
    url_price_list = rq.zrange()
    a = AiohttpClient(url_price_list,headers,cookies)
    buy_id_price = a.aiohttp_run()
    if buy_id_price:
        for item in buy_id_price:
            rb.zadd(*item)
    rq.close()
    rb.close()

def redis2buy():
    pass


if __name__ == '__main__':
    # get_config()
    # excel2mysql()
    mysql2redis()
