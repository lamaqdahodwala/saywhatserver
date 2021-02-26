from flask import Flask, Response, request
from flask_cors  import CORS
from replit import db

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return ''

@app.route('/newestposts')
def newestposts():
    top10 = [db.get(i) for i in range(10)]
    string = str(top10)
    string = string[1:-1]
    resp = Response(string)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp



@app.route('/exists/<key>')
def exists(key):
    if key in list(db.keys()):
        resp = Response('True')
        resp.headers['Access-Control-Allow-Origin'] = '*'
    else:
        resp = Response('False')
        resp.headers['Access-Control-Allow-Origin'] = '*'
    
    return resp


@app.route('/post', methods=['POST'])
def newpost():
    title = request.form['title']
    story = request.form['story']
    if title in list(db.keys()):
        resp = Response('error')
    else:
        db[title] = story
        resp = Response('Success')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp 

app.run('0.0.0.0')