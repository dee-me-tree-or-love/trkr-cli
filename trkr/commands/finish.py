"""The command to start a new task"""

from .base import Base
from .locatedb import checkdbloc

from clint.textui import puts, colored, indent
import sqlite3
#from json import dumps

from trkr.globals import StoredDBProc, getdbloc

class Finish(Base):

    dbprocedures = StoredDBProc()

    # a generalized wrapper for the command execution
    # def executedbcommand(self,text):
    #     dbcon = sqlite3.connect(getdbloc())
    #     cur = dbcon.cursor()
    #     cur.execute(text)
    #     dbcon.commit()
    #     dbcon.close()
    #
    # def executedbquery(self,text):
    #     dbcon = sqlite3.connect(getdbloc())
    #     cur = dbcon.cursor()
    #     cur.execute(text)
    #     allrows = cur.fetchall()
    #     dbcon.close()
    #     return allrows

    def closetask(self,tn):
        print(tn)

    def getlasttask(self):
        return self.dbprocedures.executedbquery(self.dbprocedures.getlasttask())

    def closetask(self, pkid):
        self.dbprocedures.executedbcommand(self.dbprocedures.closetask(pkid))

    def run(self):
        if not checkdbloc():
            #verify that the db exists
            puts(colored.red('The database does not exist, run initdb to make sure'))
        else:
            # close the old unfinished tasks first:
            try:
                # id=0; title=1; time_started=2; time_finished=3;
                lasttask = self.getlasttask()
                if lasttask != []: # if there is nothing - it returns an empty array
                    lasttask = lasttask[0]  # gets the last of the 'last tasks', since the query is general it returns a list always
                    print('Last task: ', lasttask)
                    if lasttask[3] == None:
                        print('closing...')
                        self.closetask(lasttask[0])
                        print('done!')
                    else:
                        print('task is already closed')
                else:
                    print('No recent tasks from today found')
                # self.closetask(lasttask.id)
            except Exception as e:
                print("db connection error:")
                print(e)
        # print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
