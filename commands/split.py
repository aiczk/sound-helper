import commands.core.command as commands
from pydub import AudioSegment

class split(commands.command):
    def __init__(self, value):
        super().__init__(value)

    def execute(self, audio: AudioSegment):
        if audio.duration_seconds > self.value:
            return [audio[i * self.value * 1000 : (i + 1) * self.value * 1000] for i in range(int(audio.duration_seconds // self.value))]
        return audio