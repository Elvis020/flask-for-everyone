from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
 
# SQLite
# DBs
# NoSQL and SQL DB
# SQLAlchemy
 
    #Student('Elvis',19,'male')
    #Student(1,'Elvis',19,'male')
 
 
 
# Configuring the current path of the project
current_path = os.path.abspath(os.path.dirname(__file__))
 
 
app = Flask(__name__)
 
# COnfiguring SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(current_path, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
 
#Model or Entity
class Student(db.Model):
    __tablename__ = 'Student'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    gender = db.Column(db.Text)
 
 
 
    def __init__(self,name:str,age:str,gender:str):
        self.name = name
        self.age = age
        self.gender = gender
 
 
@app.route("/")
def index():
    return "<h1>Getting started with Flask and Databases</h1>"


@app.route("/students")
def get_all_students():
    students = Student.query.all()
    return render_template('students.html',students=students)


@app.route("/students/<string:name>")
def delete_student(name):
    Student.query.filter(Student.name == name).delete(synchronize_session=False)
    remaining_students = Student.query.all()
    db.session.add_all(remaining_students)
    db.session.commit()
    return render_template('students.html',students=remaining_students)






# TODO for Joshua: Write a function to get_all_students under 18
# Write your function here



# TODO for Albert: Write a function to add a student using a form
# Write your function here

@app.route("/students/add", methods=['GET','POST'])
def add_student():
    f = request.form
    name = f['name']
    age = int(f['age'])
    gender = ['','Male','Female',][int(f['gender'])]
    db.session.add(Student(name,age, gender))
    print(f"Adding {f['name']} Age: {f['age']}  Gender: {f['gender']}")
    students = Student.query.all()
    db.session.commit()
    return render_template('students.html',students= students)


# TODO for Nicole: Write a function to get_all_students above 18
# Write your function here


# TODO for Pokuaa: Write a function to get_all_students above 18 but less than 30
# Write your function here


# TODO for Jalilu: Write a function to get_all_female_students
# Write your function here


# TODO for David: Write a function to get_all_male_students
# Write your function here


# TODO for Herbert: Write a function to get_all_male_students above 18
# Write your function here



# TODO for Edem: Write a function to get_all_female_students under 18
# Write your function here



# TODO for Kwabena: Write a function to only a particular student, where the function accepts a name of the student. 
# Write your function here