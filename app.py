from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
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
        if customer=='' or address=='':
            return render_template('index.html', message='please enter required field')
        print(customer, address, rating, comments)
        return render_template('success.html')
if __name__=='__main__':
    app.debug=True
    app.run()