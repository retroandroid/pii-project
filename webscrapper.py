import aiohttp
import asyncio
from bs4 import BeautifulSoup
#max amount of connections
concurrent = 10
#function for fetching html file for a single url
async def fetch(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            return await response.text()
    except Exception as e:
        # Replace with proper logging
        print(f"Error fetching {url}: {e}")
        return None
#and this is the main function to request request from all the urls and limit connections
async def main(urls, max_connections):
    connector = aiohttp.TCPConnector(limit_per_host=max_connections)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [fetch(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        return responses
urls=["https://weather.com/weather/tenday/l/1c31b8d17f1edca64ebd5613a3687778e56a55a8f2a8355194cb92b043cbaba9",
          "https://weather.com/weather/tenday/l/9da454d4593cabaf7c79c1c7ea5793f5dfd5871abda4aa41108a3729d4f01bbc",
          "https://weather.com/weather/tenday/l/6f1fb241e273f7a89ecfb63affce79ad89d7f21533a86b0a25d3308497d740c7",
          "https://weather.com/weather/tenday/l/Beirut+Lebanon+LEXX0003",
          "https://weather.com/weather/tenday/l/705a547e74b988a5c58785c544330ffebb6057d681d0ad48d5311bb124a43fd5",
          "https://weather.com/weather/tenday/l/e9247f409825545784ff33963cb22a7ab8af198ea7614cf8f86a0fe26b134a1a",
          "https://weather.com/weather/tenday/l/7bda8dfca67cb6b67db19bd0ab50c2fc11ee887db37fbcb506378802ba4e1439",
          "https://weather.com/weather/tenday/l/f8c98fe3df5687a07c345db49cef0d71bd40551b1610e59db509ccc9cc1cbe93",
          "https://weather.com/weather/tenday/l/edeeab195618720ffcab57b14c6ea9f839c0cdb80746de959c96327ffcea075d",
          "https://www.citypopulation.de/en/lebanon/admin/"
    ]
weather_data = asyncio.run(main(urls, concurrent))
akkar_soup=""
baalbak_soup=""
beirut_soup=""
bqaa_soups=""
keserwan_soups=""
matn_soup=""
nabatieh_soup=""
tripoli_soup=""
sidon_soup=""
populations=""
#list containing all the part names
tempsoups=[akkar_soup,baalbak_soup,beirut_soup,bqaa_soups,keserwan_soups,matn_soup,nabatieh_soup,tripoli_soup,sidon_soup,populations]
names=["akaar","baalbak","beirut","bqaa","keserwan","matn",'nabatieh','tripoli','sidon']
#converting them to soups(using the lxml library so that i can access them easily)
for data in range(len(weather_data)):
    tempsoups[data]=BeautifulSoup(weather_data[data],'lxml')
#temp converter
def fahrenheit_to_celcius(x):
    return int((x-32)*(5/9))
#feels like temp
def heat_index(temp,humid):
    c1 = -42.379
    c2 = 2.04901523
    c3 = 10.14333127
    c4 = -0.22475541
    c5 = -6.83783e-03
    c6 = -5.481717e-02
    c7 = 1.22874e-03
    c8 = 8.5282e-04
    c9 = -1.99e-06
    x=(c1
    + (c2 * temp)
    + (c3 * humid)
    + (c4 * temp * humid)
    + (c5 * temp ** 2)
    + (c6 * humid ** 2)
    + (c7 * (temp ** 2) * humid)
    + (c8 * temp * (humid ** 2))
    + (c9 * (temp ** 2) *( humid ** 2)))
    return x
def populationextractor():
    population=tempsoups[-1].find_all('td', class_='rpop')
    listy=[]
    x=0
    for i in population:
        if x==4:
            x=0
        if x==0:
            listy.append([])
        listy[-1].append(i.text)
        x+=1
    akkarpop=listy[0][3]
    baalbakpop=listy[11][3]
    beirutpop=listy[14][3]
    bqaapop=listy[2][3]
    keserwanpop=listy[16][3]
    matnpop=listy[18][3]
    nabatiehpop=listy[6][3]
    tripolipop=listy[27][3]
    sidonpop=listy[23][3]
    pops=[akkarpop,baalbakpop,beirutpop,bqaapop,keserwanpop,matnpop,nabatiehpop,tripolipop,sidonpop]
    return pops
#this generates the list used in database
def itemstorer():
    x=populationextractor()
    b=open('base.txt','w')
    for i in range(len(tempsoups)-1):
        sub=[]
        sub.append(names[i])
        temp=tempsoups[i].find('span',class_="DailyContent--temp--1s3a7 DailyContent--tempN--33RmW").text
        sub.append(temp)
        sub.append(str(fahrenheit_to_celcius(int(temp[0:-1])))+"°")
        humid=tempsoups[i].find('span',class_="DetailsTable--value--2YD0-").text
        sub.append(humid)
        #precipitation
        sub.append(tempsoups[i].find('span',class_="DetailsTable--value--2YD0-").text)
        feellikeheat=int(heat_index(int(temp[0:-1]),int(humid[0:-1])/100))
        sub.append(feellikeheat)
        sub.append(int(x[i].replace(",","")))
        sub.append(fahrenheit_to_celcius(feellikeheat))
        
        b.write(str(sub)+"\n")
    b.close()
itemstorer()
