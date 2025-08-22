from flask import Flask ,render_template,session,redirect,request
app = Flask(__name__)

app.secret_key = "123sffssddfsdfsfds"

@app.route('/')
def index():
    if 'name' in session:
        return redirect('/hello')
    return render_template("index.html")
@app.route('/login',methods=['POST'])
def login():
    session['name'] = request.form['name']
    return redirect('/hello')

@app.route('/hello')
def hello():
    name = session['name']
    return f"Hello {name}"

app.run()