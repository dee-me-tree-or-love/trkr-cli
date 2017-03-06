"""The command to check if the database contains unclosed tasks"""

from .base import Base
# from .locatedb import checkdbloc
#
from clint.textui import puts, colored, indent
# import sqlite3
from json import dumps

# from trkr.globals import StoredDBProc, getdbloc

class Verify(Base):


    def run(self):
        print(colored.red('Verify command is yet to be implemented'))
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
