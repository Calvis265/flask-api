from flask import Flask, jsonify, request
from models import db
from models.hero import Hero  # Adjust path if needed

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Initialize DB using a context block (safe with Flask 3.x)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return jsonify({'message': 'Flask Superheroes API running ✅'})

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([
        {'id': hero.id, 'name': hero.name, 'super_name': hero.super_name}
        for hero in heroes
    ])

@app.route('/heroes', methods=['POST'])
def create_hero():
    data = request.get_json()
    new_hero = Hero(name=data['name'], super_name=data['super_name'])
    db.session.add(new_hero)
    db.session.commit()
    return jsonify({
        'id': new_hero.id,
        'name': new_hero.name,
        'super_name': new_hero.super_name
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
