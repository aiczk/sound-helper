import commands.core.command as commands

class loudness_normalization(commands.command):
    def __init__(self, value):
        super().__init__(value)

    def execute(self, audio):
        return audio.apply_gain(self.value - audio.dBFS)