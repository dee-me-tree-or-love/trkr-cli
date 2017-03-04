"""The definition of the global values shared accross the app"""
from .constants import TaskSchema

dbcon = None # set to null by default
tasktable = TaskSchema() # contains the task table details