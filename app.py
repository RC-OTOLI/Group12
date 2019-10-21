from flask import Flask, render_template

app = Flask(__name__)


# app.debug = True
@app.route('/')
@app.route('/login')
def index():
    return render_template('home.html')


@app.route('/TransactionHistory')
def transaction_history():
    return render_template('TransactionHistory.html')


if __name__ == '__main__':
    app.run(debug=True)
    # testing run server with command >> python app.py
    # you can use line 4 instead of line 9 (debug=True)
