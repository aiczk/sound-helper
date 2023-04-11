# Split Audio Files by Silence
This script splits audio files based on the length of silence detected in them. 
Audio files are split into chunks wherever there is silence for a period longer than the specified minimum silence length.

### Dependencies

1. At first, install ffmpeg from the [official website](https://ffmpeg.org/).
2. Register the ffmpeg bin directory in the environment variable.
3. Install what you need using pip:
```
pip install -r requirements.txt
```

#### Usage
```bat
python split_audio_by_silence.py [--inputdir INPUTDIR] [--outputdir OUTPUTDIR] [--mintime MINTIME] [--dbfs DBFS] [--skip SKIP] [--samplerate SAMPLERATE] [--channel CHANNEL] [--format FORMAT]
```

|Argument|Description|Default|
|--------|-----------|-------|
|--input|Input directory path|.\input|
|--output|Output directory path|.\output|
|--silence|Minimum silence length (ms)|500|
|--dbfs|Silence threshold (dBFS)|-40|
|--skip|Ignore files with less than the specified seconds (sec)|2.0|
|--samplerate|Sample rate (Hz)|44100|
|--channel|Number of audio channels (1 for mono, 2 for stereo)|1|
|--format|Output file format (wav, mp3, etc.)|wav|

## Example
```bat
python split_audio_by_silence.py --inputdir ./input --outputdir ./output --mintime 500 --dbfs -40 --skip 2.0 --samplerate 44100 --channel 1 --format wav
```

The bat file is optimized for DDSP-SVC. Rewrite it as necessary.

## Thanks
I was inspired to create [this](https://self-development.info/python%e3%82%92%e7%94%a8%e3%81%84%e3%81%9f%e7%99%ba%e8%a9%b1%e5%88%86%e5%89%b2%e3%80%90ai%e3%83%9c%e3%82%a4%e3%82%b9%e3%83%81%e3%82%a7%e3%83%b3%e3%82%b8%e3%83%a3%e3%83%bc%e3%81%ae%e5%ad%a6%e7%bf%92/) site.