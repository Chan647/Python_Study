import pymysql

DB_CONFIG = dict(
    host ="localhost",
    user ="root",
    password="qwe!@#456",
    database="NewManage",
    charset="utf8"
)

class DB :
    def __init__(self,**config) :
        self.config = config

    def connect(self) :
        return pymysql.connect(**self.config) 
    
    def fetch_shoes(self) :
        sql = "SELECT * FROM Shoes "    
        with self.connect() as con :
            with con.cursor() as cur :
                cur.execute(sql)
                return cur.fetchall()
            
    def fetch_id(self) :
        sql = "SELECT ID FROM Shoes "    
        with self.connect() as con :
            with con.cursor() as cur :
                cur.execute(sql)
                return cur.fetchall()
            
    def update_price_shoes(self, id, price) :
        sql = "UPDATE Shoes SET price=%s WHERE ID=%s"
        try :
            with self.connect() as con :
                with con.cursor() as cur :
                    cur.execute(sql,(price, id))
                con.commit()
                return True

        except Exception as e :
            print(e)
            return False
        
    def update_inven_shoes(self, id, inven) :
        sql = "UPDATE Shoes SET inventory=%s WHERE ID=%s"
        try :
            with self.connect() as con :
                with con.cursor() as cur :
                    cur.execute(sql,(inven, id))
                con.commit()
                return True

        except Exception as e :
            print(e)
            return False

    
    def insert_shoes(self, type, sname, price, inven) :
        sql = "INSERT INTO Shoes(type,shoename,price,inventory) VALUES(%s, %s, %s, %s)"

        try :
            with self.connect() as con :
                with con.cursor() as cur :
                    cur.execute(sql,(type,sname,price,inven))
                con.commit()
                return True

        except Exception as e :
            print(e)
            con.rollback()
            return False
        
    def delete_shoes(self, id) :
        sql = "DELETE FROM Shoes WHERE ID=%s"

        try :
            with self.connect() as con :
                with con.cursor() as cur :
                    cur.execute(sql,(id,))
                con.commit()
                return True

        except Exception as e :
            print(e)
            con.rollback()
            return False
        
    def verify_user(self, username, password):
        sql = "SELECT COUNT(*) FROM users WHERE username=%s AND password=%s"
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql,(username,password))
                count, = cur.fetchone()
                return count == 1
            
    def insert_user(self, usname, psword) :
        sql = "INSERT INTO users(username,password) VALUES(%s, %s)"
        try :
            with self.connect() as con :
                with con.cursor() as cur :
                    cur.execute(sql,(usname,psword))
                con.commit()
                return True
            
        except Exception :
            con.rollback()
            return False
                
                
