from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
   return 'Welcome! See your name by adding /hello/name to the URL.'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
   app.run()