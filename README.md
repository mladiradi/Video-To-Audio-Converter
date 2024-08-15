# Video-To-Audio-Converter

Description

This Python script downloads audio from a YouTube video and saves it as an MP3 file on the Desktop. The user can specify the name of the MP3 file each time the script is run. The script automatically creates the file on the Desktop and replaces any existing files with the same name.
Requirements

    Python 3.x
    yt-dlp (install with pip install yt-dlp)

Usage

    Clone or download the repository to your computer.
    Install yt-dlp using the command:

    bash

pip install yt-dlp

Run the script:

bash

    python video_to_audio.py

    Enter the YouTube video URL and the desired MP3 file name when prompted.

Example Execution

mathematica

Enter YouTube video URL: https://www.youtube.com/watch?v=example
Enter the output file name (without extension): my_audio_file

The script will download the audio from the specified video and save it on your Desktop as my_audio_file.mp3. If a file with that name already exists on the Desktop, it will be replaced.
License

This project is open-source and licensed under the MIT license. See LICENSE for more details.
