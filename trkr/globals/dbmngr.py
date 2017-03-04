# """Used to manage the database"""
# import sqlite3
# from .constants import DATABASENAME, TaskSchema
# from os.path import join
#
# class Databasemngr:
#
#     def __init__(self, dbloc):
#         self.location = DATABASENAME
#         self.connection = sqlite3.connect(join(dbloc, DATABASENAME))
#         self.connection.close()
#         self.tasktable = TaskSchema()
#
#     def setupdb(self,dbloc):
#
#         curs = self.connection.cursor()
#         # create a table if does not exist
#         curs.execute('CREATE TABLE IF NOT EXISTS {tn} '
#                      '('
#                      '{cn1} {dt1}, '  # primary key id
#                      '{cn2} {dt2},'  # title
#                      '{cn3} {dt3},'  # time started
#                      '{cn4} {dt4}'  # time ended
#                      ')' \
#                      .format(tn="tasks",
#                              cn1=self.tasktable.id,
#                              dt1=self.tasktable.datatypes['id'],
#                              cn2=self.tasktable.title,
#                              dt2=self.tasktable.datatypes['title'],
#                              cn3=self.tasktable.time_started,
#                              dt3=self.tasktable.datatypes['ts'],
#                              cn4=self.tasktable.time_finished,
#                              dt4=self.tasktable.datatypes['tf'],
#                              )
#                      )
#         self.connection.commit()
#         self.connection.close()
