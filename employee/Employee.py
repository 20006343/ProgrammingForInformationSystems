from pony.orm import *

#3. The system should allow for the capture and storage of the relevant employee’s personal information
class Employee:
	def __init__(self,EmployeeModel,connectiondict,authenticationid='',employeename='',email='',phonenumber='',address='',location='',dateofbirth='',category=''):
		self.authenticationid=authenticationid
		self.employeename=employeename
		self.email=email
		self.phonenumber=phonenumber
		self.address=address
		self.location=location
		self.dateofbirth=dateofbirth
		self.category=category
		self.EmployeeModel=EmployeeModel
		self.db=Database()
		self.db.bind(provider=connectiondict['provider'], host=connectiondict['host'], user=connectiondict['user'], passwd=connectiondict['passwd'], db=connectiondict['db'],port=connectiondict['port'])

	# 21.The system should allow the owner to add, update or remove employee information
	@db_session
	def AddEmployee(self):
		employee = self.EmployeeModel(authenticationid=self.authenticationid,employeename=self.employeename,email=self.email,phonenumber=self.phonenumber,address=self.address,location=self.location,dateofbirth=self.dateofbirth,category=self.category)

	@db_session
	def UpdateEmployee(self,employeeid):
		if self.authenticationid!='':
			self.EmployeeModel[employeeid].authenticationid=self.authenticationid
		if self.employeename!='':
			self.EmployeeModel[employeeid].employeename=self.employeename
		if self.email!='':
			self.EmployeeModel[employeeid].email=self.email
		if self.phonenumber!='':
			self.EmployeeModel[employeeid].phonenumber=self.phonenumber
		if self.address!='':
			self.EmployeeModel[employeeid].address=self.address
		if self.location!='':
			self.EmployeeModel[employeeid].location=self.location
		if self.dateofbirth!='':
			self.EmployeeModel[employeeid].dateofbirth=self.dateofbirth
		if self.category!='':
			self.EmployeeModel[employeeid].category=self.category

	@db_session
	def RemoveEmployee(self,employeeid):
		delete(employee for employee in self.EmployeeModel if employee.employeeid == employeeid)