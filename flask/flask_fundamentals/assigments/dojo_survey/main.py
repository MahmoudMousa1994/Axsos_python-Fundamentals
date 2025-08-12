from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index rout will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def creat_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    gender_from_form = request.form['gender']
    location_from_form = request.form['location']
    favorite_language = request.form['favorite_language']
    comment_from_form = request.form['comment']
    receive_email_from_form = request.form['accept']
    return render_template("show.html", name_on_template=name_from_form, location_on_template = location_from_form, favorite_language_on_template=favorite_language, comment_on_template = comment_from_form, gender_on_template = gender_from_form, receive_email_on_template = receive_email_from_form )
if __name__=="__main__":
    app.run(debug = True)