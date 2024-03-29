import asyncio
import aiohttp
import sys

from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent
from datetime import datetime

BASE_URL = "https://ru.investing.com/equities/sberbank_rts"
HEADERS = {"User-Agent": UserAgent().random}

async def main():
    async with aiohttp.ClientSession() as session:
         async with session.get(BASE_URL, headers=HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, 'html.parser')
            
            items = soup.find("div", {"class": "text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]"}).text
            print(items)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())