num = int(input())
info_list = []
for i in range(num):
    info_list.append(input().split("."))

for element in info_list:
    element[1] = element[1].capitalize()

list_of_tuples = []
for element in info_list:
    list_of_tuples.append((element[0], element[1], element[2]))

list_of_tuples.sort(key = lambda x: (x[0], x[1]))

# print(list_of_tuples)

for element in list_of_tuples:
    print(element[0], element[1], element[2])


# ------- input ---------
# 4
# m.hosSein.python
# f.miNa.C
# m.aHMad.C++
# f.Sara.java


# -------- output ----------
# f Mina C
# f Sara java
# m Ahmad C++
# m Hossein python