from flask import Flask



app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret shhhh'


from webscraper import routes