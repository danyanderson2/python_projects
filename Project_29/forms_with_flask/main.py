from flask import Flask, render_template,request
from wtforms import StringField, PasswordField,SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Email,Length
from flask_bootstrap import Bootstrap5
# import werkzeug, wtforms,flask_bootstrap  # All these dependencies installed from requirement.txt
# new class to instantiate all forms

class Myform(FlaskForm): #inherits from FlaskForm
    # add all desired fields
    name     = StringField('name')
    email    = StringField(label='email',validators=[DataRequired()])
    password = PasswordField(label='password',validators=[DataRequired(),Length(min=8,message="Password is too short")])
    submit   = SubmitField(label='Log In')
app = Flask(__name__)
app.secret_key="Secret string"
bootstrap=Bootstrap5(app)
@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login",methods=['POST','GET'])
def login():
   login_form=Myform()   #instantiate my custom form
   if login_form.validate_on_submit():
        if login_form.email.data=='admin@email.com' and login_form.password.data =='123456789':
            return render_template('success.html')
        else:
             return render_template('denied.html')
   return render_template('login.html', login_form=login_form)


if __name__ == '__main__':
    app.run(port=5001)
