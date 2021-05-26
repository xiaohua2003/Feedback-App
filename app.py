from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app=Flask(__name__)
#connect data base
ENV='dev'
if ENV =='dev':
    app.debug=True
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres2021@localhost/Aritzia'
else:
    app.debug=False
    app.config['SQLALCHEMY_DATABASE_URI']=''
#get warning in the console
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#create database object
db=SQLAlchemy(app)
#create data model/structure
class Feedback(db.Model):
    __tablename__='feedback'
    id=db.Column(db.Integer, primary_key=True)
    customer=db.Column(db.String(200),unique=True)
    address=db.Column(db.String(200))
    rating=db.Column(db.Integer)
    comments=db.Column(db.Text())
    def __init__(self, customer, address, rating, comments):
        self.customer=customer
        self.address=address
        self.rating=rating
        self.comments=comments
#set homepage route
@app.route('/')
def index():
    return render_template('index.html')
#set submit route
@app.route('/submit', methods=['POST'])
def submit():
    if request.method=='POST':
        customer=request.form['customer']
        address=request.form['address']
        rating=request.form['rating']
        comments=request.form['comments']
        print(customer, address, rating, comments)
        if customer=='' or address=='':
            return render_template('index.html', message='please enter required field')
        #access to the database
        if db.session.query(Feedback).filter(Feedback.customer==customer).count()==0:
            data=Feedback(customer, address, rating,comments)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, address, rating, comments)
            return render_template('success.html')
        return render_template('index.html', message='You have already submitted feedback')
if __name__=='__main__':
    
    app.run()