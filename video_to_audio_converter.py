
import subprocess
import os


def download_audio(url, filename_mp3):
    # Determine the path to the Desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Determine the full path for the output file
    output_file = os.path.join(desktop_path, f"{filename_mp3}.mp3")

    # Remove the old file if it exists
    if os.path.exists(output_file):
        os.remove(output_file)

    command = [
        "yt-dlp",
        "-v",  # Verbose mode for more details
        "-f", "bestaudio",
        "--output", output_file,
        url
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    # Print stdout and stderr
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)

    # Check if the file has been downloaded
    if os.path.exists(output_file):
        print(f"Downloaded file: {output_file}")
    else:
        print("Failed to download file.")


if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ")
    filename = input("Enter the output file name (without extension): ")
    download_audio(video_url, filename)
