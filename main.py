import argparse
from bcolors import bcolors 
from actions.show import show 
from actions.add import add 

argumentparser = argparse.ArgumentParser(description="Bookmarks in command line!") # skipcq: FLK-E501
argumentparser.add_argument('--action', type=str, help="Choose action, can be: add or show") # skipcq: FLK-E501
argumentparser.add_argument('--folder', type=str, help="Choose folder where to do the action") # skipcq: FLK-E501
argumentparser.add_argument('--name', type=str, help="Name of the bookmark you want to add (if action=add) or see (if action=show)") # skipcq: FLK-E501
argumentparser.add_argument('--desc', type=str, help="Description of the bookmark you want to add (if action=add else its ignored)") # skipcq: FLK-E501
argumentparser.add_argument('--url', type=str, help="Url of the bookmark you want to add (if action=add) or see (if action=show)") # skipcq: FLK-E501

args = argumentparser.parse_args()

validactions = ["show", "add"]
action = None
folder = None



def warn(t):
    print(bcolors.WARNING + "Warning: " + bcolors.ENDC + t)
def error(t):
    print(bcolors.FAIL + "Error: " + bcolors.ENDC + t)

def blank():
    print("")
    print("")

if args.action:
    if args.action in validactions:
        action = args.action
    else:
        warn(args.action + " is not a valid action, using default action: show") # skipcq: FLK-E501
        action = "show"
else:
    warn("No action has been specified in --action argument, using default action: show") # skipcq: FLK-E501
    action = "show"

if args.folder:
    folder = args.folder
else:
    warn("No folder has been specified in --folder argument, using default folder: unsorted") # skipcq: FLK-E501
    folder = "unsorted"
    blank()

print(bcolors.OKGREEN + "ACTION:" + bcolors.ENDC + action + bcolors.OKGREEN + "; FOLDER:" + bcolors.ENDC + folder) # skipcq: FLK-E501

blank()

if action == "show":
    show(folder)
if action == "add":
    if args.name:
        if args.desc:
            if args.url:
                add(folder, args.name, args.url, args.desc)
            else:
                error('--url is empty, when action=add, you must specify an url using --url') # skipcq: FLK-E501 
        else:
            error('--desc is empty, when action=add, you must specify an description using --desc') # skipcq: FLK-E501
    else:
        error('--name is empty, when action=add, you must specify an name using --name') # skipcq: FLK-E501
