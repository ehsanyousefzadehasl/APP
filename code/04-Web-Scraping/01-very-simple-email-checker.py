import re

regular_expr = r'[\w\d]+@\w+\.\w{2}'

in_str = input()

result = re.search(regular_expr, in_str)

if result == None:
    print("WRONG")
else:
    print("OK")
