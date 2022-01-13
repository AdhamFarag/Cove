import threading
import tkinter
from PIL import Image, ImageTk, ImageSequence
import threading
from tkinter.tix import IMAGETEXT
from methods.actualbot import response
import speech_recognition as sr

def get_audio():
    '''
    function used to record microphone audio and converts it to text
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
            # speak("Sorry, I didn't get that")
    return said



class App(threading.Thread):
    '''
    this class is used to prove the window to animate the AI character based on emotions
    if response occurs -> idle emotion is displayed in GUI window
    if exception occurs -> mad emotion is displayed in GUI window
    '''
    def __init__(self, parent,img):
        self.parent = parent
        self.img = img
        threading.Thread.__init__(self)
        self.start()
        self.canvas = tkinter.Canvas(parent, width=600, height=400)
        self.canvas.pack(fill="both", expand=True)
        self.sequence = [ImageTk.PhotoImage(self.img)
                            for self.img in ImageSequence.Iterator(
                                    Image.open(self.img))]
        self.image = self.canvas.create_image(0,0, image=self.sequence[0],anchor="nw")
        self.animate(1)

    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(20, lambda: self.animate((counter+1) % len(self.sequence)))

    def run(self):
        loop_active = True
        while loop_active:
            text = get_audio()
            text = text.lower()
            coveResponse = response(text)
            if text!= "":
                self.img = "emotions\\AI_idle.gif"
                self.sequence = [ImageTk.PhotoImage(self.img)
                    for self.img in ImageSequence.Iterator(
                            Image.open(self.img))]
                if(response(text) == None):
                    print("I don't think I am Programmed to do that, would you like me to make a note of that")
                elif("alpha" in text.lower()):
                    loop_active =False
                    self.parent.quit()
                    self.parent.destroy()
                elif(response(text) != None):
                    try:
                        print(coveResponse)
                    except:
                        self.img = "emotions\\AI_angry.gif"
                        self.sequence = [ImageTk.PhotoImage(self.img)
                        for self.img in ImageSequence.Iterator(
                                Image.open(self.img))]
            else:
                self.img = "emotions\\AI_angry.gif"
                self.sequence = [ImageTk.PhotoImage(self.img)
                    for self.img in ImageSequence.Iterator(
                            Image.open(self.img))]



