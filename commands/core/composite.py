from functools import reduce
from pydub import AudioSegment
from typing import Union
import commands

class composite:
    def __init__(self, args):
        self.command_list = []
        self.add_optional_command(commands.skip(args.skip))
        self.add_optional_command(commands.merge(args.merge, args.output, args.oformat))
        self.add_optional_command(commands.split(args.split))
        self.add_optional_command(commands.sample_rate(args.samplerate))
        self.add_optional_command(commands.channel(args.channel))
        self.add_optional_command(commands.invert_phase(args.invert))
        self.add_optional_command(commands.loudness_normalization(args.loudness))
        self.add_optional_command(commands.lowpass(args.lowpass))
        self.add_optional_command(commands.highpass(args.highpass))
        self.add_optional_command(commands.reverse(args.reverse))
        self.add_optional_command(commands.pack(args.pack, args.output, args.oformat))
        self.add_required_command(commands.export(args.filename, args.prefix, args.output, args.oformat))

    def check(self, audio: AudioSegment):
        return any(command.check(audio) for command in self.command_list)

    def execute(self, audio: Union[AudioSegment, list]):
        return reduce(lambda audio, command: command.execute(audio) if not command.is_default() else audio, self.command_list, audio)
    
    def finalize(self):
        reduce(lambda _, command: command.finalize() if not command.is_default() else _, self.command_list, None)

    def add_optional_command(self, command: commands.command):
        if command in self.command_list or command.is_default():
            return
        self.command_list.append(command)
        print(f"Sound Effect: {command.__class__.__name__}")

    def add_required_command(self, command: commands.command):
        if not command in self.command_list: 
            self.command_list.append(command)