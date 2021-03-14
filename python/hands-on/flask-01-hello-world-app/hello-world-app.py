from flask import Flask

app = Flask(__name__)

@app.route("/")
def head():
    return "Hello World!!!"
@app.route("/yunus")
def second():
    return "This is Yunus's page"

@app.route("/third/subthird")
def third():
    return "This is subpage of third page"

if __name__=="__main__":
    app.run(debug = True)