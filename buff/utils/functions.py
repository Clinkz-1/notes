import re
from data.config import config
from data.cookies import cookies
from deal_xls import XlReader
from mysql_test import MysqlClient
from redis_test import RedisClient
from aiohttp_test import AiohttpClient


def excel2mysql():
    r = XlReader('../data/goods.xlsx')
    goods_dict = r.read('goods')
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
    s = MysqlClient(config['mysql_user'], config['mysql_password'], config['mysql_database_name'])
    r.zremall()
    goods_querys = s.find(col_list=['query_url','price'])
    for query_one in goods_querys:
        r.zadd(*query_one)
    s.close()
    r.close()


def query2redis():
    rq = RedisClient(zset_name='query_url_price')
    rb = RedisClient(zset_name='buy_id_goodstag_id')
    url_price_list = rq.zrange()
    a = AiohttpClient(url_price_list,cookies=cookies)
    buy_id_goodstag_id = a.aiohttp_run()
    if buy_id_goodstag_id:
        for item in buy_id_goodstag_id:
            rb.zadd(*item)
    rq.close()
    rb.close()


if __name__ == '__main__':
    excel2mysql()
    mysql2redis()
