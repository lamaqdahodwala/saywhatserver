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
        data[key] = [title, author, story]
        self.write('ok')
        with open('data.json', 'w') as f:
            json.dump(data, f, indent='  ')
        self.write('ok')


class NewPosts(Boilerplate):
    def get(self):
        allposts = dict(json.load(open('data.json')))
        self.write(allposts)

class GetRead(Boilerplate):
    def get(self, id):
        data = json.load(open('data.json'))
        data : dict
        return data[id]
        
def main():
    return Application([
        url(r'/', Home),
        url(r'/newestposts', NewPosts),
        url(r'/post', Post),
        url(r'/read/(.+)', GetRead)
    ])


app = main()
app.listen(5555)
print('server started')
tornado.ioloop.IOLoop.current().start()