from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from flask_bootstrap import Bootstrap5

MOVIE_DB_URL='https://api.themoviedb.org/3/search/movie'
MOVIE_DB_DETAILS_URL='https://api.themoviedb.org/3/movie/{movie_id}'
API_KEY='0ae6d3ea523836597cb1a17616007bf0'
MOVIE_IMG_URL="https://image.tmdb.org/t/p/w500"
'''
On Windows type:
python -m pip install -r requirements.txt
'''
# THE RATE MOVIE FORM
class RateMovie(FlaskForm):
    review=StringField('New Review: ')
    rating=StringField("New rating: ", [DataRequired()])
    submit=SubmitField('Done')

# THE ADD MOVIE FORM
class AddForm(FlaskForm):
    title=StringField('Movie Title')
    submit=SubmitField('Done')

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB a local file, single directory level away from my python file
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///movie.db'
class Base(DeclarativeBase):  # Base inherits from DeclarativeBase parent class. Base is used to initialize database
    pass

db=SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

# Create table
with app.app_context():
    db.create_all()

# NEW RECORD TO TABLE: This method favors adding records manually either via website form or directly via DBMS DBViewer

first_movie=Movie(
    title="The last of us",
    year=2002,
    description="The best movie ever imagined by mankind",
    rating=8.5,
    ranking=5,
    review="Nothing more to say",
    img_url='https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg'
)

second_movie = Movie(
    id=3,
    title="Avatar The Way of Water2",
    year=2022,
    description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    rating=7.3,
    ranking=9,
    review="I liked the water.",
    img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
)

# with app.app_context():
#     db.session.add(first_movie)
#     db.session.commit()
@app.route("/")
def home():
    # get hold of data from database(reading data from database)
    movies=db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all() # we order by rating
    for i in range(len(movies)):
        movies[i].ranking=len(movies)-i
    db.session.commit()
    return render_template("index.html",movies=movies)
@app.route('/edit',methods=['GET','POST'])
def edit():
    quick_form=RateMovie()
    movie_id=request.args.get("id")
    movie=db.get_or_404(Movie,movie_id)
    if quick_form.validate_on_submit():
        movie.rating=float(quick_form.rating.data)
        movie.review=quick_form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html',form=quick_form,movie=movie)
@app.route('/delete')
def delete():
    movie_id=request.args.get('id')
    movie=db.get_or_404(Movie,movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))
@app.route("/add",methods=['GET','POST'])
def add():
    add_form=AddForm()
    if add_form.validate_on_submit():
        movie_title = add_form.title.data
        response = requests.get(MOVIE_DB_URL,
                                params={"api_key": API_KEY, "query": movie_title})
        data = response.json()['results']
        return render_template('select.html',options=data)

    return render_template(template_name_or_list='add.html',form=add_form)

@app.route('/find') # enables a user to
def found():
    movie_id_api=request.args.get('id') # id of clicked movie
    if movie_id_api: # movie's id as provided after clicked
            movie_request_endpoint=f'{MOVIE_DB_DETAILS_URL}/{movie_id_api}'
            response=requests.get(movie_request_endpoint,params={"api_key":API_KEY,"language": "en-US"})
            movie_data=response.json()
            new_movie=Movie(
                title=movie_data["title"],
                # The data in release_date includes month and day, we will want to get rid of.
                year=movie_data["release_date"].split("-")[0],
                img_url=f"{movie_data['poster_path']}",
                description=movie_data["overview"]
            )
            db.session.add(new_movie)
            db.session.commit()
            return redirect(url_for(endpoint='edit',id=new_movie.id))


if __name__ == '__main__':
    app.run()


