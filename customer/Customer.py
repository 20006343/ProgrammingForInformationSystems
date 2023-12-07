from pony.orm import *
# 10. The system should capture and store the personal information of a customer for identification purposes.
class Customer:
	def __init__(self,authenticationid,customername,email,phonenumber,address,location,dateofbirth,paymentpreference,CustomerModel,connectiondict):
		self.authenticationid=authenticationid
		self.customername=customername
		self.email=email
		self.phonenumber=phonenumber
		self.address=address
		self.location=location
		self.dateofbirth=dateofbirth
		self.paymentpreference=paymentpreference
		self.CustomerModel=CustomerModel
		self.db=Database()
		self.db.bind(provider=connectiondict['provider'], host=connectiondict['host'], user=connectiondict['user'], passwd=connectiondict['passwd'], db=connectiondict['db'],port=connectiondict['port'])

	# 22.The system should allow the owner to add, update or remove customer information
	@db_session
	def AddCustomer(self):
		customer = self.CustomerModel(authenticationid=self.authenticationid,customername=self.customername,email=self.email,phonenumber=self.phonenumber,address=self.address,location=self.location,dateofbirth=self.dateofbirth,paymentpreference=self.paymentpreference)

	@db_session
	def UpdateCustomer(self,customerid):
		if self.authenticationid!='':
			self.CustomerModel[customerid].authenticationid=self.authenticationid
		if self.customername!='':
			self.CustomerModel[customerid].customername=self.customername
		if self.email!='':
			self.CustomerModel[customerid].email=self.email
		if self.phonenumber!='':
			self.CustomerModel[customerid].phonenumber=self.phonenumber
		if self.address!='':
			self.CustomerModel[customerid].address=self.address
		if self.location!='':
			self.CustomerModel[customerid].location=self.location
		if self.dateofbirth!='':
			self.CustomerModel[customerid].dateofbirth=self.dateofbirth
		if self.paymentpreference!='':
			self.CustomerModel[customerid].paymentpreference=self.paymentpreference

	@db_session
	def RemoveCustomer(self,customerid):
		delete(customer for customer in self.CustomerModel if customer.customerid == customerid)