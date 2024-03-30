import asyncio
import aiohttp
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent

HEADERS = {"User-Agent": UserAgent().random}

BASE_URL = "https://ru.investing.com/equities"
URL_SITE = "https://ru.investing.com"

            
async def IndexMOEX():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, headers=HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, 'html.parser')
            links = soup.find_all("a", {"class": "overflow-hidden text-ellipsis whitespace-nowrap font-semibold text-[#181C21] hover:text-[#1256A0]"})

            for link in links:
                URL_EQUITIES = f"{URL_SITE}/{link.get('href')}"

                async with session.get(URL_EQUITIES, headers=HEADERS) as response:
                    r = await aiohttp.StreamReader.read(response.content)
                    soup = BS(r, 'html.parser')

                    price = soup.find("div", {"class": "text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]"}).text
                    title = soup.find("h1", {"class": "mb-2.5 text-left text-xl font-bold leading-7 text-[#232526] md:mb-2 md:text-3xl md:leading-8 rtl:soft-ltr"}).text
                    
                    print(f'price: {price} ₽ \t | equities: {title}')


def mainEquities():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(IndexMOEX())

if __name__ == '__main__':
    mainEquities()
    