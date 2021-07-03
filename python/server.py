from flask import Flask
server = Flask(__name__)


@server.route("/")
def index():
    return "Index"


@server.route("/hello/<str:temp>")
def hello(temp):
    return "Hello World! %s" % temp


if __name__ == "__main__":
    server.run(host='0.0.0.0')
