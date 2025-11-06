from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class MyForm(FlaskForm):
    email = StringField(
        label="Email",
        validators=[DataRequired(), Email(check_deliverability=False)],
    )
    password = PasswordField(
        label="Password", validators=[DataRequired(), Length(min=8)]
    )
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "python123"

boostrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    email_data = form.email.data
    password_data = form.password.data
    if form.validate_on_submit():
        if email_data == "admin@email.com" and password_data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
