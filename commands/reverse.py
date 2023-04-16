import commands.core.command as commands

class reverse(commands.command):
    def __init__(self, value):
        super().__init__(value)

    def execute(self, audio):
        return self.action(audio, lambda audio: audio.reverse())