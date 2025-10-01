import pymysql

DB_CONFIG = dict(
    host ="localhost",
    user ="root",
    password="qwe!@#456",
    database="manage",
    charset="utf8"
)

class DB :
    def __init__(self,**config):
        self.config = config

    def connect(self):
        return pymysql.connect(**self.config)
    
    def fetch_sup(self) :
        sql = "SELECT type, shoename, price, inventory FROM Shoes ORDER BY type"
        with self.connect() as con :
            with con.cursor() as cur :
                cur.execute(sql)
                return cur.fetchall()
    
    def insert_sup(self, type, name, money, num) :
        sql = "INSERT INTO Shoes VALUES(%s, %s, %s, %s)"
        try :
            with self.connect() as con :
                with con.cursor() as cur :
                    cur.execute(sql,(type,name,money,num))
                con.commit()
                return True
            
        except Exception :
            con.rollback()
            return False
        
    def resume_inv(self, inventory, type) :
        sql = "UPDATE Shoes SET inventory=%s WHERE type=%s"
        try : 
            with self.connect() as con :
                with con.cursor() as cur :
                    cur.execute(sql,(inventory,type))
                con.commit()
                return True
        
        except Exception :
            con.rollback()
            return False
    
    def verify_user(self, username, password):
        sql = "SELECT COUNT(*) FROM users WHERE username=%s AND password=%s"
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql,(username,password))
                count, = cur.fetchone()
                return count == 1
            
    def delete_sup(self,type):
        sql = "DELETE FROM Shoes where type=%s"
        try :
            with self.connect() as con :
                with con.cursor() as cur :
                    cur.execute(sql,(type))
                con.commit()
                return True
            
        except Exception :
            con.rollback()
            return False
