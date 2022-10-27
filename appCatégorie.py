import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
from PIL import Image
import json
driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.amazon.fr')#on se connecte sur le site, on ferme les cookies et on va déplier la liste des catégories
driver.find_element(By.CLASS_NAME, 'a-link-emphasis').click()
driver.find_element(By.ID, 'nav-hamburger-menu').click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, 'hmenu-item.hmenu-compressed-btn').click()
time.sleep(1)
liste = {}
i = 0
for n in range (14,28):#on récupère la liste des catégories dans une liste
    liste[i] = driver.find_elements(By.CLASS_NAME, 'hmenu-item')[n].text
    i+=1
print(liste)
i = 0

def choix_categorie():
    recherche = input("Choisir une categorie: !ATTENTION certaines categories peuvent ne pas fonctionner car les pages sont construites trop differemment. Pour la demo vous pouvez essayer Livres ou Jeux vidéo et Consoles ! Il faut aussi taper exactement la catégorie car elle est sensible a la casse, aux espaces et au accents: ")
    for i in range (len(liste)):
        if (liste[i] == recherche):#on vérifie si la catégorie entrée existe
            resultat = True
            break
        else:
            resultat = False

    if (resultat == True):#si la catégorie existe on va rechercher où cliquer pour cliquer sur la catégorie entrée
        driver.find_element(By.LINK_TEXT, recherche).click()
        i+=10
        driver.find_element(By.XPATH,f'/html/body/div[3]/div[2]/div/ul[{i}]/li[3]/a').click()
    else:
        print("Categorie introuvable reessayez")
        choix_categorie()
        

choix_categorie()
#cliquer sur 'voir plus' pour avoir la liste complète des articles de cette catégorie
driver.find_element(By.CLASS_NAME,'a-size-base-plus.a-color-link.octopus-pc-card-title-seeMore').click()
#on clique sur la page actuelle pour l'actualiser et récupérer un url plus propre
driver.find_element(By.CLASS_NAME, 'a-selected').click()
time.sleep(1)
url = driver.current_url

def the_chain(url):
    
    data = []
    i = 0
        

    time.sleep(1)
    driver.get(url)
        
    articles = driver.find_elements(By.CLASS_NAME,
                    'a-cardui._cDEzb_grid-cell_1uMOS.p13n-grid-content')
    nb_art = len(articles)
    
    for n in range(nb_art):
            
        tab = {}
        i = i+1

        try:
            tab['title'] = articles[n].find_element(By.CLASS_NAME,'_cDEzb_p13n-sc-css-line-clamp-3_g3dy1').text
        except:
            try:
                tab['title'] = articles[n].find_element(By.CLASS_NAME,'_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y').text
            except:
                tab['title']  = None
            
        try:
            note = articles[n].find_element(By.CLASS_NAME,'a-icon-row').find_elements(By.TAG_NAME, 'a')[0].get_attribute('title')
            tab['notation'] = str(note)
        except:
            tab['notation'] = None
        try:
            tab['nbnotation'] = articles[n].find_elements(By.CLASS_NAME, 'a-size-small')[2].text
        except:
            tab['nbnotation'] = None
        try:
            tab['price'] = articles[n].find_element(By.CLASS_NAME, '_cDEzb_p13n-sc-price_3mJ9Z').text
        except:
            try:
                tab['price'] = articles[n].find_element(By.CLASS_NAME, 'p13n-sc-price').text
            except:
                tab['price'] = None
        try:
            tab['link'] = articles[n].find_element(By.CLASS_NAME,'a-link-normal').get_attribute('href')
        except:
            tab['link'] = None
        data.append(tab)     
    return data
document = the_chain(url)
with open('amazon_categorie.json', 'w') as file:
    json.dump(document, file, indent=2)