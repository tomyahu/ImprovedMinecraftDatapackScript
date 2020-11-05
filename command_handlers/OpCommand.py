from consts import var_player, aux_variable_name
from command_handlers.Command import Command


class OpCommand(Command):

    def __init__(self, file, args):
        Command.__init__(self, file, "var")
        self.name = "var." + args[1]
        self.operator = args[2]
        self.value = args[3]

    def parse(self):
        """
        Parses the command and its arguments to an expression
        """

        try:
            int(self.value)

            memory_allocation = "scoreboard objectives add " + aux_variable_name + " dummy\n"
            variable_initialization = "scoreboard players set " + var_player + " " + aux_variable_name + " " + self.value
            variable_update = "scoreboard players operation " + var_player + " " + self.name + " " + self.operator + " " + var_player + " " + aux_variable_name + "\n"

            return memory_allocation + variable_initialization + variable_update
        except:
            return "scoreboard players operation " + var_player + " " + self.name + " " + self.operator + " " + self.name + " " + self.value
