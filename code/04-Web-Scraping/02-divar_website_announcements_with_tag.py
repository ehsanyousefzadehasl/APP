import requests
from bs4 import BeautifulSoup
import re

result = requests.get('https://divar.ir/s/tehran')

# print(result.text)

soup = BeautifulSoup(result.text, 'html.parser')

# print(soup)

res = soup.find_all('a', attrs={'class': 'kt-post-card'})

regular_expr = r'(.*<div class="kt-post-card__top-description kt-post-card-description">توافقی</div>.*)'
link_reg_expr = r'href="(.*?)"'
for e in res:
    # print(str(e))
    # print("===========")
    # print(e.children)
    result = re.search(regular_expr, str(e))
    if result != None:
        print(e.text)
        link = re.search(link_reg_expr, str(e))
        print("https://divar.ir/" + str(link.group(0))[7:len(link.group(0))-1])
        print("--------")


# <a class = "kt-post-card kt-post-card--outlined" href = "/v/گوشی-سونی-xa-ultra_گوشی-موبایل_تهران_شهریار_دیوار/AYooF1TM" > <div class = "kt-post-card__body" > <div class = "kt-post-card__title" > گوشی سونی Xa Ultra < /div > <div class = "kt-post-card__top-description kt-post-card-description" > ۲, ۱۵۰, ۰۰۰ تومان < /div > <div class = "kt-post-card__bottom" > <div class = "kt-post-card__bottom-description-wrapper" > <span class = "kt-post-card-description kt-post-card__bottom-description kt-text-truncate" title = "لحظاتی پیش در شهریار" > لحظاتی پیش در شهریار < /span > </div > <i class = "kt-icon kt-icon-chat-bubble kt-post-card__chat-icon" > </i > </div > </div > <div class = "kt-post-card__image-wrapper" > <div > <picture class = "kt-image-block kt-image-block--rounded" style = "padding-bottom:100%" > <source type = "image/webp" data-srcset = "https://s100.divarcdn.com/static/thumbnails/1613270635/AYooF1TM.webp" srcset = "https://s100.divarcdn.com/static/thumbnails/1613270635/AYooF1TM.webp" > <img class = "kt-image-block__image ls-is-cached kt-image-block__image--lazy-loaded" alt = "گوشی سونی Xa Ultra" data-src = "https://s100.divarcdn.com/static/thumbnails/1613270635/AYooF1TM.jpg" src = "https://s100.divarcdn.com/static/thumbnails/1613270635/AYooF1TM.jpg" > </picture > </div > </div > </a >
# <div class = "kt-post-card__top-description kt-post-card-description" > توافقی < /div >
