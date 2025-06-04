import pickle # Importing the pickle module to load the saved machine learning model

import pandas as pd

#Flask: the main class for creating the web app
# render_template: to render HTML files like index.html
# request: to access user input submitted from the form
from flask import Flask, render_template,request  


model = pickle.load(open('RF_Credit_risk_model.pkl','rb'))


app = Flask(__name__)  #Creating an instance of the Flask web application, __name__ lets Flask know where to look for resources 

@app.route('/', methods=["GET", "POST"])  # Defining a route for the home page "/" , Accepts both GET and POST HTTP methods
def index():
    if request.method == "GET":
        return render_template("index.html")
    
    form_data = request.form.to_dict()   #request.form is a dictionary-like object that holds all the submitted form data. to_dict() is to convert that immutable dict to standard dict 

    # If form_data is empty, show the form again
    if not form_data:
        return render_template("index.html")
    # Otherwise, make prediction
    form_inputs = pd.DataFrame([form_data])
    form_inputs = form_inputs.astype(float)  # # Ensure all input data is converted to integer type before prediction
    prediction = model.predict(form_inputs)
    return str(prediction)        # Return the prediction as plain text on the web page
    
        
# Entry point for running the Flask app, Only runs when the script is executed directly (not imported)        
if __name__ == "__main__":
    # Run the Flask app with debug mode ON
    # Debug mode helps show error messages and auto-reloads the app on changes
     app.run(debug=True)