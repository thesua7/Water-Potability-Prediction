from flask import Flask, render_template,request
import numpy as np

import predict as pre
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route("/predict",methods = ["POST"])
def test():
    if request.method == "POST":
        int_features = [float(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = pre.wq_prediction(final_features)

        if prediction == 1:
            prediction_text = "Water is likely safe to drink"
        else:
            prediction_text = "Dont drink it"

    return render_template('index.html',final=prediction_text)


# @app.route("/sub",methods = ['POST'])
# def submit():
#     #html->py
#     if request.method == "POST":
#         one = request.form["ph"]
#         two = request.form["hardness"]
#         three = request.form["solids"]
#         four = request.form["chloramines"]
#         five = request.form["sulfate"]
#         six = request.form["conductivity"]
#         seven = request.form["organic_carbon"]
#         eight = request.form["trihalomethanes"]
#         nine = request.form["turbidity"]
#         return render_template('sub.html',one,two,three,four,five,six,seven,eight,nine)

if __name__ == "__main__":
    app.run(debug=True)