import commands.core.command as commands

class invert_phase(commands.command):
    def __init__(self, default, value):
        super().__init__(default, value)

    def execute(self, audio):
        return audio.invert_phase()