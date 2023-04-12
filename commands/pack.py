import commands.core.command as commands
from pydub import AudioSegment
import os

class pack(commands.command):
    def __init__(self, value, output_path, output_format):
        super().__init__(value)
        self.audio = AudioSegment.empty()
        self.output_path = output_path
        self.output_format = output_format
    
    def execute(self, audio: AudioSegment):
        self.audio += audio
        return audio

    def finalize(self):
        self.audio.export(os.path.join(self.output_path, f"pack.{self.output_format}"), format=self.output_format)