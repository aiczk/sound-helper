import commands.core.command as commands

class skip(commands.command):
    def __init__(self, default, value):
        super().__init__(default, value)

    def check(self, audio):
        return self.value != 0 and audio.duration_seconds < self.value