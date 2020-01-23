from bcolors import bcolors

def add(folder, name, url, desc):
    path = "bookmarks/" + folder + ".txt"
    try:
        fp = open(path, 'a')
        fp.write(url + ':' + name + ':' + desc + '\n')
    except IOError:
        fp = open(path, 'w+')
        show(folder)