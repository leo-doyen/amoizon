from appCollect import startCollect

def checkInput():
    tmp = input('Do you want to search yourself or maybe interested in existant categories ? (search/categorie)')
    if tmp == 'search':
        startCollect()
    elif tmp == 'categorie':
        print('GUILLAUME')
    else:
        print('You must enter a valid input')
        checkInput()



checkInput()

