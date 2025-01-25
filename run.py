from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

# Initialisation de l'application Flask
app = Flask(__name__)

#Configuration de la base de données
app.config.from_object('config.Config')

#Initialisation de SQLAlchemy et de Flask-Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Modèle User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Modèle Task
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Route d'inscription
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'})

# Route de connexion
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    return jsonify({'message': 'Invalid credentials'}), 401

# Route pour ajouter une tâche
@app.route('/tasks', methods=['POST'])
@jwt_required()
def add_task():
    current_user = get_jwt_identity()
    data = request.get_json()
    new_task = Task(title=data['title'], user_id=current_user)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task added'})

# Route pour récupérer les tâches
@app.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    current_user = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=current_user).all()
    return jsonify([{'id': task.id, 'title': task.title, 'done': task.done} for task in tasks])

# Route pour mettre à jour une tâche
@app.route('/tasks/<int:task_id>', methods=['PUT'])
@jwt_required()
def update_task(task_id):
    current_user = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user_id=current_user).first()
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.done = data.get('done', task.done)
    db.session.commit()
    return jsonify({'message': 'Task updated'})

# Route pour supprimer une tâche
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
    current_user = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user_id=current_user).first()
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted'})

if __name__ == '__main__':
    app.run(debug=True)
