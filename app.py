import json
from flask import Flask, render_template, request

# Create instance of Flask
app = Flask(__name__)

# Homepage route 
@app.route("/")
def index():
    # Use Python variables to hold data
    pokemon_generation = 1
    # Render index page & pass in data
    return render_template('index.html', generation=pokemon_generation)

# Results page route (after submitting form)
@app.route("/submit", methods=['POST'])
def submit():
    # Get data from HTML form input
    selected_type = request.form.get('type')
    # OPTIONAL: Read data from a JSON file
    with open('static/data.json', 'r') as file:
        data_dict = json.load(file)
    # Pass data into results page
    return render_template("results.html", type=selected_type, data=data_dict)




# RUN THE APP (or type flask run in terminal)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
