import commands.core.command as commands

class channel(commands.command):
    def __init__(self, default, value):
        super().__init__(default, value)

    def execute(self, audio):
        return audio.set_channels(self.value)