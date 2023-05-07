import pyodbc

def themnguoidung(ten):
    ketnoi  = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server}; SERVER=DESKTOP-IBKS19D\SQLEXPRESS; Database=botchat; TrustServerCertificate=yes; UID=botchat; PWD=3568;')
    curser = ketnoi.cursor()
    c = curser.execute(f"select * from userr")
    d = c.fetchall()
    id = len(d)+1
    curser.execute(f"insert userr values({id},N'{ten}')")
    ketnoi.commit()
    print("comit database success")
    c = curser.execute(f"select * from userr")
    d = c.fetchall()
    return len(d)
def getdatabase(id):
    ketnoi  = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server}; SERVER=DESKTOP-IBKS19D\SQLEXPRESS; Database=botchat; TrustServerCertificate=yes; UID=botchat; PWD=3568;')
    curser = ketnoi.cursor()
    a =  curser.execute(f"select * from userr where id = {id}")
    b = a.fetchall()
    return b
def getcountdatabase():
    ketnoi  = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server}; SERVER=DESKTOP-IBKS19D\SQLEXPRESS; Database=botchat; TrustServerCertificate=yes; UID=botchat; PWD=3568;')
    curser = ketnoi.cursor()
    a =  curser.execute(f"select * from userr")
    b = a.fetchall()
    return len(b)