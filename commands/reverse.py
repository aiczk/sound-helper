import commands.core.command as commands

class reverse(commands.command):
    def __init__(self, value):
        super().__init__(value)

    def execute(self, audio):
        if self.value == None or self.value == 0:
            return audio
        return audio.reverse()