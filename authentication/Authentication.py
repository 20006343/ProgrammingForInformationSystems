from pony.orm import *

class Authentication:
	def __init__(self,AuthenticationModel,connectiondict,username='',password='',role='',):
		self.username=username
		self.password = password
		self.role = role
		self.AuthenticationModel=AuthenticationModel
		self.db=Database()
		self.db.bind(provider=connectiondict['provider'], host=connectiondict['host'], user=connectiondict['user'], passwd=connectiondict['passwd'], db=connectiondict['db'],port=connectiondict['port'])

	#2. The system should allow the relevant system users to log-in.
	@db_session
	def Login(self,username,password):
		result=""
		user=self.AuthenticationModel.get(username=username,password=password)

		if user==None:
			result='wrong credentials'
		else:
			result={'authid':user.authenticationid,'role':user.role}

		return result
    # 1. The system should allow for the creation of accounts for the relevant system users. 
    # 25. The system should allow the owner to add, update or remove the credentials
	@db_session
	def AddUser(self):
		user = self.AuthenticationModel(username=self.username,password=self.password,role=self.role)

	@db_session
	def UpdateUser(self,authenticationid):
		if self.username!='':
			self.AuthenticationModel[authenticationid].username=self.username
		if self.password!='':
			self.AuthenticationModel[authenticationid].password=self.password
		if self.role!='':
			self.AuthenticationModel[authenticationid].role=self.role

	@db_session
	def RemoveUser(self,authenticationid):
		delete(user for user in self.AuthenticationModel if user.authenticationid == authenticationid)


