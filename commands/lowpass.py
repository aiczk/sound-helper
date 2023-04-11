import commands.core.command as commands

class lowpass(commands.command):
    def __init__(self, default, value):
        super().__init__(default, value)

    def execute(self, audio):
        return audio.low_pass_filter(self.value)