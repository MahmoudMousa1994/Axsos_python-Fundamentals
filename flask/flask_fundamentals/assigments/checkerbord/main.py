from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checker_standerd():
    return render_template('index.html', rows=8, cols=8, color1='#fef5d9', color2 = '#657039')


@app.route('/<row_num>')
def checker_row(row_num):
    rows = int(row_num)
    return render_template('index.html', rows=rows, cols=8, color1='#fef5d9', color2 = '#657039')

@app.route('/<row_num>/<cols_num>')
def checker_row_cols(row_num,cols_num):
    rows = int(row_num)
    cols = int(cols_num)
    return render_template('index.html', rows=rows, cols=cols, color1='#fef5d9', color2 = '#657039')

@app.route('/<row_num>/<cols_num>/<color1>/<color2>')
def checker_row_cols_colors(row_num,cols_num,color1,color2):
    rows = int(row_num)
    cols = int(cols_num)
    color1 = color1
    color2 = color2
    return render_template('index.html', rows=rows, cols=cols, color1=color1, color2 = color2)




if __name__=="__main__":
    app.run(debug=True)