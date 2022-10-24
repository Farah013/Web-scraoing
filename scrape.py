from bs4 import BeautifulSoup
import requests
#we're going to need requests library also because we're going to send requests to a webpage and get some response
url="https://www.pararius.com/apartments/amsterdam?ac=1"
#We need to export the data to a csv file so we're going to use the csv library
from csv import writer
page= requests.get(url)

#Soup will have all the HTML code.
soup = BeautifulSoup(page.content, 'html.parser')
#We're going to store all the sections of the class listing-search-item in lists
lists= soup.find_all('section', class_="listing-search-item")
#we have a lot of sections so we need to loop through the lists
#We have to export the data into a csv file
with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter= writer(f)
    #The writer is responsible for writing in the file
    header= ['Title', 'Location', 'Price', 'Area']
    thewriter.writerow(header)
    for list in lists:
        title= list.find('a', class_="listing-search-item__link--title").text.replace('\n', '')
        location= list.find('div', class_="listing-search-item__sub-title").text.replace('\n', '')
        price= list.find('div', class_="listing-search-item__price").text.replace('\n', '')
        area= list.find('li', class_="illustrated-features__item--surface-area").text.replace('\n','')
        info=[title, location, price, area]
        thewriter.writerow(info)