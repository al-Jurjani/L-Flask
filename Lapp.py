from flask import Flask, render_template

app = Flask(__name__)
@app.route('/', methods = ['GET'])

# def hello():
#     return 'As-Salaamu Alaikum! This is my first Flask app!'

def render_home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port = 2100, debug = True)