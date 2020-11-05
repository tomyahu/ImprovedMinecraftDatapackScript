from command_handlers.OpCommand import OpCommand


class ModCommand(OpCommand):
    """
    An operation command for modular operation
    """

    def __init__(self, file, args):
        OpCommand.__init__(self, file, [args[0], args[1], "%=", args[2]])
