from flask import Flask, render_template, request, session, redirect, url_for
import os
import requests
import json
from pprint import pprint

workdir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__,template_folder=workdir)

def followinglister():
	r = requests.get('https://api.instagram.com/v1/users/self/follows?access_token='+session['access_token'])
	data = r.json()
	ret = []
	pprint(data)

	pprint(ret)
	return ret

def followerlister():
	r = requests.get('https://api.instagram.com/v1/users/self/followed-by?access_token='+session['access_token'])
	data = r.json()
	ret = []
	pprint(data)

	pprint(ret)
	return ret

@app.route('/')
@app.route('/index')
def index():
	codeigparam = request.args.get("code")
	if (codeigparam is not None):
		post_fields = {'client_id': '6b6103bbb1054df8a045340f6f12dc47',
			   'client_secret': 'd8675b81e05e4e7fa177a58728557349',
			   'redirect_uri' : 'http://ig.habibiefaried.com',
			   'grant_type' : 'authorization_code',
			   'code': codeigparam}

		r = requests.post("https://api.instagram.com/oauth/access_token",post_fields)
		
		if (r.status_code == 200):
			data = r.json()
			
			session['access_token'] = data['access_token']
			session['full_name'] = data['user']['full_name']
			session['username'] = data['user']['username']
			session['logged_in'] = True

			pprint(data)

			return redirect(url_for('dashboard'))
		else:
			return "Error has occured, please start from beginning"

	else:
		return render_template('index.html')

@app.route('/dashboard')
def dashboard():
	if session.get('logged_in') == True:
		return render_template('main.html',data=session)
	else:
		return redirect('/')

@app.route('/dashboard/bad_friend_detector')
def bad_friend_detector():
	if session.get('logged_in') == True:
		data = followinglister()
		return 'OK'
	else:
		return redirect('/')

if __name__ == '__main__':
	app.secret_key = "!@hads738ehaisdPQLASJ+"
	app.run()
