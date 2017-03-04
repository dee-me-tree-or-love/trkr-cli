"""
trkr

Usage:
  trkr initdb
  trkr current
  trkr finish
  trkr verify
  trkr start <task-name>
  trkr locatedb
  trkr -h | --help
  trkr --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  trkr hello

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/dee-me-tree-or-love/trkr
"""

# The inspect module provides several useful
# functions to help get information about live
# objects such as modules, classes, methods, functions,
# tracebacks, frame objects, and code objects.
from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


# the cli documentation - parsed by the docopt package with docopt(__doc__, version=VERSION)


def main():
    """Main CLI entrypoint."""
    import trkr.commands  # the module with command definitions
    options = docopt(__doc__, version=VERSION)

    # Here the command the user is trying to run is being registered and compared
    # with a pre-defined command classes we've already created
    for (k, v) in options.items():  # k - key, and v is value
        if hasattr(trkr.commands, k) and v:  # if the one of the command module matches the specified input
            module = getattr(trkr.commands, k)  # gets the attributes of the modules with the mathcing name
            trkr.commands = getmembers(module, isclass)  # gets the class member of the commands module
            # mean to be tested - I am curious what that is
            ([command[1] for command in trkr.commands if command[0] != 'Base'])
            # delete line above
            command = [command[1] for command in trkr.commands if command[0] != 'Base'][0]  # actually becomes a class
            command = command(options)
            command.run()
