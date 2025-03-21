from .transcribe import transcribe

def audio_to_text( config ):
    transcribe( config.temp_dir, outPath=config.temp_dir , model=config.model )