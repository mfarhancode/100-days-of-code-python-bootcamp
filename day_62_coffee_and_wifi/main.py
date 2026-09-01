from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, SelectField, URLField
from wtforms.validators import DataRequired
import csv
from pathlib import Path

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Cafe Location on Google Maps (URL)', validators=[DataRequired()])
    open = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee = SelectField('Coffee Rating', choices=['✘', '☕', '☕☕', '☕☕☕','☕☕☕☕', '☕☕☕☕☕'])
    wifi = SelectField('Wifi Rating', choices=['✘', '💪', '💪💪', '💪💪💪','💪💪💪💪', '💪💪💪💪'])
    power = SelectField('Power Rating', choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌','🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'])
    submit = SubmitField('Submit') 

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        all_values = form.data.values()
        values = list(all_values)[:-2]
        file_path = Path(__file__).parent.joinpath('cafe-data.csv')
        with open(file_path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(values)
        return redirect('/cafes')

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    file_path = Path(__file__).parent.joinpath('cafe-data.csv')
    with open(file_path, newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
