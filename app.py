import matplotlib
matplotlib.use('Agg')
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

def get_function(func_name, x):
   functions = {
       'sin': np.sin(x),
       'cos': np.cos(x),
       'square': x**2,
       'sqrt': np.sqrt(np.abs(x))
   }
   return functions.get(func_name)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/test/<int:num_1>/<int:num_2>")
def show_squared_num_from_url(num_1, num_2):
    result = int(num_1)**2 + int(num_2)**2
    return render_template('calculator.html', num1=num_1, 
                           num2=num_2, result=result)

@app.route("/plot", methods=["GET", "POST"])
def plot():
    if request.method == "POST":
        xleft = int(request.form["xleft"])
        xright = int(request.form["xright"])
        func = request.form["function"]
        x = np.linspace(xleft, xright, 100)
        y = get_function(func, x)
        plt.figure()
        plt.plot(x, y)
        plt.grid(True)
        image_name = f"static/images/plot.png"
        plt.savefig(image_name)
        plt.close()
        return render_template("plotter.html", 
                            image_path=image_name,
                            functions=['sin', 'cos', 'square', 'sqrt'],
                            selected_func=func)
    return render_template("plotter.html", 
                        functions=['sin', 'cos', 'square', 'sqrt'])