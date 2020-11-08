import os
import sys
import consts
from shutil import copyfile, copytree, rmtree, make_archive
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
from command_handlers.WhileCommand import WhileCommand
from command_handlers.WhileNotCommand import WhileNotCommand
from commands import my_commands

# Sets the new commands to the respective handlers
my_commands["var"] = VarCommand
my_commands["+="] = AddCommand
my_commands["-="] = SubCommand
my_commands["*="] = MultCommand
my_commands["/="] = DivCommand
my_commands["%="] = ModCommand
my_commands["op"] = OpCommand
my_commands["if"] = IfCommand
my_commands["ifnot"] = IfNotCommand
my_commands["while"] = WhileCommand
my_commands["whilenot"] = WhileNotCommand

# Obtains file and export path
file_path = sys.argv[1]
export_path = file_path + "_out"
consts.export_path = export_path


# copy_file: str -> None
# copies a file as is from the datapack developed to the export file
def copy_file(extra_path):
    copyfile(file_path + extra_path, export_path + extra_path)


# translate_datapack_dir: str -> None
# copies all directories in that are not functions from the datapack module to the export. Then it translates all
# .mcfunction files to the vanilla script.
def translate_datapack_dir(extra_path):
    all_inside_dirs = [f for f in os.listdir(file_path + extra_path)]

    for dir in all_inside_dirs:
        if dir != "functions":
            if os.path.isfile(file_path + extra_path + "/" + dir):
                copy_file(extra_path + "/" + dir)
            else:
                copy_dir(extra_path + "/" + dir)
        else:
            os.mkdir(export_path + extra_path + "/" + dir)
            translate_all_files_in_dir(extra_path + "/" + dir)


# translate_all_files_in_dir: str -> None
# translates all files in a directory and saves the result in the export path.
def translate_all_files_in_dir(extra_path):
    all_inside_dirs = [f for f in os.listdir(file_path + extra_path)]
    for dir in all_inside_dirs:
        if os.path.isfile(file_path + extra_path + "/" + dir):
            file_extension = dir.split(".")[-1]
            if file_extension == "mcfunction":
                translate_file(extra_path + "/" + dir)
        else:
            translate_all_files_in_dir(extra_path + "/" + dir)


# copy_dir: str -> None
# copies a directory with all its files as they are to the export file.
def copy_dir(extra_path):
    copytree(file_path + extra_path, export_path + extra_path)


# translate_file: str -> None
# translates a single file and saves its translation in the export file.
def translate_file(file_to_translate_path):
    file = open(file_path + file_to_translate_path)
    command_list = CommandList(file)

    consts.current_path = file_to_translate_path

    # Translates the commands to the vanilla datapack language
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

    file.close()

    # Exports new file
    export_file = open(export_path + file_to_translate_path, "w")
    export_file.write(new_string)
    export_file.close()


########################################################################################################################
########################################################################################################################
########################################################################################################################
# Make export directory
try:
    os.mkdir(export_path)
except:
    pass

# Copy pack.mcmeta and pack.png
all_inside_dirs = [f for f in os.listdir(file_path) if os.path.isfile(file_path + "/" + f)]
for dir in all_inside_dirs:
    copy_file("/" + dir)

# Create data directory
os.mkdir(export_path + "/data")

# Translates the datapack
all_dirs_inside_data = [f for f in os.listdir(file_path + "/data")]
for dir in all_dirs_inside_data:
    if os.path.isfile(file_path + "/data/" + dir):
        copy_file("/data/" + dir)
    else:
        os.mkdir(export_path + "/data/" + dir)
        translate_datapack_dir("/data/" + dir)

# Zips the result
make_archive(export_path, 'zip', export_path)

# Deletes temporary directory
#rmtree(export_path)