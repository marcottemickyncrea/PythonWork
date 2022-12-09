from flask import render_template, flash, redirect, url_for
from app import app

@app.route('/')
def index():
    posts = [
        {
            'url': 'https://a0.muscache.com/im/pictures/d72d00a9-cb72-445b-92c7-285d31b3e794.jpg?im_w=720',
            'adresse': 'Quiberville, France',
            'type':'Particulier',
            'date': '8-13 janv.',
            'prix': '194',
            'note': '4.71',
        },
        {
            'url': 'https://a0.muscache.com/im/pictures/aa5dcdd3-9b49-497f-aa4e-114414dd419e.jpg?im_w=720',
            'adresse': 'Criel-sur-Mer, France',
            'type':'Particulier',
            'date': '10-16 dec.',
            'prix': '149',
            'note': '4.74',
        },
        {
            'url': 'https://a0.muscache.com/im/pictures/miso/Hosting-631888526880090604/original/2c848fcd-7fb0-4533-bb0e-a6970487afc8.jpeg?im_w=720',
            'adresse': 'Criel-sur-Mer, France',
            'type':'Particulier',
            'date': '10-16 dec.',
            'prix': '274',
            'note': '4.79',
        },
        {
            'url': 'https://a0.muscache.com/im/pictures/0a67e415-dd30-4724-9dc0-8bf3fb0bb05a.jpg?im_w=720',
            'adresse': 'Dieppe, France',
            'type':'Particulier',
            'date': '2-7 janv.',
            'prix': '86',
            'note': '4.89',
        },
        {
            'url': 'https://a0.muscache.com/im/pictures/d20f5257-d4df-45c7-b816-c39e15a9961c.jpg?im_w=720',
            'adresse': 'Le tréport, France',
            'type':'Particulier',
            'date': '9-14 dec.',
            'prix': '172',
            'note': '4.67',
        },
        {
            'url': 'https://a0.muscache.com/im/pictures/0f1fc62e-8fb9-4b6d-a6d4-f3021c13dbe3.jpg?im_w=720',
            'adresse': 'Dieppe, France',
            'type':'Professionnel',
            'date': '10-16 dec.',
            'prix': '92',
            'note': '4.74',
        },
    ]
    return render_template('index.html', title='Home', posts=posts)