import pyodbc


ketnoi  = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server}; SERVER=DESKTOP-IBKS19D\SQLEXPRESS; Database=botchat; TrustServerCertificate=yes; UID=botchat; PWD=3568;')


curser = ketnoi.cursor()

curser.execute("insert userr values(N'text_2',N'text_2 mat khau')")
ketnoi.commit()

a =  curser.execute("select * from userr")
b = a.fetchall()


print(b)