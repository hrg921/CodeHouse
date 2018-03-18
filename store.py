# -!- coding: utf-8 -!-

#!/usr/bin/python
import MySQLdb
import json
from flask import session

# Open database connection
db = MySQLdb.connect("localhost","root","rlawjddnrdlstjdusgksrjsgh","CodeHouse", charset="utf8")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# cursor.execute("SELECT VERSION()")
# INSERT INTO `users` (`mail`, `name`, `password`) VALUES ('hrg921@gmail.com', 'hrg921', 'rjsgh12');

from user import User

class UserStore:
	def __init__(self):
		self.users = []

	# 새로운 유저를 추가한다.
	def add(self, user):
		cursor.execute("INSERT INTO `users` (`email`, `name`, `password`) VALUES ('" + user.email + "', '" + user.name + "', '" + user.pw + "')")
		cursor.execute("SELECT * FROM `users` WHERE email = '" + user.email + "'")
		row = cursor.fetchone()
		cursor.execute("INSERT INTO `user_course_circumstances` (`userID`) VALUES (" + str(row[0]) + ")")
		cursor.execute("INSERT INTO `user_front_circumstances` (`userID`) VALUES (" + str(row[0]) + ")")
		db.commit()

	# 해당 이메일과 패스워드를 가진 유저를 찾는다.
	# 정상 작동 확인
	def find(self, email, pw):
		if cursor.execute("SELECT * FROM `users` WHERE email = '" + email + "' AND password = '" + pw + "'"):
			row = cursor.fetchone()
			user = User(row[1], row[3], row[2])
			return user
		else:
			return False

	# 해당 이메일을 가진 유저를 찾는다.
	# 정상 작동 확인
	# Register 함수 보조용이다.
	def emailCheck(self, email):
		if cursor.execute("SELECT * FROM `users` WHERE email = '" + email + "'"):
			row = cursor.fetchone()
			user = User(row[1], row[3], row[2])
			return user
		else:
			return False

	def updatePassword(self, password):
		cursor.execute("UPDATE `users` set `password` = '" + password + "' WHERE `email` = '" + session['email'] + "'")
		db.commit()
		# UPDATE `users` set `password` = 'password' WHERE `email` = session[`email`]

	# returnUserInfo
	# parameter: session['email']
	def returnUserInfo(self, email):
		cursor.execute("SELECT * FROM `users` WHERE email = '" + email + "'")
		row = cursor.fetchone()
		data = {
			'name': str(row[2]),
			'level': row[4],
			'job': row[5],
			'course_ing': row[6],
			'course_ed': row[7],
			'skillcount': row[8]
		}
		return json.dumps(data)

	def returnProcessingInfo(self, email):
		cursor.execute("SELECT * FROM `users` WHERE email = '" + email + "'")
		row = cursor.fetchone()
		row = cursor.execute("SELECT * FROM `user_course_circumstances` WHERE `userID` = " + str(row[0]))
		row = cursor.fetchone()
		data = {
			'front-end': row[1],
			'server': row[2],
			'C-DEV': row[3],
			'DB-MNG': row[4]
		}
		return json.dumps(data)

	def returnFrontProcessingInfo(self, email):
		cursor.execute("SELECT * FROM `users` WHERE email = '" + email + "'")
		row = cursor.fetchone()
		row = cursor.execute("SELECT * FROM `user_front_circumstances` WHERE `userID` = " + str(row[0]))
		row = cursor.fetchone()
		data = {
			'HTML': row[1],
			'CSS': row[2],
			'JS': row[3]
		}
		return json.dumps(data)
# row[1] = email
# row[2] = name
# row[3] = pw

#SELECT * FROM `users` WHERE email = 'hrg921@gmail.com' AND password = 'rjsgh12';
