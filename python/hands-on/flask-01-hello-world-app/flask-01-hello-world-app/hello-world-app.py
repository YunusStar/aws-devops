from flask import Flask

app = Flask(__name__)

@app.route("/")
def head():
    return "Hello Yunus!"

@app.route('/yunus')
def second():
    return "This is the Yunus's page"

@app.route('/third/subthird')
def third():
    return "This is the subpage of third page"


@app.route("/forth/<string:id>")
def forth(id):
    return f'Id of this page is {id}'

if __name__=='__main__':
    app.run(debug = True)