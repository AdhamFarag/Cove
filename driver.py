import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--method", choices=["flask"],required=True,default=1, type=str,help="This is how you choose to run the bot")

args = parser.parse_args()
value = args.method

if value == 'flask':
    # only import the necessary files if we choose to start server
    from FlaskApi import start_server
    start_server()
