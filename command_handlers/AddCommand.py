from command_handlers.OpCommand import OpCommand


class AddCommand(OpCommand):

    def __init__(self, file, args):
        OpCommand.__init__(self, file, [args[0], args[1], "+=", args[2]])
