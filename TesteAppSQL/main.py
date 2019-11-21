from flask import Flask
from flask import render_template
from flask import request
import models as dbHandler

app = Flask(__name__)


@app.route('/teste', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        dbHandler.insertUser(username)
        users = dbHandler.retrieveUsers()
        return render_template('index.html', users=users)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
