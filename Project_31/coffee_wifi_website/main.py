from flask import Flask, render_template,url_for,redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location= StringField(label='location URl', validators=[DataRequired(), URL(require_tld=True)])
    open= StringField(label="Opens at: ", validators=[DataRequired()])
    close = StringField(label="Closes at: ", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
                                validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
                              validators=[DataRequired()])
    power_rating = SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
                               validators=[DataRequired()])

    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST','GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
        with open('cafe-data.csv',mode='a', encoding='utf-8') as f:
            f.write(f'\n{form.cafe.data},{form.location.data},{form.open.data},{form.close.data},'
                    f'{form.coffee_rating.data},{form.wifi_rating.data},{form.power_rating.data}')
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', mode='r' ,newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        len=0
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
            len+=1
    return render_template('cafes.html', cafes=list_of_rows,length=len)


if __name__ == '__main__':
    app.run(port=5001)
