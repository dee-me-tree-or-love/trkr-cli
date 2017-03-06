"""The class to store the database procedures"""
import sqlite3
from .envvar import getdbloc

# the class contains either string attributes or the methods that return strings
class StoredDBProc:

    # a generalized wrapper for the command execution
    def executedbcommand(self, text):
        dbcon = sqlite3.connect(getdbloc())
        cur = dbcon.cursor()
        cur.execute(text)
        dbcon.commit()
        dbcon.close()

    def executedbquery(self, text):
        dbcon = sqlite3.connect(getdbloc())
        cur = dbcon.cursor()
        cur.execute(text)
        allrows = cur.fetchall()
        dbcon.close()
        return allrows

    def closeold(self):
        return 'UPDATE tasks '\
               'SET time_finished = CURRENT_TIME ' \
               'WHERE time_finished IS NULL ' \
               'AND date = CURRENT_DATE;'

    def startnewtask(self,tn):
        return 'INSERT INTO tasks '\
               '(title,time_started, date) ' \
               'VALUES ("'+tn+'",CURRENT_TIME, CURRENT_DATE);'

    def getlasttask(self):
        return 'SELECT * ' \
               'FROM tasks ' \
               'WHERE time_started = (' \
               '    SELECT MAX(time_started) ' \
               '    FROM tasks ' \
               '    WHERE date = CURRENT_DATE) ' \
               'AND date = CURRENT_DATE;' \

    def getopentasks(self):
        return 'SELECT * ' \
               'FROM tasks ' \
               'WHERE time_finished IS NULL;'

    # takes the primary key as a parameter
    def closetask(self,pkid):
        return 'UPDATE tasks ' \
               'SET time_finished = CURRENT_TIME ' \
               'WHERE id = ' + str(pkid)

    # get the list of tasks with time elapsed etc
    def getlisttasks(self):
        return "SELECT *, (strftime('%s', IFNULL(time_finished,CURRENT_TIME))- strftime( '%s', time_started)) as  seconds_elapsed " \
               "FROM TASKS;"

    def getlisttaskstoday(self):
        return "SELECT *, (strftime('%s', IFNULL(time_finished,CURRENT_TIME))- strftime( '%s', time_started)) as  seconds_elapsed  " \
               "FROM TASKS " \
               "WHERE date = CURRENT_DATE;"

# the instance to be shared:
dbprocedures = StoredDBProc()