import commands.core.command as commands
from pydub import AudioSegment
import os

class merge(commands.command):
    def __init__(self, value, output_path, output_format):
        super().__init__(value)
        self.cache = AudioSegment.empty()
        self.output_path = output_path
        self.output_format = output_format
    
    def check(self, audio: AudioSegment):
        if self.cache.duration_seconds >= self.value:
            return False
        self.cache += audio
        return self.cache.duration_seconds < self.value

    def execute(self, audio: AudioSegment):
        if self.check(audio):
            return audio
        result = self.cache
        self.cache = AudioSegment.empty()
        return result
    
    def finalize(self):
        pass # Destroy the cache even if it remains