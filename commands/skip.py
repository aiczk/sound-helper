import commands.core.command as commands

class skip(commands.command):
    def __init__(self, value):
        super().__init__(value)

    def check(self, audio):
        return audio.duration_seconds >= self.value