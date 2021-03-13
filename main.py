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
        return key
    def get(self, title, author, content):
        key = self.generate_id()
        data = dict(json.load(open('data.json')))
        


class NewPosts(Boilerplate):
    def get(self):
        allposts = dict(json.load(open('data.json')))
        self.write(allposts)
        
def main():
    return Application([
        url(r'/', Home),
        url(r'/newestposts', NewPosts)
    ])


app = main()
app.listen(5555)
print('server started')
tornado.ioloop.IOLoop.current().start()