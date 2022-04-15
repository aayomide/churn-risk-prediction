# save this as app.py
from flask import Flask, escape, request, render_template,flash
from helper import DateTransformer, predict_test
from helper import predict_test, DateTransformer

import __main__
__main__.DateTransformer = DateTransformer


app = Flask(__name__)
app.secret_key = '8f42f73854b4749e8f48838be5e6502c'  # randomly generated

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/analysis')
def analysis():
    return render_template("churn.html")

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        prediction = predict_test(request.form)
        if prediction > 2:
            flash(f"Churn risk score for this customer is {prediction} out of 5.",'success')
        else:
            flash(f"Churn risk score for this customer is {prediction} out of 5.",'warning')

        return render_template("prediction.html")        

    else:
        return render_template("prediction.html")


if __name__ == "__main__":
    app.run(debug=True)
