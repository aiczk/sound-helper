import commands.core.command as commands
from pydub import AudioSegment
import os

class export(commands.command):
    def __init__(self, value, prefix, output_path, output_format):
        super().__init__(value)
        self.audio = AudioSegment.empty()
        self.prefix = prefix or ""
        self.output_path = output_path
        self.output_format = output_format
        self.counter = 0

    def execute(self, audio):
        return self.action(audio, lambda audio: self.export(audio))
    
    def export(self, audio: AudioSegment):
        if audio is None:
            return

        self.counter += 1
        prefix_str = self.prefix if self.prefix == "" else self.prefix + "_"
        file_name = f"{prefix_str}{self.value}_{self.counter}.{self.output_format}"
        audio.export(os.path.join(self.output_path, file_name), format=self.output_format)