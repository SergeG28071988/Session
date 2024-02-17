from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from flask_bootstrap import Bootstrap
from  forms import ExamForm


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exams.db'
db = SQLAlchemy(app)


class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    teacher = db.Column(db.String(100), nullable=False)
    exam_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    result = db.Column(db.Integer)



@app.route('/')
def index():
    return "Hello, я Лапоть!"


if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run(debug=True)
    