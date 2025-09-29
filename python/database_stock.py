from bs4 import BeautifulSoup
from urllib import request

import sqlite3

con = sqlite3.connect("database_sample.db")
cur = con.cursor()

# 주식 시세 읽어와서 데이터베이스에 저장하기
# https://finance.naver.com/item/sise.naver?code=030530

# 이 주소에서 데이터 가져올거야

name = ["원익홀딩스", "삼성전자"]
site = ["030530","005930"]
stocks = list(zip(name,site))

url = "https://finance.naver.com/item/sise.naver?code={}"

for stock in stocks :
    sto_url = url.format(stock[1])

    print(sto_url)

    response1= request.urlopen(sto_url)
    html1 = response1.read()

    soup1 = BeautifulSoup(html1, "html.parser")
    info1 = soup1.select_one("#_nowVal")
    money1 = int(info1.text.replace(",",""))
    
 
    cur.execute("INSERT INTO stock VALUES('{}','{}')".format(stock[0],money1))


# cur.execute("CREATE TABLE stock(Stockname TEXT, price INT)")
# cur.execute("INSERT INTO stock VALUES ('원익홀딩스')")
# cur.execute("UPDATE stock SET price='{}' WHERE Stockname='원익홀딩스'".format(money))
# cur.execute("DELETE FROM stock WHERE price=84600")
con.commit()
con.close()


'''
# 알려준 주소에서 코드 좀 다 읽어와바
response = request.urlopen(url)
html = response.read()

# 가져온 코드의 구조를 분석해서 보유하자
soup = BeautifulSoup(html, "html.parser")

# 분석 결과 내에 내가 원하는 정보가 있다면 가져오자
info = soup.select_one("#_nowVal")
money = int(info.text.replace(",",""))


'''
# 미션
# 0. database_sample.db와 파이썬 파일을 연결하기
# 1. 주식이름과 가격을 저장할 수 있는 stock 테이블 생성하기 
# 2. 주식이름과 가격을 실제로 삽입하기
# 3. 삽입한 내용 확정하고 연결 해제 하기
# 4. 잘 되었는지 확인하기(데이터베이스 파일 열어보면 됨)
# 선택 사항. 어느정도 할 줄 알면 다른 종목도 여러개 넣기 
'''
import sqlite3

con = sqlite3.connect("database_sample.db")
cur = con.cursor()
# cur.execute("CREATE TABLE stock(Stockname TEXT, price INT)")
# cur.execute("INSERT INTO stock VALUES ('원익홀딩스')")
cur.execute("UPDATE stock SET price='{}' WHERE Stockname='원익홀딩스'".format(money))
con.commit()
con.close()'''