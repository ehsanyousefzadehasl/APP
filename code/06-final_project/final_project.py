import requests
from bs4 import BeautifulSoup
import re
import mysql.connector

def number_comma_cleaner(number):
    temp_list = number.split(',')
    # print(temp_list)
    tmp = ""
    for i in temp_list:
        tmp = tmp + i
    # print(tmp)
    return int(tmp)



number_of_pages_to_scrape = 2
main_url = "https://bama.ir/car/all-brands/all-models/all-trims?page="

# This loop for reading from the pages
# Then, extracting link of each post 
for i in range(100, 99 + number_of_pages_to_scrape + 1):
    result = requests.get(main_url + str(i))

    # print("$$$$$$$$$$$$$$$$$$$$$$ ------------------page_number: ", i)
    # print(result.text)

    page_soup = BeautifulSoup(result.text, 'html.parser')

    # print(soup)

    res_links = page_soup.find_all('a', attrs={'class': 'cartitle-desktop'})
    # This regular expression is for extracting links from which we are going to get our real data
    post_link_regular_expr = r'href="(.*?)"'

    for e in res_links:
        result_links = re.search(post_link_regular_expr, str(e))
        print(result_links.group(0))
        # print("===========")
        # Now, we have link to every post, so we can extract data from each of them
        # In each post, we have to check whether it has a price or not
        # If a post does not have price, it is useless for our model

        post_url = str(result_links.group(0))
        # print(post_url[6:len(post_url) - 1])

        # Then, we go to scrape data from each post
        post_url_to_req = post_url[6:len(post_url)-1]
        post = requests.get(post_url_to_req)
        post_soup = BeautifulSoup(post.text, 'html.parser')

        # brand, model, year, price, usage, gearbox, fuel, body_condition, color, province, motor_volume, 
        # number_of_cylinder, acceleration, fuel_usage


        # First of all, checking the price, if not price, we will continue
        # with the next post
        post_price_check_regex = r'<p>\s*<span\sclass="label">قیمت\s*<\/span>\s*<span\scontent=".*>\sتومان'
        post_price_check_result = re.search(
            post_price_check_regex, str(post_soup))

        if post_price_check_result == None:
            # print("No Price tag")
            # So, we will skip it
            continue
        else:
            # print("it seems that this post has a price tag")
            # So, first of all, we extract and clean the price
            exact_price_regex = r'<span class="label">قیمت\s*<\/span>\s*<span\scontent="(.*?)"'
            post_price_exact_result = re.search(
                exact_price_regex, str(post_soup))

            # We learned here how to use group(1) to get the specified group
            # In the previous examples, we used group(0) which made our efforts useless
            price_to_be_cleaned = post_price_exact_result.group(1)
            cleaned_price = number_comma_cleaner(price_to_be_cleaned)
            # Now, we have the price, we have to extract other information


            # brand, model, year
            brand_model_year_regex = r'<h1.*>\s*<span>(.*?)<\/span>\s<span>(.*?)<\/span><span>‏<\/span>\s.*<span>.*?<\/span>\s<span\sdatetime="(.*)">'
            post_brand_model_year_exact_result = re.search(
                brand_model_year_regex, str(post_soup))
            
            if post_brand_model_year_exact_result != None:
                brand, model, year = post_brand_model_year_exact_result.group(1), post_brand_model_year_exact_result.group(2), post_brand_model_year_exact_result.group(3)
            else:
                continue
            
            # Using a brand's number or storing then retrieving the model's assigned number
            cnx = mysql.connector.connect(user='root', password='12345',
                                        host='127.0.0.1',
                                        database='car_price_prediction')
            print("connected to model table")
            cursor = cnx.cursor(buffered=True)
            cursor.execute('select id from model where model_name LIKE "%' + model + '%";')

            # now, if it is none, we will detect and write, then read and use its id
            result = cursor.fetchone()

            if result != None:
                model_integered = result[0]
            # print(model_integered) # so we could find it
            else:
                # insert
                cursor.execute('insert into model (model_name) values("%s")'% model)

                cursor.execute('select id from model where model_name LIKE "%' + model + '%";')

                result = cursor.fetchone()

                model_integered = result[0]
                # print(model_integered)
                cnx.commit()

            cursor.execute('select id from brand where brand_name LIKE "%' + brand + '%";')

            # now, if it is none, we will detect and write, then read and use its id
            result = cursor.fetchone()

            if result != None:
                brand_integered = result[0]
            # print(model_integered) # so we could find it
            else:
                # insert
                cursor.execute(
                    'insert into brand (brand_name) values("%s")' % brand)

                cursor.execute(
                    'select id from brand where brand_name LIKE "%' + brand + '%";')

                result = cursor.fetchone()

                brand_integered = result[0]
                # print(model_integered)
                cnx.commit()





            post_usage_regex = r'<p>\s*<span\sclass="label">كاركرد\s*<\/span>\s*<span>\s*(.*)\sکیلومتر\s*<\/span>\s*<\/p>'
            post_usage_exact_result = re.search(
                post_usage_regex, str(post_soup))
            
            if post_usage_exact_result != None:
                usage = post_usage_exact_result.group(1)
                cleaned_usage = number_comma_cleaner(usage)
            else:
                continue

            # gear_box
            gear_box_regex = r'<p>\s*<span\s*class="label">گیربکس\s*<\/span>\s*<span>\s*(.*)\s*<\/span>\s*<\/p>'
            post_gear_box_result = re.search(gear_box_regex, str(post_soup))

            if post_gear_box_result != None:
                gear_box = post_gear_box_result.group(1)
            else:
                continue

            cursor.execute(
                'select id from gear_box where gear_box LIKE "%' + gear_box + '%";')

            # now, if it is none, we will detect and write, then read and use its id
            result = cursor.fetchone()

            if result != None:
                gear_box_integered = result[0]
            # print(model_integered) # so we could find it
            else:
                # insert
                cursor.execute(
                    'insert into gear_box (gear_box) values("%s")' % gear_box)

                cursor.execute(
                    'select id from gear_box where gear_box LIKE "%' + gear_box + '%";')

                result = cursor.fetchone()

                gear_box_integered = result[0]
                # print(model_integered)
                cnx.commit()

            # fuel
            fuel_regex = r'<p>\s*<span\s*class="label">سوخت\s*<\/span>\s*<span>\s*(.*)\s*<\/span>\s*<\/p>'
            post_fuel_result = re.search(fuel_regex, str(post_soup))

            if post_fuel_result != None:
                fuel = post_fuel_result.group(1)
            else:
                continue

            # body_condition
            body_condition_regex = r'<p>\s*<span\s*class="label">بدنه\s*<\/span>\s*<span>\s*(.*)\s*<\/span>\s*<\/p>'
            post_body_condition_result = re.search(body_condition_regex, str(post_soup))

            if post_body_condition_result != None:
                body_condition = post_body_condition_result.group(1)
            else:
                continue

            cursor.execute(
                'select id from body_condition where body_condition LIKE "%' + body_condition + '%";')

            # now, if it is none, we will detect and write, then read and use its id
            result = cursor.fetchone()

            if result != None:
                body_condition_integered = result[0]
            # print(model_integered) # so we could find it
            else:
                # insert
                cursor.execute(
                    'insert into body_condition (body_condition) values("%s")' % body_condition)

                cursor.execute(
                    'select id from body_condition where body_condition LIKE "%' + body_condition + '%";')

                result = cursor.fetchone()

                body_condition_integered = result[0]
                # print(model_integered)
                cnx.commit()
            # color
            color_regex = r'<p>\s*<span\s*class="label">رنگ\s*<\/span>\s*<span>\s*<f>(.*?)<\/f>'
            post_color_result = re.search(color_regex, str(post_soup))

            if post_color_result != None:
                color = post_color_result.group(1)
            else:
                continue

            cursor.execute('select id from color where color LIKE "%' + color + '%";')

            # now, if it is none, we will detect and write, then read and use its id
            result = cursor.fetchone()

            if result != None:
                color_integered = result[0]
            # print(model_integered) # so we could find it
            else:
                # insert
                cursor.execute(
                    'insert into color (color) values("%s")' % color)

                cursor.execute(
                    'select id from color where color LIKE "%' + color + '%";')

                result = cursor.fetchone()

                color_integered = result[0]
                # print(model_integered)
                cnx.commit()

            # province
            province_regex = r'<p>\s*<span\s*class="label">استان\s*<\/span>\s*<span>\s*(.*)\s*<\/span>\s*<\/p>'
            post_province_result = re.search(province_regex, str(post_soup))

            if post_province_result != None:
                province = post_province_result.group(1)
            else:
                continue

            cursor.execute(
                'select id from province where province LIKE "%' + province + '%";')

            # now, if it is none, we will detect and write, then read and use its id
            result = cursor.fetchone()

            if result != None:
                province_integered = result[0]
            # print(model_integered) # so we could find it
            else:
                # insert
                cursor.execute(
                    'insert into province (province) values("%s")' % province)

                cursor.execute(
                    'select id from province where province LIKE "%' + province + '%";')

                result = cursor.fetchone()

                province_integered = result[0]
                # print(model_integered)
                cnx.commit()

            # motor_volume
            motor_volume_regex = r'<li class="ad-detail-spec-11">\s*<span\s*class="dark-text">حجم موتور<\/span>\s*<span>(.*)لیتر<\/span>\s*<\/li>'
            post_motor_volume_result = re.search(motor_volume_regex, str(post_soup))

            if post_motor_volume_result != None:
                motor_volume = post_motor_volume_result.group(1)
            else:
                continue


            # number_of_cylinder
            num_of_cylinder_regex = r'<li class="ad-detail-spec-10">\s*<span\s*class="dark-text">پیشرانه<\/span>\s*<span>(.*)\sسیلندر.*<\/span>\s*<\/li>'
            post_num_of_cylinders = re.search(num_of_cylinder_regex, str(post_soup))

            if post_num_of_cylinders != None:
                number_of_cylinders = post_num_of_cylinders.group(1)
            else:
                continue

            # acceleration
            acceleration_regex = r'<li class="ad-detail-spec-14">\s*<span class="dark-text">شتاب<\/span>\s*<span>(.*)ثانیه<.span>\s*<\/li>'
            post_acceleration = re.search(acceleration_regex, str(post_soup))

            if post_acceleration != None:
                acceleration = post_acceleration.group(1)
            else:
                continue

            # fuel_usage
            fuel_usage_regex = r'<li class="ad-detail-spec-16">\s*<span class="dark-text">مصرف ترکیبی<\/span>\s*<span>(.*)\sلیتر'
            post_fuel_usage_result = re.search(fuel_usage_regex, str(post_soup))

            if post_fuel_usage_result != None:
                fuel_usage = post_fuel_usage_result.group(1)
                # print(fuel_usage)
            else:
                continue

        # Then, each of the above mentioned will go into our database

            # print("Connecting to db")
            # cnx = mysql.connector.connect(user='root', password='12345',
            #                             host='127.0.0.1',
            #                             database='car_price_prediction')
            # print("connected to db")
            cursor.execute("insert into complete_information (brand, model, year, price, usage_miles, gearbox, fuel, body_condition, color, province, motor_volume, num_of_cylinder, acceleration, fuel_usage) values('%s', '%s', %d, %d, %d, '%s', '%s', '%s', '%s', '%s', %f, %d, %f, %f);" % (brand, model, int(year), int(cleaned_price), int(cleaned_usage), gear_box, fuel, body_condition, color, province, float(motor_volume), int(number_of_cylinders), float(acceleration), float(fuel_usage)))
            cursor.execute("insert into training_data (brand, model, year, price, usage_miles, gear_box, body_condition, color, province, motor_volume, num_of_cylinders, acceleration, fuel_usage) values('%d', '%d', %d, %d, %d, '%d', '%d', '%d', '%d', %f, %d, %f, %f);" % (
                int(brand_integered), int(model_integered), int(year), int(cleaned_price), int(cleaned_usage), int(gear_box_integered), int(body_condition_integered), int(color_integered), int(province_integered), float(motor_volume), int(number_of_cylinders), float(acceleration), float(fuel_usage)))
            cnx.commit()
            cnx.close()   
        # For keeping the data needed for model training; all number
        # cars_data

