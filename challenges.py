from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms import validators
from wtforms.validators import Required, Email

import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.debug = True

@app.route('/')
def home():
    return "Hello, world!"

#create class to represent WTForm that inherits flask form
class ItunesForm(FlaskForm):
    artist = StringField('What is the artist name?', validators=[Required()])
    number = IntegerField('What is the number of results that iTunes API should return?', validators=[Required()])
    email = StringField('What is the user email?', validators=[Required(), Email()])
    submit = SubmitField('Submit')

@app.route('/itunes-form')
def itunes_form():
    #what code goes here?
    itunes_form = ItunesForm()
    return render_template('itunes-form.html', form=itunes_form) # HINT : create itunes-form.html to represent the form defined in your class

@app.route('/itunes-result', methods = ['GET', 'POST'])
def itunes_result():
    #what code goes here?
    form = ItunesForm(request.form)
    params = {}
    if request.method == 'POST' and form.validate_on_submit():
        params['term'] = form.artist.data
        params['limit'] = form.apires.data
        response = requests.get('https://itunes.apple.com/search?', params = params)
        response_text = json.loads(response.text)
        result_py response_text['results']
        return render_template('itunes-result.html', result_html = result_py)
    # HINT : create itunes-results.html to represent the results and return it
    flash('All fields are required!')
    return redirect(url_for('itunes_form')) #this redirects you to itunes_form if there are errors

if __name__ == '__main__':
    app.run()
