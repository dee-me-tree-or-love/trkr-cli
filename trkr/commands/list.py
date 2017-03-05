"""The command to list info about the tasks in db"""

from .base import Base
from .locatedb import checkdbloc

from clint.textui import puts, colored, indent
import sqlite3
from json import dumps

from trkr.globals import dbprocedures, getdbloc

class List(Base):

    # references
    id = 0; title = 1; time_started = 2; time_finished = 3; date = 4; seconds_elapsed = 5


    def getlistcomplete(self):
        return dbprocedures.executedbquery(dbprocedures.getlisttasks())

    def getlisttoday(self):
        return dbprocedures.executedbquery(dbprocedures.getlisttaskstoday())

    def tasktostring(self,task):


        if(task[self.seconds_elapsed] is not None):
            _hoursspent = task[self.seconds_elapsed]//3600
            _minutesspent = (task[self.seconds_elapsed] - _hoursspent*3600)//60
            _secondsspent = (task[self.seconds_elapsed] - _minutesspent*60)

        return " title: %s " \
               "\n started: %s " \
               "\n time spent: %s:%s:%s " \
               "\n time finished: %s" \
               "\n date: %s" \
               "\n<------------->" % \
               (task[self.title],
                task[self.time_started],
                _hoursspent,_minutesspent,_secondsspent,
                task[self.time_finished],
                task[self.date])

    def printoutlist(self,alltasks):
        totaltimespent = 0
        for t in alltasks: print(self.tasktostring(t)); totaltimespent += t[self.seconds_elapsed]
        return totaltimespent

    def run(self):
        if not checkdbloc():
            #verify that the db exists
            puts(colored.red('The database does not exist, run initdb to make sure'))
        else:
            alltasks = []
            # if not specified that the complete list is required - returns only today's
            if self.options['-c'] or self.options['--complete']:
                alltasks = self.getlistcomplete()
            else:
                alltasks = self.getlisttoday()
            puts(colored.blue("Total tasks: %s \n"%str(len(alltasks))))
            totaltime = self.printoutlist(alltasks)
            puts(colored.blue("Total time spent: %s h %s m %s s"%(
                totaltime//3600,
                (totaltime%3600)//60,
                (totaltime%3600)%60
            ))) ## probably deserves a method of its own..

        # print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
        # You
        # supplied
        # the
        # following
        # options: {
        #     "--help": false,
        #     "--complete": false,
        #     "--version": false,
        #     "-c": true,
        #     "<task-name>": null,
        #     "current": false,
        #     "finish": false,
        #     "initdb": false,
        #     "list": true,
        #     "locatedb": false,
        #     "start": false,
        #     "verify": false
        # }

        # print('You supplied the following args:', dumps(self.args, indent=2, sort_keys=True)) those are not used...
        # print('You supplied the following options:', dumps(self.kwargs, indent=2, sort_keys=True))
