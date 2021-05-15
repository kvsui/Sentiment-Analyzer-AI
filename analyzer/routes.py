from flask import render_template, url_for, flash, redirect, request
from analyzer import app, db, bcrypt
from analyzer.forms import RegistrationForm, LoginForm
from analyzer.models import User, Hashtag, Tweet
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import exc
import sqlite3

@app.route("/")
@app.route("/home")
def home():
    return render_template('Home.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)



@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

#Section from hashtag routes
@app.route('/hashtag', methods = ['GET','POST'])
def dashboard():
    return render_template("index.html")

@app.route('/hashtag/all', methods=['GET'])
def selectAllHashtag():
    result = Hashtag.query.all()
    return json.dumps(result, cls=AlchemyEncoder)

@app.route('/hashtag/insert', methods=['POST'])
def insertHashtag():
    hashtag = request.form['hashtag']
    new_data = Hashtag(hashtag=hashtag)
    db.session.add(new_data)
    db.session.commit()
    return json.dumps({"status":1})
    
@app.route('/hashtag/delete', methods=['POST'])
def deleteHashtag():
    id = request.form['id']
    hashtag = Hashtag.query.get(id)
    db.session.delete(hashtag)
    db.session.commit()
    return json.dumps({"status":1})

# Section for Twitter Routes



