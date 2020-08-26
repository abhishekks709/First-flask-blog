from flask import Flask, render_template
app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("about us")
def harry():
    return render_template('about us.html')

app.run(debug=True)
