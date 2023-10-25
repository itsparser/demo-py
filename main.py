from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/ping")
def ping_pong():
    return "Pong !!!"


@app.route("/greeting/", methods=['POST'])
def greeting():
    body = request.get_json()

    return {"Message": f"Welcome {body['Name']}"}


if __name__ == "__main__":
    app.run()
