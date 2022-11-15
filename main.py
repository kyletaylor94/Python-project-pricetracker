from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import requests
import lxml

#this method will search-find and show the prices of 3080 evga gpu

def price_checker():
    URL= "https://www.amazon.com/s?k=evga+3080+gpu&crid=35LUB89QEEN9N&sprefix=evga+3080+gpu%2Caps%2C172&ref=nb_sb_noss_1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "Accept-Language": "hu-HU,hu;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    response = requests.get(url=URL, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')

    prices = soup.find_all("span", "a-offscreen")
    prices_to_string = str(prices)
    formated = prices_to_string.translate({ord(i): None for i in '<span class="a-offscreen/[]'})
    print(formated)

price_checker()

