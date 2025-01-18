from flask import Flask, redirect, render_template, request, session, flash

app = Flask(__name__)
app.secret_key = "1db282c8fe829694ad4f19eb875d4046f8eaf4174e8e3beb1bf2bd332ecc26f9"


@app.get("/")
def index():
    """This is the root route."""

    return render_template("index.html")


@app.post("/process")
def process():
    """This function processes the username form."""

    print(request.form)
    session["username"] = request.form["username"]
    session["fruit"] = "banana"
    return redirect("/success")


@app.get("/success")
def success():
    """This route displays the username."""

    return render_template("success.html")


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode. 
    #app.run(debug=True, host="localhost", port=8000)