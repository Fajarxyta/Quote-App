import requests, json
from bs4 import BeautifulSoup

url: str = "https://quotes.toscrape.com/"

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
            
            data_dict: dict = {
                "quote": quote,
                "author": author,
            }
            Data_list.append(data_dict)
        with open("quote.json", "w+") as f:
            json.dump(Data_list, f)

if __name__ == "__main__":
    quotes_app(url)