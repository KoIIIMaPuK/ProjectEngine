import asyncio
import aiohttp
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent


async def IndexMOEX():
    BASE_URL = "https://ru.investing.com/equities"
    URL_SITE = "https://ru.investing.com"
    HEADERS = {"User-Agent": UserAgent().random}
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, headers=HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            variableSITE = BS(r, 'html.parser')
            links = variableSITE.find_all("a", {"class": "overflow-hidden text-ellipsis whitespace-nowrap font-semibold text-[#181C21] hover:text-[#1256A0]"})

            for link in links:
                URL_EQUITIES = f"{URL_SITE}/{link.get('href')}"

                async with session.get(URL_EQUITIES, headers=HEADERS) as response:
                    r = await aiohttp.StreamReader.read(response.content)
                    variableSITE = BS(r, 'html.parser')

                    price = variableSITE.find("div", {"class": "text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]"})
                    title = variableSITE.find("h1", {"class": "mb-2.5 text-left text-xl font-bold leading-7 text-[#232526] md:mb-2 md:text-3xl md:leading-8 rtl:soft-ltr"})
                    time = variableSITE.find("div", {"class": "flex items-center gap-1 text-xs/4 text-[#5B616E]"})
                    
                    print(f'price: {price.text} ₽ \t | equities: {title.text} \t | time: {''.join(c if (c.isdigit() or c == ':') else '' for c in time.text)}')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(IndexMOEX())
    
# Добавить гены для нейронки. Сделать их как подключаемыми файлами