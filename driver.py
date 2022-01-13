import argparse
import tkinter

parser = argparse.ArgumentParser()
parser.add_argument("--method", choices=["flask","GUI"],required=True,default=1, type=str,help="This is how you choose to run the bot")

args = parser.parse_args()
value = args.method

if value == 'flask':
    # only import the necessary files if we choose to start server
    from FlaskApi import start_server
    start_server()
elif value== 'GUI':
    from GUI import App
    root = tkinter.Tk()
    root.configure(background="black")
    app = App(root,'emotions\\AI_idle.gif')
    root.mainloop()
