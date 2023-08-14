import csv
from sklearn import tree

x = []
y = []

with open('laptops.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    for line in data:
        x.append(line[0:3])
        y.append(line[3])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

new_data = [[15, 8, 2], [13, 8, 1]]
answer = clf.predict(new_data)

print(answer)