from CommandList import CommandList
from command_handlers.DivCommand import DivCommand
from command_handlers.IfCommand import IfCommand
from command_handlers.ModCommand import ModCommand
from command_handlers.MultCommand import MultCommand
from command_handlers.OpCommand import OpCommand
from command_handlers.SubCommand import SubCommand
from command_handlers.AddCommand import AddCommand
from command_handlers.VarCommand import VarCommand
from command_handlers.IfNotCommand import IfNotCommand
from commands import my_commands

my_commands["var"] = VarCommand
my_commands["+="] = AddCommand
my_commands["-="] = SubCommand
my_commands["*="] = MultCommand
my_commands["/="] = DivCommand
my_commands["%="] = ModCommand
my_commands["op"] = OpCommand
my_commands["if"] = IfCommand
my_commands["ifnot"] = IfNotCommand

file_path = "example.imcfunction"

file = open(file_path)

command_list = CommandList(file)

new_string = ""
while not command_list.is_finished():
    command = command_list.get_current_line()
    args = command.split(" ")
    identifier = args[0]

    if identifier in my_commands:
        new_string += my_commands[identifier](command_list, args).parse()
    else:
        new_string += command

    command_list.advance_line()

print(new_string)