from Utils import Config
from Settings import *

from AudioToText import audio_to_text
from Youtube import download_audios
from VectorDb import setup_vector_db
from Rag import rag_chain
from ChatInterface import launch_chat_interface


def setup():
    return Config(
        temp_dir=TEMP_DIR, 
        whisper_model=WHISPER_MODEL,
        embedding_model = EMBEDDING_MODEL,
        vector_db_name = VECTOR_DB_NAME,
        document_split_options = DOCUMENT_SPLIT_OPTIONS,
        llm_model = LLM_MODEL,
        chat_memory = CHAT_MEMORY,
        share_chat_interface = SHARE_CHAT_INTERFACE
    )
    


def main( urls ):
    try:    
        config = setup()
        # audio_files =  download_audios(urls, config)
        # transcribed_files  = audio_to_text(audio_files, config)
        transcribed_files = ['transcribed_files']
        vector_store = setup_vector_db(transcribed_files, config)
        rag = rag_chain(vector_store, config)
        launch_chat_interface(rag, config)
    except KeyboardInterrupt as e:
        print("Exiting...")
        config.close()
    except Exception as e:
        print(e)
    return


if __name__ == "__main__":
    # The url must be of this format: https://www.youtube.com/watch?v=<VideoId>
    urls = ['https://www.youtube.com/watch?v=modXC5IWTJI']
    main( urls )