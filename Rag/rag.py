from langchain.chains import ConversationalRetrievalChain


def conversation_chain( vector_store, llm, memory ):
    retriever = vector_store.as_retriever()
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory
    )
    return conversation_chain