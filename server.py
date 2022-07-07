from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', rows=8, cols=8)


@app.route('/4')
def row_4_board():
    return render_template('index.html', rows=8, cols=4)

@app.route('/<string:x>/<string:y>')
def x_by_y_board(x, y):
    return render_template('index.html', rows=int(x), cols=int(y))


@app.route('/<string:x>/<string:y>/<string:col1>/<string:col2>')
def x_by_y_board_color(x, y, col1, col2):
    return render_template('index.html', rows=int(x), cols=int(y), col1=col1, col2=col2)







if __name__ == "__main__":
    app.run(debug=True)

