from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

with app.app_context():
    db.create_all()
# MANAGING LOGIN
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User,user_id)

@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            flash("You need to login instead. You already have an account")
            return redirect(url_for('login'))
        protected_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            name=request.form.get('name'),
            email=request.form.get('email'),
            password=protected_password
        )
        db.session.add(new_user)
        db.session.commit()
        # login_user(new_user)
        return redirect(url_for('secrets'))
    return render_template("register.html", logged_in=current_user.is_authenticated)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if not user:
            flash("Sorry but this email doesn't exist")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash("Wrong password, try again!")
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('secrets'))
    return render_template("login.html", logged_in=current_user.is_authenticated)

@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name, logged_in=True)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/download')
@login_required
def download():
    return send_from_directory(
        'static',
        path="files/cheat_sheet.pdf"
    )

if __name__ == "__main__":
    app.run()


















































# from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# from sqlalchemy import Integer, String
# from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret-key-goes-here'
#
#
# # CREATE DATABASE
#
# class Base(DeclarativeBase):
#     pass
#
#
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# db = SQLAlchemy(model_class=Base)
# db.init_app(app)
#
#
# # CREATE TABLE IN DB
#
# class User(UserMixin,db.Model):
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     email: Mapped[str] = mapped_column(String(100), unique=True)
#     password: Mapped[str] = mapped_column(String(100))
#     name: Mapped[str] = mapped_column(String(1000))
#
#
# with app.app_context():
#     db.create_all()
#
# # MANAGING LOGIN
#
# login_manager = LoginManager()
# login_manager.init_app(app)
#
# # managing login (authentication)
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     return db.get_or_404(User,user_id)
#
#
# @app.route('/')
# def home():
#     return render_template("index.html",logged_in=current_user.is_authenticated)
#
#
# @app.route('/register',methods=['GET','POST'])
# def register():
#     if request.method=='POST':
#         email = request.form.get('email')
#         user = db.session.execute(db.select(User).where(User.email==email)).scalar()
#         if user:
#             flash("You need to login instead. You already have an account")
#             return redirect(url_for('login'))
#         protected_password=generate_password_hash(
#             request.form.get('password'),
#             method='pbkdf2:sha256',
#             salt_length=8
#         )
#         new_user = User(
#             name=request.form.get('name'),
#             email=request.form.get('email'),
#             password=protected_password
#         )
#         db.session.add(new_user)
#         db.session.commit()
#         # login_user(new_user)
#         return redirect(url_for('secrets'))
#     return render_template("register.html",logged_in=current_user.is_authenticated)
#
#
# @app.route('/login',methods=['GET','POST'])
# def login():
#
#     if request.method=='POST':
#         email=request.form.get('email')
#         password=request.form.get('password')
#
#         # user authentication
#
#         result = db.session.execute(db.select(User).where(User.email == email))
#         user = result.scalar()
#         if not user:
#             flash("Sorry but this email doesn't exist")
#             return redirect(url_for('login'))
#         elif not check_password_hash(pwhash=user.password,password=password):
#             flash("Wrong password, try again!")
#             return redirect(url_for('login'))
#         else:
#             login_user(user)
#             return redirect(url_for('secrets'))
#     return render_template("login.html",logged_in=current_user.is_authenticated)
#
#
# @app.route('/secrets')
# @login_required
# def secrets():
#     print(current_user.name)
#     return render_template("secrets.html",name=current_user.name,logged_in=True)
#
#
# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('home'))
#
#
# @app.route('/download')
# @login_required
# def download():
#     return send_from_directory(
#         'static',
#         path="files/cheat_sheet.pdf"
#     )
#
#
# if __name__ == "__main__":
#     app.run()
