import asyncio
import aiohttp
import sys
from bs4 import BeautifulSoup as BS
from datetime import datetime
from fake_useragent import UserAgent

BASE_URL = "https://ru.investing.com/equities"
URL_SITE = "https://ru.investing.com"
HEADERS = {"User-Agent": UserAgent().random}

async def ALL():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, headers=HEADERS) as response:
            variableRead = await aiohttp.StreamReader.read(response.content)
            variableSITE = BS(variableRead, 'html.parser')
            links = variableSITE.find_all("a", {"class": "overflow-hidden text-ellipsis whitespace-nowrap font-semibold text-[#181C21] hover:text-[#1256A0]"})

            for link in links:
                URL_EQUITIES = f"{URL_SITE}/{link.get('href')}"

                async with session.get(URL_EQUITIES, headers=HEADERS) as response:
                    variableRead = await aiohttp.StreamReader.read(response.content)
                    variableSITE = BS(variableRead, 'html.parser')

                    price = variableSITE.find("div", {"class": "text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]"})

                    if price is not None:
                        print(f'equities: UNDEFINED\t| price: {price.text} ₽\t| links: {URL_EQUITIES}')
                    else:
                        print(f'Error: Price not found for {URL_EQUITIES}')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(ALL())