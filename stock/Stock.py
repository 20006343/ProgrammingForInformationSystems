from pony.orm import *

class Stock:
	def __init__(self,productid,supplierid,quantitysupplied,quantityremaining,supplyunitprice,dateofsupply,invoicestatus,StockModel,connectiondict):
		self.productid=productid
		self.supplierid=supplierid
		self.quantitysupplied=quantitysupplied
		self.quantityremaining=quantityremaining
		self.supplyunitprice=supplyunitprice
		self.dateofsupply=dateofsupply
		self.invoicestatus=invoicestatus
		self.StockModel=StockModel
		self.db=Database()
		self.db.bind(provider=connectiondict['provider'], host=connectiondict['host'], user=connectiondict['user'], passwd=connectiondict['passwd'], db=connectiondict['db'],port=connectiondict['port'])

	#5. The system should allow the recording and storage of product in stock and out of stock.
	#8. The system should allow for the recording of the product orders which have been supplied by the suppliers.
	#24. The system should allow the owner to add, update or remove stock information

	@db_session
	def AddStock(self):
		stock = self.StockModel(productid=self.productid,supplierid=self.supplierid,quantitysupplied=self.quantitysupplied,quantityremaining=self.quantityremaining,supplyunitprice=self.supplyunitprice,dateofsupply=self.dateofsupply,invoicestatus=self.invoicestatus)

	@db_session
	def UpdateStock(self,id,newquantityremaining):
		stock=self.StockModel.get(id=id)
		if newquantityremaining!='':
			stock.set(newquantityremaining=newquantityremaining)
	
	@db_session
	def RemoveStock(self,productid):
		delete(stock for stock in self.StockModel if stock.productid.productid == productid)