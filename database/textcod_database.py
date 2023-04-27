import pyodbc


ketnoi  = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server}; SERVER=DESKTOP-IBKS19D\SQLEXPRESS; Database=botchat; TrustServerCertificate=yes; UID=botchat; PWD=3568;')


curser = ketnoi.cursor()

for i in curser.execute("select * from userr"):
    print(i.ten)
    print(i.tuoi)