from flask import Flask, request


app = Flask('app')

@app.route("/")
def home():
    return ''

@app.route("/newestposts")
def getnewestposts():
    pass


@app.route('/post', methods=['POST'])
def post():
    pass

@app.route("/read/<id>")
def readerview(id):
    pass

@app.after_request
def after_request():
    request.headers['Access-Control-Allow-Origin'] = '*'

app.run('0.0.0.0', port=8080)