from Utils import Config
from Settings import *

from AudioToText import audio_to_text
from Youtube import download_audio, download_audios

def setup():
    return Config(temp_dir=TEMP_DIR, whisper_model=WHISPER_MODEL)
    


def main( urls ):
    config = setup()
    audio_files =  download_audios(urls, config)
    transcribed_files  = audio_to_text(audio_files, config)
    print(transcribed_files)
    pass


if __name__ == "__main__":
    urls = ['https://www.youtube.com/watch?v=6JYIGclVQdw']
    main( urls )