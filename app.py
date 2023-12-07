from pony.orm import *
from config import *
from datetime import datetime
from flask import Flask, jsonify, request,render_template,redirect,url_for,session
import models
from authentication import Authentication
from customer import Customer  
from employee import Employee  
from supplier import Supplier
from product import Product
from stock import Stock
from transaction import Transaction
from receipt import Receipt
import json


db = Database()
db.bind(provider=provider, host=host, user=user, passwd=password, db=database,port=port)
# Initiate the models to create the database tables
models.init()
connectiondict={'provider':provider,'host': host,'user':user, 'passwd':password,'db':database,'port':port}
# end database table creation

# start the definitions of the flask app
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'

@app.route('/api/authentication', methods=['POST'])
def login():
	connectiondict={'provider':provider,'host': host,'user':user, 'passwd':password,'db':database,'port':port}
	credentials= json.loads(request.data)
	auth=Authentication.Authentication(models.Authentication,connectiondict)
	loggedin=auth.Login(credentials.get('username'),credentials.get('password'))
	userdict=""

	if type(loggedin)==str:
		userdict='False'
	else:
		userdict=loggedin
	session['userdict'] = userdict
	return userdict, 200


@app.route('/api/adduser', methods=['POST'])
def add_user():
	connectiondict={'provider':provider,'host': host,'user':user, 'passwd':password,'db':database,'port':port}
	authinfo= json.loads(request.data)
	existing=""
	with db_session:
		existing=models.Authentication.get(username=authinfo.get('username'))
	
	if existing!=None:
		session['erroruser']="Username already exists. Choose Another one!!"
		if 'successuser' in session.keys():
			session.pop('successuser')
	else:
		session['successuser']="User Added Succesfully"
		if 'erroruser' in session.keys():
			session.pop('errouser')
		auth=Authentication.Authentication(models.Authentication,connectiondict,authinfo.get('username'),authinfo.get('password'),authinfo.get('role'))
		auth.AddUser()
	return "User Added", 200


@app.route('/api/addproduct', methods=['POST'])
def add_product():
	connectiondict={'provider':provider,'host': host,'user':user, 'passwd':password,'db':database,'port':port}
	productinfo= json.loads(request.data)
	product=Product.Product(productinfo.get('productname'),productinfo.get('description'),productinfo.get('category'),productinfo.get('retailunitprice'),models.Product,connectiondict)
	product.AddProduct()
	return 'Product Added', 200


@app.route('/api/employee', methods=['POST'])
def add_employee():
	connectiondict={'provider':provider,'host': host,'user':user, 'passwd':password,'db':database,'port':port}
	productinfo= json.loads(request.data)
	product=Product.Product(productinfo.get('productname'),productinfo.get('description'),productinfo.get('category'),productinfo.get('retailunitprice'),models.Product,connectiondict)
	product.AddProduct()
	return 'Employee Added', 200


###################################################
@app.route('/owner/',methods=['GET'])
def owner_view():
	products=[]
	suppliers=[]

	with db_session:
		products=list(models.Product.select())
		suppliers=list(models.Supplier.select())
		users=list(models.Authentication.select())

	return render_template('owner.html',products=products,suppliers=suppliers,session=session,users=users)

###################################################



###################################################
@app.route('/manager/',methods=['GET'])
def manager_view():
	return render_template('manager.html')

###################################################



###################################################

@app.route('/supplier/',methods=['GET'])
def supplier_view():
	return render_template('supplier.html')

###################################################


###################################################
@app.route('/employee/',methods=['GET'])
def employee_view():
	return render_template('employee.html')

###################################################


###################################################
@app.route('/customer/',methods=['GET'])
def customer_view():
	return render_template('customer.html')

###################################################

@app.route('/logout')
def signout():
	session.clear()
	return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('login.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)