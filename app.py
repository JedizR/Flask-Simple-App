import matplotlib
matplotlib.use('Agg')
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

def get_function(func_name, x):
   functions = {
       'sin': (np.sin(x), 'Sin(x)'),
       'cos': (np.cos(x), 'Cos(x)'),
       'square': (x**2, 'x²'),
       'sqrt': (np.sqrt(np.abs(x)), '√|x|'),
       'linear': (x, 'x'),
       'cubic': (x**3, 'x³')
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
    functions = ['sin', 'cos', 'square', 'sqrt', 'linear', 'cubic']
    colors = ['blue', 'red', 'green', 'purple', 'orange', 'brown']
    if request.method == "POST":
        xleft = int(request.form["xleft"])
        xright = int(request.form["xright"])
        selected_funcs = request.form.getlist("functions")
        show_grid = 'grid' in request.form
        plt.figure(figsize=(10, 6))
        x = np.linspace(xleft, xright, 100)
        for i, func in enumerate(selected_funcs):
            y, label = get_function(func, x)
            plt.plot(x, y, label=label, color=colors[i])
        plt.legend()
        plt.title('Selected Functions')
        plt.xlabel('x')
        plt.ylabel('y')
        if show_grid:
            plt.grid(True)
        image_name = f"static/images/plot.png"
        plt.savefig(image_name)
        plt.close()
        return render_template("plotter.html", 
                            image_path=image_name,
                            functions=functions,
                            selected_funcs=selected_funcs,
                            show_grid=show_grid)
    return render_template("plotter.html", functions=functions)