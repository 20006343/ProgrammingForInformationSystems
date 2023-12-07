from pony.orm import *

class Receipt:
	def __init__(self,customerid,receiptdate,receipttime,total,amountpaid,balance,paymentmethod,ReceiptModel,connectiondict):
		self.customerid=customerid
		self.receiptdate=receiptdate
		self.receipttime=receipttime
		self.total=total
		self.amountpaid=amountpaid
		self.balance=balance
		self.paymentmethod=paymentmethod
		self.ReceiptModel=ReceiptModel
		self.db=Database()
		self.db.bind(provider=connectiondict['provider'], host=connectiondict['host'], user=connectiondict['user'], passwd=connectiondict['passwd'], db=connectiondict['db'],port=connectiondict['port'])

	#12. The system should allow a user to pay for their purchase using their preferred payment method.
    #13. The system should allow for generation of receipts after customers have made their purchases.
	
	@db_session
	def AddReceipt(self):
		receipt = self.ReceiptModel(customerid=self.customerid,receiptdate=self.receiptdate,receipttime=self.receipttime,total=self.total,amountpaid=self.amountpaid,balance=self.balance,paymentmethod=self.paymentmethod)

	@db_session
	def UpdateReceipt(self,receiptdate,receipttime):
		receipt=self.ReceiptModel.get(receiptdate=receiptdate,receipttime=receipttime)
		
		if self.total!='':
			receipt.set(total=self.total)

		if self.amountpaid!='':
			receipt.set(amountpaid=self.amountpaid)

		if self.balance!='':
			receipt.set(balance=self.balance)

		if self.paymentmethod!='':
			receipt.set(paymentmethod=self.paymentmethod)
	
	@db_session
	def RemoveReceipt(self,receiptdate,receipttime):
		delete(receipt for receipt in self.ReceiptModel if receipt.receiptdate==receiptdate and receipt.receipttime==receipttime)