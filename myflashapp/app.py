from flask import Flask, render_template

app = Flask(__name__)
# app.debug = True
@app.route('/')
def index():
    return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)
    # testing run server with command >> python app.py
    # you can use line 4 instead of line 9 (debug=True)
