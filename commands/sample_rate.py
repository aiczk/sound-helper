import commands.core.command as commands

class sample_rate(commands.command):
    def __init__(self, default, value):
        super().__init__(default, value)

    def execute(self, audio):
        if self.is_default():
            return audio
        return audio.set_frame_rate(self.value)