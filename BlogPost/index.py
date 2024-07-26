from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

# flask instance
app = Flask(__name__)

# adding old sql_lite databases 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# adding new mysql databases 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Ninshuti:byasana@localhost/Flasking'

# initialising database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# creating model
class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(25), nullable=False, unique=True)
    favcolor = db.Column(db.String(25))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    # creating a string
    def __repr__(self):
        return '<name %r>' % self.name

    def __init__(self, name, email):
        self.name = name
        self.email = email

# creating secreat key
app.config['SECRET_KEY'] = 'Sdcreat(9)'

# creating a class form
class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    favcolor = StringField('Favorite color', validators=[DataRequired()])
    submit = SubmitField('Ohereza')

# updsating a user

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    form = UserForm()
    name_to_update = users.query.get_or_404(id)
    if request.method == 'POST':
        name_to_update.name = request.form['name']
        name_to_update.email = request.form['email']
        name_to_update.favcolor = request.form['favcolor']
        try:
            db.session.commit()
            flash('Hey that user was updated successfully')
            return render_template('update.html', format=form, names=name_to_update)
        except:
            flash('User wasn\'t updated successfully')
            return render_template('update.html', format=form, names=name_to_update)
    else:
        return render_template('update.html', mode=form, all_user=name_to_update)


# creating a class form
class SampleForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Ohereza')

# creating route/decorator
@app.route('/')

def index():
    _name_ = 'Ndiramiye'
    _isombe_ = ["Isombe","Inyama","Ubunyobwa","Tungurusumu","Igitunguru","Enjoyment"]
    
    return render_template("index.html", _iryambere_=_name_, Isombe=_isombe_)

# 127.0.0.1:5000/user/john
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

# adding a user
@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = users(form.name.data, form.email.data, form.favcolor)
            db.session.add(user)
            db.session.commit()
        name=form.name.data
        form.name.data = ''
        form.email.data = ''
        form.favcolor = ''
        flash('was registered sucessfully')
    our_users = users.query.order_by(users.date_added)
    return render_template('add_user.html', mode = form, names = name, all_user = our_users)


@app.route('/delete/<int:id>')
def delete(id):
    user_to_delete = users.query.get_or_404(id)

    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash('User deleted sucessfully')
    except:
@app.route('/name', methods=['GET','POST'])
def name():
    name = None
    form = SampleForm()

    # validating or updating name
    if form.validate_on_submit():
        name = form.name.data
        form.name.data =''
        flash('Form datum was submitted succesfully')
    return render_template('name.html', names = name, format = form)


# handling client side error
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# handling server side error
@app.errorhandler(500)
def server_side_error(e):
    return render_template("500.html"), 500


"""we have talked about the following jinja filters !!:

    -> capitalise : to capitalise the first character of passed variable.
    -> lower : to lower an intire passed jinja variable.
    -> upper : to capitalise intire passed jinja variable.
    -> safe : execute the tag that comes with the passed jinja variables.
    -> title : to capitalise each word of passed jinja variable.
    -> trim : to remove the tlairing space on end of passed jinja variable.
    -> striptags : to remove the tags that comes with passewed jinja variable.
"""