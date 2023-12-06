# import the flask framework
from flask import Flask
# Import the pony orm classes
from pony.orm import *
#import the builtin datetime object
from datetime import datetime

db = Database()
db.bind(provider='mysql', host='127.0.0.1', user='user', passwd='user123', db='test',port=3307)

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Api sample"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
