import commands.core.command as commands

class sample_rate(commands.command):
    def __init__(self, value):
        super().__init__(value)

    def execute(self, audio):
        return self.action(audio, lambda audio: audio.set_frame_rate(self.value))