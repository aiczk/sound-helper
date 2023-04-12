import commands.core.command as commands
from pydub import AudioSegment

class composite:
    def __init__(self):
        self.command_list = []

    def check(self, audio: AudioSegment):
        for command in self.command_list:
            if not command.check(audio):
                return False
        return True

    def execute(self, audio: AudioSegment):
        for command in self.command_list:
            if command.is_default():
                continue
            audio = command.execute(audio)
        return audio
    
    def finalize(self):
        for command in self.command_list:
            command.finalize()

    def add_optional_command(self, command: commands.command):
        if command in self.command_list or command.is_default():
            return
        self.command_list.append(command)
        print(f"applied: {command.__class__.__name__}")
    
    def add_required_command(self, command: commands.command):
        if command in self.command_list:
            return
        self.command_list.append(command)