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

# TODO: REFACTORING

parser = argparse.ArgumentParser()
parser.add_argument("--input", type=str, default=".\input", help="Input directory path")
parser.add_argument("--output", type=str, default=".\output", help="Output directory path")
parser.add_argument("--filename", type=str, default="audio", help="Output file name")
parser.add_argument("--iformat", type=str, default="wav", help="Input format(wav, mp3, etc...)")
parser.add_argument("--oformat", type=str, default="wav", help="Output format(wav, mp3, etc...)")

parser.add_argument("--duration", type=int, default=500, help="Silence length(ms)")
parser.add_argument("--silence", type=int, default=-40, help="Silence threshold(dBFS)")
parser.add_argument("--skip", type=float, default=0, help="Skip time(sec)")

parser.add_argument("--samplerate", type=int, default=0, help="Sample rate(Hz)")
parser.add_argument("--invert", type=bool, default=0, help="Invert phase audio(0: false, 1: true)")
parser.add_argument("--loudness", type=float, default=0.0, help="Loudness normalization(dBFS)")
parser.add_argument("--channel", type=int, default=0, help="Channel(0: pass, 1:mono, 2:stereo)")
parser.add_argument("--lowpass", type=int, default=0, help="Lowpass filter(Hz)")
parser.add_argument("--highpass", type=int, default=0, help="Highpass filter(Hz)")

parser.add_argument("--prefix", type=str, default=None, help="Prefix of output file name")
parser.add_argument("--pack", type=bool, default=0, help="Pack output files(0: false, 1: true)")
args = parser.parse_args()

class sound:
    def __init__(self):
        self.filelist = [file for file in [os.path.join(args.input, x) for x in os.listdir(args.input) if not x.startswith(".")] if os.path.isfile(file)]
        self.filelist.sort()

        self.composite = composite()
        self.composite.add_required_command(skip(0, args.skip))
        self.composite.add_optional_command(sample_rate(0, args.samplerate))
        self.composite.add_optional_command(channel(0, args.channel))
        self.composite.add_optional_command(invert_phase(0, args.invert))
        self.composite.add_optional_command(loudness_normalization(0, args.loudness))
        self.composite.add_optional_command(lowpass(0, args.lowpass))
        self.composite.add_optional_command(highpass(0, args.highpass))
        self.composite.add_optional_command(pack(0, args.pack, args.output, args.oformat))
        self.composite.add_required_command(export(0, args.filename, args.prefix, args.output, args.oformat))
    
    def run(self):
        for file_path in self.filelist:
            for audio in split_on_silence(AudioSegment.from_file(file_path, format=args.iformat), min_silence_len = args.duration, silence_thresh = args.silence):
                if not self.composite.check(audio): 
                    audio = self.composite.execute(audio)
        
        self.composite.finalize()
        print("Done!")

if __name__ == "__main__":
    main = sound()
    main.run()