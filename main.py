from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test/<int:num_1>/<int:num_2>")
def show_squared_num_from_url(num_1, num_2):
    return f"({int(num_1)}^2) + ({int(num_2)}^2) = {int(num_1)**2 + int(num_2)**2}</p>"