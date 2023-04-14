# Split Audio Files by Silence
This script splits audio files based on the length of silence detected in them. 

Audio files are split into chunks wherever there is silence for a period longer than the specified minimum silence length.

The bat file is optimized for DDSP-SVC. Rewrite it as necessary.

## Dependencies

1. At first, install ffmpeg from the [official website](https://ffmpeg.org/).
2. Register the ffmpeg bin directory in the environment variable.
3. Install what you need using pip:
```
pip install -r requirements.txt
```

## Usage
### Parameters
Non-required arguments are set to 0.
#### File Setting
|Argument|Description|Default|
|--------|-----------|-------|
|--input|Input directory path|.\input|
|--output|Output directory path|.\output|
|--filename|Output file name|audio|
|--iformat|Input file format (wav, mp3, etc.)|wav|
|--oformat|Output file format (wav, mp3, etc.)|wav|

#### Sound Setting
When LPF(lowpass) and HPF(highpass) are used together, they function as BPF(bandpass) and BSF(bandstop).
|Argument|Description|Default|
|--------|-----------|-------|
|--silence|Minimum silence length (ms)|500|
|--threshold|Silence threshold (dBFS)|-40|
|--skip|Ignore files with less than the specified seconds (sec)|0.0|
|--samplerate|Sample rate (Hz)|0|
|--invert|Invert phase audio(0: false, 1: true)|0|
|--loudness|Loudness normalization(dBFS)|0.0|
|--channel|Number of audio channels(0: pass, 1: mono, 2: stereo)|0|
|--lowpass|Low pass filter(Hz)|0|
|--highpass|High pass filter(Hz)|0|
|--reverse|Reverse audio(0: false, 1: true)|0|

#### Output Setting
|Argument|Description|Default|
|--------|-----------|-------|
|--pack|Combine all output files(0: false, 1: true)|0|
|--merge|Merge files under a certain number of seconds(sec)|0.0|
|--prefix|Prefix of output file name|None|

### Example
example:
```bat
python sound.py --filename "sepalate" --skip 2 --samplerate 44100 --invert 1 --reverse 1 --loudness -14 --pack 1 --highpass 80 --prefix --merge 5.0 "rev_inv_hps"
```

## Thanks
I was inspired to create [this](https://self-development.info/python%e3%82%92%e7%94%a8%e3%81%84%e3%81%9f%e7%99%ba%e8%a9%b1%e5%88%86%e5%89%b2%e3%80%90ai%e3%83%9c%e3%82%a4%e3%82%b9%e3%83%81%e3%82%a7%e3%83%b3%e3%82%b8%e3%83%a3%e3%83%bc%e3%81%ae%e5%ad%a6%e7%bf%92/) site.