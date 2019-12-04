from app import app
from app import db

if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)
    # testing run server with command >> python app.py
    # you can use line 4 instead of line 9 (debug=True)