import commands.core.command as commands

class skip(commands.command):
    def __init__(self, value):
        super().__init__(value)

    # audioはAudioSegment型かlist[AudioSegment]型である
    # リストの場合はすべての条件が揃っているかをallで確認する
    # audiosegmentの場合は条件に合致しているかを確認する
    def check(self, audio):
        if isinstance(audio, list):
            return all([i.duration_seconds < self.value for i in audio])
        return audio.duration_seconds < self.value