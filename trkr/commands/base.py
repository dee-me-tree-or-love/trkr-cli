# A base command class that all other classes will extend.
"""The base command."""


class Base(object):
    """A base command structure."""

    def __init__(self, options, *args, **kwargs):
        # Whenever we construct a new instance of a command class,
        # we’ll pass in the options that were generated using docopt.
        # This way, each sub-command has access
        # to all the user supplied CLI information.
        # -- https://stormpath.com/blog/building-simple-cli-interfaces-in-python
        self.options = options
        self.args = args
        self.kwargs = kwargs

    def run(self):
        raise NotImplementedError('You must implement the run() method yourself!')