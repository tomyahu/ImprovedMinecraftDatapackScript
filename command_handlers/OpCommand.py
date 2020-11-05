from consts import var_player, aux_variable_name
from command_handlers.Command import Command


class OpCommand(Command):
    """
    Command for operating the variables with numbers or other variables
    """

    def __init__(self, file, args):
        Command.__init__(self, file, "var")
        self.name = "var." + args[1]
        self.operator = args[2]
        self.value = args[3]

    def parse(self):
        """
        Parses the command.

        Checks if the second variable is a number, if so it allocates the value in an auxiliary variable, operates it
        with the first variable and saves the result in the first variable.

        Otherwise it just operates the first variable with the second variable and saves the result in the first
        variable.

        :return: <str> the translation of the command
        """
        try:
            int(self.value)

            memory_allocation = "scoreboard objectives add " + aux_variable_name + " dummy\n"
            variable_initialization = "scoreboard players set " + var_player + " " + aux_variable_name + " " + self.value
            variable_update = "scoreboard players operation " + var_player + " " + self.name + " " + self.operator + " " + var_player + " " + aux_variable_name + "\n"

            return memory_allocation + variable_initialization + variable_update
        except:
            return "scoreboard players operation " + var_player + " " + self.name + " " + self.operator + " " + self.name + " " + self.value
