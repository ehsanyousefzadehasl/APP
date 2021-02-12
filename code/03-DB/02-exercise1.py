import mysql.connector

# print("connecting to db")
cnx = mysql.connector.connect(user='root', password='12345',
                              host='127.0.0.1',
                              database='test2')
# print("connected to db")


cursor = cnx.cursor()

cursor.execute("select * from people order by height desc, weight asc")

for (name, height, weight) in cursor:
    print(name, height, weight)


cnx.close()

# ('Mahdi', 90, 190)
# ('Amin', 75, 180)
# ('Ahmad', 60, 175)
# ('Mohammad', 75, 175)
