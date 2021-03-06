import socket
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World! Neue Version 2.0"

@app.route('/host')
def hello_host():
    return "Host %s" % socket.gethostname()

@app.route('/<name>')
def hello_name(name):
    return "Hallo %s!" % name

@app.route('/umdrehen/<wort>')
def umderehen(wort):
    s = wort[::-1]
    return "%s" % s

if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True)
