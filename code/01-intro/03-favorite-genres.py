dictionary = {
    'Horror': 0,
    'Romance': 0,
    'Comedy': 0,
    'History': 0,
    'Adventure': 0,
    'Action': 0,
}

num_of_input = int(input())

for i in range(num_of_input):
    a, b, c, d = list(input().split())
    # print(a, b, c, d)
    if b in dictionary:
        dictionary[b] += 1

    if c in dictionary:
        dictionary[c] += 1

    if d in dictionary:
        dictionary[d] += 1

our_list = [(k, v) for k, v in dictionary.items()]
our_list.sort(key = lambda y: (-y[1], y[0]))

for element in our_list:
    print(element[0] + " : " + str(element[1]))


#---------- input -------------
# 4
# hossein Horror Romance Comedy
# mohsen Horror Action Comedy
# mina Adventure Action History
# sajjad Romance History Action


#---------- output ------------
# Action : 3
# Comedy : 2
# History : 2
# Horror : 2
# Romance : 2
# Adventure : 1