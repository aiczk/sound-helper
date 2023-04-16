import commands.core.command as commands
from pydub import AudioSegment
import os

class combine(commands.command):
    def __init__(self, value, output_path, output_format):
        super().__init__(value)
        self.audio = AudioSegment.empty()
        self.output_path = output_path
        self.output_format = output_format
    
    # audioはAudioSegment型か、list型のAudioSegment型の要素を持つ
    def execute(self, audio):
        if isinstance(audio, list):
            for a in audio:
                self.audio += a
        else:
            self.audio += audio

    def finalize(self):
        self.audio.export(os.path.join(self.output_path, f"_pack.{self.output_format}"), format=self.output_format)