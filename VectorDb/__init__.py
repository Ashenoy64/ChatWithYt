from .vector import build_vectorstore
import os

def setup_vector_db( documents, config):
    _documents = []
    for doc in documents:
        _documents.append(os.path.join(config.temp_dir, doc))
        
    return build_vectorstore(
        _documents, 
        config.embedding_model, 
        config.vector_db_name, 
        **config.document_split_options
    )