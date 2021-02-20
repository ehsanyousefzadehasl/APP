import requests
from bs4 import BeautifulSoup
import re

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
for i in range(1, number_of_pages_to_scrape + 1):
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
            pass
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
                print(brand, model, year, cleaned_price, cleaned_usage, gear_box, fuel, body_condition)
            else:
                continue

            # color

            # province

            # motor_volume

            # number_of_cylinder

            # acceleration

            # fuel_usage
            
        # Then, each of the above mentioned will go into our database
        # Our database has the following tables
        # province
        # car brand
        # car model
        # color
        # body_condition
        # gear_box
        # cars_data
        
        # We consider the tables above (meanign all except the last one)
        # to be able to represent all of our data with numbers to later giving them
        # to the model to be trained based on them
