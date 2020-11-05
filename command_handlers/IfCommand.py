from commands import my_commands
from consts import var_player
from command_handlers.Command import Command


class IfCommand(Command):
    """
    A command for parsing if statements
    """

    def __init__(self, file, args):
        Command.__init__(self, file, "if")
        self.var1 = "var." + args[1]
        self.operation = args[2]
        self.var2 = "var." + args[3].replace("\n", "")

        self.execute_mod = "if"

    def parse(self):
        """
        Parses the command.

        Translates the condition to a string that is then appended to the parsed values of every instruction inside the
        if statement. Then returns the result.
        """
        prev_string = "execute " + self.execute_mod + " score " + var_player + " " + self.var1 + " " + self.operation + " " + var_player + " " + self.var2 + " run "

        new_string = ""
        current_command = "if"
        while current_command != "end":
            self.file.advance_line()
            command = self.file.get_current_line()

            args = command.replace("\t", "").split(" ")
            current_command = args[0]

            if current_command == "end":
                break
            else:
                if current_command in my_commands:
                    new_string += my_commands[current_command](self.file, args).parse()
                else:
                    new_string += command

        splitted_commands = new_string.split("\n")

        final_result = ""
        for command in splitted_commands:
            if command.replace(" ", "") != "":
                final_result += prev_string + command + "\n"

        return final_result
