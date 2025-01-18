from flask import Flask, request, redirect, session, flash, render_template
import datetime
app = Flask(__name__)
app.secret_key = "keep it safe"




@app.route("/")
def store():
    return render_template("dojo_fruit.html")

@app.route("/checkout", methods=["POST"])
def summary():
    name=request.form["name"]
    student_id=request.form["student_id"]
    strawberries=request.form["strawberries"]
    raspberries=request.form["raspberries"]
    apples=request.form["apples"]
    oranges=request.form["oranges"]
    bananas=request.form["bananas"]
    count= int(strawberries)+int(raspberries)+int(apples)+int(oranges)+int(bananas)
    now=datetime.datetime.now()
    timestamp=now.strftime("%B %d %Y %I:%M %p")
    print(request.form)
    return render_template("checkout.html", strawberries=strawberries, raspberries=raspberries, apples=apples, oranges=oranges, bananas=bananas, count=count, timestamp=timestamp, name=name, student_id=student_id)

@app.route("/reset_session")
def reset_session():
    session.clear()
    return redirect("/")



if __name__=="__main__":
    
    app.run(debug=True) 