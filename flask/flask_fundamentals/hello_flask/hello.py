from flask import Flask  #Iimport Flask to allow us to create our app
app = Flask(__name__)  #creat a new instance of Flask class called "app"
@app.route('/') # the "@" decorator associates this route with the function immediatly
def hello_world():
    return 'Hello World!' # return the string 'Hello World!' as a response

# import statements, maybe some other routes

@app.route('/success')
def success():
    return "success"

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello," + name


if __name__=="__main__": # ensure this file is being run directly and not from a different module
    app.run(debug=True) # run the app in debug mode