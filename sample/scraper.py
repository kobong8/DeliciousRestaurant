from bs4 import BeautifulSoup
import requests
from typing import List
import re

class Scraper:
    def __init__(self):
        self.__url = "https://category.gmarket.co.kr/listview/L100000002.aspx"
        self.__headers = {
            "user-agent": "'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'"
        }

    def do(self):
        response = requests.get(self.__url, headers=self.__headers)
        print(f"response status code: {response.status_code}")

        soup = BeautifulSoup(response.text, "html.parser")
        list_box = soup.find("div", class_="plus-goods")
        item_boxes = list_box.find_all("li")

        result: List = []
        for item_box in item_boxes:
            # item 이름
            item_title = item_box.find("div", class_="img").findChild("a").find("img")["alt"]

            # item 링크
            item_link = item_box.find("div", class_="img").findChild("a").attrs["href"]
            pattern = r"https?://[^\s,']+"
            item_link = re.findall(pattern, item_link)[0]

            # item 가격
            item_price = item_box.find("div", class_="price").text

            # item 이미지
            item_img = item_box.find("div", class_="img").findChild("a").find("img")["src"]

            item = {
                "name": item_title,
                "url": item_link,
                "price": item_price,
                "image": item_img
            }

            result.append(item)

        return result

if __name__ == "__main__":
    scraper = Scraper()
    items = scraper.do()
    print(items)