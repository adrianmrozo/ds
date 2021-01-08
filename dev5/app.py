from flask import Flask, request


app = Flask(__name__)

    
@app.route('/predict/',methods=['GET','POST'])
def predict():
    if (request.method == "POST"):
        pred = "Make a prediction:"
        #How?
        return pred
    else:
        print("hte request wasn't a post, but a get.")
        return 
    
    return pred	
    
if __name__ == '__main__':
  app.run(debug=True)
