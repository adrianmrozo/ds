from flask import Flask, request

    
@app.route('/predict/',methods=['GET','POST'])
  def predict():
    pred = "Make a prediction:"
    return pred	
    
if __name__ == '__main__':
  app.run(debug=True, port=8080)
