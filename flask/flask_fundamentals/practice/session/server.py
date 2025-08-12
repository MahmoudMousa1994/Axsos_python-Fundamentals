from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'PJIXxQhJNM' # set  a secret key for security purposes
# our index rout will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/users', methods = ['POST'])
def creat_user():
    print("got post info")
    # here we add properties to session to stothe name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('show.html', name_on_template=session.get('username'), email_on_template = session.get('useremail'))
if __name__=="__main__":
    app.run(debug = True)