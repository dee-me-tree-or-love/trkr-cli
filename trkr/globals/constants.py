"""The constant values to be used across the app"""


# treat it like a constant
DEFAULTFOLDER = "trkr"
DATABASENAME = "trkr_tasks.sqlite"

# is the definition of the Tasks table for the database
class TaskSchema:
    title = "title"
    time_started = "time_started"
    time_finished = "time_finished"
    id = "id"
    date = "date"
    datatypes = {
        'title': "VARCHAR(32)",
        'ts': "TIME",
        'tf': "TIME",
        'id': "INTEGER PRIMARY KEY",  # bad to put this way, but will do for now
        'date': "DATE",
    }
    # constraints = {
    #     'id': "PRIMARY KEY",
    # }
