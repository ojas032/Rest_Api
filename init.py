from  flask import Flask
from flask_restful import Resource ,Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app=Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
Migrate(app,db)
api=Api(app)


class Student_db(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name=db.Column(db.String(80),nullable=False)
    age=db.Column(db.Integer,nullable=False)
    std=db.Column(db.String(10),nullable=False)
    def __init__(self,name,age,std):
        self.name=name
        self.age=age
        self.std=std
    def json(self):
        return {'name':self.name,'age':self.age,'std':self.std}    



class Student(Resource):

    def get(self,name,age,std):
        data=Student_db.query.filter_by(name=name,age=age,std=std).first()
        if(data):
            return data.json()
        else:
            return {'name':'none'},404

    def post(self,name,age,std):
        data=Student_db(name=name,age=age,std=std)
        db.session.add(data)
        db.session.commit()
        return {"sent":"success"}
 

api.add_resource(Student,'/student/<name>/<int:age>/<std>')

if __name__=='__main__':
    app.run(debug=True)

