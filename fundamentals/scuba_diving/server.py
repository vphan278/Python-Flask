from flask import Flask, request, redirect, session, flash, render_template
app = Flask(__name__)
app.secret_key = "keep it safe"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users", methods = ["POST"])
def create_user():
    print("Got Post Info")
    print(request.form)

    #Creating session variables
    session["id"] = request.form["id"]
    session["username"] = request.form["name"]
    session["useremail"] = request.form["email"]

    #Never render a template on a POST request
    #Instead we will redirect to our index route
    return redirect("/show")

@app.route("/show")
def show_user():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] +=1
    return render_template("show.html", name_on_template = session["username"], email_on_template =session["useremail"])


@app.route("/reset_counter")
def reset_counter():
    session.pop("count")
    return redirect("/show")

@app.route("/reset_session")
def reset_session():
    session.clear()
    return redirect("/")

@app.route("/back_to_page")
def back_page():
    
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)