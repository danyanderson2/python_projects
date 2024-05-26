import datetime

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor, CKEditorField
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from datetime import date


# MY FLASK FORM FOR CREATING NEW BLOGS
class my_form(FlaskForm):
    title=StringField(name='Blog Post Title',validators=[DataRequired()])
    subtitle=StringField(name='Subtitle',validators=[DataRequired()])
    author=StringField(name='Your name',validators=[DataRequired()])
    blog_image_url=StringField('Image URL',validators=[DataRequired(), URL()])
    content=CKEditorField('Blog Content', validators=[DataRequired()])
    submit=SubmitField('Submit Post')


class CreatePostForm(my_form):
    pass


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
ckeditor=CKEditor()
ckeditor.init_app(app)
# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    posts = []
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts=db.session.execute(db.select(BlogPost).order_by(BlogPost.id)).scalars().all()
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/<post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post=db.get_or_404(BlogPost,post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=['GET','POST'])
def create_new_post():
    form=my_form()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            img_url=form.blog_image_url.data,
            body=form.content.data,
            date=date.today().strftime("%B  %d, %Y"),
            author="Dany Anderson"
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))

    return render_template('make-post.html',form=form)


# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<id>',methods=['POST','GET'])
def edit_post(id):
    blog_post=db.get_or_404(BlogPost,id)
    date=blog_post.date
    title=blog_post.title
    edit_form = CreatePostForm(
        title=blog_post.title,
        subtitle=blog_post.subtitle,
        img_url=blog_post.img_url,
        author=blog_post.author,
        body=blog_post.body
    )
    if edit_form.validate_on_submit():
        blog_post.title=edit_form.title.data
        blog_post.subtitle=edit_form.subtitle.data
        blog_post.img_url=edit_form.blog_image_url.data
        blog_post.author="Dany Anderson"
        blog_post.date=date
        db.session.commit()
        return redirect(url_for('show_post',post_id=blog_post.id))
    return render_template('make-post.html',title=title,form=edit_form,coming_to_edit=True)

# TODO: delete_post() to remove a blog post from the database

@app.route('/delete/<id>')
def delete_post(id):
    blog_post=db.get_or_404(BlogPost,id)
    db.session.delete(blog_post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run()
get_all_posts()
