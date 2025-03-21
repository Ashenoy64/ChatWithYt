import os

class Config:
    def __init__(self, **kwargs):
        self.temp_dir = kwargs.get('temp_dir', '.temp')
        self.whisper_model = kwargs.get('whisper_model', 'base')

        self.init()

    def init(self):
        os.makedirs(self.temp_dir, exist_ok=True)
        return self
