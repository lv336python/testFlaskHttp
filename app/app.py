import json
import os
from flask import Flask, request, render_template

template_dir = os.path.abspath('static/templates')
app = Flask(__name__, template_folder=template_dir)
print(template_dir)


@app.route('/login', methods=['GET', "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]
        return login+password

@app.route('/api/v1/login', methods=["POST"])
def api_login():
    data = json.loads(request.data)

    return json.dumps(data)


@app.route('/', methods=['GET'])
def hello_world_get():
    return 'Hello, World!'
@app.route('/', methods=['POST'])
def hello_world_post():
    return 'Hello, World! Post'


if __name__ == "__main__":
    app.run("localhost", 8000)
