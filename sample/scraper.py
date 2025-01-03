from bs4 import BeautifulSoup
import requests

# regex 01 : [?|&](\w+)=([^\w+])
# regex 02 : (\w+)=([^\w+])
# ori_url = "https://shop.29cm.co.kr/category/list?categoryLargeCode=273100100&categoryMediumCode=273101100&sort=RECOMMEND&defaultSort=RECOMMEND&sortOrder=DESC&page=1&brands=&categorySmallCode=&minPrice=50000&maxPrice=100000&isFreeShipping=true&excludeSoldOut=&isDiscount=&colors=%2321ba21%2C%233585c2&tag=&extraFacets=&attributes=%5B%5D"
url = "https://shop.29cm.co.kr/category/list?"

# regex 03 : (\w+)=(\w+)&?
# regex 04 : "$1": "$2", \n
params = {
    "categoryLargeCode": "273100100",
    "categoryMediumCode": "273101100",
    "sort": "RECOMMEND",
    "defaultSort": "RECOMMEND",
    "sortOrder": "DESC",
    "page": "1",
    "minPrice": "50000",
    "maxPrice": "100000",
    "isFreeShipping": "true",
}

## 418
# url = "https://search.shopping.naver.com/search/all?"
#
# params = {
#     "brand": "147285",
#     "frm": "NVSCDIG",
#     "maxPrice": "1200000",
#     "minPrice": "480000",
#     "pagingIndex": "1",
#     "pagingSize": "40",
#     "productSet": "total",
#     "sort": "rel",
#     "spec": "M10011192",
#     "viewType": "list",
# }

# web termial : navigator.userAgent
headers = {
    "None"
}

## Error
# 403 Forbidden
# 404 Not Found
# 418 I’m a teapot

response = requests.get(url, params=params, headers=headers)
# print(response.status_code)
soup = BeautifulSoup(response.text, "html.parser")
test_find = soup.find("div", class_="pr-60")
print(test_find)
