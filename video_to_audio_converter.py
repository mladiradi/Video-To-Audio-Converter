import subprocess
import os


def download_audio(url, filename_mp3):
    # Определяне на пътя до работния плот
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Определяне на пълния път на изходния файл
    output_file = os.path.join(desktop_path, f"{filename_mp3}.mp3")

    # Премахване на стария файл, ако съществува
    if os.path.exists(output_file):
        os.remove(output_file)

    command = [
        "yt-dlp",
        "-v",  # Подробен режим за повече детайли
        "-f", "bestaudio",
        "--output", output_file,
        url
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    # Печата изхода и съобщенията за грешки
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)

    # Проверка дали файлът е изтеглен
    if os.path.exists(output_file):
        print(f"Изтеглен файл: {output_file}")
    else:
        print("Неуспешно изтегляне на файл.")


if __name__ == "__main__":
    video_url = input("Въведете URL на YouTube видео: ")
    filename = input("Въведете име на изходния файл (без разширение): ")
    download_audio(video_url, filename)
