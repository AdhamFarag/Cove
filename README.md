# Cove
AI smart assistant project

#### First Step
```
pip install -r requirements.txt
```
------------------------

#### Useful Tips
  - To retrain the bot with new data please run ```TrainBotUsingIntent.py``` after changing ```data.json``` with required information
  - the Tkinter GUI supports threading so fucntions can always be running in parallel to the animations (ex. selinium, twillio, 3rd party RESTApis)
  - To change the look and feel of the webGUI, all you need to do is edit the CSS and HTML in the index and .css files in the methods folder
  - To get response from the Web GUI bot you can use URL to have the questions ie (http://127.0.0.1:5000/how%20are%20you%20doing%20today) to ask the bot "how are you doing today"
------------------------

#### How to use:
- To run the flask API server run ```driver.py --method=flask```
- To run a GUI for the bot and use speech reognition run ```driver.py --method=GUI```
- To run a Web GUI for the bot and the questions of the bot in the url run ```driver.py --method=WebGUI```


