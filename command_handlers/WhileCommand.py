import os

from commands import my_commands
from consts import var_player
import consts
from command_handlers.Command import Command


class WhileCommand(Command):
    """
    A command for parsing while statements
    """

    def __init__(self, file, args):
        Command.__init__(self, file, "while")
        self.var1 = "var." + args[1]
        self.operation = args[2]
        self.var2 = args[3].replace("\n", "")

        self.execute_mod = "if"

    def parse(self):
        """
        Parses the command.

        Translates the condition to a string that is then appended to the parsed values of every instruction inside the
        while statement. Then returns the result.
        """
        try:
            int(self.var2)
            prev_string = "scoreboard objectives add " + consts.aux_variable_name + " dummy\n"
            prev_string += "scoreboard players set " + var_player + " " + consts.aux_variable_name + " " + self.var2 + "\n"
            prev_string += "execute " + self.execute_mod + " score " + var_player + " " + self.var1 + " " + self.operation + " " + var_player + " " + consts.aux_variable_name + " run "
        except:
            prev_string = "execute " + self.execute_mod + " score " + var_player + " " + self.var1 + " " + self.operation + " " + var_player + " var." + self.var2 + " run "

        new_string = ""
        current_command = self.command_str

        while_counter = 0
        while current_command != ("end" + self.command_str):
            self.file.advance_line()
            command = self.file.get_current_line()

            args = command.replace("\t", "").split(" ")
            current_command = args[0].replace("\n", "")

            if current_command == ("end" + self.command_str):
                if while_counter > 0:
                    while_counter -= 1
                else:
                    break
            else:
                if current_command in my_commands:
                    new_string += my_commands[current_command](self.file, args).parse()
                else:
                    new_string += command

                if current_command == self.command_str:
                    while_counter += 1

        splitted_commands = new_string.split("\n")


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



        function_dir = consts.current_path.replace("/data/", "", 1).replace("/functions/", ":", 1).replace(".mcfunction", "_aux_dir")
        function_dir += "/" + str(i) + ".mcfunction"
        file.write(prev_string + "function " + function_dir + "\n")

        file.close()

        return prev_string + "function " + function_dir
