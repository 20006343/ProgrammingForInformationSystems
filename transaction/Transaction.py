from pony.orm import *

class Transaction:
	def __init__(self,customerid,employeeid,productid,transactiondate,transactiontime,quantity,status,TransactionModel,connectiondict):
		self.customerid=customerid
		self.employeeid=employeeid
		self.productid=productid
		self.transactiondate=transactiondate
		self.transactiontime=transactiontime
		self.quantity=quantity
		self.status=status
		self.TransactionModel=TransactionModel
		self.db=Database()
		self.db.bind(provider=connectiondict['provider'], host=connectiondict['host'], user=connectiondict['user'], passwd=connectiondict['passwd'], db=connectiondict['db'],port=connectiondict['port'])

	#11. The system should capture and store the order details of a customer during the purchase process.
	#15. The system should allow for the capture and storage of employee’s sales
	
	@db_session
	def AddTransaction(self):
		transaction = self.TransactionModel(customerid=self.customerid,employeeid=self.employeeid,productid=self.productid,transactiondate=self.transactiondate,transactiontime=self.transactiontime,quantity=self.quantity,status=self.status)

	@db_session
	def FinishTransaction(self,transactiondate,transactiontime):
		transaction=self.TransactionModel.get(transactiondate=transactiondate,transactiontime=transactiontime)
		#get product id from transaction

		#get stock by product id
			#use the id to update the stock

			

		if self.quantity!='':
			transaction.set(quantity=self.quantity)

		if self.status!='':
			transaction.set(status=self.status)
	
	@db_session
	def RemoveTransaction(self,transactiondate,transactiontime):
		delete(transaction for transaction in self.TransactionModel if transaction.transactiondate==transactiondate and transaction.transactiontime==transactiontime)