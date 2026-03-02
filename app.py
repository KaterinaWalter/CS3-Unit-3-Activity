from flask import Flask, render_template, request

# Create instance of Flask
app = Flask(__name__)

# Homepage route
@app.route("/")
def index():
    return render_template("index.html")

# RUN THE APP (or type flask run in terminal)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
