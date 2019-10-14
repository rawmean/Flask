from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

#   export FLASK_APP=myTest.py
#  flask run

# .flaskenv: Environment variables for flask command
# FLASK_APP=myTest.py

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(f'user rated range is {form.range.data}')
        flash(f'Soc = {form.soc.data}, Rated Range = {form.range.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Enter Data', form=form)
