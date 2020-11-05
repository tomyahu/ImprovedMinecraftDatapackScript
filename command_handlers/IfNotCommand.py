from command_handlers.IfCommand import IfCommand


class IfNotCommand(IfCommand):

    def __init__(self, file, args):
        IfCommand.__init__(self, file, "ifnot")
        self.execute_mod = "unless"
