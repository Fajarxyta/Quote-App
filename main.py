import requests, json, os
from bs4 import BeautifulSoup

url: str = "https://quotes.toscrape.com"

headers: dict = {
    "User-Agent": "Mozilla/5.0 (X11; Linux aarch64; rv:109.0) Gecko/20100101 Firefox/115.0"
}

def quotes_app(url: str):
    req = requests.get(url, headers = headers)
    if req.status_code == 200:
        soup: BeautifulSoup = BeautifulSoup(req.text, "html.parser")
        contents = soup.find_all("div", attrs={"class": "quote"})
        Data_list: list = []
        for content in contents:
            quote = content.find("span", attrs={"class": "text"}).text.strip()
            author = content.find("small", attrs={"class": "author"}).text.strip()
            link = content.find("a")["href"]
        data_dict: dict = {
            "quote": quote,
            "author": author,
            "author_link": url + link,
        }
        Data_list.append(data_dict)
        with open("quote.json", "w+") as f:
            json.dump(Data_list, f)
        
    return data_dict

def get_detils(detils_url: str):
    req = requests.get(detils_url, headers=headers)
    if req.status_code == 200:

        soup: BeautifulSoup = BeautifulSoup(req.text,'html.parser')
        
        author_title = soup.find('h3', attrs={'class':'author-title'}).text.strip()
        born_date = soup.find('span', attrs={'class': 'author-born-date'}).text.strip()
        born_locale = soup.find('span', attrs={'class': 'author-born-location'}).text.strip()
        description = soup.find('div', attrs={'class':'author-description'}).text.strip()

        data_dict: dict = {
            'author': author_title,
            'born': f'{born_date} {born_locale}',
            'description': description,
        }
        print(data_dict)
        return data_dict
    


if __name__ == "__main__":
    os.system('clear')
    get_detils(detils_url="https://quotes.toscrape.com/author/Albert-Einstein")
    # quotes_app(url)