import asyncio
import aiohttp
import json
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent

HEADERS = {"User-Agent": UserAgent().random}

BASE_URL = "https://ru.investing.com/equities"
URL_SITE = "https://ru.investing.com"

URL_TCSG = "https://www.tinkoff.ru/invest/stocks/TCSG/"
URL_SBER = "https://www.tinkoff.ru/invest/stocks/SBER/"
URL_YNDX = "https://www.tinkoff.ru/invest/stocks/YNDX/"
URL_LKOH = "https://www.tinkoff.ru/invest/stocks/LKOH/"
URL_VTBR = "https://www.tinkoff.ru/invest/stocks/VTBR/"
URL_GAZP = "https://www.tinkoff.ru/invest/stocks/GAZP/"
URL_MGNT = "https://www.tinkoff.ru/invest/stocks/MGNT/"
URL_SGZH = "https://www.tinkoff.ru/invest/stocks/SGZH/"

DATA_EQUITIES = {
    "EQUILITES": []
}

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


async def TCSG():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL_TCSG, headers=HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, 'html.parser')

            indicators = soup.find_all("div", {"class": "SecuritySummary__value_yAWfT"})
            
            if indicators:
                priceOpen = indicators[0]
                priceClose = indicators[1]
                name = soup.find("span", {"class", "SecurityHeader__showName_iw6qC"})
                title = soup.find("span", {"class": "SecurityHeader__ticker_j7fZW"})
                
                if priceOpen and priceClose and name and title:
                    priceOpen = indicators[0].text
                    priceClose = indicators[1].text
                    name = soup.find("span", {"class", "SecurityHeader__showName_iw6qC"}).text
                    title = soup.find("span", {"class": "SecurityHeader__ticker_j7fZW"}).text
                    
                    DATA_EQUITIES["EQUILITES"].append({
                        "name": name,
                        "title": title,
                        "price_openning": priceOpen,
                        "price_closed": priceClose
                    })
                    
                    def write(data, filename):
                        data = json.dumps(data)
                        data = json.loads(str(data))
                        with open(filename, 'w', encoding = 'utf-8') as file:
                            json.dump(data, file, indent=4)
                            
                    write(DATA_EQUITIES, 'JSON_EQUITIES.json')
                            

async def SBER():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL_SBER, headers=HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, 'html.parser')

            indicators = soup.find_all("div", {"class": "SecuritySummary__value_yAWfT"})
            
            if indicators:
                priceOpen = indicators[0]
                priceClose = indicators[1]
                name = soup.find("span", {"class", "SecurityHeader__showName_iw6qC"})
                title = soup.find("span", {"class": "SecurityHeader__ticker_j7fZW"})
                
                if priceOpen and priceClose and name and title:
                    priceOpen = indicators[0].text
                    priceClose = indicators[1].text
                    name = soup.find("span", {"class", "SecurityHeader__showName_iw6qC"}).text
                    title = soup.find("span", {"class": "SecurityHeader__ticker_j7fZW"}).text
                    
                    DATA_EQUITIES["EQUILITES"].append({
                        "name": name,
                        "title": title,
                        "price_openning": priceOpen,
                        "price_closed": priceClose
                    })
                        
                    def write(data, filename):
                        data = json.dumps(data)
                        data = json.loads(str(data))
                        with open(filename, 'w', encoding = 'utf-8') as file:
                            json.dump(data, file, indent=4)
                            
                    write(DATA_EQUITIES, 'JSON_EQUITIES.json')
                    

async def YNDX():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL_YNDX, headers=HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, 'html.parser')

            indicators = soup.find_all("div", {"class": "SecuritySummary__value_yAWfT"})
            
            if indicators:
                priceOpen = indicators[0]
                priceClose = indicators[1]
                name = soup.find("span", {"class", "SecurityHeader__showName_iw6qC"})
                title = soup.find("span", {"class": "SecurityHeader__ticker_j7fZW"})
                
                if priceOpen and priceClose and name and title:
                    priceOpen = indicators[0].text
                    priceClose = indicators[1].text
                    name = soup.find("span", {"class", "SecurityHeader__showName_iw6qC"}).text
                    title = soup.find("span", {"class": "SecurityHeader__ticker_j7fZW"}).text

                    DATA_EQUITIES["EQUILITES"].append({
                        "name": name,
                        "title": title,
                        "price_openning": priceOpen,
                        "price_closed": priceClose
                    })

                    def write(data, filename):
                        data = json.dumps(data)
                        data = json.loads(str(data))
                        with open(filename, 'w', encoding = 'utf-8') as file:
                            json.dump(data, file, indent=4)
                            
                    write(DATA_EQUITIES, 'JSON_EQUITIES.json')


async def LKOH():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL_LKOH, headers=HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, 'html.parser')

            indicators = soup.find_all("div", {"class": "SecuritySummary__value_yAWfT"})
            
            if indicators:
                priceOpen = indicators[0]
                priceClose = indicators[1]
                name = soup.find("span", {"class", "SecurityHeader__showName_iw6qC"})
                title = soup.find("span", {"class": "SecurityHeader__ticker_j7fZW"})
                
                if priceOpen and priceClose and name and title:
                    priceOpen = indicators[0].text
                    priceClose = indicators[1].text
                    name = soup.find("span", {"class", "SecurityHeader__showName_iw6qC"}).text
                    title = soup.find("span", {"class": "SecurityHeader__ticker_j7fZW"}).text      
                    
                    DATA_EQUITIES["EQUILITES"].append({
                        "name": name,
                        "title": title,
                        "price_openning": priceOpen,
                        "price_closed": priceClose
                    })  

                    def write(data, filename):
                        data = json.dumps(data)
                        data = json.loads(str(data))
                        with open(filename, 'w', encoding = 'utf-8') as file:
                            json.dump(data, file, indent=4)
                            
                    write(DATA_EQUITIES, 'JSON_EQUITIES.json')


