from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time

response=requests.get('https://appbrewery.github.io/Zillow-Clone/')
website=response.text
soup = BeautifulSoup(website,'html.parser')

# Get hold of all addresses
addresses=[]
address_tags=soup.find_all(name='address')
for address in address_tags:
    addresses.append(address.getText().strip())
print(len(addresses))
# Get hold of prices
prices=[]
price_tags=soup.find_all(name='span',class_="PropertyCardWrapper__StyledPriceLine")
for price in price_tags:
    prices.append(price.getText().strip()[:6])

print(len(prices))

# Get hold of links
links=[]
link_tags=soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
for link in link_tags:
    links.append(link['href'].strip())
print(len(links))

# start filling form with selenium

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver=webdriver.Chrome(executable_path=r'D:\Python Extra\webdrivers\chrome\chromedriver.exe',options=chrome_options)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLScGqXQ5n0TAXfSv_CP98zbXGh-3Jm7TydcKTnqaUM_zrOSBDw/viewform?usp=sf_link")

for i in range(5):
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(addresses[i])
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(prices[i])
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(links[i])
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    driver.find_element_by_link_text('Envoyer une autre réponse').click()
    time.sleep(3)
