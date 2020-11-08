import consts
from command_handlers.Command import Command


class VarCommand(Command):
    """
    A command that allocates a new variable and gives it a value
    """

    def __init__(self, file, args):
        Command.__init__(self, file, "var")
        self.name = "var." + args[1]
        self.value = args[2]

    def parse(self):
        """
        Parses the command, turns it into two commands, one that allocates the variable and another one that sets its
        value
        :return: <str> the translation of the command
        """
        memory_allocation = "scoreboard objectives add " + self.name + " dummy\n"
        variable_initialization = "scoreboard players set " + consts.var_player + " " + self.name + " " + self.value

        return memory_allocation + variable_initialization