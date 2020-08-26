from flask import Flask, render_template
app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/Abhi")
def harry():
    return "Hello Abhi!"

app.run(debug=True)
