from command_handlers.IfCommand import IfCommand


class IfNotCommand(IfCommand):
    """
    A command for parsing ifnot statements
    """

    def __init__(self, file, args):
        IfCommand.__init__(self, file, args)
        self.execute_mod = "unless"
        self.command_str = "ifnot"
