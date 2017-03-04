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


