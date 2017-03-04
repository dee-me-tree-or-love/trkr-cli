"""The command to start a new task"""

from .base import Base
from .locatedb import checkdbloc

from clint.textui import puts, colored, indent
import sqlite3
from json import dumps

from trkr.globals import StoredDBProc, getdbloc

class Start(Base):

    dbprocedures = StoredDBProc()

    # a generalized wrapper for the command execution
    def executedbcommand(self,text):
        dbcon = sqlite3.connect(getdbloc())
        cur = dbcon.cursor()
        cur.execute(text)
        dbcon.commit()
        dbcon.close()


    def closeold(self):
        self.executedbcommand(self.dbprocedures.closeold)

    def starttask(self,tn):
        self.executedbcommand(self.dbprocedures.startnewtask(tn))


    def run(self):
        if not checkdbloc():
            #verify that the db exists
            puts(colored.red('The database does not exist, run initdb to make sure'))
        else:
            # do starting of the new task here

            # close the old unfinished tasks first:
            try:
                self.closeold()
                taskname = self.options['<task-name>']
                self.starttask(taskname)
                print('You have started the new task: ',taskname)
            except Exception as e:
                print("db connection error:")
                print(e)
        # print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
