import mysql.connector


def email_validation(email):
    try:
        str1, str2 = email.split('@')
    except ValueError:
        return False

    if len(str1) < 1 or len(str2) < 4:
        return False

    # email addresses can contain letters, numbers, underscores,periods and dashes
    # an underscore, period, or dash must be followed by at least a letter or digit
    for iterator in range(len(str1)):
        if str1[iterator].isalpha() or str1[iterator].isdigit():
            continue
        elif ((str1[iterator] == '-' or str1[iterator] == '_' or str1[iterator] == '.') and iterator != len(str1) - 1) and ((str1[iterator - 1] != '-' or str1[iterator - 1] != '_' or str1[iterator - 1] != '.')):
            continue
        else:
            return False

    for itr in range(len(str2)):
        if str2[itr].isalpha() or str2[itr].isdigit():
            continue
        elif (str2[itr] == '.' or str2[itr] == '-') and (str2[itr - 1] != '.' or str2[itr - 1] != '-'):
            continue
        else:
            return False

    try:
        splited_values = str2.split('.')
    except ValueError:
        return False

    if len(splited_values) < 2:
        return False

    if len(splited_values[len(splited_values) - 1]) < 2:
        return False

    for element in splited_values:
        if len(element) < 1:
            return False

    return True


def password_validation(password):
    flag_l = False
    flag_n = False

    for i in password:
        if i.isalpha():
            flag_l = True

        if i.isdigit():
            flag_n = True

    return flag_l and flag_n


email = input("Enter Your Email Address: ")

while email_validation(email) != True:
    email = input(
        "Please Enter a Valid Email Address like john.doe@gmail.com: ")

password = input(
    "Enter Your Password (It must contain digits and letters): ")

while password_validation(password) != True:
    password = input(
        "Please Enter a valid password address containing digits and letters: ")

# print("connecting to db")
cnx = mysql.connector.connect(user='root', password='12345',
                              host='127.0.0.1',
                              database='test2')
# print("connected to db")


cursor = cnx.cursor()

cursor.execute("insert into info values('%s', '%s');" % (email, password))
cnx.commit()

cnx.close()
