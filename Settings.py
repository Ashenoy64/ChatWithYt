from Utils import getEmbeddingModel

TEMP_DIR = '.temp'
WHISPER_MODEL = 'base'  # Choose from: tiny, base, small, medium, large


#embedding model
EMBEDDING_MODEL = getEmbeddingModel()  # Default: OllamaEmbeddings(temperature=0.7,model="nomic-embed-text")


VECTOR_DB_NAME = "vector_store"

DOCUMENT_SPLIT_OPTIONS = {
    'chunk_size': 500,
    'chunck_overlap': 50,
    'seperators': ["\n\n", "\n", ". ", " ", ""], 
}