import mysql.connector;

mydb=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Pavan@2003",
    database="pp"
)


mycursor=mydb.cursor()

# reading data
# mycursor.execute("show tables")
# for table in mycursor:
#     print(table)
# print("\n")

# creating table
# mycursor.execute("create table aa (name varchar(30),age int)")

# inserting into tables
# mycursor.execute("insert into aa values('pqr',20),('egf',30)")
# mydb.commit()

# sql="insert into gg (name,age) values (%s ,%s)"
# values=("ccc",22)
# mycursor.execute(sql,values)
# mydb.commit()

# mycursor.execute("select * from gg")
# for x in mycursor:
#     print(x)




