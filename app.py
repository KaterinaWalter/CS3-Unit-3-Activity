import json
from flask import Flask, render_template, request

# Create instance of Flask
app = Flask(__name__)

# Homepage route
@app.route("/")
def index():
    # Declare variables to hold data
    trainer_name = 'Katerina'
    # Pull data from a JSON file
    with open('static/data.json', 'r') as file:
        data_dict = json.load(file)
    # Render index page & pass in data
    return render_template('index.html', trainer=trainer_name, data=data_dict)

# RUN THE APP (or type flask run in terminal)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
