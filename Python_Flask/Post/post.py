from flask import Flask , render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route("/")
def index():
    return render_template("index.html")





if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode. 
    #app.run(debug=True, host="localhost", port=8000)


















if __name__ == "__main__":
    app.run(debug=True)
    #app.run(debug=True, host="localhost", port=8000)
