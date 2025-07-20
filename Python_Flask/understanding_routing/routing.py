from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route("/")
def hello_world():
    return "Hello Routing World!!!!!!"


@app.route("/dojo")
def dojo():
    return "dojo!!!"

@app.route("/say/<name>")
def say_flask(name):
    return f"Hi {name}"

@app.route("/repeat/<int:num>/<name>")
def repeat(name , num):
    return f"say: {name * num}"


@app.route("/repeat/<int:num>/<string:name>")
def repeat2(name, num):
    return f"say: {name * num}"





if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.