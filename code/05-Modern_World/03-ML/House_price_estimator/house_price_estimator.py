import csv
from sklearn import tree

x = []
y = []
# bedrooms	bathrooms	sqft_living	sqft_lot	floors	view	condition	sqft_above	sqft_basement	yr_built	yr_renovated	price
with open('data.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    for line in data:
        x.append(line[0:11])
        y.append(line[11])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

new_data = [[10, 5, 150000, 10000, 4, 5, 5, 2500, 1000, 3500, 0]]
answer = clf.predict(new_data)

print(answer)
