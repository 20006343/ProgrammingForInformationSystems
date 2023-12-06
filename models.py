# Import the pony orm classes
from pony.orm import *
from datetime import datetime
from datetime import date
from datetime import time
# Create the database instance for attaching to ORM
global db
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

# Creating the Receipt table
class Receipt(db.Entity):
	customerid=Required('Customer')
	receiptdate=Required(date)
	receipttime=Required(time)
	total=Required(float)
	amountpaid=Required(float)
	balance=Required(float)
	paymentmethod=Required(str)


# Creating the Product table
class Product(db.Entity):
	productid = PrimaryKey(int, auto=True)
	productName=Required(str)
	description=Required(str)
	category=Required(str)
	retailunitprice=Required(float)
	productidstock=Set('Stock')
	productidtransaction=Set('Transaction')


# initializing the creation of the models
def init():
	print('Creating the Database Models')
	# Binding the ORM to mysql
	db.bind(provider='mysql', host='127.0.0.1', user='user', passwd='user123', db='test',port=3307)
	db.generate_mapping(create_tables=True)

