from .download import download_audio


def download_audios(urls, config):
    for url in urls:
        download_audio(url, config.temp_dir)


def download_audio(url, config):
    download_audio(url, config.temp_dir)