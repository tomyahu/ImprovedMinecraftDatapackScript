from command_handlers.WhileCommand import WhileCommand


class WhileNotCommand(WhileCommand):
    """
    A command for parsing whilenot statements
    """

    def __init__(self, file, args):
        WhileCommand.__init__(self, file, "whilenot")
        self.execute_mod = "unless"
