from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    first = "This is my first conditions"
    return render_template('index.html', message = False)
@app.route('/ikbal')
def elnur():
    name = ["Serdar", "Orlando", "Nobel", "Vincenzo", "Callahan"]
    return render_template("body.html", object=name, developer_name =" Yunus" )

if __name__ == "__main__":
    app.run(debug=True)
