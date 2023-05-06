import pyodbc

def themnguoidung(ten,matkhau):
    
    ketnoi  = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server}; SERVER=DESKTOP-IBKS19D\SQLEXPRESS; Database=botchat; TrustServerCertificate=yes; UID=botchat; PWD=3568;')
    curser = ketnoi.cursor()
    curser.execute(f"insert userr values(N'{ten}',N'{matkhau}')")
    ketnoi.commit()
    print("comit database success")
def getdatabase(id):
    id = str(id)
    ketnoi  = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server}; SERVER=DESKTOP-IBKS19D\SQLEXPRESS; Database=botchat; TrustServerCertificate=yes; UID=botchat; PWD=3568;')
    curser = ketnoi.cursor()
    a =  curser.execute(f"select * from userr where ten = N'{id}'")
    b = a.fetchall()
    return b