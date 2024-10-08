import requests, json, os, csv
from bs4 import BeautifulSoup

class Main:
    def __init__(self):
        self.url: str = "https://quotes.toscrape.com"
        self.headers: dict = {
            "User-Agent": "Mozilla/5.0 (X11; Linux aarch64; rv:109.0) Gecko/20100101 Firefox/115.0"
        }
    def quotes_app(self, url: str):
        req = requests.get(url, headers=self.headers)
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
                    "author_link": url + str(link)
                }
                Data_list.append(data_dict)
            return Data_list

    def get_details(self, details_url: str):
        req = requests.get(details_url, headers=self.headers)
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
            return data_dict
    
    def main(self):
        try:
            results: list[dict[str, str]] = []
            data = self.quotes_app(url=self.url)
            for detail in data:
                link = detail['author_link']
                details = self.get_details(details_url=str(link))
                final_result: dict[str, str] = {**detail, **details}
                results.append(final_result)
            with open('data_list.csv', mode='w+', newline='') as file:
                writer = csv.writer(file)
                if results:
                    header = results[0].keys()
                    writer.writerow(header)
                for row in results:
                    writer.writerow(row.values())
            print("Data berhasil disimpan ke data_list.csv")
        except (Exception) as e:
            print(e)
    
if __name__ == "__main__":
    os.system('clear')
    Main().main()