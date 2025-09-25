'''
from urllib import request
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/sise.naver?code=005930"
response = request.urlopen(url)
html = response.read()

soup = BeautifulSoup(html, "html.parser")

price = soup.select_one("#_nowVal") # #기호는 id를 의미
print(price.text)
'''

from urllib import request
from bs4 import BeautifulSoup

names = ["삼성전자","원익홀딩스","두산에너빌리티"]
codes = ["005930","030530","034020"]

stocks = list(zip(names,codes))

url = "https://finance.naver.com/item/sise.naver?code={}"

# newline -> 개행문자는 따로 처리하지 않겠다
# 특정 파일에 대한 csv 작성 객체를 만든다 -> csv.writer
file = open("stock.csv", "w", encoding="utf-8")
file.write("주식 종목, 가격\n")
for stock in stocks :
    stock_url = url.format(stock[1])

    response = request.urlopen(stock_url)
    html = response.read()

    soup = BeautifulSoup(html,"html.parser")
    data = soup.select_one("#_nowVal")
    price = data.text.replace(",","")

    print(stock[0],price)

    file.write("{} , {}원\n".format(stock[0], price))
file.close()