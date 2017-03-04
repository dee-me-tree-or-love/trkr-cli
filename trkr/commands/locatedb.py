"""The command to show the database location"""

from os import path

from .base import Base

# getting the globals from there
from trkr.globals import constants

class Locatedb(Base):

    def run(self):
        # get the home user
        home = path.expanduser("~")
        self.trkrloc = path.join(home, constants.DEFAULTFOLDER, constants.DATABASENAME)
        if(path.exists(self.trkrloc)):
            print(constants.DATABASENAME, 'is stored in this directory: ', self.trkrloc)
        else:
            print('Database is not available. Expected at location: ',self.trkrloc)