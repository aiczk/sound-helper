import commands.core.command as commands
from pydub import AudioSegment

class split(commands.command):
    def __init__(self, value):
        super().__init__(value)
    
    def execute(self, audio: AudioSegment):
        if(len(audio) < self.value):
            return audio
        return [audio[i * self.value : (i + 1) * self.value] for i in range(len(audio) // self.value)]