from .rag import conversation_chain


def rag_chain( vector_store, config ):
    return conversation_chain(
        vector_store,
        config.llm_model, 
        config.chat_memory
    )