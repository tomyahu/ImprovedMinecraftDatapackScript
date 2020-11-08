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
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QLineEdit, QPushButton, QFileDialog

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


# Subclass QMainWindow to customise your application's main window
class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.import_path = ""
        self.export_path = ""

        self.setWindowTitle("Improved Datapack Script Compiler")

        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("Minecraft Version: " + consts.mc_version))

        self.layout.addSpacing(4)

        # Player Memory Value
        self.memory_player_layout = QHBoxLayout()
        self.memory_player_layout.addWidget(QLabel("Memory Player:"))

        self.memory_player_text = QLineEdit(self)
        self.memory_player_text.setText(consts.var_player)
        self.memory_player_layout.addWidget(self.memory_player_text)

        self.layout.addLayout(self.memory_player_layout)

        # Variable Prefix
        self.var_prefix_layout = QHBoxLayout()
        self.var_prefix_layout.addWidget(QLabel("Variable Prefix:"))

        self.var_prefix_text = QLineEdit(self)
        self.var_prefix_text.setText(consts.aux_variable_name)
        self.var_prefix_layout.addWidget(self.var_prefix_text)

        self.layout.addLayout(self.var_prefix_layout)

        # Translate Button
        self.translate_button = QPushButton("Translate Datapack")
        self.translate_button.clicked.connect(self.translate_datapack)

        self.layout.addWidget(self.translate_button)

        self.setLayout(self.layout)

    def translate_datapack(self):
        """
        Translates a datapack to a Zip
        """
        self.import_path = QFileDialog.getExistingDirectory().__str__()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        export_path, _ = QFileDialog.getSaveFileName()
        self.export_path = export_path.__str__()
        consts.export_path = export_path

        consts.var_player = self.memory_player_text.text()
        consts.aux_variable_name = self.var_prefix_text.text()

        self.translate_datapack_aux()

    def translate_datapack_aux(self):
        """
        TODO: Document this
        :return:
        """
        # Make export directory
        try:
            os.mkdir(self.export_path)
        except:
            pass

        # Copy pack.mcmeta and pack.png
        all_inside_dirs = [f for f in os.listdir(self.import_path) if os.path.isfile(self.import_path + "/" + f)]
        for dir in all_inside_dirs:
            self.copy_file("/" + dir)

        # Create data directory
        os.mkdir(self.export_path + "/data")

        # Translates the datapack
        all_dirs_inside_data = [f for f in os.listdir(self.import_path + "/data")]
        for dir in all_dirs_inside_data:
            if os.path.isfile(self.import_path + "/data/" + dir):
                self.copy_file("/data/" + dir)
            else:
                os.mkdir(self.export_path + "/data/" + dir)
                self.translate_datapack_dir("/data/" + dir)

        # Zips the result
        make_archive(self.export_path, 'zip', self.export_path)

        # Deletes temporary directory
        #rmtree(self.export_path)

    #TODO: Document methods
    def copy_file(self, extra_path):
        """
        copies a file as is from the datapack developed to the export file
        :param extra_path:
        :return:
        """
        copyfile(self.import_path + extra_path, self.export_path + extra_path)

    def translate_datapack_dir(self, extra_path):
        """
        copies all directories in that are not functions from the datapack module to the export. Then it translates all
        .mcfunction files to the vanilla script.
        :param extra_path:
        :return:
        """
        all_inside_dirs = [f for f in os.listdir(self.import_path + extra_path)]

        for dir in all_inside_dirs:
            if dir != "functions":
                if os.path.isfile(self.import_path + extra_path + "/" + dir):
                    self.copy_file(extra_path + "/" + dir)
                else:
                    self.copy_dir(extra_path + "/" + dir)
            else:
                os.mkdir(self.export_path + extra_path + "/" + dir)
                self.translate_all_files_in_dir(extra_path + "/" + dir)

    def translate_all_files_in_dir(self, extra_path):
        """
        translates all files in a directory and saves the result in the export path.
        :param extra_path:
        :return:
        """
        all_inside_dirs = [f for f in os.listdir(self.import_path + extra_path)]
        for dir in all_inside_dirs:
            if os.path.isfile(self.import_path + extra_path + "/" + dir):
                file_extension = dir.split(".")[-1]
                if file_extension == "mcfunction":
                    self.translate_file(extra_path + "/" + dir)
            else:
                self.translate_all_files_in_dir(extra_path + "/" + dir)

    def copy_dir(self, extra_path):
        """
        copies a directory with all its files as they are to the export file.
        :param extra_path:
        :return:
        """
        copytree(self.import_path + extra_path, self.export_path + extra_path)

    def translate_file(self, file_to_translate_path):
        """
        translates a single file and saves its translation in the export file.
        :param file_to_translate_path:
        :return:
        """
        file = open(self.import_path + file_to_translate_path)
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
        export_file = open(self.export_path + file_to_translate_path, "w")
        export_file.write(new_string)
        export_file.close()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()