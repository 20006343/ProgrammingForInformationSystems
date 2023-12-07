from pony.orm import *

class Supplier:
	def __init__(self,authenticationid,suppliername,email,phonenumber,location,address,SupplierModel,connectiondict):
		self.authenticationid=authenticationid
		self.suppliername=suppliername
		self.email=email
		self.phonenumber=phonenumber
		self.address=address
		self.location=location
		self.SupplierModel=SupplierModel
		self.db=Database()
		self.db.bind(provider=connectiondict['provider'], host=connectiondict['host'], user=connectiondict['user'], passwd=connectiondict['passwd'], db=connectiondict['db'],port=connectiondict['port'])
		
    #7. The system should allow for the capture of the relevant supplier’s personal information
	# 23.The system should allow the owner to add, update or remove supplier information
	@db_session
	def AddSupplier(self):
		supplier = self.SupplierModel(authenticationid=self.authenticationid,supplierName=self.suppliername,email=self.email,phonenumber=self.phonenumber,location=self.location,address=self.address)

	@db_session
	def UpdateSupplier(self,supplierid):
		if self.authenticationid!='':
			self.SupplierModel[supplierid].authenticationid=self.authenticationid
		if self.suppliername!='':
			self.SupplierModel[supplierid].supplierName=self.suppliername
		if self.email!='':
			self.SupplierModel[supplierid].email=self.email
		if self.phonenumber!='':
			self.SupplierModel[supplierid].phonenumber=self.phonenumber
		if self.address!='':
			self.SupplierModel[supplierid].address=self.address
		if self.location!='':
			self.SupplierModel[supplierid].location=self.location
	

	@db_session
	def RemoveSupplier(self,supplierid):
		delete(supplier for supplier in self.SupplierModel if supplier.supplierid == supplierid)