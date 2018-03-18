# -!- coding: utf-8 -!-
# Main Script.

from flask import Flask, request, session, redirect, url_for, render_template
from flask.ext.cors import CORS

import sys
import json
import urllib
import os
import MySQLdb
import json

reload(sys)
sys.setdefaultencoding("utf-8")

from manager import UserManager

userManager = UserManager()

app = Flask(__name__)
cors = CORS(app)

app.secret_key = 'F12Zr47j\3yXaliejlcxuaiuiouqwioufu19wf/,?KT'

db = MySQLdb.connect("localhost","root","rlawjddnrdlstjdusgksrjsgh","CodeHouse", charset="utf8")

cursor = db.cursor()

@app.route('/')
def mainPage():
    if 'email' in session:
        return redirect(url_for('myPage'))
    else:
        return render_template('index.html')

@app.route('/edit')
def edit():
    if 'email' in session:
        return render_template('User_Info_Edit.html')
    else:
        return redirect(url_for('mainPage'))

@app.route('/myPage')
def myPage():
    if 'email' in session:
        return render_template('MyPage.html')
    else:
        return redirect(url_for('mainPage'))

@app.route('/study/html/<num>')
def htmlStudy(num=None):
    if 'email' in session:
        cursor.execute("SELECT * FROM `HTML` WHERE id = '" + num + "'")
        row = cursor.fetchone()
        title = str(unicode(row[2]))
        desc = str(unicode(row[3]))
        has_coding = row[6]
        next_num = str(int(num) + 1)
        before_num = str(int(num) -1)
        return render_template('Study.html', num=num, title=title, desc=desc, has_coding=has_coding, next_num=next_num, before_num=before_num, subject='html', real_num=num)
    else:
        return redirect(url_for('mainPage'))

@app.route('/coding/html/<num>')
def htmlStudyCoding(num=None):
    if 'email' in session:
        cursor.execute("SELECT * FROM `HTML_Coding` WHERE course_id = '" + num + "'")
        row = cursor.fetchone()
        instruction = str(unicode(row[1]))
        next_num = str(int(num) + 1)
        before_num = str(int(num) -1)
        return render_template('Study_Coding.html', instruction=instruction, next_num=next_num, before_num=before_num, subject='html', maximum='12', real_num=num)
    else:
        return redirect(url_for('mainPage'))

@app.route('/study/css/<num>')
def cssStudy(num=None):
    if 'email' in session:
        cursor.execute("SELECT * FROM `CSS` WHERE id = '" + num + "'")
        row = cursor.fetchone()
        title = str(unicode(row[2]))
        desc = str(unicode(row[3]))
        has_coding = row[6]
        next_num = str(int(num) + 1)
        before_num = str(int(num) -1)
        return render_template('Study.html', num=num, title=title, desc=desc, has_coding=has_coding, next_num=next_num, before_num=before_num, subject='css', real_num=str(int(num)+12))
    else:
        return redirect(url_for('mainPage'))

@app.route('/coding/css/<num>')
def cssStudyCoding(num=None):
    if 'email' in session:
        num = str(int(num)+12)
        cursor.execute("SELECT * FROM `CSS_Coding` WHERE course_id = '" + num + "'")
        row = cursor.fetchone()
        instruction = str(unicode(row[1]))
        num = str(int(num)-12)
        next_num = str(int(num) + 1)
        before_num = str(int(num) -1)
        return render_template('Study_Coding.html', instruction=instruction, next_num=next_num, before_num=before_num, subject='css', maximum='12', real_num=str(int(num)+12))
    else:
        return redirect(url_for('mainPage'))


@app.route('/storage')
def storage():
    if 'email' in session:
        return render_template('code_storage.html')
    else:
        return redirect(url_for('mainPage'))

@app.route('/my_storage')
def my_storage():
    if 'email' in session:
        return render_template('my_storage.html')
    else:
        return redirect(url_for('mainPage'))

@app.route('/course_overview')
def courseOverview():
    return render_template('course_overview.html')

@app.route('/user/register', methods=['POST'])
def register():
	jsonString = urllib.unquote(request.data)
	jsonData = json.loads(jsonString)

	email = jsonData['email']
	password = jsonData['password']
	name = jsonData['name']

	user = userManager.register(email, password, name);

	if user == False:
		return "False"
	else:
		return user.getJson()

@app.route('/user/login', methods=['POST'])
def login():
	jsonString = urllib.unquote(request.data)
	jsonData = json.loads(jsonString)

	email = jsonData['email']
	password = jsonData['password']

	loginUser = userManager.login(email, password)

	if loginUser == False:
		return "False"
	else:
		session['email'] = loginUser.email
		session['name'] = loginUser.name
		return "True"

@app.route('/user/logout', methods=['POST'])
def logout():
    session.pop('email', None)
    session.pop('name', None)
    return "True"

@app.route('/user/me', methods=['POST'])
def me():
	return userManager.getUserInfo(session['email'])

@app.route('/user/process', methods=['POST'])
def process():
    return userManager.getProcessInfo(session['email'])

@app.route('/user/process/front', methods=['POST'])
def frontProcess():
    return userManager.getFrontProcessInfo(session['email'])

@app.route('/user/edit', methods=['POST'])
def editUserInfo():
    if 'email' in session:
        jsonString = urllib.unquote(request.data)
        jsonData = json.loads(jsonString)

        password = jsonData['password']

        editedUser = userManager.edit(password)
        return 'True'
    else:
        return 'no session'

@app.route('/user/isSession', methods=['POST', 'GET'])
def isSession():
    if 'email' in session:
        return "true"
    else:
        return "false"

app.debug = True
app.port = 8080

# 직접 이 파일을 실행했을 때만 서버를
if __name__ == '__main__':
	app.run(host = '0.0.0.0')
