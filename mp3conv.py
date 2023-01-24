import os
import sys
import subprocess

# set the source and destination directories
src_dir = sys.argv[1] 
dst_dir = sys.argv[2]

# loop through all files in the source directory
for file in os.listdir(src_dir):
    # check if the file is a valid audio file
    if file.endswith('.mp3') or file.endswith('.wav') or file.endswith('.flac'):
        # get the file name without the path or extension
        filename, file_extension = os.path.splitext(file)

        # convert the file to mp3 with a bitrate of 320 kbps
        subprocess.call(['ffmpeg', '-i', f'{src_dir}/{file}', '-codec:a', 'libmp3lame', '-q:a', '0', '-b:a', '320k', f'{dst_dir}/{filename}.mp3'])

