from selenium import webdriver
from selenium.webdriver.common.by import By
from utiles import Database
import time
import json
from collector import collect

# this function is used to check if the input is correct then return the input
def checkInput():
    print('What do you want to search on amazon ?')
    searchInput = input()
    if searchInput == '':
        print('You must enter a search term')
        checkInput()
    else:
        return searchInput
        
# this function strart the collect process save the data in a json file and save the data in the database
def startCollect():     
    # call to the checkInput function to get the search   
    searchInput = checkInput()
    # truncate the search to get the url (Yes i could have use the 'Next Page' on the website but i wanted to do it like this)
    searchTruncate = searchInput.replace(' ','+')

    # open the driver
    driver = webdriver.Chrome('./chromedriver.exe')
    # get the url
    driver.get('https://www.amazon.fr')


    time.sleep(3)
    # accept the cookies
    btn = driver.find_element(By.ID, "sp-cc-accept")
    btn.click()

    # get the search bar
    search = driver.find_element(By.ID, "twotabsearchtextbox")
    search.click()

    time.sleep(3)

    # enter the search term then validate
    search.send_keys(searchInput)
    searchValidate = driver.find_element(By.ID, "nav-search-submit-button")
    time.sleep(3)
    searchValidate.click()

    # get all the articles
    articles = driver.find_elements(By.CLASS_NAME,
                            'sg-col-4-of-12.s-result-item.s-asin.sg-col-4-of-16.sg-col.s-widget-spacing-small.sg-col-4-of-20')
    time.sleep(3)

    # call the collect function from collector.py
    data = collect(5,articles,driver,searchTruncate)

    # save the data in a json file
    with open('amazon_search.json', 'w') as file:
        json.dump(data, file, indent=2)

