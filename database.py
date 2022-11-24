import mysql.connector 

conn, cur = None, None

def connect():
    global conn, cur
    conn = mysql.connector.connect(user="root", host="localhost", database="garmentshop", password="123456")
    cur = conn.cursor()

def readAllRecords():
    global cur
    cur.execute("select * from stock")  # type: ignore
    recs = cur.fetchall() # type: ignore
    return recs

def readOneRecord(id):
    global cur
    cur.execute("select * from stock where pid=%s"%(id, ))  # type: ignore
    recs = cur.fetchone() # type: ignore
    return recs

def insertProduct(id, name, company, price, stock_remaining):
    global cur, conn
    cur.execute("insert into stock values (%s, '%s', '%s', %s, %s)"%(id, name, company, price, stock_remaining)) #type: ignore
    conn.commit() #type: ignore

def deleteProduct(id):
    global cur
    cur.execute("delete from stock where pid=%s"%(id, )) #type: ignore
    conn.commit()

def searchProduct(id):
    global cur
    cur.execute("select * from stock where pid=%s"%(id, ))  # type: ignore
    rec = cur.fetchone() # type: ignore
    return rec

def updateRecord(id, name, company, price, stock):
    global cur
    cur.execute("update stock set pname='%s', company='%s', price=%s, stockremaining=%s where pid=%s"%(name, company, price, stock, id)) #type: ignore

connect()
# print(readAllRecords())
# insertProduct(2, "Woolen Jacket", "Gucci", 3500, 3)