# -!- coding: utf-8 -!-

from store import UserStore
from user import User

class UserManager:
	def __init__(self):
		self.users = UserStore()

	# 로그인
	def login(self, email, password):
		user = self.users.find(email, password)
		return user

	# 회원가입
	def register(self, email, password, name):
		if self.users.emailCheck(email) != False:
			return False
		newUser = User(email, password, name)
		self.users.add(newUser)
		self.currentUser = newUser
		return newUser

	# 비밀번호 수정
	def edit(self, password):
		self.users.updatePassword(password)

	# 로그아웃
	def logout(self):
		self.currentUser = None

	def getUserInfo(self, email):
		return self.users.returnUserInfo(email)

	def getProcessInfo(self, email):
		return self.users.returnProcessingInfo(email)

	def getFrontProcessInfo(self, email):
		return self.users.returnFrontProcessingInfo(email)
