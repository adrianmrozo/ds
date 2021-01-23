# flask_ngrok_example.py
from flask import Flask, redirect, url_for, render_template, request, send_file
from test import test_new
from main import model

app = Flask(__name__)



@app.route("/")
def welcome():
    output = "<h1>Welcome!</h1><br>Please add '/predict' to your browser line to pick yourself a test image out of the CIFAR-10 test dataset"
    return output

@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        output = '<form action="#" method="post"><p>Pick a number between 1 and 9999, the system will take out of the CIFAR-10 dataset the corresponding picture:</p><p><input type="text" name="nm" /></p><p><input type="submit" value="submit"/></p></form>'
        return output

@app.route("/<usr>")
def user(usr):
    test_data, test_label, pred_label, number = test_new(model, int(usr))
    if pred_label == test_label:
        pred_corr = "correct"
    else:
        pred_corr = "not correct"
    output = "<h1>Welcome!</h1><br>Please find below an overview of the testing.<br><br>You have selected the following image number out of the CIFAR 10 test dataset: " + str(number) + "<br><br>The model predicted the following category of the picture: " + str(pred_label) + "<br><br>The following category is the correct one: " + str(test_label) + "<br><br> Therefore, the prediction was " + pred_corr + "<br><br>Please replace in your browser URL your number and the hashtag and enter '/predict/yourimage' to see your test image, out of the CIFAR 10 test dataset. If it is the second time you are picking and testing a picture, you should reload it again so that your new picture is loaded."
    return output


@app.route('/predict/yourimage')
def get_image():
    filename = 'test.png'
    return send_file(filename, mimetype='image/png')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
