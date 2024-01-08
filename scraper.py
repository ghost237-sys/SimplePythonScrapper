from bs4 import BeautifulSoup
import requests

Jumia_flashsale_link ='https://www.jumia.co.ke/flash-sales'

page = input("There are 6 pages in Jumia Flash sale. Write the page you want to go to: ")

page_no = f'{Jumia_flashsale_link}/?page={page}'

source = requests.get(page_no).text

soup = BeautifulSoup(source,'lxml')


for items in soup.find_all("div",class_='info'):
    item_name = items.h3.text
    item_price = items.find("div",class_='prc')
    
    print(item_name)
    print(item_price.text)
    
    print()

print(page_no)