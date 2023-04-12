from pydub import AudioSegment

class command:
    def __init__(self, value):
        self.value = value

    def is_default(self):
        return self.value == None
    
    def check(self, audio: AudioSegment):
        return True

    # TODO: change the second argument to a class with AudioSegment and file_path
    def execute(self, audio: AudioSegment):
        return audio

    def finalize(self):
        pass