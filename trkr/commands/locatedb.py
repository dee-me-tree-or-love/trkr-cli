"""The command to show the database location"""

from os import path

# for console tools:
from clint.textui import puts, colored, indent

from .base import Base

# getting the globals from there
from trkr.globals import constants, envvar


# let it be module wide method
def checkdbloc():
    # get the home user
    # home = path.expanduser("~")
    # self.trkrloc = path.join(home, constants.DEFAULTFOLDER, constants.DATABASENAME)
    dbloc = envvar.getdbloc()  # gets the standard location of the database
    return path.exists(dbloc)


class Locatedb(Base):
    def run(self):
        if checkdbloc():
            self.trkrloc = envvar.getdbloc()
            puts(constants.DATABASENAME + 'is stored in this directory: ') # the usage of clint
            with indent(4):
                puts(colored.blue(self.trkrloc))
        else:
            puts(colored.red('Database is not available'))
            with indent(4):
                puts('Expected at location: ' + self.trkrloc)