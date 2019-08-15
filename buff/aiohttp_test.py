import aiohttp
import asyncio

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
class AiohttpClient:
    def __init__(self,url_price_list,cookies={},headers=headers,pool=5):
        self.url_price_dict = {url_price[0]:url_price[1] for url_price in url_price_list}
        self.cookies = cookies
        self.headers = headers
        self.pool = pool
        self.buy_id_price = []

    async def main(self):  # 启动
        sem = asyncio.Semaphore(self.pool)
        async with aiohttp.ClientSession(headers=self.headers,cookies=self.cookies) as session:  # 给所有的请求，创建同一个session
            tasks = []
            for url in self.url_price_dict:
                tasks.append(self.control_sem(sem,url,session))
            await asyncio.wait(tasks)


    async def control_sem(self,sem, url, session):  # 限制信号量
        async with sem:
            await self.fetch(url, session)


    async def fetch(self,url, session):  # 开启异步请求
        try:
            async with session.get(url) as resp:
                query_goods = await resp.json()
                self.deal_data(url,query_goods)
        except Exception as e:
            print(url,e)
            pass


    def aiohttp_run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.main())
        return self.buy_id_price

    def deal_data(self,url,query_goods):
        for goods in query_goods['data']['items']:
            if float(goods['price']) <= self.url_price_dict[url]:
                self.buy_id_price.append((goods['id'],float(goods['price'])))


if __name__ == '__main__':
    a = AiohttpClient(url_price_list,cookies)
    buy_id_price = a.aiohttp_run()

