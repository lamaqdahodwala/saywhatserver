from tornado.web import Application, url, RequestHandler
import tornado.ioloop
import json
import string
from random import choice



class Boilerplate(RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
    

class Home(Boilerplate):
    def get(self):
        self.write('tumaaro mummi guhno lumbo che')

class Post(Boilerplate):
    def generate_id(self):
        letters = list(string.digits)
        key = ''
        for i in range(50):
            key += str(choice(letters))
        if key in json.load(open('data.json')):
            self.generate_id
        else:
            return key
    def post(self):
        data = self.get_argument('body')    
        title = data[0]
        author = data[1]
        story = data[2]
        key = self.generate_id()
        data = dict(json.load(open('data.json')))
        data[key] = [title, author, content]
        self.write('ok')
        with open('data.json', 'w') as f:
            json.dump(data, f, indent='  ')


class NewPosts(Boilerplate):
    def get(self):
        allposts = dict(json.load(open('data.json')))
        self.write(allposts)
        
def main():
    return Application([
        url(r'/', Home),
        url(r'/newestposts', NewPosts),
        url(r'/post', Post)
    ])


app = main()
app.listen(5555)
print('server started')
tornado.ioloop.IOLoop.current().start()