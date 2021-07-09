from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

#file_path = os.path.abspath(os.getcwd())+"\test.db"


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://sql6423797:uunBv5sHVq@sql6.freemysqlhosting.net/sql6423797'
db= SQLAlchemy(app)
class FileContents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/upload',methods=['POST'])
def upload():
    file = request.files['inputFile']
    newFile = FileContents(name=file.filename,data=file.read())
    db.session.add(newFile)
    db.session.commit()
    return "Saved"+file.filename+' to the database'

if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True)