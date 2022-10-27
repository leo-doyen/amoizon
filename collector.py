from selenium import webdriver
from selenium.webdriver.common.by import By
from utiles import Database
import time

def the_chain(nb_pages, articles,driver):
    Database.connectDb()
    Database.createTable()
    
    data = []
    start_urls = [f'https://www.amazon.fr/s?k=Intelligence+artificielle&page={n}' for n in range(1,nb_pages+1)]
    i = 0
    for n in range(0, nb_pages) :
        
        print(start_urls[n])
        lien = start_urls[n]
        time.sleep(1)
        driver.get(lien)
        
        articles = driver.find_elements(By.CLASS_NAME,
                        'sg-col-4-of-12.s-result-item.s-asin.sg-col-4-of-16.sg-col.s-widget-spacing-small.sg-col-4-of-20')
        nb_art = len(articles)
        
        for n in range(nb_art):
            
            tab = {}
            i = i+1
    #         print(n)
        #     a-size-base-plus a-color-base a-text-normal
            try:
                name = articles[n].find_element(By.CLASS_NAME,'a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal')
                print(name.text)
                tab['title'] = str(name.text)
            except:
                name = articles[n].find_element(By.CLASS_NAME,'a-size-base-plus.a-color-base.a-text-normal')
                print(name.text)
                tab['title']  = None
            try:

                note = articles[n].find_element(By.CLASS_NAME, 'a-row.a-size-small').find_elements(By.TAG_NAME, 'span')[0].get_attribute('aria-label')
    #             note.find_elements(By.CLASS_NAME,'a-icon-alt')
                print('NOTE '+note)
                tab['notation'] = str(note)
            except:
                note = 'NULLOS'
                print(note)
                tab['notation'] = None
            try:
                nb_avis = articles[n].find_element(By.CLASS_NAME,'a-row.a-size-small')
                nb_avis.find_elements(By.CLASS_NAME,'a-size-base.s-underline-text')
                print('NB : '+nb_avis.text)
                tab['nbnotation'] = str(nb_avis.text)
            except:
                nb_avis = 'NULLOS'
                print(nb_avis)
                tab['nbnotation'] = None
            try:
                prix=articles[n].find_element(By.CLASS_NAME,'a-price-whole')
                prix_symbole = articles[n].find_element(By.CLASS_NAME,'a-price-symbol')
                print('PRIX : '+prix.text+' '+prix_symbole.text)
                tab['price'] = str(prix.text+' '+prix_symbole.text)
            except:
                prix = 'NULLOS'
                print(prix) 
                tab['price'] = None
            try:
                link=articles[n].find_element(By.CLASS_NAME,'a-link-normal.s-no-outline').get_attribute('href')
                print(link)
                tab['link'] = str(link)
            except:
                link = 'NULLOS'
                print(link)
                tab['link'] = None
            data.append(tab)
            Database.addRowSearch(tab)     
    print('TOTAL')            
    print(i)
    return data