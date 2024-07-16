from flask import Flask, render_template

# flask instance
app = Flask(__name__)
"""we have talked about the following jinja filters !!:

    -> capitalise : to capitalise the first character of passed variable.
    -> lower : to lower an intire passed jinja variable.
    -> upper : to capitalise intire passed jinja variable.
    -> safe : execute the tag that comes with the passed jinja variables.
    -> title : to capitalise each word of passed jinja variable.
    -> trim : to remove the tlairing space on end of passed jinja variable.
    -> striptags : to remove the tags that comes with passewed jinja variable.
"""
# creating route/decorator
@app.route('/')

def index():
    _name_ = 'Ndiramiye'
    _isombe_ = ["Isombe","Inyama","Ubunyobwa","Tungurusumu","Igitunguru","Enjoyment"]
    
    return render_template("index.html",
    _iryambere_=_name_,
    Isombe=_isombe_
    )
# 127.0.0.1:5000/user/john
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

# handling client side error
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# handling server side error
@app.errorhandler(500)
def server_side_error(e):
    return render_template("500.html"), 500