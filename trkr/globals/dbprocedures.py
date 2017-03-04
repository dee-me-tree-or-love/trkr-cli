"""The class to store the database procedures"""

# the class contains either string attributes or the methods that return strings
class StoredDBProc:

    closeold = 'UPDATE tasks '\
                'SET time_finished = CURRENT_TIME ' \
                'WHERE time_finished IS NULL;'

    def startnewtask(self,tn):
        return 'INSERT INTO tasks '\
               '(title,time_started) ' \
               'VALUES ("'+tn+'",CURRENT_TIME);'

    def getlasttask(self):
        return 'SELECT * ' \
               'FROM tasks ' \
               'WHERE time_started = (' \
               '    SELECT MAX(time_started) ' \
               '    FROM tasks);' \

    def getopentasks(self):
        return 'SELECT * ' \
               'FROM tasks ' \
               'WHERE time_finished IS NULL;'

    # takes the primary key as a parameter
    def closetask(self,pkid):
        return 'UPDATE tasks ' \
               'SET time_finished = CURRENT_TIME ' \
               'WHERE id = ' + str(pkid)