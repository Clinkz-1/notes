import aiohttp
import asyncio

url_list = ['https://buff.163.com/market/?game=dota2#tab=selling&page_num={}'.format(i) for i in range(20)]

async def main(pool,url_list):  # 启动
    sem = asyncio.Semaphore(pool)
    async with aiohttp.ClientSession() as session:  # 给所有的请求，创建同一个session
        tasks = []
        for url in url_list:
            tasks.append(control_sem(sem,url,session))
        await asyncio.wait(tasks)


async def control_sem(sem, url, session):  # 限制信号量
    async with sem:
        await fetch(url, session)


async def fetch(url, session):  # 开启异步请求
    async with session.get(url,headers=headers) as resp:
        html = await resp.text()
        print(url)

def aiohttp_run(url_list):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(2,url_list))

if __name__ == '__main__':
    aiohttp_run(url_list)
