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
        if self.cache.duration_seconds <= 0:
            return
        
        print("An audio file was created that did not reach the specified number of seconds.")
        self.cache.export(os.path.join(self.output_path, f"_merge(shortage).{self.output_format}"), format=self.output_format)