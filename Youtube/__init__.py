from .download import __download_audio

def download_audios( urls, config ):
    audio_files = []
    for url in urls:
        _file = __download_audio( url, output_path = config.temp_dir )
        if _file:
            audio_files.append( _file )
    return audio_files


def download_audio( url, config ):
    return __download_audio( url, config.temp_dir )