
class StoredDBProc:

    updtaskstocurtime = 'UPDATE tasks'\
                        'SET time_finished = CURRENT_TIME'\
                        'WHERE time_finished IS NULL;'

    def startnewtask(self,tn):
        return 'INSERT INTO tasks'\
               '(title,time_started)' \
               'VALUES ('+tn+',CURRENT_TIME);'


