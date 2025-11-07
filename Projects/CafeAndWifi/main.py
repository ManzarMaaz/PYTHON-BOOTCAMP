import csv

from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import URL, DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location = StringField("Location URL", validators=[DataRequired(), URL()])
    opening = StringField("Opening Time", validators=[DataRequired()])
    closing = StringField("Closing Time", validators=[DataRequired()])
    coffee = SelectField(
        "Coffee Ratings",
        choices=["✘", "☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
        validators=[DataRequired()],
    )
    wifi = SelectField(
        "Wifi Ratings",
        choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
        validators=[DataRequired()],
    )
    power = SelectField(
        "Power Ratings",
        choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
        validators=[DataRequired()],
    )
    submit = SubmitField("Submit")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["POST", "GET"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open(
            "DAY 62-coffee-and-wifi/cafe-data.csv",
            newline="",
            encoding="utf-8",
            mode="a",
        ) as csv_file:
            new_row = (
                f"\n{form.cafe.data},"
                f"{form.location.data},"
                f"{form.opening.data},"
                f"{form.closing.data},"
                f"{form.coffee.data},"
                f"{form.wifi.data},"
                f"{form.power.data}"
            )
            csv_file.write(new_row)
        return redirect(url_for("cafes"))
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open(
        "DAY 62-coffee-and-wifi/cafe-data.csv", newline="", encoding="utf-8"
    ) as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = [row for row in csv_data]
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
