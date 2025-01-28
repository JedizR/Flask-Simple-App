import matplotlib
matplotlib.use('Agg')
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/test/<int:num_1>/<int:num_2>")
def show_squared_num_from_url(num_1, num_2):
    result = int(num_1)**2 + int(num_2)**2
    return render_template('calculator.html', num1=num_1, num2=num_2, result=result)

@app.route("/plot", methods=["GET", "POST"])
def plot():
    if request.method == "POST":
        xleft = int(request.form["xleft"])
        xright = int(request.form["xright"])
        x = np.linspace(xleft, xright, 100)
        y = np.sin(x)
        plt.figure()
        plt.plot(x, y)
        image_name = f"static/images/plot.png"
        plt.savefig(image_name)
        plt.close()
        return render_template("plotter.html", image_path=image_name)
    return render_template("plotter.html")