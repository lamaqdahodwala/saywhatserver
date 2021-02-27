from flask import Flask, Response, request
from flask_cors import CORS
import json
from threading import Thread

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return ''


def savetojson():
    with open('db.json', 'w') as f:
        json.dump(db, f)


db = json.load(open('db.json'))
print(db)
Thread(target=savetojson).start()
@app.route('/newestposts')
def newestposts():
    top10 = {}
    for i in range(10):
        try:
            key = list(db.keys())[i]
            val = dict(db)[key]
            top10[i] = [key, val]
        except IndexError:
            top10[i] = "null"
    string = str(top10)
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
    data = request.get_json()
    title = data['title']
    story = data['story']
    author = data['author']
    if title in list(db.keys()):
        resp = Response('error')
    else:
        db[title] = [author, story]
        resp = Response('Success')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


app.run('0.0.0.0')
