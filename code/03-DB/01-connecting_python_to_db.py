import mysql.connector

print("connecting to db")
cnx = mysql.connector.connect(user='root', password='#',
                              host='127.0.0.1',
                              database='test')
print("connected to db")


cursor = cnx.cursor()
cursor.execute("INSERT INTO pet values('cat', 'Akbar','mammal', 'f', '1994-07-12', '2009-12-12');")

cursor.execute("select * from pet;")

for element in cursor:
    print(element)


cnx.close()