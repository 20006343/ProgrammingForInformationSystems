from flask import Flask
from employee import Employee

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Api sample"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
