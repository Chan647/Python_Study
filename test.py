
numbers = [1, 2, 3, 4, 5, 6]

total = ""
for number in numbers :
    total += str(number)

print(total)
print("::".join(total))


from urllib import request
from bs4 import BeautifulSoup

names = ["삼성전자","원익홀딩스","두산에너빌리티"]
codes = ["005930","030530","034020"]

stocks = list(zip(names,codes))

url = "https://finance.naver.com/item/sise.naver?code={}"

for stock in stocks :
    stock_url = url.format(stock[1])

    response = request.urlopen(stock_url)
    html = response.read()

    soup = BeautifulSoup(html,"html.parser")
    data = soup.select_one("#_rate")
    data2 = soup.select_one("#_nowVal")
    percent = data.text
    price = data2.text.replace(",","")
    print(stock[0],price, percent)


import csv

csv_file = open("sample.csv", "w", encoding="utf-8", newline="")
writer = csv.writer()
writer.writerow(["~~","~~"])

csv_file.close()

