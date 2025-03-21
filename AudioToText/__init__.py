from .transcribe import transcribe
import os

def audio_to_text( files, config ):
    transcribed_files = []
    for file in files:
        _file = transcribe( os.path.join(config.temp_dir, file) , outPath=config.temp_dir , model=config.whisper_model )
        if _file:
            transcribed_files.append(_file)
    return transcribed_files