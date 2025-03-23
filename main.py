from Utils import Config
from Settings import *

from AudioToText import audio_to_text
from Youtube import download_audios
from VectorDb import setup_vector_db

def setup():
    return Config(
        temp_dir=TEMP_DIR, 
        whisper_model=WHISPER_MODEL,
        embedding_model = EMBEDDING_MODEL,
        vector_db_name = VECTOR_DB_NAME,
        document_split_options = DOCUMENT_SPLIT_OPTIONS,
    )
    


def main( urls ):
    config = setup()
    audio_files =  download_audios(urls, config)
    transcribed_files  = audio_to_text(audio_files, config)
    vector_store = setup_vector_db(transcribed_files, config)
    pass


if __name__ == "__main__":
    urls = ['https://www.youtube.com/watch?v=6JYIGclVQdw']
    main( urls )