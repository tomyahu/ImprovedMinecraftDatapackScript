from consts import var_player
from command_handlers.Command import Command


class VarCommand(Command):

    def __init__(self, file, args):
        Command.__init__(self, file, "var")
        self.name = "var." + args[1]
        self.value = args[2]

    def parse(self):
        """
        Parses the command and its arguments to an expression
        """
        memory_allocation = "scoreboard objectives add " + self.name + " dummy\n"
        variable_initialization = "scoreboard players set " + var_player + " " + self.name + " " + self.value

        return memory_allocation + variable_initialization