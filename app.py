from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Define a simple model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

# Create DB tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Hello, Flask + SQLAlchemy!"

if __name__ == '__main__':
    app.run(debug=True)
