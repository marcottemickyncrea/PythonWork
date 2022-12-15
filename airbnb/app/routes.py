from flask import render_template, request, redirect, url_for, flash
from app import app

import mysql.connector as mysqlpy

user = 'root'
password = 'example'
host = 'localhost'
port = '3308'
database = 'airbnb'

bdd = mysqlpy.connect(user=user, password=password,
                      host=host, port=port, database=database)
cursor = bdd.cursor()

@app.route('/index')
def destinations():
    cursor.execute('SELECT * FROM destinations;')
    destinations = cursor.fetchall()
    return render_template('index.html', destinations = destinations)

@app.route('/ajout-destination', methods= ['GET', 'POST'])
def ajouter_destination():
    if request.method == 'POST':
        url_image = request.form['url-image']        
        adresse_destination = request.form['localisation']
        type_destination = request.form['type']
        dates = request.form['dates']
        prix_destination = request.form['prix']
        note_destination = 0
        query=('INSERT INTO destinations(url_image, adresse_destination, type_destination, dates, prix_destination, note_destination) VALUES(%s,%s,%s,%s,%s,%s);')
        cursor.execute(query, (url_image, adresse_destination, type_destination, dates, prix_destination, note_destination))
        bdd.commit() 
        return redirect('index')
    return render_template('ajout-destination.html')

@app.route('/modifier-destination', methods = ['GET', 'POST'])
def modifier_destination():
    return render_template('modifier-destination.html')
