from flask import Flask, render_template, request, session
import os
import requests
import json

workdir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__,template_folder=workdir)

@app.route('/')
def mainPage():
	codeigparam = request.args.get("code")
	if (codeigparam is not None):
		post_fields = {'client_id': '6b6103bbb1054df8a045340f6f12dc47',
			   'client_secret': 'd8675b81e05e4e7fa177a58728557349',
			   'redirect_uri' : 'http://ig.habibiefaried.com',
			   'grant_type' : 'authorization_code',
			   'code': codeigparam}

		r = requests.post("https://api.instagram.com/oauth/access_token",post_fields)
		data = r.json()
		
		session['access_token'] = data['access_token']
		session['full_name'] = data['user']['full_name']
		session['username'] = data['user']['username']

		return render_template('main.html',data=session)

	else:
		return render_template('index.html')

if __name__ == '__main__':
	app.secret_key = '1239dasHAUHS123&#L!'
	app.run()