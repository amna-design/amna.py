
from flask import Flask, redirect,url_for,request
app = Flask(__name__)
@app.route('/success/<name>')
def success(name):
    return 'welcome ' %name
app.route('\login',methods= ['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['mn']
        return redirect(url_for('success',name=user))
    else:
        user = request.args.__get('mn')
        return  redirect(url_for('success',name = user))
if __name__  == ' __main__ ':
    app.run(debug = True)
