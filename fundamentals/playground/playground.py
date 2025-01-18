from flask import Flask, render_template
app = Flask(__name__)



@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/play")
def play():
    return render_template("play.html")


@app.route("/play/<num_of_boxes>")
def block(num_of_boxes):
    repeat = int(num_of_boxes)
    return render_template("play2.html", repeat = repeat)


@app.route("/play/<num_of_boxes>/<color_change>")
def box_color(num_of_boxes,color_change):
    repeat = (int(num_of_boxes))
    colorChange = color_change
    return render_template('play3.html', repeat = repeat, colorChange = colorChange )

if __name__=="__main__":
    app.run(debug=True)