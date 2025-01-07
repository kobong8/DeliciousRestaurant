from bs4 import BeautifulSoup
import requests

# regex 01(example) : [?|&](\w+)=([^\w+])
# regex 02(replace) : (\w+)=([^\w+])
# regex 03-1 : (\w+)=(\w+)&?
# regex 03-2 : "$1": "$2", \n

# url = "https://www.coupang.com/np/campaigns/82/components/317679?"
#
# params = {
#     "listSize": "60",
#     "isPriceRange": "false",
#     "channel": "user",
#     "fromComponent": "Y",
#     "sorter": "bestAsc",
#     "component": "317679",
#     "rating": "0"
# }
url = "https://category.gmarket.co.kr/listview/L100000002.aspx"

# web termial : navigator.userAgent
headers = {
    "user-agent": "'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'"
}

## Error
# 200 OK
# 401 Unauthorized
# 403 Forbidden
# 404 Not Found
# 418 I’m a teapot

# response = requests.get(url, params=params, headers=headers)
response = requests.get(url, headers=headers)
print(f"response status code: {response.status_code}")
soup = BeautifulSoup(response.text, "html.parser")
list_box = soup.find("div", class_="best-list")
# print(list_box)
item_box = list_box.find_all("li")
print(item_box)
# for item in item_box:
#     item_link = item.find("a").get("href")
#     print(item_link)