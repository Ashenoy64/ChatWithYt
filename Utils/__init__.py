import os
from langchain_community.embeddings import OllamaEmbeddings

def getEmbeddingModel():
    return OllamaEmbeddings(temperature=0.7,model="nomic-embed-text")


class Config:
    def __init__(self, **kwargs):
        self.temp_dir = kwargs.get('temp_dir', '.temp')
        self.whisper_model = kwargs.get('whisper_model', 'base')
        self.embedding_model = kwargs.get('embedding_model', getEmbeddingModel())
        self.vector_db_name = kwargs.get('vector_db_name', 'vector_store')
        self.document_split_options = kwargs.get('document_split_options', {
            'chunk_size': 500,
            'chunck_overlap': 50,
            'seperators': ["\n\n", "\n", ". ", " ", ""]
        })
        self.init()

    def init(self):
        os.makedirs(self.temp_dir, exist_ok=True)
        return self


