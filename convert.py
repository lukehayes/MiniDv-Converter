#!/usr/bin/python3

# ----------------------------------------------
# Module Imports
# ----------------------------------------------

# Imports the 'sys' module included with Python.
# It's holds helpers system specific helpers
import sys

# Imports the 'os' module included with Python.
# It's holds operating system specific helpers.
import os

# I use this module because 'Path' gives me a nice
# way to get the name of a file and cut the
# extention off of it. It's very helpful.'
from pathlib import Path

# Helper that gets every file inside a directory
import glob

# ----------------------------------------------
# Variables - Change these values if needed
# ----------------------------------------------
minidv_extention = ".mp4"
mp4_extention    = ".mp4"
output_folder    = "Converted_Videos"

# -crf means Constant Rate Factor. All you really need to know is that
# it is the quality of the x264 or x265 codec. Higher numbers mean
# more compression but that could lead to worse video quality.
# Play around with the number and see what results you get.
quality = "-crf 28"

# The codec to use during conversion. Defaults to x265 but can be
# be changed to x264 for example.
codec = "x264"

# Number of videos converted. Don't touch it.
video_count = 0

# ----------------------------------------------
# Video Conversion Part
# ----------------------------------------------

# The below line searches the current folder for a specific file type.
# In your case, it will be file names ending in ".dv". It will loop
# through each item and then convert it to the chosen format.
# 
# Finally, it will move the converted video to the output folder.
for file in glob.glob(f"*{minidv_extention}"):

    # The current file. It will be a .dv file.
    input_video = file

    # The name of the output file. Its the same as input_video except
    # that we change the extention from ".dv" to ".mp4"
    output_video = "converted-" + Path(file).stem + mp4_extention

    # The command that will convert the videos. We store it in a string here for use later.
    conversion_command = f"ffmpeg -i {input_video} -vcodec lib{codec} {quality} {output_video}"

    print(f"Found file: {file}")
    print(f"Converting file: {file} using: {conversion_command}")

    # Run FFMpeg to convert the videos.
    os.system(conversion_command)

    # Once the conversion has finished, we want to move the new video to a fresh folder.
    # If that folder doesn't exist, the lines below create the folder. The name of 
    # the folder can be changed using the output_folder variable in the variables
    # section of this script. Write the name of the folder you want INSIDE
    # the quotes!
    #
    if not os.path.exists(f"{output_folder}"):
        print(f"Creating {output_folder}")
        os.makedirs(f"{output_folder}")

    # Here we move the newly converted video to the output folder that has
    # been defined in the 'variable' section near the top of this file.
    os.system(f"mv {output_video} {output_folder}")
    video_count += 1


print("---")
print(f"{video_count} videos converted and moved to {output_folder}.")
print("---")

