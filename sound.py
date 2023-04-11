import argparse
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

parser = argparse.ArgumentParser()
parser.add_argument("--input", type=str, default=".\input", help="Input directory path")
parser.add_argument("--output", type=str, default=".\output", help="Output directory path")
parser.add_argument("--silence", type=int, default=500, help="Silence length(ms)")
parser.add_argument("--dbfs", type=int, default=-40, help="Silence threshold(dBFS)")
parser.add_argument("--skip", type=float, default=0.0, help="Skip time(sec)")
parser.add_argument("--samplerate", type=int, default=48000, help="Sample rate(Hz)")
parser.add_argument("--channel", type=int, default=1, help="channel(1:mono, 2:stereo)")
parser.add_argument("--format", type=str, default="wav", help="format(wav, mp3, etc...)")
args = parser.parse_args()

input = args.input
output = args.output
silence = args.silence
dbfs = args.dbfs
skip_sec = args.skip
sample_rate = args.samplerate
channel = args.channel
format = args.format

def run(input, output, silence, dbfs, skip_sec, sample_rate, channel, format):
    filenames = [os.path.join(input, x) for x in sorted(os.listdir(input)) if not x.startswith(".")]
    filelist=[file for file in filenames if os.path.isfile(file)]
    filelist.sort()

    for i in range(len(filelist)):
        file_path = filelist[i]
        audio = AudioSegment.from_file(file_path, format="wav")
        chunks = split_on_silence(audio, min_silence_len = silence, silence_thresh = dbfs)
        for j in range(len(chunks)):
            chunk = chunks[j]

            if skip_sec != 0 and chunk.duration_seconds < skip_sec:
                continue

            chunk.frame_rate = sample_rate
            chunk.channels = channel
            chunk.export(os.path.join(output, f"{os.path.splitext(os.path.basename(file_path))[0]}_{i}_{j}.{format}"), format=format)
    
    print("Done!")

run(input, output, silence, dbfs, skip_sec, sample_rate, channel, format)