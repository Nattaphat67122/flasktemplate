from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',title='MY Home Page')

@app.route('/about')
def about():
    title='About Page',
    name = 'nataphat uthumporn',
    email = 'rocket0242@gmail.com',
    phone = '082-895-0426'
    return render_template('abou.html',
                           title = title,
                           name = name,
                           email = email,
                           phone= phone)

@app.route('/favorite/foods')
def favorite_foods():
    title='Favorite Foods Page'
    foods = ['Pizza', 'Sushi', 'Ice Cream', 'Tomyam', 'Noodles']
    return render_template('fav_foods.html',
                            foods=foods,
                            title=title)

@app.route('/favorite/sports')
def favorite_sports():
    title='Favorite Sports Page'
    sports = ['Football', 'Petong', 'Badminton', 'Weight Training', 'Volleyball']
    return render_template('fav_sports.html',
                            sports=sports,
                            title=title)

@app.route('/greeting/<username>')
def greeting(username):
    title='Welcome Page'
    return render_template ('welcome.html',
                            title=title,
                            username=username)