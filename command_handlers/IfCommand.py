import os

from commands import my_commands
from consts import var_player
import consts
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
        if_counter = 0
        while current_command != "endif":
            self.file.advance_line()
            command = self.file.get_current_line()

            args = command.replace("\t", "").split(" ")
            current_command = args[0].replace("\n", "")

            if current_command == "endif":
                if if_counter > 0:
                    if_counter -= 1
                else:
                    break
            else:
                if current_command in my_commands:
                    new_string += my_commands[current_command](self.file, args).parse()
                else:
                    new_string += command

                if current_command == "if":
                    if_counter += 1

        splitted_commands = new_string.split("\n")

        if len(splitted_commands) == 2:
            final_result = ""
            for command in splitted_commands:
                if command.replace(" ", "") != "":
                    final_result += prev_string + command + "\n"

            return final_result
        elif len(splitted_commands) > 2:
            aux_dir_path = (consts.export_path + consts.current_path).replace(".mcfunction", "_aux_dir")
            try:
                os.mkdir(aux_dir_path)
            except:
                pass

            aux_files = [f for f in os.listdir(aux_dir_path)]

            i = len(aux_files)
            aux_file_name = aux_dir_path + "/" + str(i) + ".mcfunction"
            while aux_file_name in aux_files:
                i += 1
                aux_file_name = aux_dir_path + "/" + str(i) + ".mcfunction"

            file = open(aux_file_name, "w")

            for command in splitted_commands:
                file.write(command + "\n")
            file.close()

            function_dir = consts.current_path.replace("/data/", "", 1).replace("/functions/", ":", 1).replace(".mcfunction", "_aux_dir")
            function_dir += "/" + str(i) + ".mcfunction"
            return prev_string + "function " + function_dir



        return ""
