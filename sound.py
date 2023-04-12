import argparse
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
from commands.core.composite import composite
from commands.sample_rate import sample_rate
from commands.channel import channel
from commands.invert_phase import invert_phase
from commands.loudness_normalization import loudness_normalization
from commands.lowpass import lowpass
from commands.highpass import highpass
from commands.pack import pack
from commands.skip import skip
from commands.export import export
from commands.reverse import reverse

# TODO: REFACTORING

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
parser.add_argument("--pack", type=int, help="Pack output files(0: false, 1: true)")
args = parser.parse_args()

class sound:
    def __init__(self):
        self.filelist = [file for file in [os.path.join(args.input, x) for x in os.listdir(args.input) if not x.startswith(".")] if os.path.isfile(file)]
        self.filelist.sort()

        self.composite = composite()
        self.composite.add_optional_command(skip(args.skip))
        self.composite.add_optional_command(sample_rate(args.samplerate))
        self.composite.add_optional_command(channel(args.channel))
        self.composite.add_optional_command(invert_phase(args.invert))
        self.composite.add_optional_command(loudness_normalization(args.loudness))
        self.composite.add_optional_command(lowpass(args.lowpass))
        self.composite.add_optional_command(highpass(args.highpass))
        self.composite.add_optional_command(reverse(args.reverse))
        self.composite.add_optional_command(pack(args.pack, args.output, args.oformat))
        self.composite.add_required_command(export(args.filename, args.prefix, args.output, args.oformat))
    
    def run(self):
        for file_path in self.filelist:
            for audio in split_on_silence(AudioSegment.from_file(file_path, format=args.iformat), min_silence_len = args.silence, silence_thresh = args.threshold):
                if self.composite.check(audio): 
                    audio = self.composite.execute(audio)
        
        self.composite.finalize()
        print("Done!")

if __name__ == "__main__":
    main = sound()
    main.run()