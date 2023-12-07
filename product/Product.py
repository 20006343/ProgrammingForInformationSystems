from pony.orm import *

class Product:
	def __init__(self,productName,description,category,retailunitprice,ProductModel,connectiondict):
		self.productName=productName
		self.description=description
		self.category=category
		self.retailunitprice=retailunitprice
		self.ProductModel=ProductModel
		self.db=Database()
		self.db.bind(provider=connectiondict['provider'], host=connectiondict['host'], user=connectiondict['user'], passwd=connectiondict['passwd'], db=connectiondict['db'],port=connectiondict['port'])
		

	# 4. The system should allow recording and storage of product information 
	@db_session
	def AddProduct(self):
		product = self.ProductModel(productName=self.productName,description=self.description,category=self.category,retailunitprice=self.retailunitprice)

	@db_session
	def UpdateProduct(self,productid):
		if self.productName!='':
			self.ProductModel[productid].productName=self.productName
		if self.description!='':
			self.ProductModel[productid].description=self.description
		if self.category!='':
			self.ProductModel[productid].category=self.category
		if self.retailunitprice!='':
			self.ProductModel[productid].retailunitprice=self.retailunitprice
	
	@db_session
	def RemoveProduct(self,productid):
		delete(product for product in self.ProductModel if product.productid == productid)