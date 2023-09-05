from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drinks.db'
db = SQLAlchemy()
db.init_app(app)


class Drinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"Drink : ('{self.name}', '{self.description}')"

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return "Hello World"


@app.route('/drinks')
def get_drinks():
    result = db.session.execute(db.select(Drinks))
    all_drinks = result.scalars().all()
    return jsonify(drinks=[drink.to_dict() for drink in all_drinks])


@app.route('/drinks/<int:id>')
def get_drink(id):
    drink = db.get_or_404(Drinks, id)
    return jsonify(drink=drink.to_dict())


@app.route('/drinks', methods=['POST'])
def add_drink():
    new_drink = Drinks(
        name=request.json['name'],
        description=request.json['description']
    )
    db.session.add(new_drink)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new drink."})


@app.route('/drinks/<int:id>', methods=['DELETE'])
def delete_drink(id):
    drink = db.get_or_404(Drinks, id)
    if drink:
        db.session.delete(drink)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted the drink from the database."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a drink with that id was not found in the database."}), 404

if __name__ == "__main__":
    app.run(debug=True)
