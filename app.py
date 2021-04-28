from flask import Flask, render_template, flash, redirect, request, session, logging, url_for

from flask_sqlalchemy import SQLAlchemy

from forms import LoginForm, RegisterForm, TransValidateForm, ValidateForm

from werkzeug.security import generate_password_hash, check_password_hash
import pymysql as MySQLdb

import predict



app = Flask(__name__)

app.config['SECRET_KEY'] = '!9m@S-dThyIlW[pHQbN^'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/test'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



class User(db.Model):

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)

    name= db.Column(db.String(15), unique=True)

    username = db.Column(db.String(15), unique=True)

    email = db.Column(db.String(50), unique=True)

    password = db.Column(db.String(256), unique=True)

    role = db.Column(db.String(256), server_default="member" )

@app.route('/', methods = ['GET', 'POST'])
def home():

    session['logged_in'] = True

    session['email'] = "perezogayo@gmail.com" 

    session['username'] = "Guest"

    session['role'] = "Validator"

    lang_iso_map={
    "luo" : "Dholuo",
    "ach" : "Acholi",
    "adh" : "Adhola"
    }

    if request.method == 'POST':
        data= request.form['text-message']
        source=request.form['source']
        target=request.form['target']

        lang={}

        if source=="en":
            lang['source'] = "English"
            lang["target"] = lang_iso_map[target]

        else:
            lang['source'] = lang_iso_map[source]
            lang["target"] = "English"

        results=predict.return_results(data, source, target)

        return render_template('index.html',
                                     original_input=data,           
                                     result=results,
                                     lang=lang
                                     )


    return render_template('index.html')

@app.route('/login/', methods = ['GET', 'POST'])
def login():

    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate:

        user = User.query.filter_by(email = form.email.data).first()

        if user:

            if check_password_hash(user.password, form.password.data):

                flash('You have successfully logged in.', "success")
                
                session['logged_in'] = True

                session['email'] = user.email 

                session['username'] = user.username

                session['role'] = user.role

                return redirect(url_for('home'))

            else:

                flash('Username or Password Incorrect', "Danger")

                return redirect(url_for('login'))

    return render_template('login.html', form = form)


@app.route('/register/', methods = ['GET', 'POST'])

def register():
    
    form = RegisterForm(request.form)
    
    if request.method == 'POST' and form.validate():
    
        hashed_password = generate_password_hash(form.password.data, method='sha256')
    
        new_user = User(
            
            name = form.name.data, 
            
            username = form.username.data, 
            
            email = form.email.data, 
            
            password = hashed_password)
    
        db.session.add(new_user)
    
        db.session.commit()
    
        flash('You have successfully registered', 'success')
    
        return redirect(url_for('login'))
    
    else:
    
        return render_template('register.html', form = form)

@app.route('/logout/')
def logout():
    
    session['logged_in'] = False

    return redirect(url_for('home'))

@app.route('/predict/', methods = ['GET', 'POST'])


@app.route('/trans-valid/', methods = ['GET', 'POST'])
def transValid():

    form = TransValidateForm(request.form)

    if request.method == 'POST' and form.validate:

        user = User.query.filter_by(email = session['email']).first()

        if user:

            user.role=form.example.data
            session['role']=form.example.data
            db.session.commit()
            return redirect(url_for('home'))

    return render_template('trans-validate.html', form = form)


@app.route('/translate/', methods = ['GET', 'POST'])
def translate():

    form = TransValidateForm(request.form)

    if request.method == 'POST' and form.validate:

        user = User.query.filter_by(email = session['email']).first()

        if user:

            user.role=form.example.data
            db.session.commit()
            return redirect(url_for('home'))

    return render_template('translate.html', form = form)

@app.route('/validate/', methods = ['GET', 'POST'])
def validate():

    form = ValidateForm(request.form)

    if request.method == 'POST' and form.validate:

        user = User.query.filter_by(email = session['email']).first()

        if user:

            valid=form.isValid.data
            db.session.commit()
            return redirect(url_for('home'))

    return render_template('validate.html', form = form)


if __name__ == '__main__':
    
    db.create_all()
    
    app.run()


