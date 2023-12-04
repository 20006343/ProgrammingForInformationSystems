# import the flask framework
from flask import Flask
# Import the pony orm classes
from pony.orm import *
#import the builtin datetime object
from datetime import datetime

# Create the database instance for attaching to ORM
db = Database()

# Creating the Suppliers table
class Supplier(db.Entity):
	supplierid = PrimaryKey(int, auto=True)
	authenticationid=Required('Authentication')
	supplierName=Required(str)
	email=Required(str)
	phonenumber=Required(str)
	location=Required(str)
	address=Required(str)
	supplieridstock=Optional('Stock')

# Creating the Employee table
class Employee(db.Entity):
	employeeid = PrimaryKey(int, auto=True)
	authenticationid=Required('Authentication')
	employeename=Required(str)
	email=Required(str)
	phonenumber=Required(str)
	address=Required(str)
	location=Required(str)
	dateofbirth=Required(datetime,6)
	category=Required(str)
	employeeidtransaction=Set('Transaction')

# Creating the Customer table
class Customer(db.Entity):
	customerid = PrimaryKey(int, auto=True)
	authenticationid=Required('Authentication')
	customername=Required(str)
	email=Required(str)
	phonenumber=Required(str)
	address=Required(str)
	location=Required(str)
	dateofbirth=Required(datetime,6)
	paymentpreference=Required(str)
	customeridtransaction=Set('Transaction')
	customeridreceipt=Set('Receipt')


# Creating the Authentication table
class Authentication(db.Entity):
	authenticationid = PrimaryKey(int, auto=True)
	username=Required(str)
	password=Required(str)
	role=Required(str)
	authenticationidsupplier=Optional('Supplier')
	authenticationidemployee=Optional('Employee')
	authenticationidcustomer=Optional('Customer')

# Creating the Stock table
class Stock(db.Entity):
	productid=Required('Product')
	supplierid=Required('Supplier')
	quantitysupplied=Required(float)
	supplyunitprice=Required(float)
	dateofsupply=Required(datetime)
	invoicestatus=Required(str)

# Creating the Transaction table
class Transaction(db.Entity):
	customerid=Required('Customer')
	employeeid=Required('Employee')
	productid=Required('Product')
	transactiondate=Required(date)
	transactiontime=Required(time)
	quantity=Required(float)
	status=Required(str)



app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Api sample"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
