import pymysql

try : 
    con = pymysql.connect(
        host= "localhost",
        user= "root",
        password= "qwe!@#456",
        database= "example",
        charset= "utf8" 
    )

    cur = con.cursor()
    sql = "UPDATE users SET email=%s WHERE id='12'"
    cur.execute(sql, "hong@gmail.com")
    con.commit()

except Exception as e :
    print("에러가 발생하였습니다.", e)
    con.rollback()

cur.close()
con.close()