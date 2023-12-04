# import the flask framework
from flask import Flask
# Import the pony orm classes
from pony.orm import *

# Create the database instance for attaching to ORM
db = Database()

# Creating the Authentication table
class Authentication(db.Entity):
	authenticationid = PrimaryKey(int, auto=True)
	username=Required(str)
	password=Required(str)
	role=Required(str)
	authenticationidsupplier=Optional('Supplier')
	authenticationidemployee=Optional('Employee')
	authenticationidcustomer=Optional('Customer')


app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Api sample"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
