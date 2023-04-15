import argparse
import os
from tqdm.auto import tqdm
from pydub import AudioSegment
from pydub.silence import split_on_silence
from commands.core import composite as core

parser = argparse.ArgumentParser()
parser.add_argument("--input", type=str, default="./input", help="Input directory path")
parser.add_argument("--output", type=str, default="./output", help="Output directory path")
parser.add_argument("--filename", type=str, default="audio", help="Output file name")
parser.add_argument("--iformat", type=str, default="wav", help="Input format(wav, mp3, etc...)")
parser.add_argument("--oformat", type=str, default="wav", help="Output format(wav, mp3, etc...)")

parser.add_argument("--silence", type=int, default=500, help="Silence length(ms)")
parser.add_argument("--threshold", type=int, default=-40, help="Silence threshold(dBFS)")
parser.add_argument("--skip", type=float, help="Skip time(sec)")

parser.add_argument("--samplerate", type=int, help="Sample rate(Hz)")
parser.add_argument("--invert", type=int, help="Invert phase audio(0: false, 1: true)")
parser.add_argument("--loudness", type=float, help="Loudness normalization(dBFS)")
parser.add_argument("--channel", type=int, help="Channel(0: pass, 1:mono, 2:stereo)")
parser.add_argument("--lowpass", type=int, help="Lowpass filter(Hz)")
parser.add_argument("--highpass", type=int, help="Highpass filter(Hz)")
parser.add_argument("--reverse", type=int, help="Reverse audio(0: false, 1: true)")

parser.add_argument("--prefix", type=str, help="Prefix of output file name")
parser.add_argument("--merge", type=int, help="Merge files under a certain number of seconds(ms)")
parser.add_argument("--split", type=int, help="Split files longer than a specified number of seconds(ms)")
parser.add_argument("--pack", type=int, help="Pack output files(0: false, 1: true)")
args = parser.parse_args()

class sound:
    def __init__(self):
        self.filelist = [os.path.join(args.input, file) for file in os.listdir(args.input) if not file.startswith(".")]
        self.composite = core.composite(args)
    
    def run(self):
        for file_path in self.filelist:
            split_audio = sorted(split_on_silence(AudioSegment.from_file(file_path, args.iformat), args.silence, args.threshold), key=lambda x: x.duration_seconds)
            for audio in tqdm(split_audio, desc=os.path.basename(file_path)):
                if self.composite.check(audio):
                    continue
                audio = self.composite.execute(audio)
        self.composite.finalize()

if __name__ == "__main__":
    main = sound()
    main.run()