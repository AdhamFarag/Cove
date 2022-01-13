from flask import Flask,render_template
from sklearn.metrics import coverage_error
import json
from methods.actualbot import response
app = Flask(__name__)


@app.route("/<text>")
def MainResponse(text):
    text = text.lower()
    coveResponse = response(text)
    print(text)
    if(coveResponse == None):
        coveResponse = "I don't think I am Programmed to do that, would you like me to make a note of that"
    elif("alpha" in text.lower()):
        # TODO: Handle exit of code here using alpha as a failsafe word
        pass
    returnedJSON = app.response_class(
        response=json.dumps({"status":"success","code":0,"data":coveResponse}),
        status=200,
        mimetype='application/json'
    )
    return returnedJSON



def start_server():
    app.run()
