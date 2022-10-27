from itemadapter import ItemAdapter
import mysql.connector

class Utiles:
    def process_item(self, item, spider):
        return item

class Database:
    def connectDb():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS amazon")

    def createTable():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="amazon"
        )
        mycursor = mydb.cursor()
       
        mycursor.execute("CREATE TABLE IF NOT EXISTS categorie (id INT(11) AUTO_INCREMENT PRIMARY KEY,title VARCHAR(255), price VARCHAR(255), notation TEXT(50000), nbnotation VARCHAR(255), link TEXT(50000))")
        mycursor.execute("CREATE TABLE IF NOT EXISTS search (id INT(11) AUTO_INCREMENT PRIMARY KEY,title VARCHAR(255), price VARCHAR(255), notation TEXT(50000), nbnotation VARCHAR(255), link TEXT(50000))")

    def addRow(item):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="amazon"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO movie (title, img, author, time, genre, score, description, releaseDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (item['title'], item['img'], item['author'], item['time'], item['genre'], item['score'], item['desc'], item['release'])
        mycursor.execute(sql, val)
        mydb.commit()
        # print("Title :" , type(item['title']) , "Img :" , type(item['img']) , "Author :" , type(item['author']) , "Time :" , type(item['time']) , "Genre :" , type(item['genre']) , "Score :" , type(item['score']) , "Description :" , type(item['desc']) , "Release Date :" , type(item['release']))

    def addRowSearch(tab):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="amazon"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO search (title, price, notation, nbnotation, link) VALUES (%s, %s, %s, %s, %s)"
        val = (tab['title'], tab['price'], tab['notation'], tab['nbnotation'], tab['link'])
        mycursor.execute(sql, val)
        mydb.commit()

    def addRowCategorie(item):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="amazon"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO categorie (title, price, notation, nbnotation, link) VALUES (%s, %s, %s, %s, %s)"
        val = (item['title'], item['price'], item['notation'], item['nbnotation'], item['link'])
        mycursor.execute(sql, val)
        mydb.commit()