import mysql.connector

print("connecting to db")
cnx = mysql.connector.connect(user='root', password='12345',
                              host='127.0.0.1',
                              database='test2')
print("connected to db")


cursor = cnx.cursor()

cursor.execute("select * from people order by height desc, weight asc")

for element in cursor:
    print(element)


cnx.close()
