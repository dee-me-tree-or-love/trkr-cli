# init command for trkr implementation, do not confuse with __init__.py stuff
"""The init command"""

from json import dumps
import sqlite3  # for creating the database
from os import makedirs, path

from .base import Base

# getting the globals from there
from trkr.globals import *

class Initdb(Base):
    """say initialied"""  # the description for the doc

    #used to initialize the database
    def setupdb(self):
        dbcon = sqlite3.connect(path.join(self.trkrloc, DATABASENAME))
        curs = dbcon.cursor()

        # create a table if does not exist
        curs.execute('CREATE TABLE IF NOT EXISTS {tn} '
                     '('
                     '{cn1} {dt1}, '  # primary key id
                     '{cn2} {dt2},'  # title
                     '{cn3} {dt3},'  # time started
                     '{cn4} {dt4},'  # time ended
                     '{cn5} {dt5}'  # date
                     ')' \
                     .format(tn="tasks",
                             cn1=tasktable.id,
                             dt1=tasktable.datatypes['id'],
                             cn2=tasktable.title,
                             dt2=tasktable.datatypes['title'],
                             cn3=tasktable.time_started,
                             dt3=tasktable.datatypes['ts'],
                             cn4=tasktable.time_finished,
                             dt4=tasktable.datatypes['tf'],
                             cn5=tasktable.date,
                             dt5=tasktable.datatypes['date'],
                             )
                     )
        dbcon.commit()
        dbcon.close()

    def run(self):
        # the rule is that the database will be stored at the ~/trkr location
        # get default user location
        # home = path.expanduser("~")
        # self.trkrloc = path.join(home, DEFAULTFOLDER)
        self.trkrloc = gettrkrloc()
        # check if the trkr location exists
        if not path.exists(self.trkrloc):
            # create a folder if not
            makedirs(self.trkrloc)

        # create a table tasks if necessary
        self.setupdb()

        print(DATABASENAME, 'is initialized in this directory: ')
        print(self.trkrloc)
        # nice for testing what parameters were supplied
        # print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
