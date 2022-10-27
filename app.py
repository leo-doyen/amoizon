from appCollect import startCollect
from appCatégorie import startCategorie
def checkInput():
    tmp = input('Do you want to search yourself or maybe interested in existant categories ? (search/categorie)')
    if tmp == 'search':
        startCollect()
    elif tmp == 'categorie':
        startCategorie()
    else:
        print('You must enter a valid input')
        checkInput()



checkInput()

