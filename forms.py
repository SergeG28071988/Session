from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField
from wtforms.validators import DataRequired

class ExamForm(FlaskForm):
    student = StringField('Student', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    teacher = StringField('Teacher', validators=[DataRequired()])
    exam_date = DateField('Exam Date', validators=[DataRequired()])
    result = IntegerField('Result', validators=[DataRequired()])
