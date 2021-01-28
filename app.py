from flask import Flask

app = Flask(__name__)
# this is a route that tell flask how to get to this page and display it.
# at the browser when [127.0.0.1:5000/] is entered flask will call upon the 
# "home" python function.
# that "home" python function will then do what ever that is in the return section
# of the function.
# in this case it will return the text " search" & "update" with html tags
# search
# update
@app.route("/")
def home():
    return "<p>search</p> <p>update</p>"

if __name__ == "__main__":
    app.run()