from flask import Flask, render_template,request
app=Flask(__name__)
#set homepage route
@app.route('/')
def index():
    return render_template('index.html')
if __name__=='__main__':
    app.debug=True
    app.run()