# Mysql 같은것, 파이썬 기본 내장
import sqlite3 

# 전제 : 이 파이썬 파일과 같은 폴더 내에 *.db 파일이 하나 존재한다
# 이 파이썬 파일과 데이터베이스 파일 연결 작업가능하게 만듬
con = sqlite3.connect("database_sample.db")
# 연결이 되었다면, 연결된 파일에 sql 구문을 전달해서 실행할 객체를 생성해야함
cur = con.cursor()
# 테이블 생성 명령 실행
#cur.execute("CREATE TABLE customer(name TEXT,age INT)")
# 명령 실행완료했으니, 확정시키고 연결 해제
# 위에서 만든 테이블에 데이터 두개 삽입후, 한개 삭제해보기
cur.execute("INSERT INTO customer VALUES ('LEE', 18)")
cur.execute("INSERT INTO customer VALUES ('KIM', 19)")
cur.execute("DELETE FROM customer WHERE name='LEE'") 
con.commit() # 작업확정
con.close() # 연결 해제