import commands.core.command as commands

class skip(commands.command):
    def __init__(self, value):
        super().__init__(value)

    def check(self, audio):
        if isinstance(audio, list):
            return all([len(i) < self.value for i in audio])
        return len(audio) < self.value