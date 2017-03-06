"""The command to check the current status of trkr - if there are unclosed tasks, how much time is spent on current and so on"""

from .base import Base
# from .locatedb import checkdbloc
#
from clint.textui import puts, colored, indent
# import sqlite3
from json import dumps

# from trkr.globals import StoredDBProc, getdbloc

class Status(Base):


    def run(self):
        print(colored.red('Status command is yet to be implemented'))
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
