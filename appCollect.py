from selenium import webdriver
from selenium.webdriver.common.by import By
from utiles import Database
import time
import json
from collector import the_chain




driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://www.amazon.fr')

time.sleep(3)
btn = driver.find_element(By.ID, "sp-cc-accept")
btn.click()

search = driver.find_element(By.ID, "twotabsearchtextbox")
search.click()

time.sleep(3)


search.send_keys("Intelligence artificielle")
searchValidate = driver.find_element(By.ID, "nav-search-submit-button")
time.sleep(3)
searchValidate.click()

articles = driver.find_elements(By.CLASS_NAME,
                        'sg-col-4-of-12.s-result-item.s-asin.sg-col-4-of-16.sg-col.s-widget-spacing-small.sg-col-4-of-20')
time.sleep(3)
data = the_chain(5,articles,driver)

with open('amazon_search.json', 'w') as file:
    json.dump(data, file, indent=2)
