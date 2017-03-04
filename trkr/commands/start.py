"""The command to start a new task"""

from .base import Base
from .locatedb import checkdbloc

from clint.textui import puts, colored
import sqlite3
from json import dumps



class Start(Base):

    # def closeold(self):
    #      dbcon = sqlite3.connect()
    #
    # def starttask(self,tn):
    #     print()

    def run(self):
        # if not checkdbloc():
        #     puts(colored.red('The database does not exist, run initdb to make sure'))
        # else:
        #     print('You have started the new task: ',self.options['<task-name>'])

        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
