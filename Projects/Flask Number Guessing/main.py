from random import randint

from flask import Flask

app = Flask(__name__)

number = randint(0, 9)


@app.route("/")
def start():
    return (
        '<h1 style="color: purple;">Guess a number between 0 and 9</h1>'
        '<img src="https://media.giphy.com/media/l3vR85PnGsBwu1PFK/giphy.gif">'
    )


@app.route("/<int:input>")
def game(input):
    if 0 <= input <= 9:
        if input == number:
            # 🎉 Correct guess
            return (
                '<h1 style="color: green;">🎯 You got it right!</h1>'
                '<img src="https://media.giphy.com/media/111ebonMs90YLu/giphy.gif">'
            )
        elif input < number:
            # 📉 Too low
            return (
                '<h1 style="color: red;">Too low! Try a higher number 🔺</h1>'
                '<img src="https://media.giphy.com/media/3oEduSbSGpGaRX2Vri/giphy.gif">'
            )
        else:
            # 📈 Too high
            return (
                '<h1 style="color: blue;">Too high! Try a lower number 🔻</h1>'
                '<img src="https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif">'
            )
    else:
        # 🚫 Out of range
        return (
            '<h1 style="color: orange;">Out of Range! Pick between 0 and 9.</h1>'
            '<img src="https://media.giphy.com/media/3ohhwk7cE2E0y2I6t6/giphy.gif">'
        )


if __name__ == "__main__":
    app.run(debug=True)
