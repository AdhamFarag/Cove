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
------------------------

#### How to use:
To run the flask API server run ```driver.py --method=flask```
To run a GUI for the bot and use speech reognition run ```driver.py --method=GUI```

