from flask import Flask, render_template, request, redirect, session
import random


app = Flask(__name__)
app.secret_key = 'jWxxBAKym9'
@app.route('/')
def firstPage():
    session['random_num'] = random.randint(1,100)
    print(session['random_num'])
    return render_template("index.html")

@app.route('/takeGuess', methods= ['POST'])
def guess():
    guess = int(request.form['guess'])
    return redirect("/")
if __name__=="__main__":
    app.run(debug = True)