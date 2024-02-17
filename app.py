from flask import Flask, render_template, request, url_for, redirect 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from flask_bootstrap import Bootstrap
from  forms import ExamForm


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exams.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'
db = SQLAlchemy(app)


class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    teacher = db.Column(db.String(100), nullable=False)
    exam_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    result = db.Column(db.Integer)



@app.route('/', methods=['POST', 'GET'])
def index():
    form = ExamForm()

    if form.validate_on_submit():
        student = form.student.data
        subject = form.subject.data
        teacher = form.teacher.data
        result = form.result.data

        exam = Exam(student=student, subject=subject, teacher=teacher, result=result)
        db.session.add(exam)
        db.session.commit()
        return redirect(url_for('index'))

    exams = Exam.query.all()
    return render_template('index.html', form=form, exams=exams)


@app.route('/exams/<int:id>')
def exam_detail(id):
    exam =Exam.query.get(id)   
    return render_template("exam_detail.html", exam=exam)



@app.route('/exams/<int:id>/delete')
def exam_delete(id):
    exam = Exam.query.get_or_404(id)

    try:
        db.session.delete(exam)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return "При удалении экзамена произошла ошибка!!!"


@app.route('/exams/<int:id>/update', methods=['POST', 'GET'])
def exam_update(id):    
    exam = Exam.query.get(id)
    form = ExamForm(obj=exam)
    if request.method == 'POST':
        exam.student = request.form['student']
        exam.subject = request.form['subject']
        exam.teacher = request.form['teacher']
        exam.result = request.form['result']   
        try:            
            db.session.commit()
            return redirect(url_for('index'))
        except:
            return "При изменении экзамена  произошла ошибка!!!"
    else:
        
        return render_template("exam_update.html", exam=exam, form=form) 



if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run(debug=True)
