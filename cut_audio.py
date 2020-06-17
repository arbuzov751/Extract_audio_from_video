import sys
import glob
from pydub import AudioSegment

# For this script to work, you need to download ffmpeg from the official site
# and register the full path to exe file in AudioSegment.converter

AudioSegment.converter = f"D:\Extract_audio_from_video\\venv_for_audio\\ffmpeg-20200617-0b3bd00-win64-static\\bin\\ffmpeg.exe"

# all_files = glob.glob(f"{sys.argv[1]}\**\*.wav")
all_files = glob.glob(f"D:\Download\data_set\**\*.wav")

length_of_chunk = 15
count_chunks = 5

for file in all_files:
    song = AudioSegment.from_wav(file)

    startMin = 0
    startSec = 0

    endMin = length_of_chunk // 60
    endSec = length_of_chunk % 60

    # Time to miliseconds
    startTime = startMin * 60 * 1000 + startSec * 1000
    endTime = endMin * 60 * 1000 + endSec * 1000

    for i in range(count_chunks):
        # Opening file and extracting segment
        try:
            extract = song[startTime:endTime]
            file_name = file.split('/')[-1]
            file_name = file_name.split('.')[0]
            # Saving
            extract.export(file_name + f'-extract{i}.ogg', format="ogg")

            startTime = endTime
            endTime += length_of_chunk * 1000
        except:
            break
