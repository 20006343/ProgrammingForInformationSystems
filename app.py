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
			session.pop('erroruser')
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


@app.route('/api/addemployee', methods=['POST'])
def add_employee():
	connectiondict={'provider':provider,'host': host,'user':user, 'passwd':password,'db':database,'port':port}
	employeeinfo= json.loads(request.data)
	print(str(employeeinfo))
	employee=Employee.Employee(models.Employee,connectiondict,employeeinfo.get('authenticationid'),employeeinfo.get('employeename'),employeeinfo.get('email'),employeeinfo.get('phonenumber'),employeeinfo.get('address'),employeeinfo.get('location'),employeeinfo.get('dob'),employeeinfo.get('category'))
	employee.AddEmployee()
	return 'Employee Added', 200

@app.route('/api/addsupplier', methods=['POST'])
def add_supplier():
	connectiondict={'provider':provider,'host': host,'user':user, 'passwd':password,'db':database,'port':port}
	supplierinfo= json.loads(request.data)
	supplier=Supplier.Supplier(supplierinfo.get('supplierauthenticationid'),supplierinfo.get('suppliername'),supplierinfo.get('supplieremail'),supplierinfo.get('supplierphonenumber'),supplierinfo.get('supplieraddress'),supplierinfo.get('supplierlocation'),models.Supplier,connectiondict)
	supplier.AddSupplier()
	return 'Supplier Added', 200


@app.route('/api/addstock', methods=['POST'])
def add_stock():
	connectiondict={'provider':provider,'host': host,'user':user, 'passwd':password,'db':database,'port':port}
	stockinfo= json.loads(request.data)
	stock=Stock.Stock(stockinfo.get('stockproductid'),stockinfo.get('stocksupplierid'),stockinfo.get('stockquantity'),stockinfo.get('stockquantity'),stockinfo.get('stocksupplyunitprice'),stockinfo.get('stocksupplydate'),"Uninvoiced",models.Stock,connectiondict)
	stock.AddStock()
	return 'Stock Added', 200



###################################################
@app.route('/owner/',methods=['GET'])
def owner_view():
	products=[]
	suppliers=[]

	with db_session:
		products=list(reversed(list(models.Product.select())))
		employees=list(reversed(list(models.Employee.select())))
		customers=list(reversed(list(models.Customer.select())))
		suppliers=list(reversed(list(models.Supplier.select())))
		stocks=[]

		for stockitem in list(reversed(list(models.Stock.select()))):
			stockdict={}
			stockdict['productName']=models.Product.get(productid=stockitem.productid.productid).productName
			stockdict['supplierName']=models.Supplier.get(supplierid=stockitem.supplierid.supplierid).supplierName
			stockdict['quantitysupplied']=stockitem.quantitysupplied
			stockdict['quantityremaining']=stockitem.quantityremaining
			stockdict['supplyunitprice']=stockitem.supplyunitprice
			stockdict['dateofsupply']=stockitem.dateofsupply.strftime("%b %d, %Y")
			stocks.append(stockdict)

		#ensuring that the authenticationids are not used more than once
		usedauthenticationsids=[]

		for customer in customers:
			usedauthenticationsids.append(int(customer.authenticationid.authenticationid))

		for employee in employees:
			usedauthenticationsids.append(int(employee.authenticationid.authenticationid))

		for supplier in suppliers:
			usedauthenticationsids.append(int(supplier.authenticationid.authenticationid))

		allusers=list(reversed(list(models.Authentication.select())))
		users=[]

		for user in allusers:
			if user.authenticationid in usedauthenticationsids:
				pass
			else:
				users.append(user)
		#end ensuring that the authenticationids are not used more than once

	return render_template('owner.html',products=products,suppliers=suppliers,stocks=stocks,session=session,users=users,employees=employees,allusers=allusers)

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