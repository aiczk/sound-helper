from pydub import AudioSegment

class command:
    def __init__(self, value):
        self.value = value

    def is_default(self):
        return self.value == 0 or self.value == None
    
    def check(self, audio: AudioSegment):
        return True

    def execute(self, audio: AudioSegment):
        return audio

    def finalize(self):
        pass