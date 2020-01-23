# **bookmarks** in the terminal

## Basics:
Every time you run the script you need to specify a folder and an action. If you don't, the script will use the defaults values which are:
**action=show**
**folder=unsorted**. So it will show (print) the bookmarks in the unsorted folder

## Usage:
### Getting started
```
python3 main.py
```
This will use the default action: `show` and the default folder: `unsorted` (as explained in the basics section)

### Showing bookmarks from specific folders

Just add `--folder <name of the folder>`. If there are no bookmarks in the folder, it will create a file to store them in `bookmarks/<folder name>.txt`

### Adding bookmarks

Just set `--action add` and specify `--folder` (otherwise it will use the default value, `unsorted`), `--name` with the name of the bookmark, `--url` with the url, `--desc` with the description.

If the selected folder does not exisit, it will create a file to store them in `bookmarks/<folder name>.txt`

## Exporting and importing bookmarks 

`bookmarks/` folder is the folder you need to save put your bookmarks for exporting and importing