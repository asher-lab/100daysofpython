from flask import Flask

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p> This is a paragraph. Gonna input gif: </p>' \
           '<img src="https://media.itsnicethat.com/original_images/giphy_animation_itsnicethat_work_from_home.gif">'

@app.route("/username/<name>/<age>")
def username(name, age):
    return f"<p>Hello, {name}, you are {age} years old!</p>"

# make use of debugger
# converting variable type
@app.route("/error/<name>/<int:age>")
def error(name, age):
    return f"Hello there {name + age}, you are cute!"


if __name__ == '__main__':
    app.run(debug=True)
