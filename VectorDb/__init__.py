from .vector import build_vectorstore


def setup_vector_db( documents, config):
    return build_vectorstore(
        documents, 
        config.embedding_model, 
        config.vector_db_name, 
        **config.document_split_options
    )