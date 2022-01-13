import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--method", choices=["flask","GUI","WebGUI"],required=True,default=1, type=str,help="This is how you choose to run the bot")

args = parser.parse_args()
value = args.method

# only import the necessary files depending on what we need to use

if value == 'flask':
    from methods.FlaskApi import start_server
    start_server()

elif value== 'GUI':
    import tkinter
    from methods.GUI import App
    root = tkinter.Tk()
    root.configure(background="black")
    app = App(root,'emotions\\AI_idle.gif')
    root.mainloop()

elif value== 'WebGUI':
    from methods.WebGUI import start_server
    start_server()
