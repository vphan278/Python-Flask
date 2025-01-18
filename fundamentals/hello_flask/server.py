from flask import Flask , render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/change")
def change():
    return "You changed a different page"

@app.route("/Hello/<name>")
def Hello(name):
    return f"Hello {name}"
    #return "Hello, " + name
    

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

#Type Converters
# Here the second parameter is cast into an integer before being passed to the function
@app.route('/hello/<name>/<int:num>') 
def hello(name, num):
    #return f"Hello, {name * num}"
    return render_template("hello.html", name = name, num =num)

@app.route("/say/age/<int:age>")
def sasy_age(age):
    return f"You are {age}"

@app.route("/addtwo/<int:first>/<int:second>")
def add_two(first, second):
    return f"The sum is: {first + second}."

@app.route("/lists")
def render_lists():
    student_info = [
        {"name": "Michael", "age" : 35},
        {"name": "John", "age" : 30},
        {"name": "Mark", "age" : 25},
        {"name": "KB", "age" : 27},
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)
    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode. 
    #app.run(debug=True, host="localhost", port=8000)



    