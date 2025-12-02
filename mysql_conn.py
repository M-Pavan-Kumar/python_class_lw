import mysql.connector;

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pavan@2003",
    database="pp"
)
# print(db)

cursorr=db.cursor()
cursorr.execute("select * from ss")
res=cursorr.fetchone()

for x in res:
    print(x)
