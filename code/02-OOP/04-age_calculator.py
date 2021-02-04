import datetime
birth_date = input()
temp = list(birth_date.split('/'))

flag = 0
if len(temp) != 3 or len(temp[0]) != 4 or len(temp[1]) != 2 or len(temp[2]) != 2:
    print('WRONG')
    flag = 1

if int(temp[1]) > 12 or int(temp[1]) < 1 or int(temp[2]) > 31 or int(temp[2]) < 1:
    print('WRONG')
    flag = 1

if flag == 0:
    now = str(datetime.date.today())
    current_year = int(now[0:4])
    print(current_year - int(temp[0]))
    # print(current_year)
    # print(now)