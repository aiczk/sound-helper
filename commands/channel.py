import commands.core.command as commands

class channel(commands.command):
    def __init__(self, value):
        super().__init__(value)

    def execute(self, audio):
        return self.action(audio, lambda audio: audio.set_channels(self.value))