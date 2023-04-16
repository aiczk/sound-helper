from pydub import AudioSegment
from typing import Union

class command:
    def __init__(self, value):
        self.value = value

    def is_default(self):
        return self.value == 0 or self.value == None
    
    def check(self, audio: Union[AudioSegment, list]):
        return False

    def execute(self, audio: Union[AudioSegment, list]):
        return audio

    def finalize(self):
        pass

    def action(self, audio: Union[AudioSegment, list], act):
        if isinstance(audio, list):
            return [act(segment) for segment in audio]
        return act(audio)