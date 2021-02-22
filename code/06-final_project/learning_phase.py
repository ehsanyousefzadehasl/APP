# This script reads from the training_data table and
# trains our model

from sklearn import tree
import mysql.connector

x = []
y = []
cnx = mysql.connector.connect(user='root', password='12345', host='127.0.0.1', database='car_price_prediction')
cursor = cnx.cursor(buffered=True)

cursor.execute('select * from training_data;')
for row in cursor:
    x.append(row[0:3] + row[4:14])
    y.append(row[3])


clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

# (brand, model, year, usage_miles, gear_box, body_condition, color,
#  province, motor_volume, num_of_cylinders, acceleration, fuel_usage)
new_data = [[6, 16, 1399, 450000, 2, 4, 4, 1, 2.8, 6, 20, 10]]
answer = clf.predict(new_data)

print(answer)
