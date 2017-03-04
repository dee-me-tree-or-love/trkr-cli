"""The definition of the global values shared accross the app"""
from .constants import TaskSchema, DEFAULTFOLDER, DATABASENAME
from os.path import join,expanduser

dbcon = None # set to null by default
tasktable = TaskSchema() # contains the task table details

def gettrkrloc():
    home = expanduser("~")
    return join(home, DEFAULTFOLDER)

def getdbloc():
    home = expanduser("~")
    return join(home, DEFAULTFOLDER,DATABASENAME)