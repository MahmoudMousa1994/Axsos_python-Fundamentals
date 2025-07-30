from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def  main_page():
    return "<h1>Welcome This is the main page for my playground</h1>"

@app.route('/play')
def level1():
    # boxs_num = int(num)
    # boxs_color = color
    return render_template("index.html", boxs_num = 3, boxs_color = '#9fc5f8')

@app.route('/play/<num>')
def level2(num):
    boxs_num = int(num)
    # boxs_color = color
    return render_template("index.html", boxs_num = boxs_num, boxs_color = '#9fc5f8')


@app.route('/play/<num>/<color>')
def level3(num, color):
    boxs_num = int(num)
    boxs_color = color
    return render_template("index.html", boxs_num = boxs_num, boxs_color = boxs_color)

if __name__=="__main__":
    app.run(debug=True)