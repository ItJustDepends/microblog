from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Samuel'} # fake user
	return render_template('index.html',
							user=user)

