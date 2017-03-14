"""The command to check if the database contains unclosed tasks"""

from .base import Base
from .locatedb import checkdbloc
#
from clint.textui import puts, colored, indent
# import sqlite3
from json import dumps

from trkr.globals import dbprocedures, getdbloc

class Verify(Base):


    PASSED = ':)';

    def getopentasks(self):
        return dbprocedures.executedbquery(dbprocedures.getopentasks())

    # check if db exists
    def checkdbexists(self):
        result = colored.magenta("to be implemented...")
        # do checks here
        # should return the result in a text form? either good or not -- like a tick or something
        return result
    # check if table exists
    def checktblexists(self):
        result = colored.magenta("to be implemented...")
        # do checks here
        # should return the result in a text form? either good or not -- like a tick or something
        return result
    # check columns conistency
    def checkcolumns(self):
        result = colored.magenta("to be implemented...")
        # do checks here
        # should return the result in a text form? either good or not -- like a tick or something
        return result
    # check for unclosed tasks
    def checktasks(self):
        result = colored.magenta("to be implemented...")
        # do checks here
        # should return the result in a text form? either good or not -- like a tick or something
        return result

    # to contain the error reports
    errorreports = []

    def addtoreport(self,text):
        self.errorreports.append(text)

    def puterrorreport(self,errorsfound):
        if errorsfound:
            puts(colored.red('\nDeviations:'))
            with indent(4, quote=' ! >'):
                # want a niceR oneliner here!!
                for err in errorsfound: puts(err)

    def run(self):
        puts(colored.yellow("Testing the db consistency"))
        with indent(4, quote=' >'):
            puts("db exists: " + (self.checkdbexists()))
            puts("table exists: " + (self.checktblexists()))
            puts("columns exist: "+ (self.checkcolumns()))
            puts("at most one open task: "+ (self.checktasks()))
        if len(self.errorreports) > 0:
            self.puterrorreport()


        # print(colored.red('Verify command is yet to be implemented'))
        # print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
