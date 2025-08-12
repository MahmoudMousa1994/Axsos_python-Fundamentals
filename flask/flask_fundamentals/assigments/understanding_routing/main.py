from flask import Flask


# main route
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World, this is the understand routing assigment"


#  champion route
@app.route('/champion')
def success():
    return "Champion"

#  say hi route
@app.route('/say/<name>')
def hello(name):
    say_hi=(f"Hi {name}!")
    return say_hi

#  repeat route
@app.route('/repeat/<num>/<name>')
def repeat(num,name):
    num= int(num)
    times = (name + " ") * num

    return times

# error message route
@app.errorhandler(404)
def not_found(e):
    return "Sorry! No response. Try agin."

if __name__=="__main__":
    app.run(debug=True) 