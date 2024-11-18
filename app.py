from flask import Flask, request, render_template
import pandas as pd
import joblib
#git test
#git test3
#git test4
# Declare a Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    
    # If a form is submitted
    if request.method == "POST":
        
        # Unpickle classifier
        #clf = joblib.load("clf.pkl")
        
        # Get values through input bars
        delivery_number = request.form.get("delivery_number")
        #weight = request.form.get("weight")
        
        # Put inputs to dataframe
        #X = pd.DataFrame([[height, weight]], columns = ["Height", "Weight"])
        
        # Get prediction
        prediction = delivery_number
        
    else:
        prediction = ""
        
    return render_template("website.html", output = prediction)

# Running the app
if __name__ == '__main__':
    app.run(debug = True)