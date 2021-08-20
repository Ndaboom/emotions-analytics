from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

query = input("Enter the subject:")
clean_query = query.replace(" ", "%20")


root = "https://www.google.com/"
link = "https://www.google.com/search?q="+clean_query+"&sxsrf=ALeKk03t0Sm61H3hL9VtJTnWmEU24Q8MIw:1629324178016&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjlwOrGybvyAhVFxIUKHd9nBU8Q_AUoAXoECAIQAw&biw=1366&bih=612"

req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

def fetch_data(link):
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
   
    with requests.Session() as c:
        soup = BeautifulSoup(webpage, 'html5lib')
        for item in soup.find_all('div', attrs={'class': 'ZINbbc xpd O9g5cc uUPGi'}):
            raw_link = (item.find('a', href=True)['href'])
            link = (raw_link.split("/url?q=")[1]).split('&sa=U&')[0]
            
            
            title = (item.find('div', attrs={'class': 'BNeawe vvjwJb AP7Wnd'}).get_text())
            print(title)
            print(link)
            description = (item.find('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'}).get_text())
            title = title.replace(",", "")
            description = description.replace(",", "")

            time = description.split(" · ")[0]
            details = description.split(" · ")[1]

            with open('data.txt', 'a') as f:
                f.write("{}, {}, {}, {}  \n".format(title, time, details, link))
        
        next = soup.find('a', attrs={'aria-label':'Next page'})
        next = (next['href'])
        link = root + next
        fetch_data(link)

fetch_data(link)

