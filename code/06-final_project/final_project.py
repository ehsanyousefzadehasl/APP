import requests
from bs4 import BeautifulSoup
import re

number_of_pages_to_scrape = 2
main_url = "https://bama.ir/car/all-brands/all-models/all-trims?page="

# This loop for reading from the pages
# Then, extracting link of each post 
for i in range(1, number_of_pages_to_scrape + 1):
    result = requests.get(main_url + str(i))

    # print("$$$$$$$$$$$$$$$$$$$$$$ ------------------page_number: ", i)
    # print(result.text)

    soup = BeautifulSoup(result.text, 'html.parser')

    # print(soup)

    res_links = soup.find_all('a', attrs={'class': 'cartitle'})
    # This regular expression is for extracting links from which we are going to get our real data
    post_link_regular_expr = r'href="(.*?)"'

    
    for e in res_links:
        result_links = re.search(post_link_regular_expr, str(e))
        # print(result_links.group(0))
        # print("===========")
        # Now, we have link to every post, so we can extract data from each of them
        # In each post, we have to check whether it has a price or not
        # If a post does not have price, it is useless for our model

        post_url = str(result_links.group(0))
        print(post_url)    

        # Then, we go to scrape data from each post
        # brand, model, year, price, usage, gearbox, fuel, body_condition, color, province, motor_volume, 
        # number_of_cylinder, acceleration, fuel_usage

        # We have to have different regular expressions forextracting these features



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