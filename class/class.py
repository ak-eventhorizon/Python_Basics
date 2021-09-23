class User:
	"""docstring for User"""

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login = None
		self.login_attempts = 0
		self.privileges = Privileges()

	def set_login(self, login):
		self.login = login

	def get_login(self):
		return self.login

	def get_login_attempts(self):
		return self.login_attempts

	def get_full_name(self):
		return f'{self.first_name} {self.last_name}'

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0


class Privileges:
	"""docstring for Privileges"""
	def __init__(self):
		self.list = ['read', 'wright', 'execute', 'delete', 'none']
		

if __name__ == '__main__':

	new_user = User('Mike', 'Tyulikhov')
	print(new_user.privileges.list[0])
