import aiohttp
import asyncio

url_list = ['https://buff.163.com/market/?game=dota2#tab=selling&page_num={}'.format(i) for i in range(20)]

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        print(html)


def aiohttp_run(url_list):
    loop = asyncio.get_event_loop()

    tasks = [main(url) for url in url_list]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__ == '__main__':
    aiohttp_run(url_list)
