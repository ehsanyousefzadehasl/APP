import requests
from bs4 import BeautifulSoup
import re
import mysql.connector

cnx = mysql.connector.connect(user='root', password='12345',
                              host='127.0.0.1',
                              database='test2')
cursor = cnx.cursor()

result = requests.get('https://www.truecar.com/used-cars-for-sale/listings/')

soup = BeautifulSoup(result.text, 'html.parser')

res = soup.find_all(
    'div', attrs={'data-test': 'cardContent'})

regular_expr = r'rice">\$(.*?)<'
miler = r'vg>(\d+\,\d+)<!'
counter = 0
for e in res:
    # print(str(e))
    counter = counter + 1
    result = re.search(regular_expr, str(e))
    mile = re.search(miler, str(e))

    price = result.group(0)[7:len(result.group(0))-1]
    miles = mile.group(0)[3:len(mile.group(0))-2]
    price_p1, price_p2 = price.split(',')
    price = price_p1 + price_p2

    miles_p1, miles_p2 = miles.split(',')
    miles = miles_p1 + miles_p2
    print(counter, ': ', 'Price ', price, 'Miles: ',
          miles, 'Inseted into cars Table!')

    price = int(price)
    miles = int(miles)
    cursor.execute("insert into cars values('%i', '%i');" % (price, miles))
    if counter == 20:
        break


cnx.commit()
cnx.close()
