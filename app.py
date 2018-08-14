
# http://flask.pocoo.org/
from flask import Flask
# here's a blank html and it's fill it
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schools.db'
db = SQLAlchemy(app)

# we create a model
class School(db.Model):
  __tablename__ = 'schools'
  __table_args__ = {
    'autoload': True,
    'autoload_with': db.engine
  }
  dbn = db.Column(db.String, primary_key=True)



@app.route("/")
def hello():
    return "Hello World!"


@app.route("/schools/")
def schools():
	schools = School.query.all()
	return render_template("list.html", schools=schools)
# try localhost:5000/shools

@app.route("/school/<dbn>/")
# put dbn
# it works like an function
# we can just put dbn after localhost:5000/school/xxx
def school(dbn):
	# select school, limit 1
	school = School.query.filter_by(dbn=dbn).first()
	return render_template("show.html",school = school)
# try localhost:5000/shool

# @app.route("/search")
# def search():
#   name = request.args.get('query')
#   schools = School.query.filter(School.school_name.contains(name)).all()
#   return render_template("list.html", schools=schools)

# if this is running from the command line
# do somthing
if __name__ == '__main__':
  app.run(debug=True)

 # 在 command line 里open python app.py
 # 打开: localhost:5000

