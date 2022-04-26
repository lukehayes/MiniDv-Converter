#MiniDV Video Converter Script

This script is designed to be used to convert MiniDV videos to .mp4 using FFMpeg. It will convert them in batches so that means *every* video file in the folder that the script is in.
You should just be able to run and forget it.

*All things you type into the terminal should be typed without the back ticks. Just type the text.*

I have heavily commented the script, so you can read through it at understand it. That's not important though.
You can also change some of the values to get better conversion quality etc.

## Dependencies
Open the terminal and type `python3 --version`. Something like `python version 3.*` should be printed. If it says `python 3.4` or higher, you should be good to go.
If it doesn't let me know, I can change the script to work for Python 2 in two seconds.

Also, in the terminal type `ffmpeg --version`. If you get any version back, you're good to go. If not, let me know.

**BACKUP YOUR FILES JUST IN CASE!**

## Prerequisite
Create a new folder on the desktop and copy one or two of the videos that you want converted into that folder.

## Quick Instructions
Unzip the project and copy or move the file `convert.py` into a folder that contains MiniDV videos.
To set the terminal to be inside the correct folder, you open a terminal and type `cd $HOME/Desktop/NAME_OF_YOUR_FOLDER`. e.g `cd $HOME/Desktop/MyVideos` <- MyVideos is the folder with videos in it. You will need to create it if you haven't already.

After yoo have changed the directory to be your videos folder, type `chmod +x convert.py` <- This just makes the file executable.

Finally, in the same terminal, type `./convert.py` and the script *should* run. If it doesn't then let me know.

It will convert all of the videos and move them to a folder called "Converted_Videos" and that folder will be in the same directory.


### In Depth Instructions

* Once you have downloaded this project unzip it to the Desktop.
* There is a folder called `convert.py`. Move that into a folder with MiniDV videos that you want to convert.