async def VTBR():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL_VTBR, headers=HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, 'html.parser')

            indicators = soup.find_all("div", {"class": "SecuritySummary__value_yAWfT"})
            
            if indicators:
                priceOpen = indicators[0]
                priceClose = indicators[1]
                name = soup.find("span", {"class", "SecurityHeader__showName_iw6qC"})
                title = soup.find("span", {"class": "SecurityHeader__ticker_j7fZW"})
                
                if priceOpen and priceClose and name and title:
                    priceOpen = indicators[0].text
                    priceClose = indicators[1].text
                    name = soup.find("span", {"class", "SecurityHeader__showName_iw6qC"}).text
                    title = soup.find("span", {"class": "SecurityHeader__ticker_j7fZW"}).text
                    
                    DATA_EQUITIES["EQUILITES"].append({
                        "name": name,
                        "title": title,
                        "price_openning": priceOpen,
                        "price_closed": priceClose
                    })       

                    def write(data, filename):
                        data = json.dumps(data)
                        data = json.loads(str(data))
                        with open(filename, 'w', encoding = 'utf-8') as file:
                            json.dump(data, file, indent=4)
                            
                    write(DATA_EQUITIES, 'JSON_EQUITIES.json')


async def GAZP():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL_GAZP, headers=HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, 'html.parser')

            indicators = soup.find_all("div", {"class": "SecuritySummary__value_yAWfT"})
            
            if indicators:
                priceOpen = indicators[0]
                priceClose = indicators[1]
                name = soup.find("span", {"class", "SecurityHeader__showName_iw6qC"})
                title = soup.find("span", {"class": "SecurityHeader__ticker_j7fZW"})
                
                if priceOpen and priceClose and name and title:
                    priceOpen = indicators[0].text
                    priceClose = indicators[1].text
                    name = soup.find("span", {"class", "SecurityHeader__showName_iw6qC"}).text
                    title = soup.find("span", {"class": "SecurityHeader__ticker_j7fZW"}).text
                    
                    DATA_EQUITIES["EQUILITES"].append({
                        "name": name,
                        "title": title,
                        "price_openning": priceOpen,
                        "price_closed": priceClose
                    })

                    def write(data, filename):
                        data = json.dumps(data)
                        data = json.loads(str(data))
                        with open(filename, 'w', encoding = 'utf-8') as file:
                            json.dump(data, file, indent=4)
                            
                    write(DATA_EQUITIES, 'JSON_EQUITIES.json')

                    
async def MGNT():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL_MGNT, headers=HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, 'html.parser')

            indicators = soup.find_all("div", {"class": "SecuritySummary__value_yAWfT"})
            
            if indicators:
                priceOpen = indicators[0]
                priceClose = indicators[1]
                name = soup.find("span", {"class", "SecurityHeader__showName_iw6qC"})
                title = soup.find("span", {"class": "SecurityHeader__ticker_j7fZW"})
                
                if priceOpen and priceClose and name and title:
                    priceOpen = indicators[0].text
                    priceClose = indicators[1].text
                    name = soup.find("span", {"class", "SecurityHeader__showName_iw6qC"}).text
                    title = soup.find("span", {"class": "SecurityHeader__ticker_j7fZW"}).text
                    
                    DATA_EQUITIES["EQUILITES"].append({
                        "name": name,
                        "title": title,
                        "price_openning": priceOpen,
                        "price_closed": priceClose
                    })
                    
                    def write(data, filename):
                        data = json.dumps(data)
                        data = json.loads(str(data))
                        with open(filename, 'w', encoding = 'utf-8') as file:
                            json.dump(data, file, indent=4)
                            
                    write(DATA_EQUITIES, 'JSON_EQUITIES.json')   


async def SGZH():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL_SGZH, headers=HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, 'html.parser')

            indicators = soup.find_all("div", {"class": "SecuritySummary__value_yAWfT"})
            
            if indicators:
                priceOpen = indicators[0]
                priceClose = indicators[1]
                name = soup.find("span", {"class", "SecurityHeader__showName_iw6qC"})
                title = soup.find("span", {"class": "SecurityHeader__ticker_j7fZW"})
                
                if priceOpen and priceClose and name and title:
                    priceOpen = indicators[0].text
                    priceClose = indicators[1].text
                    name = soup.find("span", {"class", "SecurityHeader__showName_iw6qC"}).text
                    title = soup.find("span", {"class": "SecurityHeader__ticker_j7fZW"}).text
                    
                    DATA_EQUITIES["EQUILITES"].append({
                        "name": name,
                        "title": title,
                        "price_openning": priceOpen,
                        "price_closed": priceClose
                    })
                    
                    def write(data, filename):
                        data = json.dumps(data)
                        data = json.loads(str(data))
                        with open(filename, 'w', encoding = 'utf-8') as file:
                            json.dump(data, file, indent=4)
                            
                    write(DATA_EQUITIES, 'JSON_EQUITIES.json')   
          

def mainEquities():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(TCSG())
    loop.run_until_complete(SBER())
    loop.run_until_complete(YNDX())
    loop.run_until_complete(LKOH())
    loop.run_until_complete(VTBR())
    loop.run_until_complete(GAZP())
    loop.run_until_complete(MGNT())
    loop.run_until_complete(SGZH())
    
if __name__ == '__main__':
    mainEquities()


# print(f'{priceClose}, {priceOpen}, {title}, {name}')