# print("Connecting to db")
# cnx = mysql.connector.connect(user='root', password='12345',
#                                         host='127.0.0.1',
#                                         database='car_price_prediction')
# print("connected to db")
# cursor = cnx.cursor()
# cursor.execute("select * from complete_information;")

# for row in cursor:
#     print(row)
# cnx.commit()
# cnx.close()

        # Our database has the following tables

        # Tables for mapping to numbers purpose
        # car brand
        # car model
        # gear_box
        # body_condition
        # color
        # province

        # car brand table
        # --------------
        # | id | brand |
        # --------------

        # first, we have to read from the complete_information table
        # then, filling our database, and in another program, we will use that 
        # database for training our model
        
# SQLs to create and test the tables on MySQL database
#         create table complete_information(
#             id int not null auto_increment primary key,
#             brand varchar(50) NOT NULL,
#             model varchar(50) NOT NULL,
#             year MEDIUMINT NOT NULL,
#             price int not null,
#             usage_miles int not null,
#             gearbox smallint not null,
#             fuel varchar(50) not null,
#             body_condition varchar(50) not null,
#             color varchar(50) not null,
#             province varchar(50) not null,
#             motor_volume float(4, 2) not null,
#             num_of_cylinder smallint not null,
#             acceleration float(6, 2) not null,
#             fuel_usage float(6, 2) not null);

# insert into complete_information(brand, model, year, price, usage_miles, gearbox, fuel, body_condition, color, province, motor_volume, num_of_cylinder, acceleration, fuel_usage) values('سایپا', 'پراید ۱۰۱', 1395, 98000000, 23000, 6, 'بنزین', 'بدون رنگ', 'سفید', 'تهران', 4.2, 5, 12.23, 9.2)

#  create table brand(
#      id int auto_increment not null primary key,
#      brand_name varchar(50) not null);


#  create table model(
#     id int autoincrement not null primary key,
#      model_name varchar(50) not null);

# create table gear_box(
#     id int auto_increment not null primary key,
#     gear_box varchar(50) not null);

# mysql> create table body_condition(
#     -> id int auto_increment not null primary key,
#     -> body_condition varchar(50) not null);

# create table color (
#     id int auto_increment not null primary key,
#     color varchar(50) not null);

# mysql> create table province(
#     -> id int auto_increment not null primary key,
#     -> province varchar(50) not null);


#  alter table training_data modify price bigint
