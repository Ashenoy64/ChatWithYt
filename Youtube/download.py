from pytubefix import YouTube as Yt
from pydub import AudioSegment
import os

def download_audio(youtube_url, output_path="."):
    try:
        yt = Yt(youtube_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        if audio_stream:
            print(f"Downloading audio from: {yt.title}")
            downloaded_file = audio_stream.download(output_path)
            print(f"Audio downloaded successfully to: {downloaded_file}")
            file_root, file_ext = os.path.splitext(downloaded_file)
            input_format = file_ext[1:] if file_ext.startswith('.') else file_ext
            audio = AudioSegment.from_file(downloaded_file, format=input_format)
            mp3_filename = file_root + ".mp3"
            audio.export(mp3_filename, format="mp3")
            print(f"Audio converted to MP3 and saved as: {mp3_filename}")
            os.remove(downloaded_file)
        else:
            print("No audio stream found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    download_audio("https://www.youtube.com/watch?v=5qap5aO4i9A")