

class CommandList:
    """
    A class that represents the list of commands to translate
    """

    def __init__(self, file):
        self.commands = file.readlines()
        self.current_line = 0

    def get_current_line(self):
        """
        Gets the string corresponding to the current line of the file being read.
        :return: <str> the line of the file being read
        """
        return self.commands[self.current_line]

    def is_finished(self):
        """
        checks if all the commands have been read
        :return: <bool> true if the file has stopped and false otherwise
        """
        return self.current_line >= len(self.commands)

    def advance_line(self):
        """
        Advances one line in the file to read
        """
        self.current_line += 1