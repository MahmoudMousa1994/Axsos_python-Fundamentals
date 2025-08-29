from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'WdV0yHyDcg'
@app.route('/')
def counter():
    if  'view_count'in session:
        print('view_count exists, increese by 1')
        session['view_count']+= 1
    else:
        print('view_count does not exists, creat one')
        session['view_count'] = 1

    return render_template("index.html", count=session['view_count'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()

    return redirect("/")

@app.route('/add2')
def add2():
    session['view_count'] += 2
    return redirect("/")

@app.route('/addnum', methods=['POST'])
def addnum():
    form_num = request.form['num']
    num = int(form_num) -1
    print(num)
    session['view_count'] += num
    return redirect("/")



if __name__=="__main__":
    app.run(debug = True)
