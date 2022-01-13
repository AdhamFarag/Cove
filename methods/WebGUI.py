from flask import Flask,render_template
from methods.actualbot import response

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html",Response="Hello")


@app.route("/<text>")
def Main(text):
    text = text.lower()
    responseVariable = response(text,Detailed=True)
    coveResponse = responseVariable[0]
    if(response(text)[0] == None):
        coveResponse = "I don't think I am Programmed to do that, would you like me to make a note of that"
    elif("alpha" in text.lower()):
        # TODO: HANDLE EXITING OF SERVER
        pass
    elif(coveResponse != None):
        # check to see if the user requested to see images and send them in HTML
        return render_template("index.html",Response=coveResponse)



def start_server():
    app.run()
