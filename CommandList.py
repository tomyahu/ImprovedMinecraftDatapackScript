

class CommandList:

    def __init__(self, file):
        self.commands = file.readlines()
        self.current_line = 0

    def get_current_line(self):
        return self.commands[self.current_line]

    def is_finished(self):
        return self.current_line >= len(self.commands)

    def advance_line(self):
        self.current_line += 1