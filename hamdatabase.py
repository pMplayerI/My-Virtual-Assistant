import pyodbc

def themnguoidung(ten):
    ketnoi  = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=DESKTOP-Q4I6JM0; Database=botchat; TrustServerCertificate=yes; UID=ph; PWD=1234;')
    curser = ketnoi.cursor()
    c = curser.execute(f"select * from userr")
    d = c.fetchall()
    id = len(d)+1
    curser.execute(f"insert userr values({id},N'{ten}')")
    ketnoi.commit()
    print("commit database success")
    c = curser.execute(f"select * from userr")
    d = c.fetchall()
    return len(d)
def getdatabase(id):
    ketnoi  = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=DESKTOP-Q4I6JM0; Database=botchat; TrustServerCertificate=yes; UID=ph; PWD=1234;')
    curser = ketnoi.cursor()
    a =  curser.execute(f"select * from userr where id = {id}")
    b = a.fetchall()
    return b
def getcountdatabase():
    ketnoi  = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=DESKTOP-Q4I6JM0; Database=botchat; TrustServerCertificate=yes; UID=ph; PWD=1234;')
    curser = ketnoi.cursor()
    a =  curser.execute(f"select * from userr")
    b = a.fetchall()
    return len(b)