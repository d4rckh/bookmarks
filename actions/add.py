from bcolors import bcolors

def add(folder, name, url, desc):
    folder = folder
    path = "bookmarks/" + folder + ".txt"
    try:
        with open(path, 'a') as fp:
            fp.write(url + ':' + name + ':' + desc + '\n')
    except IOError:
        with open(path, 'w+') as fp:
            show(folder)