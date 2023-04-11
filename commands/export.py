import commands.core.command as commands
from pydub import AudioSegment
import os

class export(commands.command):
    def __init__(self, default, value, prefix, output_path, output_format):
        super().__init__(default, value)
        self.audio = AudioSegment.empty()
        self.prefix = prefix
        self.output_path = output_path
        self.output_format = output_format
        self.counter = 0

    def execute(self, audio: AudioSegment):
        self.counter += 1
        prefix_str = self.prefix if self.prefix == "" else self.prefix + "_"

        # file_name = f"{prefix_str}{os.path.splitext(os.path.basename(file_path))[0]}_{i}_{j}.{self.output_format}"
        file_name = f"{prefix_str}{self.value}_{self.counter}.{self.output_format}"

        audio.export(os.path.join(self.output_path, file_name), format=self.output_format)
        return audio