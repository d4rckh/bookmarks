from bcolors import bcolors

def show(folder):
    folder = folder
    path = "bookmarks/" + folder + ".txt"
    try:
        with open(path) as fp:
            bookmarks = fp.read().split("\n")
            parsed = []
            for bookmark in bookmarks:
                
                
                if bookmark == '':
                    pass
                else:

                    url = bookmark.split(":")[0]
                    name = bookmark.split(":")[1]
                    description = bookmark.split(":")[2]
                    

                    parsed.append({
                        "url": url,
                        "name": name,
                        "description": description,
                        "folder": folder
                    })
            for bookmark in parsed:
                print(bcolors.OKBLUE + bookmark["name"] + bcolors.ENDC)
                print(bcolors.OKGREEN + "URL: " + bcolors.ENDC + bcolors.UNDERLINE + bookmark["url"] + bcolors.ENDC)
                print(bcolors.OKGREEN + "Description: " + bcolors.ENDC + bookmark["description"])
    except IOError:
        with open(path, 'w+') as fp:
            show(folder)