import pickle # Importing the pickle module to load the saved machine learning model

import pandas as pd
#Flask: the main class for creating the web app
# render_template: to render HTML files like index.html
# request: to access user input submitted from the form
from flask import Flask, render_template,request  


model = pickle.load(open('RF_Credit_risk_model.pkl','rb'))


app = Flask(__name__)  #Creating an instance of the Flask web application, __name__ lets Flask know where to look for resources 

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    
    form_data = request.form.to_dict()

    # Check if form data is empty (e.g., on HEAD request or accidental blank POST)
    if not form_data:
        return render_template("index.html")

    try:
        form_inputs = pd.DataFrame([form_data])
        form_inputs = form_inputs.astype(float)  # Ensure numeric
        prediction = model.predict(form_inputs)
        return str(prediction)
    
    except Exception as e:
        # Optional: show an error message on the page instead of crashing
        return f"Error during prediction: {str(e)}"

#@app.route('/', methods=["GET","POST"])   # Defining a route for the home page "/" , Accepts both GET and POST HTTP methods
#def index():
#    
#    # If it's a GET request (page first opens), show the input form (index.html)
#    if request.method=="GET":
#        return render_template("index.html")
#        form_data = request.form.to_dict()
#    else:
#        # If it's a POST request (form is submitted),
#        # collect the form inputs and convert to a DataFrame 
#        form_inputs = pd.DataFrame(request.form.to_dict(),index=[0])  #request.form is a dictionary-like object that holds all the submitted form data. to_dict() is to convert that immutable dict to standard dict 
#        
#        prediction = model.predict(form_inputs.astype('float'))   # Ensure all input data is converted to integer type before prediction
#        
#        return str(prediction)   # Return the prediction as plain text on the web page
#        
        
# Entry point for running the Flask app, Only runs when the script is executed directly (not imported)        
if __name__ == "__main__":
    # Run the Flask app with debug mode ON
    # Debug mode helps show error messages and auto-reloads the app on changes
     app.run(debug=True)