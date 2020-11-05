

class Command:
    """
    A class that represents a new command
    """

    def __init__(self, file, command_str):
        self.command_str = command_str
        self.file = file

    def parse(self):
        """
        Parses the command and its arguments to an expression
        :return: <str> the translation of the command
        """
        return ""
