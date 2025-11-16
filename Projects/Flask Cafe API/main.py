import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, Integer, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["GET", "POST"])
def cafe():
    with app.app_context():
        cafe_data = db.session.execute(select(Cafe).order_by(Cafe.id)).scalars().all()
        cafe = random.choice(cafe_data)

        return jsonify(
            cafe={
                "id": cafe.id,
                "name": cafe.name,
                "map_url": cafe.map_url,
                "img_url": cafe.img_url,
                "location": cafe.location,
                "seats": cafe.seats,
                "has_toilet": cafe.has_toilet,
                "has_wifi": cafe.has_wifi,
                "has_sockets": cafe.has_sockets,
                "can_take_calls": cafe.can_take_calls,
                "coffee_price": cafe.coffee_price,
            }
        )


@app.route("/all")
def all_cafes():
    with app.app_context():
        cafe_data = db.session.execute(select(Cafe).order_by(Cafe.id)).scalars().all()
        for cafe in cafe_data:
            return jsonify(
                cafes=[
                    {
                        "id": cafe.id,
                        "name": cafe.name,
                        "map_url": cafe.map_url,
                        "img_url": cafe.img_url,
                        "location": cafe.location,
                        "seats": cafe.seats,
                        "has_toilet": cafe.has_toilet,
                        "has_wifi": cafe.has_wifi,
                        "has_sockets": cafe.has_sockets,
                        "can_take_calls": cafe.can_take_calls,
                        "coffee_price": cafe.coffee_price,
                    }
                    for cafe in cafe_data
                ]
            )


@app.route("/search", methods=["POST", "GET"])
def search():
    with app.app_context():
        loc = request.args.get("loc")
        cafe = db.session.execute(
            select(Cafe).where(Cafe.location == loc.title())
        ).scalar()
        if cafe:
            return jsonify(
                cafe={
                    "id": cafe.id,
                    "name": cafe.name,
                    "map_url": cafe.map_url,
                    "img_url": cafe.img_url,
                    "location": cafe.location,
                    "seats": cafe.seats,
                    "has_toilet": cafe.has_toilet,
                    "has_wifi": cafe.has_wifi,
                    "has_sockets": cafe.has_sockets,
                    "can_take_calls": cafe.can_take_calls,
                    "coffee_price": cafe.coffee_price,
                }
            )
        else:
            return jsonify(error="Sorry, We didn't found the Location")


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update(cafe_id):
    with app.app_context():
        new_price = request.args.get("new_price")
        try:
            cafe = db.session.execute(select(Cafe).where(Cafe.id == cafe_id)).scalar()
            if cafe:
                cafe.coffee_price = new_price
                db.session.commit()
                return jsonify(success="Successfully updated the price.")
        except Exception:
            return jsonify(
                error={
                    "Not Found": "Sorry a cafe with that id was not found in the database."
                }
            )


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    with app.app_context():
        api_key = request.args.get("api_key")
        if api_key == "TopSecretAPIKey":
            try:
                cafe_to_delete = db.get_or_404(Cafe, cafe_id)
            except Exception:
                return jsonify(
                    error={
                        "Not Found": "Sorry a cafe with that id was not found in the database."
                    }
                ), 404
            else:
                db.session.delete(cafe_to_delete)
                db.session.commit()

                return jsonify(
                    response={
                        "success": "Successfully deleted the cafe from the database."
                    }
                ), 200
        else:
            return jsonify(
                error={
                    "Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."
                }
            ), 403


if __name__ == "__main__":
    app.run(debug=True, port=5001, use_reloader=True)
